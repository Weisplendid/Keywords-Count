/*
****************
*This is a test*
****************
*/

#define A 5
# if (A<3)					//macro definition:if 
#include <iostream>
# else
#include <iostream>
#define con (int i = 1)	   //macro definition:int
#endif
#include <string>
 
using namespace std;


//int if switch case													line comment for interference


/**double break; return													block comment for interference*/			


int/**/a = 1;

//			/**

string s = "This string will be compiled";
int num1 =1;

//			**/This block comment is affected

/*             //This line comment is affected        */  string s0 = "This string will be compiled"; int num2 = 1;



//String for interference
string s1 = "float a = 0.1; default; if() {...} else {}";
string s2 = "float int double\
			if else int double default\
			case switch\
			";
//string with escape symbol
string s3 = "int \" int double \"char\"";
string s4 = "float int double\
			if else int\" do\\u\"ble\" default\
			case switch\
			";
//escape symbol escape the escape symbol
string s5 = "int \\ int \\";

string s6 = "这是句中文";
string s7 = "Это предложение на русском языке"; 

//Variable name for interference
int int_double_float = 1;
int Int =2;
int DOUBLE= 3;


int main() {
	//switch 
	switch(1)		//switch without braces
		case 0:		//only case
		case 1:
		case 2:
		case 3:		//one_line case without braces
			cout << 3 << endl;
			
	switch(1) {		//switch with braces
		case 0:		//case with braces
		{
			cout << "0_1" << endl;
			cout << "0_2" << endl;
			cout << "0_3" << endl;
			break;
		}
		case 1:		//multiline case without braces
			cout << "1_1" << endl;
			cout << "1_2" << endl;
		case 2:
			cout << "2_1" << endl;
	}
	
	
	//nested switch
	switch(0){
		case 0:
			switch(1)
				case 0:
	case 1:
		switch(0){
				case 0:
			   /*Chaotic writing format*/
		  	cout << "nested switch case 0_1_0" << endl;											
							break;
					 	case 1:
			    				cout << "nested switch case 0_1_1" << endl;
							break;
					}case 1:{
			cout << "nested switch case 1" << endl;
			switch(1)
				case 1:
					cout << "nested switch case 1_1" << endl;break;}
}
//switch num:  6
//case num:  [4, 3, 2, 2, 1, 2]
	int i = -1,j = 0;
    if(i<0){
        if(i<-1){
			cout << "if_if" << endl;		//if with braces
		}
        else cout << "if_else" << endl;		//if without braces
    }
    else if(i>0){
        if (i>2){
		cout << "else if_if" << endl;}
        else if (i==2) {cout << "else if_else if1" << endl;
        
        
		}
        else if (i>1) 
        	cout << "else if_else if2" << endl;			
        else cout << "else if_else" << endl;
    }
    else{
        if(j!=0){cout << "else_if" << endl;}
        else{
		
		
		cout << "else_else" << endl;}
    }
    return 0;

	//nested switch and if
	switch(j) {
		case 1:
			if(i < 3)
				i++;
			else if (i < 5)
				i--;
			else 
				i += 10;
		case 2:
			if(i < 3){
				i--;
				break;
			}
			else 
				i += 10;
	}
	
	
	
	
	
	
	
	
/*****************************
*		Final Answer:
*
*	total num: 57
*	switch num: 7
*	case num: 4 3 2 2 1 2 2
*	if-else num: 3
*	if-elseif-else num: 3
******************************/
}

