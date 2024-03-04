#include <stdlib.h>
#include "lists.h"

listint_t *insert_node(listint_t **head, int n)
{
    listint_t *current;
    listint_t *new_node;
    listint_t *prev;

    current = *head;
    prev = NULL;
    new_node = malloc(sizeof(listint_t));

    if (new_node == NULL)
        return (NULL);

    new_node->n = n;
    new_node->next = NULL;

    if (*head == NULL || (*head)->n >= number){
        new_node->next = *head
        *head = new_node;
        return (new_node);
    }

    
    while (current && current->n < number) {
        prev = current;
        current = current->next;
    }

    new_node->next = current;
    prev->next = new_node;

    return (new_node);
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
