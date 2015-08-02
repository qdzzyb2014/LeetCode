void merge_sort(int* nums, int low, int high);
void merge(int* nums, int low, int mid, int high);

int majorityElement(int* nums, int numsSize) {
    merge_sort(nums, 0, numsSize - 1);
    return nums[numsSize/2];
}

void merge_sort(int* nums, int low, int high) {
    if (low < high){
        int mid = (low + high)/2;

        merge_sort(nums, low, mid);
        merge_sort(nums, mid+1, high);
        merge(nums, low, mid, high);
    }
}

void merge(int* nums, int low, int mid, int high){
    int *aux = (int*)malloc((high-low+1)*sizeof(int));
    int left = low;
    int right = mid+1;
    int paux = 0

    while (left <= mid && right <= high) {
        if (nums[left] <= nums[right])
            aux[paux++] = nums[left++];
        else:
            aux[paux++] = nums[right++];
    }

    while (left <= mid)
        aux[paux++] = nums[left++];
    while (right <= high)
        aux[paux++] = nums[right++];

    for (paux = low; paux <= high; paux++)
        nums[paux] = aux[paux - low];
}