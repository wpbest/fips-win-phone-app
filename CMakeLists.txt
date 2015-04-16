#
# project: fips-win-phone-app
#
cmake_minimum_required(VERSION 3.0)

# include the fips main cmake file
get_filename_component(FIPS_ROOT_DIR "../fips" ABSOLUTE)
include("${FIPS_ROOT_DIR}/cmake/fips.cmake")

fips_setup()
fips_project(fips-win-phone-app)
fips_add_subdirectory(src)
fips_finish()


