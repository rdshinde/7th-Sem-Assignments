class travellingSalesman{
    public static void main(String[] args){
        int[][] graph = {{0, 10, 15, 20},
                         {10, 0, 35, 25},
                         {15, 35, 0, 30},
                         {20, 25, 30, 0}};
        int n = graph.length;
        travellingSalesman tsp = new travellingSalesman();
        tsp.tsp(graph);
    }
    void tsp(int[][] graph){
        int n = graph.length;
        int[] vertex = new int[n];
        for (int i=0; i<n; i++)
            vertex[i] = i;
        int min_path = Integer.MAX_VALUE;
        do{
            int current_pathweight = 0;
            int k = vertex[0];
            for (int i=0; i<n-1; i++){
                current_pathweight += graph[k][vertex[i+1]];
                k = vertex[i+1];
            }
            current_pathweight += graph[k][vertex[0]];
            min_path = Math.min(min_path, current_pathweight);
        }while (nextPermutation(vertex));
        System.out.println(min_path);
    }
    boolean nextPermutation(int[] p){
        for (int a = p.length - 2; a >= 0; --a){
            if (p[a] < p[a + 1])
                for (int b = p.length - 1; ; --b){
                    if (p[b] > p[a]){
                        int t = p[a];
                        p[a] = p[b];
                        p[b] = t;
                        for (++a, b = p.length - 1; a < b; ++a, --b){
                            t = p[a];
                            p[a] = p[b];
                            p[b] = t;
                        }
                        return true;
                    }
                }
        }
        return false;
    }
}