import java.util.*;

class DoleOutCadbury{
	static int c = 0;
	public static void main(String args[]){
		Scanner sc = new Scanner(System.in);
		int p = sc.nextInt();
		int q = sc.nextInt();
		int r = sc.nextInt();
		int s = sc.nextInt();
		
		int a[][] = new int[1501][1501];
		for(int i=0; i<1501; i++){
			for(int j=0; j<1501; j++){
				a[i][j] = 0;
			}
		}
		
		for(int i=1; i<2; i++){
			for(int j=1; j<1501; j++){
				a[i][j] = j;
			}
		}

		for(int i=1; i<1501; i++){
			for(int j=1; j<2; j++){
				a[i][j] = i;
			}
		}

		for(int i=0; i<1501; i++){
			for(int j=0; j<1501; j++){
				if(i==j) a[i][j] = 1;
				else if(i>j) a[i][j] = 1 + a[i-j][j];
				else a[i][j] = 1 + a[i][j-i];
			}
		}

		for(int i=p; i<q+1; i++){
			for(int j=r; j<s+1; j++){
				c += a[i][j];
			}
		}

		System.out.println(DoleOutCadbury.c);

	}
}