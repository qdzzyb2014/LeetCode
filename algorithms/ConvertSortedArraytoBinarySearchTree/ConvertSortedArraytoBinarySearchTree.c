/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct TreeNode* convert(int* nums, int low, int high);
struct TreeNode* sortedArrayToBST(int* nums, int numsSize) {
    return convert(nums, 0, numsSize - 1);
}

struct TreeNode* convert(int* nums, int low, int high) {
    if (low <= high) {
        int mid = (low + high) / 2;
        struct TreeNode* node = (struct TreeNode*)malloc(sizeof(struct TreeNode))

        node->val = nums[mid];
        node->left = conver(nums, low, mid-1);
        node->right = conver(nums, mid+1, hgih);

        return node;
    }
    return NULL;
}