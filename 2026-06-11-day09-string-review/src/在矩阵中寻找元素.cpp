class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        for(const auto& row:matrix)//循环编列每一行
        {
            auto it = lower_bound(row.begin(),row.end(),target);//对于每一行，调用二分查找函数，返回一个迭代器
            if(it!=row.end() && *it == target)//判断返回的迭代器的值
            {
                return true;
            }
        }
        return false;
        
    }
};