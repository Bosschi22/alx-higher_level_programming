#include "lists.h"
/**
 * check_cycle - checks if a linked list contain
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
listint_t *slow = list;
listint_t *fast = list;
	if (!list)
		return (0);
	while (sl && fa && fa->next)
	{
		sl = sl->next;
		fa = fa->next->next;
		if (sl == fa)
			return (1);
	}
	return (0);
}