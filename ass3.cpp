#include <iostream>
#include <string>
#include <vector>
#include <map>
using namespace std;

int main(){
    int n;
    string alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    int l = alphabet.length();
    cin >> n;
    vector<uint32_t> v(l);
    map<int,char> m;
    uint32_t c = 2;
    m[1] = 'A';
    v[0] = 1;
    for (int i = 1;i<=l;i++){
        v[i] = c;
        m[c] = alphabet[i]; 
        c*=2;
    }
    int idx = l-1;
    while (true){
        for (int i = idx;i>=0;i--){
            if (v[i] < n){
                n-= v[i];
                idx = i;
                break;
            }else if (v[i] == n){
                cout << m[n];
                return 0;
            }
        }
    }
    return 0;
}   