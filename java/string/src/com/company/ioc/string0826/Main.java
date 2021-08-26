package com.company.ioc.string0826;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // backjoon 10808
        Scanner scan = new Scanner(System.in);
        String s = scan.next();
        int[] arr = new int[26];
        for (int i = 0 ; i<s.length(); i++){
            arr[s.charAt(i)-97]++;
        }
        for (int index : arr){
            System.out.print(index+" ");
        }



    }
}
