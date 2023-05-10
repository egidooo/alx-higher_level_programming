#include "lists.h"
/**
 * insert_node - insert a number into a sortted linked list
 * @head: pointer
 * @number: number to be inserted
 * 0 if it fails and inserted number otherwise
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *inserted;

	inserted = malloc(sizeof(listint_t));
	if (inserted == NULL)
		return (NULL);
	inserted->n = number;
	if (node == NULL || node->n >= number)
	{
		inserted->next = node;
		*head = inserted;
		return (inserted);
	}
	while (node && node->next && node->next->n < number)
	{
		node = node->next;
		inserted->next = node->next;
		node->next = inserted;
	}
		return (inserted);
}
