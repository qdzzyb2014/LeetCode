struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode *cur;
    struct ListNode *res = cur;
    if(!l1 && l2)
            return l2;
        if(l1 && !l2)
            return l1;
        if(!l1 && !l2)
            return NULL;
    while (l1 && l2) {
        if(l1->val <= l2->val)
        {
            cur->next = l1;
            l1 = l1->next;
        }
        else
        {
            cur->next = l2;
            l2 = l2->next;
        }
        cur = cur->next;
    }
    if(l1)
        cur->next = l1;
    if(l2)
        cur->next = l2;
  
    return res->next;
}