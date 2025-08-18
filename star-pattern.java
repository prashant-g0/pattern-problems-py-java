public class sum{
    public static void main(String[] args) {
        int n = 4;
        for(int i=n;i>=1;i--){
            for(int j=i;j>0;j--){
                System.out.print("* ");
            }
            System.out.println();
        }
    }
}

//Output:
// * * * * 
// * * * 
// * * 
// * 
