#include<stdio.h>

void reversestring1(char s[]){
	int n = sizeof(s)/sizeof(char);
	int start=0,end=n-1;
	
	while(start<end){
		int temp = s[start];
		s[start] = s[end];
		s[end] = temp;
		start++;
		end--;
	}
	
	printf("\nString after reversal :");
	for(int i=0;i<sizeof(s)/sizeof(char);i++){
		printf("%c",s[i]);
	}
}

int main(){
	char s[] = {'h','e','l','l','o'};
	
	printf("String Before Reversal : ");
	for(int i=0;i<sizeof(s)/sizeof(char);i++){
		printf("%c",s[i]);
	}
	
	reversestring1(s);
}
