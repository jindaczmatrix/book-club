package bst;

public class LeafNode <T extends Comparable<T>> implements TreeNode<T> {
    /**
     * @param data
     * @return
     */
    @Override
    public TreeNode addNode(T data) {
        return new RootNode<T>(data, new LeafNode<T>(), new LeafNode<T>());
    }

    /**
     * @return
     */
    @Override
    public int size() {
        return 0;
    }

    /**
     * @return
     */
    @Override
    public int height() {
        return 0;
    }

    /**
     * @param data
     * @return
     */
    @Override
    public boolean present(T data) {
        return false;
    }

    /**
     * @return
     */
    @Override
    public T minimum() {
        return null;
    }

    /**
     * @return
     */
    @Override
    public T maximum() {
        return null;
    }

    /**
     * @return
     */
    @Override
    public String preOrder() {
        return "";
    }

    /**
     * @return
     */
    @Override
    public String inOrder() {
        return "";
    }

    /**
     * @return
     */
    @Override
    public String postOrder() {
        return "";
    }
}
