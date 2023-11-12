/**
 * Simple sorting algorithms and their performance 
 * Reg: E/19/129
 *
 */

 public class Sorting_Algo_Measurements {

    //create an array of given size and populate it with random data  
    static int [] create_rand_data(int size_of_array) {
	int [] data = new int[size_of_array];
	int i; 
	for(i=0; i < data.length; i++)
	    data[i] = (int)(Math.random() * 100);
	return data; 
    }

    //create an array of given size and populate it with worst data arrangement 
    static int [] create_worst_data(int size_of_array) {
	int [] data = new int[size_of_array];
	int i; 
	for(i=0; i < data.length; i++)
	    data[i] = data.length - i;
	return data; 
    }

    //create an array of given size and populate it with best data arrangement 
    static int [] create_best_data(int size_of_array) {
	int [] data = new int[size_of_array];
	int i; 
	for(i=0; i < data.length; i++)
	    data[i] = i;
	return data; 
    }

    // function to swap. Would be useful since all need this 
    static void swap(int []d, int i, int j) { 
	int tmp = d[i]; 
	d[i] = d[j]; 
	d[j] = tmp;
    }

    // check if the soring worked on the array 
    static boolean isSorted(int [] data) {
	int i;
	for(i=1; i < data.length; i++)
	    if(data[i] < data[i-1]) break;
	return (i == data.length);
    }

    // If you want just display the array as well :) 
    static void display(int []data) { 
	System.out.println("=======");
	for(int i=0; i < data.length; i++) 
	    System.out.print(data[i] + "  "); 
	System.out.println("\n=======");
    }

    
    /**********************************************************
     *     Implementation of sorting algorithms               *
     *********************************************************/

    static void buble_sort(int [] data)  {
		// Implement 
		boolean flag = true;
		while (flag) {
			flag = false;
			for (int j=0; j < data.length-1; j++){

				if (data[j] > data[j+1])
				{
					swap(data, j, j+1);
					flag = true;
				}

			}
		}
    }

    static void selection_sort(int [] data) {
		// Implement 
		for (int i=0; i<data.length-1; i++){
			int minmum = data[i];
			int index = i;

			for (int j=i; j<data.length; j++){
				if (minmum > data[j])
				{
					minmum = data[j];
					index = j;
				}
			}

			swap(data, i, index);
		}
    }

    static void insertion_sort(int [] data) {
		// Implement
		for (int i=1; i<data.length; i++){

				for (int j=i; j>0; j--){
					
					if (data[j] > data[j-1]){
						break;
					}

					swap(data, j, j-1);
				}
		}
    }

	public static void main(String[] args) {
        // create arrays of different sizes populated with data
        // measure the time taken by different algorithms to
        // sort the array.
        // Think about effects of caches, other apps running, etc.

		// define the arra sizes
        int[] arr_sizes = {10, 20, 100, 150, 1000, 10000, 100000};

        // Print best-case table headers
        System.out.println("Best-Case Data");
        System.out.println("-----------------------------------------------------------------------");
        System.out.printf("%-12s | %-16s | %-16s | %-16s |%n", "Array Size", "Bubble Sort", "Selection Sort", "Insertion Sort");
        System.out.println("-----------------------------------------------------------------------");

        for (int i = 0; i < arr_sizes.length; i++) {
            int[] arr = create_best_data(arr_sizes[i]);

            System.out.printf("%-12d |", arr_sizes[i]);

            for (int j = 0; j < 3; j++) {
                int[] temp_arr = arr.clone();

                long start, end;

                if (j == 0) {
                    start = System.nanoTime();
                    buble_sort(temp_arr);
                    end = System.nanoTime();
                    System.out.printf(" %13d ns |", (end - start));
                }
                if (j == 1) {
                    start = System.nanoTime();
                    selection_sort(temp_arr);
                    end = System.nanoTime();
                    System.out.printf(" %13d ns |", (end - start));
                }
                if (j == 2) {
                    start = System.nanoTime();
                    insertion_sort(temp_arr);
                    end = System.nanoTime();
                    System.out.printf(" %13d ns |", (end - start));
                }
            }

            System.out.println(); 
        }

        System.out.println("-----------------------------------------------------------------------");

        // Print worst-case table headers
        System.out.println("\nWorst-Case Data");
        System.out.println("-----------------------------------------------------------------------");
        System.out.printf("%-12s | %-16s | %-16s | %-16s |%n", "Array Size", "Bubble Sort", "Selection Sort", "Insertion Sort");
        System.out.println("-----------------------------------------------------------------------");

        for (int i = 0; i < arr_sizes.length; i++) {
            int[] arr = create_worst_data(arr_sizes[i]);

            System.out.printf("%-12d |", arr_sizes[i]);

            for (int j = 0; j < 3; j++) {
                int[] temp_arr = arr.clone();

                long start, end;

                if (j == 0) {
                    start = System.nanoTime();
                    buble_sort(temp_arr);
                    end = System.nanoTime();
                    System.out.printf(" %13d ns |", (end - start));
                }
                if (j == 1) {
                    start = System.nanoTime();
                    selection_sort(temp_arr);
                    end = System.nanoTime();
                    System.out.printf(" %13d ns |", (end - start));
                }
                if (j == 2) {
                    start = System.nanoTime();
                    insertion_sort(temp_arr);
                    end = System.nanoTime();
                    System.out.printf(" %13d ns |", (end - start));
                }
            }

            System.out.println(); 
        }

        System.out.println("-----------------------------------------------------------------------");

        // Print average-case table headers
        System.out.println("\nAverage-Case Data");
        System.out.println("-----------------------------------------------------------------------");
        System.out.printf("%-12s | %-16s | %-16s | %-16s |%n", "Array Size", "Bubble Sort", "Selection Sort", "Insertion Sort");
        System.out.println("-----------------------------------------------------------------------");

        for (int i = 0; i < arr_sizes.length; i++) {
            int[] arr = create_rand_data(arr_sizes[i]);

            System.out.printf("%-12d |", arr_sizes[i]);

            for (int j = 0; j < 3; j++) {
                int[] temp_arr = arr.clone();

                long start, end;

                if (j == 0) {
                    start = System.nanoTime();
                    buble_sort(temp_arr);
                    end = System.nanoTime();
                    System.out.printf(" %13d ns |", (end - start));
                }
                if (j == 1) {
                    start = System.nanoTime();
                    selection_sort(temp_arr);
                    end = System.nanoTime();
                    System.out.printf(" %13d ns |", (end - start));
                }
                if (j == 2) {
                    start = System.nanoTime();
                    insertion_sort(temp_arr);
                    end = System.nanoTime();
                    System.out.printf(" %13d ns |", (end - start));
                }
            }

            System.out.println();
        }

        System.out.println("-----------------------------------------------------------------------");
    }
}