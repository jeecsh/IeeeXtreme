#include <bits/stdc++.h>
using namespace std;
using ll = long long;

inline ll largestRectangleArea(vector<int>& heights, const int N) {
    ll maxArea = 0;
    vector<int> stack;
    stack.reserve(N + 1);  // Preallocate stack size
    
    for (int i = 0; i <= N; i++) {
        int currHeight = (i == N) ? 0 : heights[i];
        
        while (!stack.empty() && heights[stack.back()] > currHeight) {
            int h = heights[stack.back()];
            stack.pop_back();
            
            ll width = stack.empty() ? i : i - stack.back() - 1;
            maxArea = max(maxArea, h * width);
        }
        stack.push_back(i);
    }
    
    return maxArea;
}

inline ll maxrec(const int N, const int X, vector<int>& A) {
    ll maxArea = largestRectangleArea(A, N);
    
    // Optimize by checking if modification would help
    for (int i = 0; i < N; i++) {
        if (A[i] < X) {
            int originalHeight = A[i];
            A[i] = X;
            
            maxArea = max(maxArea, largestRectangleArea(A, N));
            A[i] = originalHeight;
        }
    }
    
    return maxArea;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int N, X;
    cin >> N >> X;
    
    vector<int> A(N);
    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }
    
    cout << maxrec(N, X, A) << '\n';
    
    return 0;
}