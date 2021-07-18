#include <bits/stdc++.h> 
using namespace std; 
typedef long long ll; 

int main() {
    ll n; 
    cin >> n; 
    ll arr[n]; 
    ll moves = 0; 
    ll diff = 0; 

    for (ll i = 0; i < n; i++) {
        cin >> arr[i]; 
    } 
    for (ll j = 1; j < n; j++) {
        if (arr[j] < arr[j-1]) {
            diff = arr[j-1] - arr[j]; 
            moves += diff; 
            arr[j] = arr[j-1]; 
        }
    }
    

    cout << moves; 
}
