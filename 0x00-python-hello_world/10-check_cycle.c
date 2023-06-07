#include "lists.h"

/**
 * check_cycle - checks if a singly-linked list has a cycle
 * @list: the singly_linked list to check
 *
 * Return: 1 for cycle || 0 for no cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}

	return (0);
}
