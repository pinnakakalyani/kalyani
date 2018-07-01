/**
 * 
 */
package org.practice.add;

import java.util.Scanner;

/**
 * @author Kalyani
 *
 */
public class addition {

	/**
	 * 
	 */
	public  int a;
	public  int b;
	public  int c;
	
	
	
	public addition(int e,int d) {
		// TODO Auto-generated constructor stub
		this.a=e;
		this.b=d;
	}
	
	public void add(int x,int y) {
		c=a+b;
		System.out.println("Addition of 2 no's " +c );
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//addition ad = new addition(a,b);
		Scanner s = new Scanner(System.in);
		System.out.println("Enter value for a");
		int p=s.nextInt();
		System.out.println("enter b value");
		 int q=s.nextInt();
		addition ad = new addition(p,q);
		ad.add(p,q);
		
	}

}
