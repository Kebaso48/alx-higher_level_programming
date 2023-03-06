#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if a single linked list contains a cycle
 * @list: the single limked list
 * Return: 1 if it has cycle, 0 if it does not
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *quick;

	if (list == NULL || list->next == NULL)
		return (0);

	slow = list->next;
	quick = list->next->next;

	while (slow && quick && quick->next)
	{
		if (slow == quick)
			return (1);

		slow = slow->next;
		quick = quick->next->next;
	}
	return (0);
}
