#include <stdlib.h>
#include "lists.h"

listint_t *insert_node(listint_t **head, int n)
{
    listint_t *current = *head;
    listint_t *new = malloc(sizeof(listint_t));;
    listint_t *prev = NULL;


    if (new == NULL)
        return (NULL);

    new->n = n;
    new->next = NULL;

    if (*head == NULL)
        *head = new;
    else
    {
        while (current->next != NULL)
            current = current->next;
        current->next = new;
    }

    new->next = current;
    prev->next = new;

    return (new);
}





/* listint_t *insert_node(listint_t *previous, const int data)
{
    if(previous == NULL)
        return (NULL);

    listint_t *new;
    listint_t *current;

    current = previous;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    new->data = data;
    new->next = previous->next;
    previous->next= new;

    return (new);
} */
