# -- an example to run SPEC 429.mcf on gem5, put it under 429.mcf folder --
export GEM5_DIR=/home/eng/s/sxs220196/CA_Project
export BENCHMARK=/home/eng/s/sxs220196/CA_Project/benchmarks/458.sjeng/src/benchmark
export ARGUMENT=/home/eng/s/sxs220196/CA_Project/benchmarks/458.sjeng/data/test.txt
time $GEM5_DIR/build/X86/gem5.opt -d ~/m5out $GEM5_DIR/configs/example/se.py -c $BENCHMARK -o $ARGUMENT -I 5000000 --cpu-type=atomic --caches --l2cache --l1d_size=128kB --l1i_size=128kB --l2_size=1MB --l1d_assoc=2 --l1i_assoc=2 --l2_assoc=1 --cacheline_size=64
