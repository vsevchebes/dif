find_library(FFTW_LIBRARY
  NAMES ${FFTW_LIBRARY_NAMES}
  PATHS
    /usr/lib
	/usr/lib/fftw
	/usr/lib/fftw3
    /usr/local/lib
    /usr/local/lib/fftw
	/usr/local/lib/fftw3
    "$ENV{LIB_DIR}/lib"
    "$ENV{LIB}"
)
