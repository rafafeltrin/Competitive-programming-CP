#include <iostream>
#include <vector>
#include <climits>
using namespace std;

const int INF = INT_MAX;

void floydWarshall(vector<vector<int>>& dist) {
    int V = dist.size();

    for (int k = 0; k < V; k++) {
        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                if (dist[i][k] != INT_MAX && dist[k][j] != INT_MAX) {
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
                }
            }
        }
    }
}

int main() {
    int V, E;
    cin >> V >> E;

    vector<vector<int>> dist(V, vector<int>(V, INF));

    for (int i = 0; i < V; i++) {
        dist[i][i] = 0; // Distância de um vértice para ele mesmo é 0
    }

    for (int i = 0; i < E; i++) {
        int u, v, peso;
        cin >> u >> v >> peso;
        dist[u][v] = peso;
    }

    floydWarshall(dist);

    for (int i = 0; i < V; i++) {
        for (int j = 0; j < V; j++) {
            if (dist[i][j] == INF) {
                cout << "INF ";
            } else {
                cout << dist[i][j] << " ";
            }
        }
        cout << endl;
    }

    return 0;
}