#include <iostream>
#include <vector>
#include <queue>
#include <limits>

using namespace std;

const long long INF = numeric_limits<long long>::max();

vector<long long> bellmanFord(int V, vector<vector<pair<int, int>>>& listaDeAdjacencia, int origem, int maxInter = -1){
    vector<long long> dist(V, INF);

    dist[origem] = 0;

    if (maxInter < 0) maxInter = V-1;  

    for (int i = 0; i < maxInter; i++){
        for (int u = 0; u < V; u++){
            for (const auto& vizinho: listaDeAdjacencia[u]){
                int v = vizinho.first;
                int pesoArestaV = vizinho.second;

                if (dist[u] != INF && dist[u] + pesoArestaV < dist[v]){
                    dist[v] = dist[u] + pesoArestaV;
                }
            }
        }
    }


    return dist;
}

int main(){
    int V, E;
    cin >> V >> E;

    vector<vector<pair<int, int>>> listaDeAdjacencia(V);

    for (int i = 0; i < E; i++){
        int u, v, peso;
        cin >> u >> v >> peso;

        listaDeAdjacencia[u-1].push_back({v-1, -peso});
    }

    vector<long long> dist = bellmanFord(V, listaDeAdjacencia, 0);
    vector<long long> dist2 = bellmanFord(V, listaDeAdjacencia, 0, V);

    if(dist[V-1] == INF || dist2[V-1] != dist[V-1]){
        cout << "inf\n";
    } else {
        cout << -dist[V-1] << "\n";
    }

    return 0;
}