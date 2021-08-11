from libv1 import gen_samples, write_samples, get_freq

samples = gen_samples(0, 1.2)
samples += gen_samples(349.22, 0.4)

samples += gen_samples(261.62, 0.4)
samples += gen_samples(349.22, 0.4)
samples += gen_samples(261.62, 0.4)
samples += gen_samples(349.22, 0.4)

samples += gen_samples(329.62, 0.4)
samples += gen_samples(0, 0.01)
samples += gen_samples(329.62, 0.8)
samples += gen_samples(0, 0.01)
samples += gen_samples(329.62, 0.4)

samples += gen_samples(261.62, 0.4)
samples += gen_samples(329.62, 0.4)
samples += gen_samples(261.62, 0.4)
samples += gen_samples(329.62, 0.4)

samples += gen_samples(349.22, 0.4)
samples += gen_samples(0, 0.01)
samples += gen_samples(349.22, 0.8)
samples += gen_samples(0, 0.01)
samples += gen_samples(349.22, 0.4)

write_samples("example2.wav", samples)
