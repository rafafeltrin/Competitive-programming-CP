#include <bits/stdc++.h>
using namespace std;

#define UNVISITED -1
#define VISITED 1
typedef pair <int,int> ii;
typedef vector<ii> vii;
typedef vector <int> vi;
const int MAXN = 150000 + 200;

vector<int> lista_adjacencia[MAXN];

vi dfs_num;

long long vertices = 0;
long long edges = 0;

void dfs(int v)
{
    vertices++;
    dfs_num[v] = VISITED;
    for (auto i : lista_adjacencia[v]) {
        edges++;
        if (dfs_num[i] == UNVISITED) {
            dfs(i);
        }
    }
}

int main()
{
    int n,m;
    cin >> n >> m;
    for (int i = 0; i < m; i++) {
        int x,y;
        cin >> x >> y;
        lista_adjacencia[x].push_back(y);
        lista_adjacencia[y].push_back(x);
    }

    dfs_num.assign(n+1, UNVISITED);

    for (int i = 1; i <= n; i++) {
        if (dfs_num[i] == UNVISITED) {
            dfs(i);
            if (edges != vertices*(vertices-1)) {
                cout << "NO" << endl;
                return 0;
            }
            edges = 0;
            vertices = 0;
        }
    }

    
    cout << "YES" << endl;
    return 0;
}
