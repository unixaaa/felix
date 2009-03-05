import fbuild
from fbuild.path import Path
from fbuild.record import Record

import buildsystem

# ------------------------------------------------------------------------------

def build_runtime(phase):
    path = Path('src/tre')
    buildsystem.copy_hpps_to_rtl(
        fbuild.buildroot / 'config/target/flx_target_tre_config.h',
        path / 'tre-regex.h',
        path / 'tre-config.h',
    )

    dst = fbuild.buildroot / 'lib/rtl/tre'
    srcs = Path.glob('src/tre/*.c')
    includes = [fbuild.buildroot / 'config/target']
    macros = ['BUILD_TRE']

    return Record(
        static=buildsystem.build_c_static_lib(phase, dst, srcs,
            includes=includes,
            macros=macros),
        shared=buildsystem.build_c_shared_lib(phase, dst, srcs,
            includes=includes,
            macros=macros))

def build_flx(builder):
    return buildsystem.copy_flxs_to_lib(Path('src/tre/*.flx').glob())
