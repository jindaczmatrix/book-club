package bst;

import com.sun.source.tree.Tree;

public class RootNode<T extends Comparable<T>> implements TreeNode<T> {
    private T data;
    private TreeNode<T> left;
    private TreeNode<T> right;

    public RootNode(T data, TreeNode<T> left, TreeNode<T> right) {
        this.data = data;
        this.left = left;
        this.right = right;
    }

    /**
     * @param data
     * @return
     */
    @Override
    public TreeNode addNode(T data) {
        if (this.data.compareTo(data) > 0) {
            this.left = this.left.addNode(data);
        } else if (this.data.compareTo(data) < 0) {
            this.right = this.right.addNode(data);
        }
        return this;
    }

    /**
     * @return
     */
    @Override
    public int size() {
        return 1 + this.left.size() + this.right.size();
    }

    /**
     * @return
     */
    @Override
    public int height() {
        int leftHeight = this.left.height();
        int rightHeight = this.right.height();
        if (leftHeight > rightHeight) {
            return leftHeight + 1;
        }
        return rightHeight + 1;
    }

    /**
     * @param data
     * @return
     */
    @Override
    public boolean present(T data) {
        return this.data.equals(data) || this.left.present(data) || this.right.present(data);
    }

    /**
     * @return
     */
    @Override
    public T minimum() {
        T min;
        min = this.left.minimum();
        if (min == null) {
            return this.data;
        }
        return min;
    }

    /**
     * @return
     */
    @Override
    public T maximum() {
        T max;
        max = this.right.maximum();
        if (max == null) {
            return this.data;
        }
        return max;
    }

    /**
     * @return
     */
    @Override
    public String preOrder() {
        String result = " " + this.data.toString();
        result += " " + this.left.preOrder();
        result += " " + this.right.preOrder();
        return result;
    }

    @Override public String inOrder() {
        String result = " " + this.left.inOrder();
        result += " " + this.data.toString();
        result += " " + this.right.inOrder();
        return result;
    }

    @Override public String postOrder() {
        String result = " " + this.left.postOrder();
        result += " " + this.right.postOrder();
        result += " " + this.data.toString();
        return result;
    }
}
