#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(){
    int n;
    string alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    int l = alphabet.length();
    cin >> n;
    vector<uint32_t> v(l);
    uint32_t c = 1;
    for (int i = 1;i<=l;i++){
        v[i-1] = c*2 - 1;
        c*=2;
    }
    int idx = l-1;
    // for (int i = 0;i<l;i++){
    //     cout<<v[i]<<endl;
    // }
    n--;
    while (v[idx] != n){
        for (int i = idx;i>=0;i--){
            if (v[i] < n){
                idx = i;
                break;
            }else if (v[i] == n){
                cout << alphabet[i] <<endl;
                return 0;
            }
        }
        n-= v[idx];
    }
    cout << alphabet[idx] <<endl;
    return 0;
}   