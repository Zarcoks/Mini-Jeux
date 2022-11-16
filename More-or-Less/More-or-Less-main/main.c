#include <stdio.h>
#include <stdlib.h>
#include <time.h>


int main()
{
    srand(time(NULL)); // initialise la fonction

    printf("Welcome to the More-or-Less game !");
    printf("\n==================================");
    printf("\n//The computer will find randomly a number between 0 to 100, and your goal is to find it !");

    int nombreMystere;
    int nombreEntre;
    int compteur;
    nombreMystere = rand()%101;
    int continu = 1;

    while (continu){
    nombreMystere = rand()%101;
    compteur = 0;
    while ((compteur != 10) && (nombreEntre != nombreMystere)){
        printf("\nYour number : ");
        scanf("%d", &nombreEntre);

        if (nombreEntre > nombreMystere){
            printf("Less !");
        }
        else if (nombreEntre < nombreMystere){
            printf("More !");
        }
        else{
            compteur++;
            printf("Congratulations ! You found the mystery number, the answer is : %d ! \nYou made %d loops",nombreEntre, compteur);
        }
        compteur++;
    }
    if (compteur == 10){
        printf("You took too much loops to win, you failed !");
    }
    printf("\nContinue (1: yes / 0: no) = ");
    scanf("%d", &continu);
}
}
