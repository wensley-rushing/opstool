import os
import h5py
import numpy as np
import openseespy.opensees as ops
from typing import Union
from numpy.typing import ArrayLike
from itertools import cycle
from rich import print

from ..utils import check_file
from ._get_model_base import (get_truss_info, get_beam_info, get_beam_info2, get_link_info,
                              get_other_line_info, get_all_line_info, get_plane_info, get_all_face_info,
                              get_tet_info, get_bri_info, get_node_coords, get_ele_mid, get_bounds,
                              get_node_fix, get_beam_resp, get_node_resp)


class GetFEMdata:
    """
    Get the data in the openseespy model domain.

    Parameters
    ----------
    results_dir: str, default="opstool_output"
        The dir that results saved.
    """

    def __init__(self, results_dir: str = "opstool_output"):

        self.out_dir = results_dir
        if not os.path.exists(self.out_dir):
            os.makedirs(self.out_dir)

        self.model_info = dict()
        self.get_model_data_finished = False

        # Initialize cell connection data
        self.cells = dict()

        # Initialize eigenvalue data
        self.eigen = None

        # Analysis step model update data
        self.model_info_steps = dict()
        # Ele connection update data
        self.cells_steps = dict()
        # Update node response data
        self.node_resp_names = ("disp", "vel", "accel")
        self.node_resp_steps = dict()
        self.step_node_track = 0

        self.beam_infos = dict()
        self.beam_resp_names = ['localForces']
        # 'basicDeformations'
        self.beam_resp_step = dict()
        # ["N_1", "Vy_1", "Vz_1", "T_1", "My_1", "Mz_1",
        #  "N_2", "Vy_2", "Vz_2", "T_2", "My_2", "Mz_2"]
        # ["eps", "thetaZ_1", "thetaZ_2", "thetaY_1", "thetaY_2", "thetaX"]
        self.step_beam_track = 0

        # On/Off and Tracking for Model Updates
        self.model_update = False

        # self.reset_model_state()
        # self.reset_eigen_state()
        self.reset_steps_state()

        # fiber section data
        self.fiber_sec_tags = None
        self.fiber_sec_data = dict()
        self.fiber_sec_step_data = dict()
        self.step_fiber_track = 0

        # terminal print colors
        colors = ['#00aeff', '#3369e7', '#8e43e7', '#b84592', '#ff4f81',
                  '#ff6c5f', '#ffc168', '#2dde98', '#1cc7d0', '#49a942']
        self.colors_cycle = cycle(colors)

    def reset_model_state(self):
        """Reset the state of results extract of model data."""
        for name in self.model_info.keys():
            self.model_info[name] = None
        for name in self.cells.keys():
            self.cells[name] = None

    def reset_eigen_state(self):
        """Reset the state of results extract of eigen data."""
        self.eigen = dict()
        for name in self.eigen.keys():
            self.eigen[name] = None

    def _reset_model_step(self):
        for name in self.model_info.keys():
            self.model_info_steps[name] = []
        for name in self.cells.keys():
            self.cells_steps[name] = []
        self.model_info_steps['step_track'] = 0
        self.cells_steps['step_track'] = 0

    def _reset_node_resp(self):
        self.step_node_track = 0
        for name in self.node_resp_names:
            self.node_resp_steps[name] = []

    def _reset_beam_step(self):
        self.step_beam_track = 0
        for name in self.beam_infos.keys():
            self.beam_infos[name] = None
        for name in self.beam_resp_names:
            self.beam_resp_step[name] = []

    def _reset_fiber_step(self):
        self.step_fiber_track = 0
        self.fiber_sec_step_data = dict()

    def reset_steps_state(self):
        """Reset the state of results extract in analysis step.

        .. important::
            As the data is saved in the loop analysis using the list append method,
            it is important to clear the data from previous analysis case before each analysis loop.
        """

        self._reset_model_step()
        self._reset_node_resp()
        self._reset_beam_step()
        self._reset_fiber_step()

        # Truss Element Analysis Step Response Data

        # Beam Element Analysis Step Response Data

    def get_model_data(self, save_file: Union[str, bool] = "ModelData.hdf5"):
        """Get data from the current model domain.
        The data will saved to file ``results_dir`` + ``save_file`` in hdf5 style.

        Parameters
        -----------
        save_file: str, default="ModelData.hdf5"
            The file name that data saved.
            If None of False, the data will not be saved.

            .. warning::
                Be careful not to include any path, only filename,
                the file will be saved to the directory ``results_dir``.

        """
        if save_file:
            check_file(save_file, ['.hdf5', '.h5', '.he5'])
        # --------------------------------
        # print(ops.constrainedDOFs())   constrainedDOFs
        node_coords, node_index, model_dims, node_tags = get_node_coords()
        fixed_nodes, fixed_dofs = get_node_fix()
        ele_tags = ops.getEleTags()
        num_ele = len(ele_tags)
        truss_cells, truss_cells_tags = get_truss_info(ele_tags, node_index)
        (link_cells, link_cells_tags, link_midpoints,
         link_xlocal, link_ylocal, link_zlocal) = get_link_info(ele_tags, node_coords, node_index)
        (beam_cells, beam_cells_tags, beam_midpoints,
         beam_xlocal, beam_ylocal, beam_zlocal) = get_beam_info(ele_tags, node_coords, node_index)
        other_line_cells, other_line_cells_tags = get_other_line_info(ele_tags, node_index)
        all_lines_cells, all_lines_cells_tags = get_all_line_info(ele_tags, node_index)
        plane_cells, plane_cells_tags = get_plane_info(ele_tags, node_index)
        tetrahedron_cells, tetrahedron_cells_tags = get_tet_info(ele_tags, node_index)
        brick_cells, brick_cells_tags = get_bri_info(ele_tags, node_coords, node_index)
        all_faces_cells = plane_cells + tetrahedron_cells + brick_cells
        all_faces_cells_tags = plane_cells_tags + tetrahedron_cells_tags + brick_cells_tags
        ele_midpoints = get_ele_mid(ele_tags, node_coords, node_index)
        bounds, max_bound = get_bounds(node_coords)
        # -------------------------------------
        model_info = dict()
        model_info["coord_no_deform"] = node_coords
        model_info["coord_ele_midpoints"] = ele_midpoints
        model_info["bound"] = bounds
        model_info["max_bound"] = max_bound
        model_info["num_ele"] = num_ele
        model_info["NodeTags"] = node_tags
        model_info["num_node"] = len(node_tags)
        model_info["FixNodeTags"] = fixed_nodes
        model_info["FixNodeDofs"] = fixed_dofs
        model_info["EleTags"] = ele_tags
        model_info["model_dims"] = model_dims
        model_info["coord_ele_midpoints"] = ele_midpoints
        model_info["beam_midpoints"] = beam_midpoints
        model_info["beam_xlocal"] = beam_xlocal
        model_info["beam_ylocal"] = beam_ylocal
        model_info["beam_zlocal"] = beam_zlocal
        model_info["link_midpoints"] = link_midpoints
        model_info["link_xlocal"] = link_xlocal
        model_info["link_ylocal"] = link_ylocal
        model_info["link_zlocal"] = link_zlocal

        cells = dict()
        cells["all_lines"] = all_lines_cells
        cells['all_lines_tags'] = all_lines_cells_tags
        cells["all_faces"] = all_faces_cells
        cells["all_faces_tags"] = all_faces_cells_tags
        cells["plane"] = plane_cells
        cells["plane_tags"] = plane_cells_tags
        cells["tetrahedron"] = tetrahedron_cells
        cells["tetrahedron_tags"] = tetrahedron_cells_tags
        cells["brick"] = brick_cells
        cells["brick_tags"] = brick_cells_tags
        cells["truss"] = truss_cells
        cells["truss_tags"] = truss_cells_tags
        cells["link"] = link_cells
        cells["link_tags"] = link_cells_tags
        cells["beam"] = beam_cells
        cells["beam_tags"] = beam_cells_tags
        cells["other_line"] = other_line_cells
        cells["other_line_tags"] = other_line_cells_tags
        for key, value in cells.items():
            cells[key] = np.array(value)

        self.model_info.update(model_info)
        self.cells.update(cells)
        self.get_model_data_finished = True
        if save_file:
            output_filename = self.out_dir + '/' + save_file
            with h5py.File(output_filename, "w") as f:
                grp1 = f.create_group("ModelInfo")
                for name, value in self.model_info.items():
                    grp1.create_dataset(name, data=value)
                grp2 = f.create_group("Cell")
                for name, value in self.cells.items():
                    grp2.create_dataset(name, data=value)
            print(f"Model data saved in [bold {next(self.colors_cycle)}]{output_filename}[/] !")

    def get_eigen_data(
        self,
        mode_tag: int = 1,
        solver: str = "-genBandArpack",
        save_file: str = 'EigenData.hdf5',
    ):
        """Get eigenvalue Analysis Data.
        The data will saved to file ``results_dir`` + ``save_file``.

        Parameters
        ----------
        mode_tag: int
            mode tag.
        solver: str, default '-genBandArpack'
            type of solver, optional '-genBandArpack', '-fullGenLapack',
            see https://openseespydoc.readthedocs.io/en/latest/src/eigen.html.
        save_file: str, default='EigenData.hdf5'
            The file name that data saved.
            If None of False, the data will not be saved.

            .. warning::
                Be careful not to include any path, only filename,
                the file will be saved to the directory ``results_dir``.

        Returns
        -------
        None
        """
        # ----------------------------------
        if save_file:
            check_file(save_file, ['.hdf5', '.h5', '.he5'])
        self.get_model_data(save_file=False)
        self.reset_eigen_state()
        # ----------------------------------
        ops.wipeAnalysis()
        if mode_tag == 1:
            eigen_values = ops.eigen(solver, 2)[:1]
        else:
            eigen_values = ops.eigen(solver, mode_tag)
        omega = np.sqrt(eigen_values)
        f = omega / (2 * np.pi)
        self.eigen["f"] = f
        eigenvectors = []
        for mode_tag in range(1, mode_tag + 1):
            # ------------------------------------------
            eigen_vector = np.zeros((self.model_info["num_node"], 3))
            for i, Tag in enumerate(self.model_info["NodeTags"]):
                coord = ops.nodeCoord(Tag)
                eigen = ops.nodeEigenvector(Tag, mode_tag)
                if len(coord) == 1:
                    coord.extend([0, 0])
                    eigen.extend([0, 0])
                elif len(coord) == 2:
                    coord.extend([0])
                    if len(eigen) == 3 or len(eigen) == 2:
                        eigen = eigen[:2]
                        eigen.extend([0])
                    elif len(eigen) == 1:
                        eigen.extend([0, 0])
                else:
                    eigen = eigen[:3]
                eigen_vector[i] = np.array(eigen)
            eigenvectors.append(eigen_vector)
        self.eigen["eigenvector"] = eigenvectors

        self.eigen.update(self.model_info)
        self.eigen.update(self.cells)
        # ----------------------------------------------------------------
        # output_filename = self.out_dir + '/EigenData'
        # with shelve.open(output_filename) as db:
        #     db["EigenInfo"] = self.eigen
        if save_file:
            output_filename = self.out_dir + '/' + save_file
            with h5py.File(output_filename, "w") as f:
                grp = f.create_group("EigenInfo")
                for name, value in self.eigen.items():
                    grp.create_dataset(name, data=value)
            print(f"Eigen data saved in [bold {next(self.colors_cycle)}]{output_filename}[/] !")

    def get_node_resp_step(self,
                           num_steps: int = 100000000000,
                           total_time: float = 100000000000,
                           stop_cond: bool = False,
                           save_file: str = "NodeRespStepData-1.hdf5",
                           model_update: bool = False):
        """Get the node response data step by step.

        .. note::
            You need to call this function at each analysis step in OpenSees.
            The advantage is that you can modify the iterative algorithm at
            each analysis step to facilitate convergence.

        Parameters
        -----------------
        num_steps: int, default=100000000000
            Total number of steps, set to determine when to save data.
        total_time: float, default=100000000000
            Total analysis time, set to determine when to save data.
            You can specify one of the parameters *num_steps* and `total_time`.
            If both are used, it depends on which one arrives first.
        stop_cond: bool, default = False
            Condition used to determine when data is saved
            if ``num_steps`` and ``total_time`` unavailable.
            For example, stop_cond = ops.nodeDisp(nodeTag, 1) >= 0.1, i.e., once the displacement of node
            with tag nodeTag and dof 1 is greater than 0.1, the loop is terminated to save the data.
        save_file: str, default='NodeRespStepData-1.hdf5'
            The file name that data saved.
            If None of False, the data will not be saved.

            .. warning::
                Be careful not to include any path, only filename,
                the file will be saved to the directory ``results_dir``.
                You need to specify different suffixes to distinguish between the different analysis cases.
                Such as "NodeRespStepData-1.hdf5", "NodeRespStepData-2.hdf5", etc.

        model_update: bool, default False
            whether to update the model domain data at each analysis step,
            this will be useful if model data has changed.
            For example, some elements and nodes were removed.

        Returns
        -------
        None
        """
        if save_file:
            check_file(save_file, ['.hdf5', '.h5', '.he5'])
        if model_update:
            self.get_model_data(save_file=False)
        else:
            if not self.get_model_data_finished:
                self.get_model_data()

        node_tags = self.model_info["NodeTags"]
        (node_disp, node_vel, node_accel, node_deform_coord) = get_node_resp(node_tags)

        self.node_resp_steps["disp"].append(node_disp)
        self.node_resp_steps["vel"].append(node_vel)
        self.node_resp_steps["accel"].append(node_accel)

        if model_update:
            if self.step_node_track == self.model_info_steps['step_track']:
                for name in self.model_info.keys():
                    self.model_info_steps[name].append(self.model_info[name])
                self.model_info_steps['step_track'] += 1
            if self.step_node_track == self.cells_steps['step_track']:
                for name in self.cells.keys():
                    self.cells_steps[name].append(self.cells[name])
                self.cells_steps['step_track'] += 1
        else:
            if self.step_node_track == 0:
                self.model_info_steps.update(self.model_info)
                self.cells_steps.update(self.cells)
        # --------------------------------
        self.model_update = model_update
        self.step_node_track += 1
        # --------------------------------
        if save_file:
            if self.step_node_track >= num_steps or ops.getTime() >= total_time or stop_cond:
                output_filename = self.out_dir + '/' + save_file
                with h5py.File(output_filename, "w") as f:
                    n = len(self.node_resp_steps['disp'])
                    f.create_dataset("Nsteps", data=n)
                    grp1 = f.create_group("ModelInfoSteps")
                    grp2 = f.create_group("CellSteps")
                    grp3 = f.create_group("NodeRespSteps")
                    for name, value in self.model_info_steps.items():
                        if name not in ['step_track']:
                            if model_update:
                                subgrp = grp1.create_group(name)
                                for i in range(n):
                                    subgrp.create_dataset(f"step{i + 1}", data=value[i])
                            else:
                                grp1.create_dataset(name, data=value)
                    for name, value in self.cells_steps.items():
                        if name not in ['step_track']:
                            if model_update:
                                subgrp = grp2.create_group(name)
                                for i in range(n):
                                    subgrp.create_dataset(f"step{i + 1}", data=value[i])
                            else:
                                grp2.create_dataset(name, data=value)
                    for name, value in self.node_resp_steps.items():
                        subgrp = grp3.create_group(name)
                        for i in range(n):
                            subgrp.create_dataset(f"step{i + 1}", data=value[i])
                print(f"Node response data saved in [bold {next(self.colors_cycle)}]{output_filename}[/] !")

    def get_frame_resp_step(self,
                            num_steps: int = 100000000000,
                            total_time: float = 100000000000,
                            stop_cond: bool = False,
                            save_file: str = "BeamRespStepData-1.hdf5"
                            ):
        """Get the response data step by step.
        .. note::
            You need to call this function at each analysis step in OpenSees.
            The advantage is that you can modify the iterative algorithm at
            each analysis step to facilitate convergence.

        Parameters
        ----------
        num_steps: int, default=100000000000
            Total number of steps, set to determine when to save data.
        total_time: float, default=100000000000
            Total analysis time, set to determine when to save data.
            You can specify one of the parameters *num_steps* and `total_time`.
            If both are used, it depends on which one arrives first.
        stop_cond: bool, default = False
            Condition used to determine when data is saved
            if ``num_steps`` and ``total_time`` unavailable.
            For example, stop_cond = ops.nodeDisp(nodeTag, 1) >= 0.1, i.e., once the displacement of node
            with tag nodeTag and dof 1 is greater than 0.1, the loop is terminated to save the data.
        save_file: str, default='BeamRespStepData-1.hdf5'
            The file name that data saved.
            If None of False, the data will not be saved.

            .. warning::
                Be careful not to include any path, only filename,
                the file will be saved to the directory ``results_dir``.
                You need to specify different suffixes to distinguish between the different analysis cases.
                Such as "BeamRespStepData-1.hdf5", "BeamRespStepData-2.hdf5", etc.

        Returns
        -------
        None
        """
        if save_file:
            check_file(save_file, ['.hdf5', '.h5', '.he5'])

        (beam_tags, beam_node_coords, beam_cells,
         xlocals, ylocals, zlocals, bounds) = get_beam_info2()
        self.beam_infos['beam_tags'] = beam_tags
        self.beam_infos['beam_node_coords'] = beam_node_coords
        self.beam_infos['beam_cells'] = beam_cells
        self.beam_infos['xlocal'] = xlocals
        self.beam_infos['ylocal'] = ylocals
        self.beam_infos['zlocal'] = zlocals
        self.beam_infos['bounds'] = bounds

        beam_resp_steps = get_beam_resp(beam_tags)
        self.beam_resp_step['localForces'].append(beam_resp_steps)
        # ----------------------------------------------------------------
        self.step_beam_track += 1
        # ------------------------------------------
        if save_file:
            if self.step_beam_track >= num_steps or ops.getTime() >= total_time or stop_cond:
                output_filename = self.out_dir + '/' + save_file
                with h5py.File(output_filename, "w") as f:
                    n = len(self.beam_resp_step['localForces'])
                    f.create_dataset("Nsteps", data=n)
                    grp1 = f.create_group("BeamInfos")
                    grp2 = f.create_group("BeamRespSteps")
                    for name, value in self.beam_infos.items():
                        grp1.create_dataset(name, data=value)
                    for name, value in self.beam_resp_step.items():
                        subgrp = grp2.create_group(name)
                        for i in range(n):
                            subgrp.create_dataset(f"step{i + 1}", data=value[i])
                print(f"Frame elements response data saved in [bold {next(self.colors_cycle)}]{output_filename}[/] !")

    def get_fiber_data(self, ele_sec: list[tuple[int, int]], save_file: str = 'FiberData.hdf5'):
        """Get data from the section assigned by parameter ele_sec.

        Parameters
        ----------
        ele_sec: list[tuple[int, int]]
            A list or tuple composed of element tag and sectag.
            e.g., [(ele1, sec1), (ele2, sec2), ... , (elen, secn)],
            The section is attached to an element in the order from end i to end j of that element.
        save_file: str, default='FiberData.hdf5'
            The file name that data saved.
            If None of False, the data will not be saved.

            .. warning::
                Be careful not to include any path, only filename,
                the file will be saved to the directory ``results_dir``.

        Returns
        -------
        None
        """
        if save_file:
            check_file(save_file, ['.hdf5', '.h5', '.he5'])
        self.fiber_sec_tags = ele_sec
        for ele_sec_i in ele_sec:
            key = f"{ele_sec_i[0]}-{ele_sec_i[1]}"
            self.fiber_sec_data[key] = None

        # get data
        for ele_sec_i in self.fiber_sec_tags:
            ele_tag = ele_sec_i[0]
            sec_tag = ele_sec_i[1]
            key = f"{ele_sec_i[0]}-{ele_sec_i[1]}"
            fiber_data = _get_fiber_sec_data(ele_tag, sec_tag)
            self.fiber_sec_data[key] = fiber_data
        # ---------------------------------------------
        if save_file:
            output_filename = self.out_dir + '/' + save_file
            with h5py.File(output_filename, "w") as f:
                for name, value in self.fiber_sec_data.items():
                    f.create_dataset(name, data=value)
            print(f"Fiber section data saved in [bold {next(self.colors_cycle)}]{output_filename}[/] !")

    def get_fiber_resp_step(self,
                            num_steps: int = 100000000000,
                            total_time: float = 100000000000,
                            stop_cond: bool = False,
                            save_file: str = "FiberRespStepData-1.hdf5"):
        """Get analysis step data for fiber section.

        Parameters
        ----------
        num_steps: int, default=100000000000
            Total number of steps, set to determine when to save data.
        total_time: float, default=100000000000
            Total analysis time, set to determine when to save data.
            You can specify one of the parameters *num_steps* and `total_time`.
            If both are used, it depends on which one arrives first.
        stop_cond: bool, default = False
            Condition used to determine when data is saved
            if ``num_steps`` and ``total_time`` unavailable.
            For example, stop_cond = ops.nodeDisp(nodeTag, 1) >= 0.1, i.e., once the displacement of node
            with tag nodeTag and dof 1 is greater than 0.1, the loop is terminated to save the data.
        save_file: str, default='FiberRespStepData-1.hdf5'
            The file name that data saved.
            If None of False, the data will not be saved.

            .. warning::
                Be careful not to include any path, only filename,
                the file will be saved to the directory ``results_dir``.
                You need to specify different suffixes to distinguish between the different analysis cases.
                Such as "FiberRespStepData-1.hdf5", "FiberRespStepData-2.hdf5", etc.

        Returns
        -------
        None
        """
        if save_file:
            check_file(save_file, ['.hdf5', '.h5', '.he5'])
        if not self.fiber_sec_data:
            raise ValueError(
                "Run get_fiber_step_data must run get_fiber_data() in advance!"
            )
        if self.step_fiber_track == 0:
            for ele_sec_i in self.fiber_sec_tags:
                key = f"{ele_sec_i[0]}-{ele_sec_i[1]}"
                self.fiber_sec_step_data[key] = []

        for ele_sec_i in self.fiber_sec_tags:
            ele_tag = ele_sec_i[0]
            sec_tag = ele_sec_i[1]
            key = f"{ele_sec_i[0]}-{ele_sec_i[1]}"
            fiber_data = _get_fiber_sec_data(ele_tag, sec_tag)
            defo_fo = ops.eleResponse(ele_tag, "section", sec_tag, "forceAndDeformation")
            if len(defo_fo) == 6:
                defo_fo = [defo_fo[0], defo_fo[1], 0., defo_fo[2],
                           defo_fo[3], defo_fo[4], 0., defo_fo[5]]
            sec_defo_fo = np.array([defo_fo] * fiber_data.shape[0], dtype=float)
            data = np.hstack([fiber_data, sec_defo_fo])
            self.fiber_sec_step_data[key].append(data)
        # ------------------------
        self.step_fiber_track += 1
        # ------------------------
        if save_file:
            if self.step_fiber_track >= num_steps or ops.getTime() >= total_time or stop_cond:
                output_filename = self.out_dir + '/' + save_file
                with h5py.File(output_filename, "w") as f:
                    f.create_dataset("Nsteps", data=self.step_fiber_track)
                    grp = f.create_group("FiberRespSteps")
                    for name, value in self.fiber_sec_step_data.items():
                        subgrp = grp.create_group(name)
                        for i in range(self.step_fiber_track):
                            subgrp.create_dataset(f"step{i + 1}", data=value[i])
                print(f"Fiber section responses data saved in [bold {next(self.colors_cycle)}]{output_filename}[/] !")


def _get_fiber_sec_data(ele_tag: int, sec_tag: int = 1) -> ArrayLike:
    """Get the fiber sec data for a beam element.

    Parameters
    ----------
    ele_tag: int
        The element tag to which the section is to be displayed.
    sec_tag: int
        Which integration point section is displayed, tag from 1 from segment i to j.

    Returns
    -------
    fiber_data: ArrayLike
    """
    # Extract fiber data using eleResponse() command
    fiber_data = ops.eleResponse(ele_tag, "section", sec_tag, "fiberData2")
    if len(fiber_data) == 0:
        fiber_data = ops.eleResponse(ele_tag, "section", "fiberData2")
    # From column 1 to 6: "yCoord", "zCoord", "area", 'mat', "stress", "strain"
    fiber_data = np.array(fiber_data).reshape((-1, 6))  # 变形为6列数组
    return fiber_data
