from libv1 import gen_samples, write_samples

samples = gen_samples(440, 10)
write_samples("example1.wav", samples)
