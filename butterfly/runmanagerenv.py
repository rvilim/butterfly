import os


def bluecfd(folder):
    """Environment variables fo blueCFD.

    The variables are based on setvars.bat file for blueCFD source.
    """
    bluecfd_env_base = {
        'AddOns_ParaView_DIR': os.path.join(folder, r'AddOns\ParaView'),
        'BLUECFDPATH': folder,
        'USER': 'ofuser',
        'USERNAME': 'ofuser',
        'WM_PROJECT': 'OpenFOAM',
        'WM_PROJECT_VERSION': '5.x',
        'FOAM_INST_DIR': folder,
        'WM_PROJECT_INST_DIR': folder,
        'WM_PROJECT_DIR': os.path.join(folder, 'OpenFOAM-5.x'),
        'WM_PROJECT_USER_DIR': os.path.join(folder, 'ofuser-of5'),
        'WM_THIRD_PARTY_DIR': os.path.join(folder, 'ThirdParty-5.x'),
        'WM_ARCH': 'mingw_w64',
        'WM_ARCH_OPTION': '64',
        'WM_CC': 'x86_64-w64-mingw32-gcc',
        'WM_COMPILER': 'Gcc',
        'WM_COMPILER_ARCH': 'x86_64-w64-mingw32',
        'WM_COMPILER_TYPE': 'system',
        'WM_COMPILE_OPTION': 'Opt',
        'WM_CXX': 'x86_64-w64-mingw32-g++',
        'WM_DIR': os.path.join(folder, 'OpenFOAM-5.x', 'wmake'),
        'WM_LABEL_OPTION': 'Int32',
        'WM_LABEL_SIZE': '32',
        'WM_LINK_LANGUAGE': 'c++',
        'WM_MPLIB': 'MSMPI71',
        'WM_OSTYPE': 'MSwindows',
        'WM_PRECISION_OPTION': 'DP',
        'WM_TARGET_ARCH': 'mingw_w64',
        'WM_OPTIONS': 'mingw_w64GccDPInt32Opt',
        'ParaView_DIR': os.path.join(folder, r'AddOns\ParaView'),
        'ParaView_MAJOR': '5.4',
        'ParaView_VERSION': '5.4.1',
        'BOOST_ARCH_PATH': os.path.join(folder, r'msys64\mingw64'),
        'CGAL_ARCH_PATH': os.path.join(folder, r'msys64\mingw64'),
        'MPI_ACCESSORY_OPTIONS': '-genvlist WM_PROJECT_DIR,MPI_BUFFER_SIZE,PATH',
        'MPI_ARCH_PATH': os.path.join(folder,
            r'ThirdParty-5.x\platforms\mingw_w64Gcc\MS-MPI-7.1'),
        'MPI_BUFFER_SIZE': '20000000',
        'FOAMY_HEX_MESH': '1',
        'FOAM_APP': os.path.join(folder, r'OpenFOAM-5.x\applications'),
        'FOAM_APPBIN': os.path.join(folder,
            r'OpenFOAM-5.x\platforms\mingw_w64GccDPInt32Opt\bin'),
        'FOAM_ETC': os.path.join(folder, r'OpenFOAM-5.x\etc'),
        'FOAM_EXT_LIBBIN': os.path.join(folder,
            r'ThirdParty-5.x\platforms\mingw_w64GccDPInt32\lib'),
        'FOAM_JOB_DIR': os.path.join(folder, r'jobControl'),
        'FOAM_LIBBIN': os.path.join(folder,
            r'OpenFOAM-5.x\platforms\mingw_w64GccDPInt32Opt\lib'),
        'FOAM_MPI': 'MS-MPI-7.1',
        'FOAM_RUN': os.path.join(folder, r'ofuser-of5\run'),
        'FOAM_SIGFPE': '1',
        'FOAM_SITE_APPBIN': os.path.join(folder,
            r'site\5.x\platforms\mingw_w64GccDPInt32Opt\bin'),
        'FOAM_SITE_LIBBIN': os.path.join(folder,
            r'site\5.x\platforms\mingw_w64GccDPInt32Opt\lib'),
        'FOAM_SOLVERS': os.path.join(folder, r'OpenFOAM-5.x\applications\solvers'),
        'FOAM_SRC': os.path.join(folder, r'OpenFOAM-5.x\src'),
        'FOAM_TUTORIALS': os.path.join(folder, r'OpenFOAM-5.x\tutorials'),
        'FOAM_USER_APPBIN': os.path.join(folder,
            r'ofuser-of5\platforms\mingw_w64GccDPInt32Opt\bin'),
        'FOAM_USER_LIBBIN': os.path.join(folder,
            r'ofuser-of5\platforms\mingw_w64GccDPInt32Opt\lib'),
        'FOAM_UTILITIES': os.path.join(folder, r'OpenFOAM-5.x\applications\utilities'),
        'PATH': ';'.join([
            os.path.join(folder, r'msys64\usr\bin'),
            os.path.join(folder, r'ThirdParty-5.x\platforms\mingw_w64Gcc\MS-MPI-7.1\bin'),
            os.path.join(folder, r'ofuser-of5\platforms\mingw_w64GccDPInt32Opt\bin'),
            os.path.join(folder, r'site\5.x\platforms\mingw_w64GccDPInt32Opt\bin'),
            os.path.join(folder, r'OpenFOAM-5.x\platforms\mingw_w64GccDPInt32Opt\bin'),
            os.path.join(folder, r'OpenFOAM-5.x\bin'),
            os.path.join(folder, r'OpenFOAM-5.x\wmake'),
            os.path.join(folder, r'msys64\mingw64\bin'),
            os.path.join(folder, r'AddOns\gnuplot\bin'),
            os.path.join(folder, r'AddOns\notepad2'),
            os.path.join(folder, r'ofuser-of5\platforms\mingw_w64GccDPInt32Opt\lib'),
            os.path.join(folder,
                r'OpenFOAM-5.x\platforms\mingw_w64GccDPInt32Opt\lib\MS-MPI-7.1'),
            os.path.join(folder,
                r'ThirdParty-5.x\platforms\mingw_w64GccDPInt32\lib\MS-MPI-7.1'),
            os.path.join(folder, r'ThirdParty-5.x\platforms\mingw_w64Gcc\MS-MPI-7.1\lib'),
            os.path.join(folder, r'site\5.x\platforms\mingw_w64GccDPInt32Opt\lib'),
            os.path.join(folder, r'OpenFOAM-5.x\platforms\mingw_w64GccDPInt32Opt\lib'),
            os.path.join(folder, r'ThirdParty-5.x\platforms\mingw_w64GccDPInt32\lib'),
            os.path.join(folder, r'OpenFOAM-5.x\platforms\mingw_w64GccDPInt32Opt\lib\dummy')
        ])
    }

    return bluecfd_env_base
