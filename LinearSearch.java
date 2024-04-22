public class LinearSearch {
    public static void main(String[] args) {
        int[] arr = {12, 34, 10, 6, 40};
        int key = 40;
        System.out.println(findNumber(arr, key));
    }

    public static String findNumber(int[] arr, int key) {
        String result = key + " is not found";
        for (int i = 0; i < arr.length; i++) {
            if(arr[i] == key) {
                result = key + " is found at " + i + "th position";
            }
        }
        return result;
    }
}
