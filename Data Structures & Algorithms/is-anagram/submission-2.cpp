class Solution {
public:
    bool isAnagram(string s, string t) {
        if ( s.size() != t.size() ) return false;

        std::map<char, int> letters_s;
        std::map<char, int> letters_t;

        for ( int i = 0; i < s.size(); ++i ) {
            letters_s[s[i]]++;
            letters_t[t[i]]++;
        }

        return ( letters_s == letters_t );
    }
};
