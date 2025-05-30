#include <iostream>
#include <vector>
#include <queue>
#include <limits>

using namespace std;

const long long INF = numeric_limits<long long>::max();

vector<long long> dijkstra(int V, vector<vector<pair<int, int>>>& listaDeAdjacencia, int origem){
    vector<long long> dist(V, INF);
    
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

        listaDeAdjacencia[u-1].push_back({v-1, peso});
        listaDeAdjacencia[v-1].push_back({u-1, peso});
    }

    

    vector<long long> dist = dijkstra(V, listaDeAdjacencia, origem-1);

    long long l;
    cin >> l;
    long long x = 0;
    
    for (int i = 0; i < V; i++){
        if (dist[i] == l){
            x++;
        }
    }

    for(int u = 0; u < V; u++){
        if (dist[u] == INF) {
            continue;
        }
        for(auto const& edge : listaDeAdjacencia[u]){ 
            int v = edge.first;
            int peso_aresta_uv = edge.second;

            if (dist[v] == INF) {
                continue;
            }

            if(u < v){
                bool x1 = (dist[u] < l && (long long)dist[u] + peso_aresta_uv > l);

                bool x2 = (dist[v] < l && (long long)dist[v] + peso_aresta_uv > l);
                
                long long soma_dist_mais_peso = (long long)dist[u] + dist[v] + peso_aresta_uv;

                int silos_nesta_aresta = 0;

                if (x1 && soma_dist_mais_peso >= 2LL * l) {
                    silos_nesta_aresta++;
                }
                if (x2 && soma_dist_mais_peso >= 2LL * l) {
                    silos_nesta_aresta++;
                }
                if (silos_nesta_aresta == 2 && soma_dist_mais_peso == 2LL * l) {
                    x++; 
                } else if (silos_nesta_aresta > 0) {
                    x += silos_nesta_aresta;
                }
            }
        }
    }

    cout << x << endl;
    return 0;
}