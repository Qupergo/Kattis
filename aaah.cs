using System;

class MainClass {
  public static void Main (string[] args) {
	  int current_amount = Console.ReadLine().Length;
	  int required_amount = Console.ReadLine().Length;

	  if (current_amount >= required_amount)
	  {
		  Console.WriteLine("go");
	  }
	  else
	  {
		  Console.WriteLine("no");
	  }

  }
}
