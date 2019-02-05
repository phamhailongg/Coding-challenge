def helper_dp(data, k, memo) : 
    if k == 0 : 
        return 1 
    s = data.length - k 
    if data[s] == "0" : 
        return 0 
    if memo[k] != null : 
        return memo[k]
    result = helper_dp(data, k - 1, memo)
    if k >= 2 and int(data[s : s + 2]) <= 26 : 
        result += helper_dp(data, k - 2, memo)
    memo[k] = result    
    return result 
def num_ways_dp(data) : 
    
    return helper_dp(data, data.length, memo)      

num_ways_dp("12345")
