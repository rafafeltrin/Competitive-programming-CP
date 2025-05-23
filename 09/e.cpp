#include <bits/stdc++.h>
using namespace std;


#define UNVISITED -1
#define VISITED 1
typedef pair <int,int> ii;
typedef vector<ii> vii;
typedef vector <int> vi;

vector<int> lista_adjacencia[1000000];

vi dfs_num;

void dfs(int u){
    dfs_num[u] = VISITED;
    for (auto i : lista_adjacencia[u]) {
        if (dfs_num[i] == UNVISITED) {
            dfs_num[i] = VISITED;
            dfs(i);
        }
    }
}
int matriz[1000][1000];

int main() {
    int n = 0, m = 0;

    std::cin >> n >> m;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            char c;
            std::cin >> c;
            matriz[i][j] = (c == '#') ? 0 : 1;
        }
    }

    int encontrados = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (matriz[i][j] == 1) {
                lista_adjacencia[i*m+j].push_back(i*m+j);
                if (i > 0 && matriz[i-1][j] == 1) {
                    lista_adjacencia[i*m+j].push_back((i-1)*m+j);
                }
                if (i < n-1 && matriz[i+1][j] == 1) {
                    lista_adjacencia[i*m+j].push_back((i+1)*m+j);
                }
                if (j > 0 && matriz[i][j-1] == 1) {
                    lista_adjacencia[i*m+j].push_back(i*m+j-1);
                }
                if (j < m-1 && matriz[i][j+1] == 1) {
                    lista_adjacencia[i*m+j].push_back(i*m+j+1);
                }
            }
        }
    }

    int numero_quartos = 0;
    dfs_num.assign(n*m, UNVISITED);
    for (int i = 0; i < n*m; i++) {
        if (!lista_adjacencia[i].empty()) {
            if (dfs_num[i] == UNVISITED) {
                dfs(i);
                numero_quartos++;
            }
        }
    }

    std::cout << numero_quartos << std::endl;

    return 0;
}

