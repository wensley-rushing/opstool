import openseespy.opensees as ops


def Shell3D():
    print(
        "The original Tcl file comes from http://www.dinochen.com/, "
        "and the Python version is converted by opstool.tcl2py()."
    )
    ops.wipe()
    ops.model("basic", "-ndm", 3, "-ndf", 6)
    ops.node(1, 0.0, 0.0, 0.0)
    ops.node(2, 6000.0, 0.0, 0.0)
    ops.node(3, 6000.0, 0.0, 3000.0)
    ops.node(4, 0.0, 0.0, 3000.0)
    ops.node(5, 1200.0, 0.0, 0.0)
    ops.node(6, 1200.0, 0.0, 600.0)
    ops.node(7, 0.0, 0.0, 600.0)
    ops.node(8, 1200.0, 0.0, 1200.0)
    ops.node(9, 0.0, 0.0, 1200.0)
    ops.node(10, 1200.0, 0.0, 1800.0)
    ops.node(11, 0.0, 0.0, 1800.0)
    ops.node(12, 1200.0, 0.0, 2400.0)
    ops.node(13, 0.0, 0.0, 2400.0)
    ops.node(14, 1200.0, 0.0, 3000.0)
    ops.node(15, 2400.0, 0.0, 0.0)
    ops.node(16, 2400.0, 0.0, 600.0)
    ops.node(17, 2400.0, 0.0, 1200.0)
    ops.node(18, 2400.0, 0.0, 1800.0)
    ops.node(19, 2400.0, 0.0, 2400.0)
    ops.node(20, 2400.0, 0.0, 3000.0)
    ops.node(21, 3600.0, 0.0, 0.0)
    ops.node(22, 3600.0, 0.0, 600.0)
    ops.node(23, 3600.0, 0.0, 1200.0)
    ops.node(24, 3600.0, 0.0, 1800.0)
    ops.node(25, 3600.0, 0.0, 2400.0)
    ops.node(26, 3600.0, 0.0, 3000.0)
    ops.node(27, 4800.0, 0.0, 0.0)
    ops.node(28, 4800.0, 0.0, 600.0)
    ops.node(29, 4800.0, 0.0, 1200.0)
    ops.node(30, 4800.0, 0.0, 1800.0)
    ops.node(31, 4800.0, 0.0, 2400.0)
    ops.node(32, 4800.0, 0.0, 3000.0)
    ops.node(33, 6000.0, 0.0, 600.0)
    ops.node(34, 6000.0, 0.0, 1200.0)
    ops.node(35, 6000.0, 0.0, 1800.0)
    ops.node(36, 6000.0, 0.0, 2400.0)
    ops.node(37, 600.0, 0.0, 0.0)
    ops.node(38, 600.0, 0.0, 300.0)
    ops.node(39, 0.0, 0.0, 300.0)
    ops.node(40, 600.0, 0.0, 600.0)
    ops.node(41, 1200.0, 0.0, 300.0)
    ops.node(42, 600.0, 0.0, 900.0)
    ops.node(43, 0.0, 0.0, 900.0)
    ops.node(44, 600.0, 0.0, 1200.0)
    ops.node(45, 1200.0, 0.0, 900.0)
    ops.node(46, 600.0, 0.0, 1500.0)
    ops.node(47, 0.0, 0.0, 1500.0)
    ops.node(48, 600.0, 0.0, 1800.0)
    ops.node(49, 1200.0, 0.0, 1500.0)
    ops.node(50, 600.0, 0.0, 2100.0)
    ops.node(51, 0.0, 0.0, 2100.0)
    ops.node(52, 600.0, 0.0, 2400.0)
    ops.node(53, 1200.0, 0.0, 2100.0)
    ops.node(54, 600.0, 0.0, 2700.0)
    ops.node(55, 0.0, 0.0, 2700.0)
    ops.node(56, 600.0, 0.0, 3000.0)
    ops.node(57, 1200.0, 0.0, 2700.0)
    ops.node(58, 1800.0, 0.0, 0.0)
    ops.node(59, 1800.0, 0.0, 300.0)
    ops.node(60, 1800.0, 0.0, 600.0)
    ops.node(61, 2400.0, 0.0, 300.0)
    ops.node(62, 1800.0, 0.0, 900.0)
    ops.node(63, 1800.0, 0.0, 1200.0)
    ops.node(64, 2400.0, 0.0, 900.0)
    ops.node(65, 1800.0, 0.0, 1500.0)
    ops.node(66, 1800.0, 0.0, 1800.0)
    ops.node(67, 2400.0, 0.0, 1500.0)
    ops.node(68, 1800.0, 0.0, 2100.0)
    ops.node(69, 1800.0, 0.0, 2400.0)
    ops.node(70, 2400.0, 0.0, 2100.0)
    ops.node(71, 1800.0, 0.0, 2700.0)
    ops.node(72, 1800.0, 0.0, 3000.0)
    ops.node(73, 2400.0, 0.0, 2700.0)
    ops.node(74, 3000.0, 0.0, 0.0)
    ops.node(75, 3000.0, 0.0, 300.0)
    ops.node(76, 3000.0, 0.0, 600.0)
    ops.node(77, 3600.0, 0.0, 300.0)
    ops.node(78, 3000.0, 0.0, 900.0)
    ops.node(79, 3000.0, 0.0, 1200.0)
    ops.node(80, 3600.0, 0.0, 900.0)
    ops.node(81, 3000.0, 0.0, 1500.0)
    ops.node(82, 3000.0, 0.0, 1800.0)
    ops.node(83, 3600.0, 0.0, 1500.0)
    ops.node(84, 3000.0, 0.0, 2100.0)
    ops.node(85, 3000.0, 0.0, 2400.0)
    ops.node(86, 3600.0, 0.0, 2100.0)
    ops.node(87, 3000.0, 0.0, 2700.0)
    ops.node(88, 3000.0, 0.0, 3000.0)
    ops.node(89, 3600.0, 0.0, 2700.0)
    ops.node(90, 4200.0, 0.0, 0.0)
    ops.node(91, 4200.0, 0.0, 300.0)
    ops.node(92, 4200.0, 0.0, 600.0)
    ops.node(93, 4800.0, 0.0, 300.0)
    ops.node(94, 4200.0, 0.0, 900.0)
    ops.node(95, 4200.0, 0.0, 1200.0)
    ops.node(96, 4800.0, 0.0, 900.0)
    ops.node(97, 4200.0, 0.0, 1500.0)
    ops.node(98, 4200.0, 0.0, 1800.0)
    ops.node(99, 4800.0, 0.0, 1500.0)
    ops.node(100, 4200.0, 0.0, 2100.0)
    ops.node(101, 4200.0, 0.0, 2400.0)
    ops.node(102, 4800.0, 0.0, 2100.0)
    ops.node(103, 4200.0, 0.0, 2700.0)
    ops.node(104, 4200.0, 0.0, 3000.0)
    ops.node(105, 4800.0, 0.0, 2700.0)
    ops.node(106, 5400.0, 0.0, 0.0)
    ops.node(107, 5400.0, 0.0, 300.0)
    ops.node(108, 5400.0, 0.0, 600.0)
    ops.node(109, 6000.0, 0.0, 300.0)
    ops.node(110, 5400.0, 0.0, 900.0)
    ops.node(111, 5400.0, 0.0, 1200.0)
    ops.node(112, 6000.0, 0.0, 900.0)
    ops.node(113, 5400.0, 0.0, 1500.0)
    ops.node(114, 5400.0, 0.0, 1800.0)
    ops.node(115, 6000.0, 0.0, 1500.0)
    ops.node(116, 5400.0, 0.0, 2100.0)
    ops.node(117, 5400.0, 0.0, 2400.0)
    ops.node(118, 6000.0, 0.0, 2100.0)
    ops.node(119, 5400.0, 0.0, 2700.0)
    ops.node(120, 5400.0, 0.0, 3000.0)
    ops.node(121, 6000.0, 0.0, 2700.0)
    ops.mass(1, 0.3241, 0.3241, 0.3241, 0.0, 0.0, 0.0)
    ops.mass(2, 0.3241, 0.3241, 0.3241, 0.0, 0.0, 0.0)
    ops.mass(3, 0.3241, 0.3241, 0.3241, 0.0, 0.0, 0.0)
    ops.mass(4, 0.3241, 0.3241, 0.3241, 0.0, 0.0, 0.0)
    ops.mass(5, 0.6483, 0.6483, 0.6483, 0.0, 0.0, 0.0)
    ops.mass(14, 0.6483, 0.6483, 0.6483, 0.0, 0.0, 0.0)
    ops.mass(15, 0.6483, 0.6483, 0.6483, 0.0, 0.0, 0.0)
    ops.mass(20, 0.6483, 0.6483, 0.6483, 0.0, 0.0, 0.0)
    ops.mass(21, 0.6483, 0.6483, 0.6483, 0.0, 0.0, 0.0)
    ops.mass(26, 0.6483, 0.6483, 0.6483, 0.0, 0.0, 0.0)
    ops.mass(27, 0.6483, 0.6483, 0.6483, 0.0, 0.0, 0.0)
    ops.mass(32, 0.6483, 0.6483, 0.6483, 0.0, 0.0, 0.0)
    ops.mass(37, 0.6483, 0.6483, 0.6483, 0.0, 0.0, 0.0)
    ops.mass(56, 0.6483, 0.6483, 0.6483, 0.0, 0.0, 0.0)
    ops.mass(58, 0.6483, 0.6483, 0.6483, 0.0, 0.0, 0.0)
    ops.mass(72, 0.6483, 0.6483, 0.6483, 0.0, 0.0, 0.0)
    ops.mass(74, 0.6483, 0.6483, 0.6483, 0.0, 0.0, 0.0)
    ops.mass(88, 0.6483, 0.6483, 0.6483, 0.0, 0.0, 0.0)
    ops.mass(90, 0.6483, 0.6483, 0.6483, 0.0, 0.0, 0.0)
    ops.mass(104, 0.6483, 0.6483, 0.6483, 0.0, 0.0, 0.0)
    ops.mass(106, 0.6483, 0.6483, 0.6483, 0.0, 0.0, 0.0)
    ops.mass(120, 0.6483, 0.6483, 0.6483, 0.0, 0.0, 0.0)
    ops.fix(1, 1, 1, 1, 1, 1, 1)
    ops.fix(2, 1, 1, 1, 1, 1, 1)
    ops.fix(3, 0, 0, 0, 1, 1, 1)
    ops.fix(4, 0, 0, 0, 1, 1, 1)
    ops.fix(5, 1, 1, 1, 1, 1, 1)
    ops.fix(6, 0, 0, 0, 1, 1, 1)
    ops.fix(7, 0, 0, 0, 1, 1, 1)
    ops.fix(8, 0, 0, 0, 1, 1, 1)
    ops.fix(9, 0, 0, 0, 1, 1, 1)
    ops.fix(10, 0, 0, 0, 1, 1, 1)
    ops.fix(11, 0, 0, 0, 1, 1, 1)
    ops.fix(12, 0, 0, 0, 1, 1, 1)
    ops.fix(13, 0, 0, 0, 1, 1, 1)
    ops.fix(14, 0, 0, 0, 1, 1, 1)
    ops.fix(15, 1, 1, 1, 1, 1, 1)
    ops.fix(16, 0, 0, 0, 1, 1, 1)
    ops.fix(17, 0, 0, 0, 1, 1, 1)
    ops.fix(18, 0, 0, 0, 1, 1, 1)
    ops.fix(19, 0, 0, 0, 1, 1, 1)
    ops.fix(20, 0, 0, 0, 1, 1, 1)
    ops.fix(21, 1, 1, 1, 1, 1, 1)
    ops.fix(22, 0, 0, 0, 1, 1, 1)
    ops.fix(23, 0, 0, 0, 1, 1, 1)
    ops.fix(24, 0, 0, 0, 1, 1, 1)
    ops.fix(25, 0, 0, 0, 1, 1, 1)
    ops.fix(26, 0, 0, 0, 1, 1, 1)
    ops.fix(27, 1, 1, 1, 1, 1, 1)
    ops.fix(28, 0, 0, 0, 1, 1, 1)
    ops.fix(29, 0, 0, 0, 1, 1, 1)
    ops.fix(30, 0, 0, 0, 1, 1, 1)
    ops.fix(31, 0, 0, 0, 1, 1, 1)
    ops.fix(32, 0, 0, 0, 1, 1, 1)
    ops.fix(33, 0, 0, 0, 1, 1, 1)
    ops.fix(34, 0, 0, 0, 1, 1, 1)
    ops.fix(35, 0, 0, 0, 1, 1, 1)
    ops.fix(36, 0, 0, 0, 1, 1, 1)
    ops.fix(37, 1, 1, 1, 1, 1, 1)
    ops.fix(38, 0, 0, 0, 1, 1, 1)
    ops.fix(39, 0, 0, 0, 1, 1, 1)
    ops.fix(40, 0, 0, 0, 1, 1, 1)
    ops.fix(41, 0, 0, 0, 1, 1, 1)
    ops.fix(42, 0, 0, 0, 1, 1, 1)
    ops.fix(43, 0, 0, 0, 1, 1, 1)
    ops.fix(44, 0, 0, 0, 1, 1, 1)
    ops.fix(45, 0, 0, 0, 1, 1, 1)
    ops.fix(46, 0, 0, 0, 1, 1, 1)
    ops.fix(47, 0, 0, 0, 1, 1, 1)
    ops.fix(48, 0, 0, 0, 1, 1, 1)
    ops.fix(49, 0, 0, 0, 1, 1, 1)
    ops.fix(50, 0, 0, 0, 1, 1, 1)
    ops.fix(51, 0, 0, 0, 1, 1, 1)
    ops.fix(52, 0, 0, 0, 1, 1, 1)
    ops.fix(53, 0, 0, 0, 1, 1, 1)
    ops.fix(54, 0, 0, 0, 1, 1, 1)
    ops.fix(55, 0, 0, 0, 1, 1, 1)
    ops.fix(56, 0, 0, 0, 1, 1, 1)
    ops.fix(57, 0, 0, 0, 1, 1, 1)
    ops.fix(58, 1, 1, 1, 1, 1, 1)
    ops.fix(59, 0, 0, 0, 1, 1, 1)
    ops.fix(60, 0, 0, 0, 1, 1, 1)
    ops.fix(61, 0, 0, 0, 1, 1, 1)
    ops.fix(62, 0, 0, 0, 1, 1, 1)
    ops.fix(63, 0, 0, 0, 1, 1, 1)
    ops.fix(64, 0, 0, 0, 1, 1, 1)
    ops.fix(65, 0, 0, 0, 1, 1, 1)
    ops.fix(66, 0, 0, 0, 1, 1, 1)
    ops.fix(68, 0, 0, 0, 1, 1, 1)
    ops.fix(69, 0, 0, 0, 1, 1, 1)
    ops.fix(70, 0, 0, 0, 1, 1, 1)
    ops.fix(71, 0, 0, 0, 1, 1, 1)
    ops.fix(72, 0, 0, 0, 1, 1, 1)
    ops.fix(73, 0, 0, 0, 1, 1, 1)
    ops.fix(74, 1, 1, 1, 1, 1, 1)
    ops.fix(75, 0, 0, 0, 1, 1, 1)
    ops.fix(76, 0, 0, 0, 1, 1, 1)
    ops.fix(77, 0, 0, 0, 1, 1, 1)
    ops.fix(78, 0, 0, 0, 1, 1, 1)
    ops.fix(79, 0, 0, 0, 1, 1, 1)
    ops.fix(80, 0, 0, 0, 1, 1, 1)
    ops.fix(82, 0, 0, 0, 1, 1, 1)
    ops.fix(84, 0, 0, 0, 1, 1, 1)
    ops.fix(85, 0, 0, 0, 1, 1, 1)
    ops.fix(86, 0, 0, 0, 1, 1, 1)
    ops.fix(87, 0, 0, 0, 1, 1, 1)
    ops.fix(88, 0, 0, 0, 1, 1, 1)
    ops.fix(89, 0, 0, 0, 1, 1, 1)
    ops.fix(90, 1, 1, 1, 1, 1, 1)
    ops.fix(91, 0, 0, 0, 1, 1, 1)
    ops.fix(92, 0, 0, 0, 1, 1, 1)
    ops.fix(93, 0, 0, 0, 1, 1, 1)
    ops.fix(94, 0, 0, 0, 1, 1, 1)
    ops.fix(95, 0, 0, 0, 1, 1, 1)
    ops.fix(96, 0, 0, 0, 1, 1, 1)
    ops.fix(97, 0, 0, 0, 1, 1, 1)
    ops.fix(98, 0, 0, 0, 1, 1, 1)
    ops.fix(99, 0, 0, 0, 1, 1, 1)
    ops.fix(100, 0, 0, 0, 1, 1, 1)
    ops.fix(101, 0, 0, 0, 1, 1, 1)
    ops.fix(102, 0, 0, 0, 1, 1, 1)
    ops.fix(103, 0, 0, 0, 1, 1, 1)
    ops.fix(104, 0, 0, 0, 1, 1, 1)
    ops.fix(105, 0, 0, 0, 1, 1, 1)
    ops.fix(106, 1, 1, 1, 1, 1, 1)
    ops.fix(107, 0, 0, 0, 1, 1, 1)
    ops.fix(108, 0, 0, 0, 1, 1, 1)
    ops.fix(109, 0, 0, 0, 1, 1, 1)
    ops.fix(110, 0, 0, 0, 1, 1, 1)
    ops.fix(111, 0, 0, 0, 1, 1, 1)
    ops.fix(112, 0, 0, 0, 1, 1, 1)
    ops.fix(113, 0, 0, 0, 1, 1, 1)
    ops.fix(114, 0, 0, 0, 1, 1, 1)
    ops.fix(115, 0, 0, 0, 1, 1, 1)
    ops.fix(116, 0, 0, 0, 1, 1, 1)
    ops.fix(117, 0, 0, 0, 1, 1, 1)
    ops.fix(118, 0, 0, 0, 1, 1, 1)
    ops.fix(119, 0, 0, 0, 1, 1, 1)
    ops.fix(120, 0, 0, 0, 1, 1, 1)
    ops.fix(121, 0, 0, 0, 1, 1, 1)
    ops.uniaxialMaterial("Elastic", 1, 199900.0)
    ops.nDMaterial("ElasticIsotropic", 2, 24820.0, 0.2)
    ops.uniaxialMaterial("Elastic", 3, 199900.0)
    ops.nDMaterial("PlateFiber", 601, 2)
    ops.section("PlateFiber", 701, 601, 300.0)
    ops.nDMaterial("PlateFiber", 602, 2)
    ops.section("PlateFiber", 702, 602, 250.0)
    ops.element("ShellMITC4", 1, 1, 37, 38, 39, 701)
    ops.element("ShellMITC4", 2, 39, 38, 40, 7, 701)
    ops.element("ShellMITC4", 3, 37, 5, 41, 38, 701)
    ops.element("ShellMITC4", 4, 38, 41, 6, 40, 701)
    ops.element("ShellMITC4", 5, 7, 40, 42, 43, 701)
    ops.element("ShellMITC4", 6, 43, 42, 44, 9, 701)
    ops.element("ShellMITC4", 7, 40, 6, 45, 42, 701)
    ops.element("ShellMITC4", 8, 42, 45, 8, 44, 701)
    ops.element("ShellMITC4", 9, 9, 44, 46, 47, 701)
    ops.element("ShellMITC4", 10, 47, 46, 48, 11, 701)
    ops.element("ShellMITC4", 11, 44, 8, 49, 46, 701)
    ops.element("ShellMITC4", 12, 46, 49, 10, 48, 701)
    ops.element("ShellMITC4", 13, 11, 48, 50, 51, 701)
    ops.element("ShellMITC4", 14, 51, 50, 52, 13, 701)
    ops.element("ShellMITC4", 15, 48, 10, 53, 50, 701)
    ops.element("ShellMITC4", 16, 50, 53, 12, 52, 701)
    ops.element("ShellMITC4", 17, 13, 52, 54, 55, 701)
    ops.element("ShellMITC4", 18, 55, 54, 56, 4, 701)
    ops.element("ShellMITC4", 19, 52, 12, 57, 54, 701)
    ops.element("ShellMITC4", 20, 54, 57, 14, 56, 701)
    ops.element("ShellMITC4", 21, 5, 58, 59, 41, 701)
    ops.element("ShellMITC4", 22, 41, 59, 60, 6, 701)
    ops.element("ShellMITC4", 23, 58, 15, 61, 59, 701)
    ops.element("ShellMITC4", 24, 59, 61, 16, 60, 701)
    ops.element("ShellMITC4", 25, 6, 60, 62, 45, 701)
    ops.element("ShellMITC4", 26, 45, 62, 63, 8, 701)
    ops.element("ShellMITC4", 27, 60, 16, 64, 62, 701)
    ops.element("ShellMITC4", 28, 62, 64, 17, 63, 701)
    ops.element("ShellMITC4", 29, 8, 63, 65, 49, 701)
    ops.element("ShellMITC4", 30, 49, 65, 66, 10, 701)
    ops.element("ShellMITC4", 31, 63, 17, 67, 65, 701)
    ops.element("ShellMITC4", 32, 65, 67, 18, 66, 701)
    ops.element("ShellMITC4", 33, 10, 66, 68, 53, 701)
    ops.element("ShellMITC4", 34, 53, 68, 69, 12, 701)
    ops.element("ShellMITC4", 35, 66, 18, 70, 68, 701)
    ops.element("ShellMITC4", 36, 68, 70, 19, 69, 701)
    ops.element("ShellMITC4", 37, 12, 69, 71, 57, 701)
    ops.element("ShellMITC4", 38, 57, 71, 72, 14, 701)
    ops.element("ShellMITC4", 39, 69, 19, 73, 71, 701)
    ops.element("ShellMITC4", 40, 71, 73, 20, 72, 701)
    ops.element("ShellMITC4", 41, 15, 74, 75, 61, 701)
    ops.element("ShellMITC4", 42, 61, 75, 76, 16, 701)
    ops.element("ShellMITC4", 43, 74, 21, 77, 75, 701)
    ops.element("ShellMITC4", 44, 75, 77, 22, 76, 701)
    ops.element("ShellMITC4", 45, 16, 76, 78, 64, 701)
    ops.element("ShellMITC4", 46, 64, 78, 79, 17, 701)
    ops.element("ShellMITC4", 47, 76, 22, 80, 78, 701)
    ops.element("ShellMITC4", 48, 78, 80, 23, 79, 701)
    ops.element("ShellMITC4", 49, 17, 79, 81, 67, 701)
    ops.element("ShellMITC4", 50, 67, 81, 82, 18, 701)
    ops.element("ShellMITC4", 51, 79, 23, 83, 81, 701)
    ops.element("ShellMITC4", 52, 81, 83, 24, 82, 701)
    ops.element("ShellMITC4", 53, 18, 82, 84, 70, 701)
    ops.element("ShellMITC4", 54, 70, 84, 85, 19, 701)
    ops.element("ShellMITC4", 55, 82, 24, 86, 84, 701)
    ops.element("ShellMITC4", 56, 84, 86, 25, 85, 701)
    ops.element("ShellMITC4", 57, 19, 85, 87, 73, 701)
    ops.element("ShellMITC4", 58, 73, 87, 88, 20, 701)
    ops.element("ShellMITC4", 59, 85, 25, 89, 87, 701)
    ops.element("ShellMITC4", 60, 87, 89, 26, 88, 701)
    ops.element("ShellMITC4", 61, 21, 90, 91, 77, 701)
    ops.element("ShellMITC4", 62, 77, 91, 92, 22, 701)
    ops.element("ShellMITC4", 63, 90, 27, 93, 91, 701)
    ops.element("ShellMITC4", 64, 91, 93, 28, 92, 701)
    ops.element("ShellMITC4", 65, 22, 92, 94, 80, 701)
    ops.element("ShellMITC4", 66, 80, 94, 95, 23, 701)
    ops.element("ShellMITC4", 67, 92, 28, 96, 94, 701)
    ops.element("ShellMITC4", 68, 94, 96, 29, 95, 701)
    ops.element("ShellMITC4", 69, 23, 95, 97, 83, 701)
    ops.element("ShellMITC4", 70, 83, 97, 98, 24, 701)
    ops.element("ShellMITC4", 71, 95, 29, 99, 97, 701)
    ops.element("ShellMITC4", 72, 97, 99, 30, 98, 701)
    ops.element("ShellMITC4", 73, 24, 98, 100, 86, 701)
    ops.element("ShellMITC4", 74, 86, 100, 101, 25, 701)
    ops.element("ShellMITC4", 75, 98, 30, 102, 100, 701)
    ops.element("ShellMITC4", 76, 100, 102, 31, 101, 701)
    ops.element("ShellMITC4", 77, 25, 101, 103, 89, 701)
    ops.element("ShellMITC4", 78, 89, 103, 104, 26, 701)
    ops.element("ShellMITC4", 79, 101, 31, 105, 103, 701)
    ops.element("ShellMITC4", 80, 103, 105, 32, 104, 701)
    ops.element("ShellMITC4", 81, 27, 106, 107, 93, 701)
    ops.element("ShellMITC4", 82, 93, 107, 108, 28, 701)
    ops.element("ShellMITC4", 83, 106, 2, 109, 107, 701)
    ops.element("ShellMITC4", 84, 107, 109, 33, 108, 701)
    ops.element("ShellMITC4", 85, 28, 108, 110, 96, 701)
    ops.element("ShellMITC4", 86, 96, 110, 111, 29, 701)
    ops.element("ShellMITC4", 87, 108, 33, 112, 110, 701)
    ops.element("ShellMITC4", 88, 110, 112, 34, 111, 701)
    ops.element("ShellMITC4", 89, 29, 111, 113, 99, 701)
    ops.element("ShellMITC4", 90, 99, 113, 114, 30, 701)
    ops.element("ShellMITC4", 91, 111, 34, 115, 113, 701)
    ops.element("ShellMITC4", 92, 113, 115, 35, 114, 701)
    ops.element("ShellMITC4", 93, 30, 114, 116, 102, 701)
    ops.element("ShellMITC4", 94, 102, 116, 117, 31, 701)
    ops.element("ShellMITC4", 95, 114, 35, 118, 116, 701)
    ops.element("ShellMITC4", 96, 116, 118, 36, 117, 701)
    ops.element("ShellMITC4", 97, 31, 117, 119, 105, 701)
    ops.element("ShellMITC4", 98, 105, 119, 120, 32, 701)
    ops.element("ShellMITC4", 99, 117, 36, 121, 119, 701)
    ops.element("ShellMITC4", 100, 119, 121, 3, 120, 701)
