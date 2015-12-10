import java.util.*;

public class DrawTree {
    public ArrayList<String> output = new ArrayList<String>();
    public String depth = " ";

    public void print(HashMap<String, ArrayList<String>> map,
                    String root) {
        ArrayList<String> children;
        children = map.get(root);
        depth += " ";
        int size = children.size();
        for (int i = 0; i < size; i++) {
            String curnode = children.get(i);
            int curnodesize = map.get(curnode).size();
            output.add(depth + "+-" + curnode);
            // System.out.println(depth +"+-" + curnode);
            if (curnodesize != 0 && i != size - 1) {
                depth += "|";
                print(map, curnode);
                depth = depth.substring(0, depth.length() - 1);
            } else if (curnodesize != 0 && i == size - 1) {
                depth += " ";
                print(map, curnode);
                depth = depth.substring(0, depth.length() - 1);
            }
        }
        depth = depth.substring(0, depth.length() - 1); // backtrack
    }

    public String[] draw(int[] parents, String[] names) {
        // construct a hashmap with parents as keys and arraylists of children
        // as values
        HashMap<String, ArrayList<String>> map = new HashMap<>();
        String root = null;

        for (String name : names) {
            map.put(name, new ArrayList<String>());
        }
        for (int i = 0; i < parents.length; i++) {
            if (parents[i] == -1) {
                root = names[i];
            } else {
                ArrayList<String> myList;
                myList = map.get(names[parents[i]]);
                myList.add(names[i]);
            }
        }

        System.out.println(map.toString());
        output.add("+-" + root);

        print(map, root);
        for (String result : output) {
            System.out.println(result);
        }
        return output.toArray(new String[output.size()]);
    }

    /*
     * public static void main(String[] args) { // int[] parents = { -1, 0, 1,
     * 1, 2, 2, 3, 3, 0, 8, 8, 9, 9, 10, // 10 }; // String[] names = { "A",
     * "B", "C", "D", "E", "F", "G", "H", // "I", "J", "K", "L", "M", "N", "O"
     * }; int[] parents = {1,2,3,4,6,6,-1}; String[] names =
     * {"A","B","C","D","E","F","G"}; DrawTree test = new DrawTree(); //
     * System.out
     * .println(Arrays.toString(test.getParent(parents,names,"Root")));
     * test.draw(parents, names); }
     */
}

/*
 * 
 * this is my output (only the vertical pipes are not right): +-A +-B +-C | +-E
 * | +-F +-D | +-G | +-H +-I +-J | +-L | +-M +-K | +-N | +-O
 * 
 * This is the correct output: {"+-A", "  +-B", "  | +-C", "  | | +-E",
 * "  | | +-F", "  | +-D", "  |   +-G", "  |   +-H", "  +-I", "    +-J",
 * "    | +-L", "    | +-M", "    +-K", "      +-N", "      +-O" }
 */
