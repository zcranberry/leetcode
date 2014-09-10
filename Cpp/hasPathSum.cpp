/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

//一开始用了static变量，WA,leetcode每次都用同一个instance,static变量不会清零，慎用
class Solution {
public:
   bool hasPathSum(TreeNode * root , int sum){
	   if (root == NULL)
		   return false;
	   return firTravel(root,sum);
   }
   bool firTravel(TreeNode *root, int sum, int accum = 0) {
       if (root == NULL)
            return false;
       accum += root->val;
       if (accum == sum && !root->left && !root->right)
           return true;
       if (root->left)
           if (firTravel(root->left, sum,accum))
               return true;
       if (root->right)
           if (firTravel(root->right, sum,accum))
               return true;
       accum -= root->val;
       return false;
   }
};
