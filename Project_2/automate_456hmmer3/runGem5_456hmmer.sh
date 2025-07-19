export GEM5_DIR=/home/eng/s/sxs220196/CA_Project
export BENCHMARK=/home/eng/s/sxs220196/CA_Project/benchmarks/456.hmmer/src/benchmark
export ARGUMENT=/home/eng/s/sxs220196/CA_Project/benchmarks/456.hmmer/data/bombesin.hmm
time $GEM5_DIR/build/X86/gem5.opt -d ~/m5out $GEM5_DIR/configs/example/se.py -c $BENCHMARK -o $ARGUMENT -I 50000000 --cpu-type=timing --caches --l2cache --l1d_size=L1d_size --l1i_size=L1i_size --l2_size=L2_size --l1d_assoc=L1d_assoc --l1i_assoc=L1i_assoc --l2_assoc=L2_assoc --cacheline_size=cache_block_size
