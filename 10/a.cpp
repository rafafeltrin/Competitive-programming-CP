#include <iostream>
#include <vector>
#include <queue>
#include <limits>

using namespace std;

const int INF = numeric_limits<int>::max();

vector<int> bellmanFord(int V, vector<vector<pair<int, int>>>& listaDeAdjacencia, int origem){
    vector<int> dist(V, INF);

    dist[origem] = 0;

    for (int i = 0; i< V; i++){
        for (int u = 0; u < V; u++){
            for (const auto& vizinho: listaDeAdjacencia[u]){
                int v = vizinho.first;
                int pesoArestaV = vizinho.second;

                if (dist[u] != INF && dist[u] + pesoArestaV < dist[v]){
                    if (i == V - 1){
                        cout << "NEGATIVE CYCLE" << endl;
                        return {};
                    }
                    dist[v] = dist[u] + pesoArestaV;
                }
            }
        }
    }
    return dist;
}

int main(){
    int V, E, origem;
    cin >> V >> E >> origem;

    vector<vector<pair<int, int>>> listaDeAdjacencia(V);

    for (int i = 0; i < E; i++){
        int u, v, peso;
        cin >> u >> v >> peso;

        listaDeAdjacencia[u].push_back({v, peso});
    }

    vector<int> dist = bellmanFord(V, listaDeAdjacencia, origem);

    if (dist.empty()){
        return 0;
    }

    for (int i = 0; i < V; i++){
        if (dist[i] == INF){
            cout << "INF" << endl;
        } else {
            cout << dist[i] << endl;
        }
    }

    return 0;
}