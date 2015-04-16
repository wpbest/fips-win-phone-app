"""verb import test"""

from mod import log

#-------------------------------------------------------------------------------
def run(proj_dir, fips_dir, args) :
    log.info("fips-win-phone-app test verb executed")

#-------------------------------------------------------------------------------
def help() :
    log.info(log.YELLOW +
            "fips fips-win-phone-app\n"
            + log.DEF +
            "    test an imported project verb")
