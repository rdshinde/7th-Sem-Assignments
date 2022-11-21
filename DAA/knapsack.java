class knapsack{
    public static void main(String[] args){
        int[] weights = {1, 2, 3, 4, 5};
        int[] values = {1, 6, 10, 16, 20};
        int capacity = 10;
        int[][] table = new int[weights.length + 1][capacity + 1];
        for(int i = 0; i < weights.length; i++){
            for(int j = 0; j < capacity; j++){
                if(weights[i] > j){
                    table[i + 1][j + 1] = table[i][j + 1];
                }else{
                    table[i + 1][j + 1] = Math.max(table[i][j + 1], table[i][j + 1 - weights[i]] + values[i]);
                }
            }
        }
        System.out.println(table[weights.length][capacity]);
    }
}