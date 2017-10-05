#include <bits/stdc++.h>
using namespace std;
#define MAXN 256
#define HEADER L"Abacateabacatexupaime"
#define MAXNOISESIZE 1000000

wstring text, key, ciphered, deciphered;
wchar_t mapForward[MAXN], mapBack[MAXN];
int currentKeyPos, nCarac;

//Knuth-Morris-Pratt
class KMP{
private:
	wstring P;
	vector<int> b;
	int m, n;
public:
	KMP(wstring _P){
		P = _P;
		m = P.size();
		b.resize(m+1);
		b[0] = -1;
		for(int i = 0, j = -1; i < m;) {
			while (j >= 0 && P[i] != P[j]) j = b[j];
			i++; j++;
			b[i] = j;
		}
	}
	int match(wstring T){
		n = T.size();
		for (int i=0, j=0; i < n;) {
			while (j >= 0 && T[i] != P[j]) j = b[j];
			i++; j++;
			if (j == m) return i - j;
		}
		return -1;
	}
};

void buildMap() {
	int j=1;
	nCarac = 0;
	for(int i=0; i<MAXN; i++) {
		if (i < 32 || (i > 126 && i < 161)) continue;
		nCarac++;
		mapBack[j] = i;
		mapForward[i] = j;
		j++;
	}
}

void readFiles(char *keyPath, char *textPath) {
	
	//auxuliary variables
	wchar_t carac;
	
	//read text
	FILE * inputFile = fopen(textPath, "r");
	while(!feof(inputFile)) {
		fscanf(inputFile, "%lc", &carac);
		text.push_back(carac);
	}
	fclose(inputFile);
	inputFile = NULL;
	
	//read key
	FILE * keyFile = fopen(keyPath, "r");
	while(!feof(keyFile)) {
		fscanf(keyFile, "%lc", &carac);
		key.push_back(carac);
	}
	fclose(keyFile);
	keyFile = NULL;
}

wchar_t per[MAXN], inv[MAXN];

//gets next permutation
void getNextPermutation() {
	for(int i=1; i<=nCarac; i++) {
		int delta = 0;
		for(int j=0; j<3; j++) {
			delta = delta*10 + key[currentKeyPos] - L'0';
			currentKeyPos++;
			if (currentKeyPos >= key.size()) currentKeyPos = 0;
		}
		delta %= (nCarac - i + 1);
		swap(per[i], per[i+delta]);
	}
	for(int i=1; i<=nCarac; i++) {
		inv[per[i]] = i;
	}
}

void initialize() {
	currentKeyPos = 0;
	buildMap();
	for(wchar_t i=1; i<=nCarac; i++) per[i] = inv[i] = i;
}

void cipher() {
	
	//start from beggining to sync with decipher
	initialize();
	ciphered.clear();
	
	//insert random amount of noise
	wstring header = wstring(HEADER);
	KMP kmp(header);
	srand(time(NULL));
	int noiseSize = rand()%MAXNOISESIZE;
	do {	//try until header is not part of message
		ciphered.clear();
		for(int i=0; i<noiseSize; i++) {
			ciphered.push_back(mapBack[rand()%nCarac + 1]);
		}
	} while(kmp.match(ciphered) != -1);
	
	//add header
	ciphered = ciphered + header;
	
	//add more noise with size of header
	for(int i=0; i<(int)header.size(); i++) {
		ciphered.push_back(mapBack[rand()%nCarac + 1]);
	}
	
	//add ciphered message
	for(int i=0; i<(int)text.size(); i++) {
		getNextPermutation();
		ciphered.push_back(mapBack[per[mapForward[text[i]]]]);
	}
}

void decipher() {
	
	//search for header
	wstring header = wstring(HEADER);
	KMP kmp(header);
	int headerStartPos = kmp.match(ciphered);
	int messageStartPos = headerStartPos + 2*header.size();
	
	//decipher
	initialize();
	deciphered.clear();
	for(int i=messageStartPos; i<(int)ciphered.size(); i++) {
		getNextPermutation();
		deciphered.push_back(mapBack[inv[mapForward[ciphered[i]]]]);
	}
}

void cipheranalisys() {
	int freq[MAXN], tot = 0;
	memset(&freq, 0, sizeof freq);
	for(int i=0; i<(int)ciphered.size(); i++) {
		tot++;
		freq[ciphered[i]]++;
	}
	printf("Character apararences:\n");
	for(int i=0; i<MAXN; i++) {
		printf("%lc: %d, %.4f%%\n", wchar_t(i), freq[i], freq[i]*100.0/tot);
	}
}

int main(int argc, char *argv[]) {
	
	//read files
	readFiles(argv[2], argv[1]);
	
	wprintf(L"Texto:\n|%s|\n", text.c_str());
	
	cipher();
	wprintf(L"Mensagem (%u):\n|%s|\n", ciphered.size(), ciphered.c_str());
	
	cipheranalisys();
	
	decipher();
	wprintf(L"Decifrado:\n|%s|\n", deciphered.c_str());
	
	return 0;
}