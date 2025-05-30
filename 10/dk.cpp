#include <iostream>
#include <vector>
#include <queue>
#include <limits>

using namespace std;

const int INF = numeric_limits<int>::max();
vector<int> dijkstra(int V, vector<vector<pair<int, int>>>& listaDeAdjacencia, int origem){
    vector<int> dist(V, INF);
    
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

    dist[origem] = 0;
    pq.push({0, origem});

    while (!pq.empty()){
        int distU = pq.top().first;
        int u = pq.top().second;
        pq.pop();

        if (distU > dist[u]){
            continue;
        }

        for (const auto& vizinho: listaDeAdjacencia[u]){
            int v = vizinho.first;
            int pesoArestaV = vizinho.second;

            if (dist[u]+pesoArestaV < dist[v]){
                dist[v] = dist[u]+pesoArestaV;

                pq.push({dist[v], v});
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

    vector<int> dist = dijkstra(V, listaDeAdjacencia, origem);

    for (int i = 0; i < V; i++){
        if (dist[i] == INF){
            cout << "INF" << endl;
        } else {
            cout << dist[i] << endl;
        }
    }

    return 0;
}