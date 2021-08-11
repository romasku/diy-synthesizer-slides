#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <cmath>

const int SAMPLE_RATE = 44100;

std::vector<double> gen_samples(double freq, double duration_sec) {
	int samples_cnt = duration_sec * SAMPLE_RATE;
	std::vector<double> res;
	for (int sample_idx = 0; sample_idx < samples_cnt; sample_idx++) {
	    double time = sample_idx * 1.0 / SAMPLE_RATE;
		res.push_back(sin(time * 2 * M_PI * freq));
	}
	return res;
}

struct WavHeader {
    char chunkId[4];
    int chunkSize;
    char format[4];
    char subchunk1Id[4];
    int subchunk1Size;
    short audioFormat;
    short numChannels;
    int sampleRate;
    int byteRate;
    short blockAlign;
    short bitsPerSample;
    char subchunk2Id[4];
    int subchunk2Size;
};

void write_samples(std::string const& filename, std::vector<double> & samples) {
    int cnt_samples = samples.size();
    int data_size = cnt_samples * 2;
    std::ofstream file(filename, std::ios::out | std::ios::binary);
    WavHeader header = {
        {'R', 'I', 'F', 'F'},
        36 +data_size,
        {'W', 'A', 'V', 'E'},
        {'f', 'm', 't', ' '},
        16,
        1,
        1,
        44100,
        88200,
        2,
        16,
        {'d', 'a', 't', 'a'},
        data_size
    };
    file.write((char*)&header, sizeof(header));

    short short_range = (1 << 15) - 1;
    for (int i = 0; i < samples.size(); i++) {
        short sample = samples[i] * short_range;
        file.write((char*)&sample, sizeof(short));
    }
    file.close();

}

int main()
{
    std::vector<double> samples = gen_samples(440.0, 10.0);
    write_samples("test-cpp.wav", samples);
    return 0;
}
