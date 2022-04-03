// papa.cpp.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <string>

using namespace std;

int main() {
	string bolletjes;

	cout << "Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is. ";
	cout << "Hoeveel bolletjes wilt u? ";
	cin >> bolletjes;
	if (bolletjes <= "3") {
		cout << "Wilt u deze " << bolletjes << " bolletje(s) in A) een hoorntje of B) een bakje ?";
	}

	else if (bolletjes > "3" && bolletjes < "9") {
		cout << "Dan krijgt u van mij een bakje met " << bolletjes << " bolletjes.";
	}

	else bolletjes >= "9";
		cout << "Sorry, zulke grote bakken hebben we niet ";

}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
