using System;
using System.Linq;
using System.Collections.Generic;
using System.Diagnostics.Tracing;
using Internal;
namespace Main
{
    public class MainProgram
    {
        public static void Main(string[] args)
        {
            int c = 0;
            
            try
            {
                StreamReader sr = new StreamReader("Advent-of-Code/2023/C#/Day 1 Part 1 - C#/Inputs.txt");
                line = sr.ReadLine();
                while (line != null)
                {
                    int f = 0;
                    int t = 0;
                    int l = 0;
                    string p = line;
                    foreach(char a in p){
                        if(a>='0' && a<='9'){
                            try
                            {
                                a = Convert.ToInt32(a);
                            }
                            catch (FormatException err)
                            {
                                Console.WriteLine("uhmmm this is awkward");
                            }
                            if(t==0){
                                int f = a;
                                t+=1;
                            }
                            else if (t>=1){
                                l = a;
                            }
                        }
                    }
                    if(l==0){
                        l=f;
                    }
                    try
                    {
                        g=Convert.ToBase64String(f)+Convert.ToBase64String(l);
                    }
                    catch (FormatException err)
                    {
                        Console.WriteLine("a");
                    }
                    try
                    {
                        c+=Convert.ToInt32(g);
                    }
                    catch (FormatException err)
                    {
                        Console.WriteLine("b");
                    }
                    line = sr.ReadLine();
                }
                    sr.Close();
                    Console.ReadLine();
                }
                catch(Exception e)
                {
                    Console.WriteLine("Exception: " + e.Message);
                }
                finally
                {
                    Console.WriteLine("Executing finally block.");
                }
        }
    }
}
