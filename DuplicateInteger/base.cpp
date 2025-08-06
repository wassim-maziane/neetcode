#include <bits/stdc++.h>

typedef long long ll;
using namespace std;

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);

  ll n;
  int element;
  set<int> s;

  cin >> n;

  for (int i = 0; i < n; i++) {
    cin >> element;
    if (s.find(element) != s.end()) {
      cout << "false";
      return 0;
    }
    s.insert(element);
  }
  cout << "true";
}
