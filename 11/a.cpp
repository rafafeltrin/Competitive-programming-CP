#include <iostream>
#include <vector>
#include <climits> 
#include <cstdio>  

using namespace std;

const int INF = INT_MAX; 

void floydWarshall(vector<vector<int>>& dist, vector<vector<int>>& pred) {
    int V = dist.size();

    for (int k = 0; k < V; k++) {
        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                if (dist[i][k] != INF && dist[k][j] != INF) { 
                    if (dist[i][k] + dist[k][j] < dist[i][j]) {
                        dist[i][j] = dist[i][k] + dist[k][j];
                        pred[i][j] = pred[k][j];
                    }
                }
            }
        }
    }
}

void imprimirCaminhoCorrigido(int inicio, int fim, 
                              const vector<vector<int>>& pred) {
    if (inicio == fim) {
        cout << inicio + 1;
    } else if (pred[inicio][fim] == inicio) { 
        cout << inicio + 1 << " " << fim + 1;
    } else {
        imprimirCaminhoCorrigido(inicio, pred[inicio][fim], pred);
        cout << " " << fim + 1;
    }
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);                 

    int V;
    cin >> V;
    int caso = 1;
    while (V != 0) {

        vector<vector<int>> dist(V, vector<int>(V, INF));
        vector<vector<int>> pred(V, vector<int>(V));

        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                pred[i][j] = i; 
            }
            dist[i][i] = 0; 
        }

        for (int i = 0; i < V; i++) { 
            int arestas;
            cin >> arestas;
            for (int j = 0; j < arestas; j++) {
                int v_destino, peso; 
                cin >> v_destino >> peso;
                dist[i][v_destino - 1] = peso; 
                                           
            }
        }

        int entrada, saida; 
        cin >> entrada >> saida;
        entrada--; 
        saida--;   

        floydWarshall(dist, pred);

        cout << "Case " << caso << ": Path = ";
        
        if (dist[entrada][saida] == INF) {

        } else {
            imprimirCaminhoCorrigido(entrada, saida, pred);
        }
        
        cout << "; " << dist[entrada][saida] << " second delay" << endl;
        caso++;
        cin >> V;
    }

    return 0;
}