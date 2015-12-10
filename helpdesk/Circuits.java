public class Circuits {
    private static int[][] matrix;

    public int howLong(String[] connects, String[] costs) {
        // fill in code here
        int N = connects.length;
        matrix = new int[N][N];
        for (int i = 0; i < N; i++)
            for (int j = 0; j < N; j++)
                matrix[i][j] = 10000 * 10000;

        for (int i = 0; i < N; i++) {
            String[] conn = connects[i].split(" ");
            String[] cost = costs[i].split(" ");
            for (int j = 0; j < conn.length; j++) {
                if (conn[j].equals("")) {
                    break;
                }
                matrix[i][Integer.parseInt(conn[j])] = -Integer
                                .parseInt(cost[j]);
            }
        }

        int min = 10000 * 10000;
        for (int k = 0; k < N; k++) {
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    if (matrix[i][j] > matrix[i][k] + matrix[k][j]) {
                        matrix[i][j] = matrix[i][k] + matrix[k][j];
                    }
                    if (matrix[i][j] < min) {
                        min = matrix[i][j];
                    }
                }
            }
        }

        return -min;
    }

    // public static void main(String[] args) {
    // String[] connects = { "1 2", "2", "" };
    // String[] costs = { "5 3", "7", "" };
    // Circuits test = new Circuits();
    // System.out.println(test.howLong(connects, costs));
    // }
}
