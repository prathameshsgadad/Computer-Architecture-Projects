import os
import subprocess
import itertools

stats_values = '/home/eng/s/sxs220196/CA_Project/Outputs_456'

BPtype = '/home/eng/s/sxs220196/CA_Project/src/cpu/pred/BranchPredictor.py'
BPtemplate = '/home/eng/s/sxs220196/Automation/automate_456hmmer/BPpytemplate.py'

CPUtype = '/home/eng/s/sxs220196/CA_Project/src/cpu/simple/BaseSimpleCPU.py'
CPUtemplate = '/home/eng/s/sxs220196/Automation/automate_456hmmer/CPUtypetemplate.py'

runGem5_456hmmer = '/home/eng/s/sxs220196/CA_Project/benchmarks/456.hmmer/runGem5.sh'
runGem5template_456hmmer = '/home/eng/s/sxs220196/Automation/automate_456hmmer/runGem5_456hmmer.sh'

sconspath = 'build/X86/gem5.opt'

BTBentries = [2048, 4096]
LBPlp = TBPlp = [1024, 2048]
BMBPgp = BMBPcp = [2048, 4096, 8192]
TBPgp = TBPcp = [4096, 8192]

def rewriteshell(loc1):
	
	f2 = open(runGem5template_456hmmer, "r")
	lines = f2.readlines()
	f2.close()
	f2 = open(runGem5_456hmmer, "w")
	for line in lines:
		if('~/m5out' in line):
			line = line.replace('~/m5out', loc1)
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
		tempfolder1 = '/456LocalBP' + str(c[0]) + '_' + str(c[1]) + '/'
		outloc1 = stats_values + tempfolder1
		
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
		rewriteshell(outloc1)

		subprocess.call(['scons', sconspath], cwd="/home/eng/s/sxs220196/CA_Project")
	
		subprocess.call(['sh', runGem5_456hmmer], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		print("Completed iteration of " + tempfolder1)

					
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

		tempfolder1 = '/456BiModeBP' + str(c[0]) + '_' + str(c[1]) + '_' + str(c[2]) + '/'
		outloc1 = stats_values + tempfolder1

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

		rewriteshell(outloc1)

		subprocess.call(['scons', sconspath], cwd="/home/eng/s/sxs220196/CA_Project")
		
		subprocess.call(['sh', runGem5_456hmmer], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		print("Completed iteration of " + tempfolder1)

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

		tempfolder1 = '/456TournamentBP' + str(c[0]) + '_' + str(c[1]) + '_' + str(c[2]) + '_' + str(c[3]) + '/'
		outloc1 = stats_values + tempfolder1

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

		rewriteshell(outloc1)

		subprocess.call(['scons', sconspath], cwd="/home/eng/s/sxs220196/CA_Project")

		subprocess.call(['sh', runGem5_456hmmer], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		print("Completed iteration of " + tempfolder1)

if __name__ == '__main__':
	print("##############################Starting the automate_456hmmer#########################")
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

