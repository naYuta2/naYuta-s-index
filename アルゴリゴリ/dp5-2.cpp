/*
問題: 
*/

#include<iostream>
#include<vector>
using namespace std;

int main(){
    int N, M;

    cin >> N >> M;

    vector<int> a(N, 0);
    for (int i = 0; i < N; i++){
        cin >> a[i];
    }

    vector<vector<bool>> dp(N+1, vector<bool>(M+1, false));
    dp[0][0] = true;
    for (int i = 1; i < N+1; i++){
        for (int j = 1; j < M+1; j++){
            if (dp[i-1][j]){
                dp[i][j] = true;
            }
            if (j-a[i-1] < M+1 && j-a[i-1] >= 0){
                if (dp[i][j-a[i]]){
                    dp[i][j] = true;
                }
            }
        }
    }
    
    if (dp[N][M]){
        cout << "Yes" << endl;
    }
    else {
        cout << "No" << endl;
    }
}
