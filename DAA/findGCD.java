class findGCD{
    public static void main(String[] args){
        int a = 10;
        int b = 15;
        int gcd = findGCD(a, b);
        System.out.println("GCD of " + a + " and " + b + " is " + gcd);
    } 

    public static int findGCD(int a,int b){
        if(b == 0){
            return a;
        }
        return findGCD(b, a%b);
    }
}