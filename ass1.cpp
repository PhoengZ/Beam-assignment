#include <iostream>
#include <vector>

using namespace std;

int main(){
    vector<int> v;
    int n;
    int h = 0, w = 0; 
    while (cin >> n){
        v.push_back(n);
        h = max(h,n);
        w+= 2*n;
    }   
    vector<vector<char>>result(h, vector<char>(w,' '));
    int idx = 0;
    for (auto &e:v){
        int t = h-1;
        for (int i = 0;i<e;i++){
            result[t--][idx++] = '/';
        }
        t++;
        for (int i = 0;i<e;i++){
            result[t++][idx++] = '\\';
        }
    }
    for (int i = 0;i<h;i++){
        for (int j = 0;j<w;j++){
            cout << result[i][j];
        }
        cout << endl;
    }

    return 0;
}