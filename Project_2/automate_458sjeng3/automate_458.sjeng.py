import os
import subprocess
import itertools

stats_values = '/home/eng/s/sxs220196/CA_Project/OutputsP3/Outputs_458_1'

runGem5_458sjeng = '/home/eng/s/sxs220196/CA_Project/benchmarks/458.sjeng/runGem5.sh'
runGem5template_458sjeng = '/home/eng/s/sxs220196/CA_Project/automate_458sjeng3/runGem5_458sjeng.sh'

sconspath = 'build/X86/gem5.opt'

L1i_sizes = L1d_sizes = [2**i for i in range(6,8)]
L2_sizes = [2**i for i in range(11,14)]
L1i_assoc = L1d_assoc = [1,2,4]
L1_assoc = [1,2,4]
L2_assoc = [1,2]
cache_block_size = [32, 64]

def runconfigs():

	l = [L1d_sizes, L1i_sizes, L2_sizes, L1_assoc, L2_assoc, cache_block_size]
	combos = list(itertools.product(*l))

	for c in combos[:len(combos)//2]:
		tempfolder2 = '/458L1S_' + str(c[0]) + '_' + str(c[1]) + '_L2S_' + str(c[2]) + '_L1a_'+str(c[3]) + '_L2a_' + str(c[4]) + '_cbs_' + str(c[5])
		outloc2 = stats_values+ tempfolder2

		f2 = open(runGem5template_458sjeng, "r")
		lines = f2.readlines()
		f2.close()
		f2 = open(runGem5_458sjeng, "w")
		for line in lines:
			if('~/m5out' in line):
				line = line.replace('~/m5out', outloc2)
			if('L1d_size' in line):
				line = line.replace('L1d_size', str(c[0])+'kB')
			if('L1i_size' in line):
				line = line.replace('L1i_size', str(c[1])+'kB')
			if('L2_size' in line):
				if(c[2] == 1024):
					line = line.replace('L2_size', str(1)+'MB')
				else:
					line = line.replace('L2_size', str(c[2])+'kB')
			if('L1d_assoc' in line):
				line = line.replace('L1d_assoc', str(c[3]))
			if('L1i_assoc' in line):
				line = line.replace('L1i_assoc', str(c[3]))
			if('L2_assoc' in line):
				line = line.replace('L2_assoc', str(c[4]))
			if('cache_block_size' in line):
				line = line.replace('cache_block_size', str(c[5]))			
			f2.write(line)
		f2.close()

		#subprocess call to run shell script
		subprocess.call(['sh', runGem5_458sjeng], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		print("Completed iteration of " + tempfolder2)
	
if __name__ == '__main__':
	print("Starting Script")

	print("Running 1st Set Of Cache Configurations On 458.sjeng")
	runconfigs()

	print("All Simulations Completed")
