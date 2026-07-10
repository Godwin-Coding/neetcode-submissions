class Solution {
    public boolean hasDuplicate(int[] nums) {
        Collection<Integer> seen = new ArrayList<>(nums.length);
        for (int i : nums){
            if (seen.contains(i)) {
                return true;}
            else{
                seen.add(i);}
        }
        return false;
        }
    }