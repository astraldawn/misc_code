import java.util.*;

public class Internet {
    private static boolean[] visited;
    private static int[][] matrix;

    public int articulationPoints(String[] routers) {
        int n = routers.length;
        matrix = new int[n][n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++)
                matrix[i][j] = 0;
        }

        /*
         * The way the adjList is built is not correct. The edges are
         * bi-directional. I will suggest for this problem to use an adj matrix
         * instead, as you can delete a node x in M[1..N][1..M] by setting
         * M[x][1..M] = 0 and M[1..N][x] = 0
         */

        for (int i = 0; i < routers.length; i++) {
            String[] newlist = routers[i].split(" ");
            for (int j = 0; j < newlist.length; j++) {
                matrix[i][Integer.parseInt(newlist[j])] = 1;
            }

        }

        int count = 0;
        for (int i = 0; i < matrix.length; i++) {

            /*
             * This is not correct. Do not use adjacency list when you need to
             * remove edges. This deletes all edges from i --> anything, but
             * does not remove the edges from anything --> i
             */
            ArrayList<Integer> store = new ArrayList<>();
            for (int j = 0; j < matrix[i].length; j++) {
                if (matrix[i][j] == 1) {
                    matrix[i][j] = 0;
                    matrix[j][i] = 0;
                    store.add(j);
                }
            }

            int a = matrix.length;
            visited = new boolean[a];

            // Run DFS
            for (int j = 0; j < matrix.length; j++) {
                if (j != i) {
                    dfs(j);
                    break;
                }
            }

            // Check for visited
            for (int j = 0; j < matrix.length; j++) {
                if (!visited[j] && j != i) {
                    count++;
                    break;
                }
            }

            // Simpler way to save / restore
            for(int j = 0; j <store.size();j++) {
                int x = store.get(j);
                matrix[x][i] = matrix[i][x] = 1;
            }
        }
        return count;
    }

    private void dfs(int currentNodeName) {
        visited[currentNodeName] = true;
        for (int i = 0; i < matrix.length; i++) {
            if (matrix[currentNodeName][i] != 0) {
                if (!visited[i]) {
                    dfs(i);
                }
            }
        }
    }

    public static void main(String[] args) {
//        String[] routers = { "3 10", "8 4", "7 10", "0 9", "6 1",
//                        "9", "4 11", "11 2", "1", "3 5", "0 2", "7 6" };
//        String [] routers = {"2","2 3","0 1 3 4","1 2","2 5 6","4 6","4 5"};
        String [] routers = {"1 2","0 2","0 1 3","2"};
        Internet test = new Internet();
        System.out.println(test.articulationPoints(routers));
    }
}
