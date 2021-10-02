#include <iostream>
#include <math.h>
#include <string>
#include <iomanip>
using namespace std;

void tabular(int total, float arango[]);
void cambiov(int total, int ncambio, float arango[]);
void correct(int total, float arango[]);

int main() {

	int total;
	int x, f = 0;
	cout<<"Total de valores: "; cin>>total;
	float arango[total];
	try {

		if (total == false) {
			throw total;
		}
	} catch(int e) {
		cout<<"\n     SE ESPERABA UN VALOR NUMERICO"<<endl;
	}
	for (size_t i = 0; i < total; i++) {

		f += 1;
		cout<<"Valor "<<f<<": "; cin>>arango[i];
	}
		try {
			for (size_t i = 0; i < total; i++) {

				if (arango[i] == false) {
					throw 2;
				}
			}
			correct(total, arango);
		} catch(int ex) {
			cout<<"\n     SE ESPERABA UN VALOR NUMERICO"<<endl;
		}

	return 0;
}

void tabular(int total, float arango[]) {
	int g = 0;
	float intervalo = round(1 + (3.3 * log10(total)));
	float minimo = arango[0];
	float maximo = arango[0];

	for (size_t i = 0; i < total; i++) {

		if (minimo > arango[i]) {
			minimo = arango[i];
		}
	}

	for (size_t i = 0; i < total; i++) {

		if (maximo < arango[i]) {
			maximo = arango[i];
		}
	}

	cout<<"\n valor minimo: "<<minimo<<endl;
	cout<<" valor maximo: "<<maximo<<endl;
	float rango = maximo - minimo;
	cout<<" rango: "<<rango<<endl;
  cout<<" intervalo: "<<intervalo<<endl;
	float c = rango/intervalo;
	cout<<" c: "<<c<<endl;
	int interv = rango/c;
	float n[interv];
	float iminimo[interv];
	int h[interv];

	for (size_t i = 0; i < interv; i++) {
		float y = minimo+c*(i+1);

		for (size_t j = 0; j < total; j++) {

			if ((y > arango[j] && y - c <= arango[j]) && i != interv-1) {
				g += 1;
			}
			if (i == interv-1 && (y >= arango[j] && y - c <= arango[j])) {
				g += 1;
			}
		}
		h[i] = g;
		g = 0;
	}

	for (size_t i = 0; i < interv; i++) {
		float y = minimo+c*(i+1);
		float ye = minimo+c*(i);

		if (i == 0) {
			iminimo[i] = (minimo);
			n[i] = (y);
		} else {
			iminimo[i] = (ye);
			n[i] = (y);
		}
	}

	cout<<"______________________________"<<endl;
	cout<<"|        N        |    FA    |"<<endl;
	cout<<"|─────────────────|──────────|"<<endl;

	for (size_t i = 0; i < interv; i++) {
		cout<<"| "<<fixed<<setprecision(2)<<iminimo[i]<<"   -   "<<n[i]<<" |    "<<h[i]<<"     |"<<endl;
		cout<<"|─────────────────|──────────|"<<endl;
	}
}

void cambiov(int total, int ncambio, float arango[]) {
	float acambio;
	string aceptar;
	cout<<"\nQue valor quieres poner?" <<endl;
	cout<<"Valor: "; cin>>acambio;
	cout<<"Se cambiara: "<<arango[ncambio]<<" por: "<<acambio<<" es correcto?"<<endl;
	cout<<"[si/no]: "; cin>>aceptar;
	int no = aceptar.compare("no");
	int si = aceptar.compare("si");

	if (no == 0) {
		cambiov(total, ncambio, arango);
	}

	if (si == 0) {
		arango[ncambio] = acambio;
		cout<<"Valor "<<ncambio+1<<": "<<arango[ncambio];
    correct(total, arango);
	} else {
		cout<<"     OPCION INCORRECTA"<<endl;
	}
}

void correct (int total, float arango[]) {
	string cambio;
	int ncambio;
	cout<<"\nTodos los valores son correctos?\n"<<"[si/no]: "; cin>>cambio;
	int no = cambio.compare("no");
	int si = cambio.compare("si");

	if (no == 0) {
		cout<<"Que valor quieres cambiar?"<<endl;
		cout<<"Valor: "; cin>>ncambio;
		ncambio = ncambio - 1;
		cout<<"Valor a cambiar: "<<arango[ncambio];
		cambiov(total, ncambio, arango);
	}

	if (si == 0) {
		tabular(total, arango);
	} else {
		cout<<"     OPCION INCORRECTA";
	}

}
