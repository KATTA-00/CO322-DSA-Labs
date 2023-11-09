/**
 * Simple sorting algorithms and their performance 
 * Reg: E/19/129
 *
 */

 public class Sort {

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

		       

    public static void main(String [] args) {
	// create arrays of different size populate with data
	// measure the time taken by different algorithms to
	// sort the array.
	// Think about effects of caches, other apps running etc. 

		// define some arrays
		int[] arr1_best = create_best_data(10);
		int[] arr2_best = create_best_data(10);
		int[] arr3_best = create_best_data(10);

		int[] arr1_normal = create_rand_data(10);
		int[] arr2_normal = create_rand_data(10);
		int[] arr3_normal = create_rand_data(10);


		int[] arr1_worst = create_worst_data(10);
		int[] arr2_worst = create_worst_data(10);
		int[] arr3_worst = create_worst_data(10);

		// define var for store time values
		long start, end;

		// Bubble Sort
		System.out.println("------Bubble Sort------");

		System.out.println("Best Case:");
		display(arr1_best);
		// sort the array and get the times
		start = System.nanoTime();
		buble_sort(arr1_best);
		end = System.nanoTime();
		display(arr1_best);
		System.out.println("Time: " + (end-start) + "ms");
		display(arr1_best);
		
		System.out.println();
		
		System.out.println("Normal Case:");
		display(arr1_normal);
		// sort the array and get the times
		start = System.nanoTime();
		buble_sort(arr1_normal);
		end = System.nanoTime();
		System.out.println("Time: " + (end-start) + "ms");
		display(arr1_normal);
		
		System.out.println();
		
		System.out.println("Worst Case:");
		display(arr1_worst);
		// sort the array and get the times
		start = System.nanoTime();
		buble_sort(arr1_worst);
		end = System.nanoTime();
		System.out.println("Time: " + (end-start) + "ms");
		display(arr1_worst);
		
		System.out.println();
		
		// Selection Sort
		System.out.println("-----Selection Sort-----");

		System.out.println("Best Case:");
		display(arr2_best);
		// sort the array and get the times
		start = System.nanoTime();
		selection_sort(arr2_best);
		end = System.nanoTime();
		display(arr2_best);
		System.out.println("Time: " + (end-start) + "ms");
		
		System.out.println();
		
		System.out.println("Normal Case:");
		display(arr2_normal);
		// sort the array and get the times
		start = System.nanoTime();
		selection_sort(arr2_normal);
		// sort the array and get the times
		start = System.nanoTime();
		end = System.nanoTime();
		display(arr2_normal);
		System.out.println("Time: " + (end-start) + "ms");
		
		System.out.println();
		
		System.out.println("Worst Case:");
		display(arr2_worst);
		// sort the array and get the times
		start = System.nanoTime();
		selection_sort(arr2_worst);
		end = System.nanoTime();
		display(arr2_worst);
		System.out.println("Time: " + (end-start) + "ms");
		
		System.out.println();

		// Selection Sort
		System.out.println("-----Insertion Sort-----");

		System.out.println("Best Case:");
		display(arr3_best);
		// sort the array and get the times
		start = System.nanoTime();
		insertion_sort(arr3_best);
		end = System.nanoTime();
		display(arr3_best);
		System.out.println("Time: " + (end-start) + "ms");
		
		System.out.println();
		
		System.out.println("Normal Case:");
		display(arr3_normal);
		// sort the array and get the times
		start = System.nanoTime();
		insertion_sort(arr3_normal);
		end = System.nanoTime();
		display(arr3_normal);
		System.out.println("Time: " + (end-start) + "ms");

		System.out.println();
		
		System.out.println("Worst Case:");
		display(arr3_worst);
		// sort the array and get the times
		start = System.nanoTime();
		insertion_sort(arr3_worst);
		end = System.nanoTime();
		display(arr3_worst);
		System.out.println("Time: " + (end-start) + "ms");
		
		System.out.println();

    }
}