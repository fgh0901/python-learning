class Solution {
public:
    string reverseWords(string s) {
        int left = 0;
        int right = s.size()-1;
        vector<string> v;//创建一个vector容器来保存每一个单词
        string temp;//创建临时的temp来保存每一个临时的单词，以便于放入vector
        while(left<=right)
        {
            temp.clear();//清空当前temp中的所有元素
            while(left<=right&&s[left]!=' ')//循环内的作用是，将空格前的单词放入temp中
            {
                temp+=s[left];
                left++;
            }
            left++;
            if(!temp.empty())v.push_back(temp);//如果当前元素不为空，那么放入vector容器中，避免了元素为空放入导致空格的情况
        }
        reverse(v.begin(),v.end());//使用了algorithm库中的reverse函数，反转了vector中的元素顺序
        string ss;//新建一个临时的string
        for(int i=0;i<v.size();i++)//循环内容为将每一个单词加入字符串中
        {
            ss+=v[i];
            ss+=' ';
        }
        ss.erase(ss.size()-1);
        return ss;
        
    }
};