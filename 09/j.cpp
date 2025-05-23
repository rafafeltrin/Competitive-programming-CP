#include <bits/stdc++.h>
using namespace std;

const int MAXN = 2e5 + 5;

int subordinados[MAXN];

vector<int> lista_adjacencia[MAXN];

void dfs(int v)
{
    for (auto i : lista_adjacencia[v]) {
        dfs(i);
        subordinados[v] += subordinados[i] + 1;
    }
}

int main()
{
    int n;
    cin >> n;

    for (int i = 0; i < n-1; i++) {
        int x;
        cin >> x;
        lista_adjacencia[x].push_back(i+2);
    }

    dfs(1);

    for (int i = 1; i <= n; i++) {
        cout << subordinados[i] << " ";
    }
    cout << endl;

    return 0;
}