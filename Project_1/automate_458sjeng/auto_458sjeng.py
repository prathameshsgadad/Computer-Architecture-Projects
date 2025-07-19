import os
import subprocess
import itertools

rootoutput = '/home/eng/s/sxs220196/CA_Project/Outputs_458'

BPtype = '/home/eng/s/sxs220196/CA_Project/src/cpu/pred/BranchPredictor.py'
BPtemplate = '/home/eng/s/sxs220196/CA_Project/automate_458sjeng/BPpytemplate.py'

CPUtype = '/home/eng/s/sxs220196/CA_Project/src/cpu/simple/BaseSimpleCPU.py'
CPUtemplate = '/home/eng/s/sxs220196/CA_Project/automate_458sjeng/CPUtypetemplate.py'

runGem5_458sjeng = '/home/eng/s/sxs220196/CA_Project/benchmarks/458.sjeng/runGem5.sh'
runGem5template_458sjeng = '/home/eng/s/sxs220196/CA_Project/automate_458sjeng/runGem5_458sjeng.sh'

sconspath = 'build/X86/gem5.opt'

BTBentries = [2048, 4096]
LBPlp = TBPlp = [1024, 2048]
BMBPgp = BMBPcp = [2048, 4096, 8192]
TBPgp = TBPcp = [4096, 8192]

def rewriteshell(loc2):
	
	f2 = open(runGem5template_458sjeng, "r")
	lines = f2.readlines()
	f2.close()
	f2 = open(runGem5_458sjeng, "w")
	for line in lines:
		if('~/m5out' in line):
			line = line.replace('~/m5out', loc2)
		f2.write(line)
	f2.close()

def runLocalBP():

	f3 = open(CPUtemplate, "r")
	lines = f3.readlines()
	f3.close()
	f3 = open(CPUtype, "w")
	for line in lines:
		if('BPtype' in line):
			line = line.replace('BPtype', 'LocalBP()')
		f3.write(line)
	f3.close()

	l = [BTBentries, LBPlp]
	combos = list(itertools.product(*l))
	for c in combos:
		tempfolder2 = '/458LocalBP' + str(c[0]) + '_' + str(c[1]) + '/'
		outloc2 = rootoutput + tempfolder2
		
		f1 = open(BPtemplate, "r")
		lines = f1.readlines()
		f1.close()
		f1 = open(BPtype,'w')
		for line in lines:
			if('L1' in line):
				line = line.replace('L1', str(c[0]))
			if('L2' in line):
				line = line.replace('L2', str(c[1]))
			if('L3' in line):
				line = line.replace('L3', str(BMBPgp[0]))
			if('L4' in line):
				line = line.replace('L4', str(BMBPcp[0]))
			if('L5' in line):
				line = line.replace('L5', str(TBPlp[0]))
			if('L6' in line):
				line = line.replace('L6', str(TBPgp[0]))
			if('L7' in line):
				line = line.replace('L7', str(TBPcp[0]))
			f1.write(line)
		f1.close()
		rewriteshell(outloc2)
		
		subprocess.call(['scons', sconspath], cwd="/home/eng/s/sxs220196/CA_Project")

		subprocess.call(['sh', runGem5_458sjeng], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		print("Completed iteration of " + tempfolder2)

							
def runBiModeBP():
	f3 = open(CPUtemplate, "r")
	lines = f3.readlines()
	f3.close()
	f3 = open(CPUtype, "w")
	for line in lines:
		if('BPtype' in line):
			line = line.replace('BPtype', 'BiModeBP()')
		f3.write(line)
	f3.close()

	l = [BTBentries, BMBPgp, BMBPcp]
	combos = list(itertools.product(*l))
	for c in combos:

		tempfolder2 = '/458BiModeBP' + str(c[0]) + '_' + str(c[1]) + '_' + str(c[2]) + '/'
		outloc2 = rootoutput + tempfolder2

		f1 = open(BPtemplate, "r")
		lines = f1.readlines()
		f1.close()
		f1 = open(BPtype,'w')
		for line in lines:
			if('L1' in line):
				line = line.replace('L1', str(c[0]))
			if('L2' in line):
				line = line.replace('L2', str(LBPlp[0]))
			if('L3' in line):
				line = line.replace('L3', str(c[1]))
			if('L4' in line):
				line = line.replace('L4', str(c[2]))
			if('L5' in line):
				line = line.replace('L5', str(TBPlp[0]))
			if('L6' in line):
				line = line.replace('L6', str(TBPgp[0]))
			if('L7' in line):
				line = line.replace('L7', str(TBPcp[0]))
			f1.write(line)
		f1.close()

		subprocess.call(['scons', sconspath], cwd="/home/eng/s/sxs220196/CA_Project")

		rewriteshell(outloc2)

		subprocess.call(['sh', runGem5_458sjeng], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		print("Completed iteration of " + tempfolder2)



def runTournamentBP():

	f3 = open(CPUtemplate, "r")
	lines = f3.readlines()
	f3.close()
	f3 = open(CPUtype, "w")
	for line in lines:
		if('BPtype' in line):
			line = line.replace('BPtype', 'TournamentBP()')
		f3.write(line)
	f3.close()

	l = [BTBentries, TBPlp, TBPgp, TBPcp]
	combos = list(itertools.product(*l))
	for c in combos:

		tempfolder2 = '/458TournamentBP' + str(c[0]) + '_' + str(c[1]) + '_' + str(c[2]) + '_' + str(c[3]) + '/'
		outloc2 = rootoutput + tempfolder2

		f1 = open(BPtemplate, "r")
		lines = f1.readlines()
		f1.close()
		f1 = open(BPtype,'w')
		for line in lines:
			if('L1' in line):
				line = line.replace('L1', str(c[0]))
			if('L2' in line):
				line = line.replace('L2', str(LBPlp[0]))
			if('L3' in line):
				line = line.replace('L3', str(BMBPgp[0]))
			if('L4' in line):
				line = line.replace('L4', str(BMBPcp[0]))
			if('L5' in line):
				line = line.replace('L5', str(c[1]))
			if('L6' in line):
				line = line.replace('L6', str(c[2]))
			if('L7' in line):
				line = line.replace('L7', str(c[3]))
			f1.write(line)
		f1.close()

		rewriteshell(outloc2)

		subprocess.call(['scons', sconspath], cwd="/home/eng/s/sxs220196/CA_Project")

		subprocess.call(['sh', runGem5_458sjeng], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		print("Completed iteration of " + tempfolder2)



if __name__ == '__main__':
	print("##############################Starting the Automation#########################")
	print("------------------------------------------------------------------------------")

	print("Running the LocalBP for all configurations on both the benchmarks")
	print("------------------------------------------------------------------------------")
	runLocalBP()

	print("Running the BiModeBP for all configurations on both the benchmarks")
	print("------------------------------------------------------------------------------")
	runBiModeBP()

	print("Running the TournamentBP for all configurations on both the benchmarks")
	print("------------------------------------------------------------------------------")
	runTournamentBP()

	print("###########################All Simulations completed##########################")

