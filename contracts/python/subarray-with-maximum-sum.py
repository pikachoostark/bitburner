def subarray_with_maximum_sum(arr: list) -> float:
    local_sum = 0
    global_sum = float("-inf")

    for num in arr:
        local_sum += num
        global_sum = max(global_sum, local_sum)

        if (local_sum < 0):
            local_sum = 0
    
    return global_sum

def main():
    assert subarray_with_maximum_sum([-10, -5]) == -5

    # contract-585764-Netburners.cct: 2500 faction reputation for Netburners
    assert subarray_with_maximum_sum([-10,-8,3,1,-2,3,-5,7,2,-8,-4,10,3,0,6,-10,2,7,10,-10,6,4,10,-5,-2,-9]) == 38
    # contract-384565.cct: $75.000m
    assert subarray_with_maximum_sum([-3,1,3,-1,9,0,10,-1,6,-9,8,-3,0,7,1,4,3,-10,-5,-3,-2,-10,-9,-1,-8,-3,-1,-7,-9,2,10,9,5,4,-6,-9,0,-4,9]) == 38

if __name__ == "__main__":
    main()
