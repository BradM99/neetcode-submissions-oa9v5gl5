class Solution {
public:
    bool isPalindrome(string s) {

        int l = 0;
        int r = s.size() - 1;
        char left;
        char right;

        while(l < r) {
            while (l < r && !isalnum(s[l])) {
                l++;
            }  
            while (l < r && !isalnum(s[r])) {
                r--;
            }

            left = tolower(static_cast<unsigned char>(s[l]));
            right = tolower(static_cast<unsigned char>(s[r]));
            if(left != right) {
                return false;
            }
            l++;
            r--;
        }
    return true;
    }
};
