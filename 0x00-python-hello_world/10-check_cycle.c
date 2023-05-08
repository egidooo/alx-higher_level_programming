#include "lists.h"

/**
 * check_cycle - functions that check if the linked list contains a cycle
 * @list: linked list
 * Return: 0 if no cycle and 1 if there is cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *first = list;
	listint_t *last = list;

	if (!list)
		return (0);
	while (first && last && first->next)
	{
		if (first == last)
			return (1);

		first = first->next;
		last = last->next->next;
	}
	return (0);
}
