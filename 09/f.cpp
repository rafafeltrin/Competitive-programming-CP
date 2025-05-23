#include <bits/stdc++.h>
using namespace std;

#define UNVISITED -1
#define VISITED 1
typedef pair <int,int> ii;
typedef vector<ii> vii;
typedef vector <int> vi;
const int MAXN = 2e5 + 5;

vector<int> lista_adjacencia[MAXN];

vi topo_sort;

vi dfs_num;

void dfs(int v)
{
    dfs_num[v] = VISITED;
    for (auto i : lista_adjacencia[v]) {
        if (dfs_num[i] == UNVISITED) {
            dfs(i);
        }
    }
    topo_sort.push_back(v);
}


int main()
{
    int n,m;
    cin >> n >> m;
    for (int i = 0; i < m; i++) {
        int x,y;
        cin >> x >> y;
        lista_adjacencia[x].push_back(y);
    }
    
    for (int i = 1; i <= n; i++) {
        sort(lista_adjacencia[i].begin(), lista_adjacencia[i].end());
    }

    topo_sort.clear();
    dfs_num.assign(n+1, UNVISITED);

    //for deve ser decrescente
    for (int i = 1; i <= n; i++) {
        if (dfs_num[i] == UNVISITED) {
            dfs(i);
        }
    }

    reverse(topo_sort.begin(), topo_sort.end());
    
    bool unique = true;
    for (int i = 0; i + 1 < (int)topo_sort.size(); i++) {
        int u = topo_sort[i], v = topo_sort[i+1];
        if (!binary_search(lista_adjacencia[u].begin(),
                           lista_adjacencia[u].end(),
                           v)) {
            unique = false;
            break;
        }
    }
    if (!unique) {
        cout << "No\n";
        return 0;
    }

    vector<int> A(n+1);
    for (int i = 0; i < n; i++) {
        A[topo_sort[i]] = i + 1;
    }

    cout << "Yes\n";
    for (int i = 1; i <= n; i++) {
        cout << A[i] << (i == n ? '\n' : ' ');
    }
    
    return 0;
}