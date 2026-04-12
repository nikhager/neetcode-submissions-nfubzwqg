class Solution {
public:
    bool isAnagram(string s, string t) {
        if ( s.size() != t.size() ) return false;

        std::unordered_map<char, int> count;

        for ( size_t i = 0; i < s.size(); ++i ) {
            count[s[i]]++;
            count[t[i]]--;
        }

        for ( const auto& p : count ) {
            if ( p.second != 0 ) return false;
        }
        return true;
    }
};
