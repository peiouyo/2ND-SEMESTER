#include <stdio.h>
#include <stdlib.h>
#define MAX 7

int stack[MAX];
int top = -1;

int main() {
    void push();
    void pop();
    
    while(1) {
        int choice;
        
        printf("\n=====~+~=====\n");
        printf("  Stack Menu\n");
        printf("-------------\n");
        printf(" 1. Push\n");
        printf(" 2. Pop\n");
        printf(" 3. Exit\n");
        printf("-------------\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch(choice) {
            case 1:
                push();
                break;
            case 2:
                pop();
                break;
            case 3:
                printf("Exiting~\n");
                system("pause");
                return 0;
            default:
                printf("Invalid choice. Try again!!\n");
            
        }
    }
}

void push() {
    int value;

    if(top == MAX - 1) {
        printf("The Stack is Full! -w-\n");
    } else {
        printf("Enter a value to push: ");
        scanf("%d", &value);
        top++;
        stack[top] = value;
        printf("Pushed %d to the stack.\n", value);
    }
}

void pop() {
    if(top == -1) {
        printf("The Stack is Empty -w-\n");
    } else {
        int value = stack[top];
        top--;
        printf("Popped %d from the stack.\n", value);
    }
}