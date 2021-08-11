from libv1 import gen_samples2, write_samples, get_freq

samples = []
samples += gen_samples2(349.22, 0.4)

samples += gen_samples2(261.62, 0.4)
samples += gen_samples2(349.22, 0.4)
samples += gen_samples2(261.62, 0.4)
samples += gen_samples2(349.22, 0.4)

samples += gen_samples2(329.62, 0.4)
samples += gen_samples2(329.62, 0.8)
samples += gen_samples2(329.62, 0.4)

samples += gen_samples2(261.62, 0.4)
samples += gen_samples2(329.62, 0.4)
samples += gen_samples2(261.62, 0.4)
samples += gen_samples2(329.62, 0.4)

samples += gen_samples2(349.22, 0.4)
samples += gen_samples2(349.22, 0.8)
samples += gen_samples2(349.22, 0.4)

write_samples("example3.wav", samples)
