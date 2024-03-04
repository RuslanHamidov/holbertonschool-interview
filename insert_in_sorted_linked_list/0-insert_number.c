#include <stdlib.h>
#include "lists.h"

listint_t *insert_node(listint_t *previous, const int data)
{
    if(previous == NULL)
        return (NULL);

    listint_t *new;
    listint_t *current;

    current = *previous;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    new->data = data;
    new->next = previous->next;
    previous->next= new;

    return (new);
}
