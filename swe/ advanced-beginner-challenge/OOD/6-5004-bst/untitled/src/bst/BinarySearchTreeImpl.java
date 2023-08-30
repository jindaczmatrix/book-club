package bst;

public class BinarySearchTreeImpl <T extends Comparable<T>> implements BinarySearchTree<T> {
    private TreeNode<T> root;
    public BinarySearchTreeImpl() {
        this.root = new LeafNode<T>();
    }
    /**
     * Add data to the binary search tree. This is ignored if the data item is
     * already present
     *
     * @param data the data to be added
     */
    @Override
    public void add(T data) {
        if (data == null) {
            return;
        }
        this.root = this.root.addNode(data);
    }

    /**
     * Return the size of the tree (i.e., the number of elements in this tree).
     *
     * @return The number of elements in this tree
     */
    @Override
    public int size() {
        return this.root.size();
    }

    /**
     * Return the height of the tree..
     *
     * @return the height of the tree
     */
    @Override
    public int height() {
        return this.root.height();
    }

    /**
     * Find if this data is present in the binary search tree.
     *
     * @param data the data to be searched
     * @return true if the data is present, false otherwise
     */
    @Override
    public boolean present(T data) {
        return this.root.present(data);
    }

    /**
     * Determine and return the minimum data in the tree as defined by its ordering.
     *
     * @return the minimum data if it exists, null otherwise
     */
    @Override
    public T minimum() {
        return this.root.minimum();
    }

    /**
     * Determine and return the maximum data in the tree as defined by its ordering.
     *
     * @return the maximum data if it exists, null otherwise
     */
    @Override
    public T maximum() {
        return this.root.maximum();
    }

    /**
     * Returns a string that present all the data in the tree, sorted in ascending
     * order. The string is formatted as [d1 d2 ... dn]
     *
     * @return a string containing the preorder traveral
     */

    @Override public String preOrder() {
        String result = this.root.preOrder();
        result = result.strip();
        result = result.replaceAll(" [ ]*", " ");
        return "[" + result + "]";
    }

    @Override public String inOrder() {
        String result = this.root.inOrder();
        result = result.strip();
        result = result.replaceAll(" [ ]*", " ");
        return "[" + result + "]";
    }

    @Override public String postOrder() {
        String result = this.root.postOrder();
        result = result.strip();
        result = result.replaceAll(" [ ]*", " ");
        return "[" + result + "]";
    }

    @Override public String toString() {
        return this.inOrder();
    }
}
