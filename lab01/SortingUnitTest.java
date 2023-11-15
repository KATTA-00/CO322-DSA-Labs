import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import org.junit.jupiter.api.Test;

public class SortingUnitTest {

    @Test
    void testBubbleSort() {
        int[] input = {4, 2, 7, 1, 9, 3};
        int[] expected = {1, 2, 3, 4, 7, 9};
        SortingMeasurements.buble_sort(input);
        assertArrayEquals(expected, input);
    }

    @Test
    void testSelectionSort() {
        int[] input = {4, 2, 7, 1, 9, 3};
        int[] expected = {1, 2, 3, 4, 7, 9};
        SortingMeasurements.selection_sort(input);
        assertArrayEquals(expected, input);
    }

    @Test
    void testInsertionSort() {
        int[] input = {4, 2, 7, 1, 9, 3};
        int[] expected = {1, 2, 3, 4, 7, 9};
        SortingMeasurements.insertion_sort(input);
        assertArrayEquals(expected, input);
    }
}
