#include "stdio.h"


/** 
 * Calcula a média dos números x e y.
 */
double media(double x, double y) {
    return (x + y) * 0.5;
}


int main() {
    double x, y;

    printf("x: ");
    scanf("%lf", &x);
    printf("y: ");
    scanf("%lf", &y);
    
    printf("Resultado: %lf\n", media(x, y));
}