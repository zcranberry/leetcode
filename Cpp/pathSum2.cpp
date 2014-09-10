//http://oj.leetcode.com/problems/path-sum-ii/
#include<iostream>
#include<vector>
#include<iterator>
using namespace std;
class TreeNode {
public:
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x, TreeNode* l = NULL, TreeNode* r = NULL) : val(x), left(l), right(r) {}
};


class Solution {
public:
    vector<int> path;
    vector<vector<int> > res;
    vector<vector<int> > hasPathSum(TreeNode * root , int sum){
    	path.clear();
    	res.clear();
        if (root != NULL)
            firTravel(root,sum);
        return res;
    }
    void firTravel(TreeNode *root, int sum, int accum = 0) {
        accum += root->val;
        path.push_back(root->val);
        if (accum == sum && !root->left && !root->right){
            res.push_back(path); 
        }
        if (root->left)
            firTravel(root->left, sum,accum);
        if (root->right)
            firTravel(root->right, sum,accum);
        accum -= root->val;
        path.pop_back();
    }
};


int main()
{
   TreeNode* node7 = new TreeNode(7);
   TreeNode* node2 = new TreeNode(2);
   TreeNode* node5b = new TreeNode(5);
   TreeNode* node1 = new TreeNode(1);
   TreeNode* node11 = new TreeNode(11,node7,node2);
   TreeNode* node4b = new TreeNode(4 ,node5b,node1);
   TreeNode* node13 = new TreeNode(13);
   TreeNode* node4a = new TreeNode(4, node11);
   TreeNode* node8  = new TreeNode(8,node13,node4b);
   TreeNode* node5a  = new TreeNode(5,node4a,node8);
   Solution* slu = new Solution();
   slu->hasPathSum(node5a, 22);
   vector<vector<int> >::iterator iter1;
   vector<int>::iterator iter2;
   for (iter1 = slu->res.begin(); iter1 != slu->res.end(); iter1++)
   {
        for (iter2 = (*iter1).begin(); iter2 != (*iter1).end() ; iter2++)
            cout<<*iter2<<",";
        cout<<endl;
   }

   return 0;
}

