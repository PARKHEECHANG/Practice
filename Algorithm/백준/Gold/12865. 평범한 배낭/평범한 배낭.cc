#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <stack>
using namespace std;

int dp[101][100001];
int w[101];
int v[101];

int main() {

	int n, limit;
	int res;
	cin >> n >> limit;

	for (int i = 1; i <= n; i++) {
		cin >> w[i] >> v[i];
	}

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= limit; j++) {

			if (j >= w[i]) {
				dp[i][j] = max(dp[i - 1][j], dp[i-1][j-w[i]]+ v[i]);
			}
			else {
				dp[i][j] = dp[i - 1][j];
			}

		}
	}

	cout << dp[n][limit];

}