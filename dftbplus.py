# tools to manage dftb+ code with SIMAN

import copy

from siman import header

def write_dftb_hsd(name='noname', st, driver='geomopt', slakos='./slakos/3ob', kspacing=0.2, forces='y', mulliken='n'):
	"""generate input file .hsd from siman Structure() to run dftb+ code"""

	# name: filename. Generated file will be called name.hsd
	# st: SIMAN structure object
	# driver: 
	# slakos: path to Slater-Koster parameters set
	# kspacing: 


	# analogue of st.write_poscar





	return path


def write_dftb_geometry(st, file=False):
	# just geometry block of input .hsd file

	xred = st.xred
	typat = st.typat
	

