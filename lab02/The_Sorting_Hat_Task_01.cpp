#include <bits/stdc++.h>

using namespace std;

int n;
vector<string> names;
vector<pair<int, int>> bravery_scores;
map<int, string> names_map;
map<int, int> bravery_scores_map;

void quick_sort(){

    
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   

    cin >> n;
    string name;
    int score;

    for (int i=0; i<n; i++){
        cin >> name;
        names.push_back(name);
        names_map[i] = name;
    }

    for (int i=0; i<n; i++){
        cin >> score;
        bravery_scores.push_back({score, i});
        bravery_scores_map[score] = i;
    }

    quick_sort();

    for (int i=0; i<n; i++){
        cout << bravery_scores[i].first << endl;
    }

    return 0;
}
