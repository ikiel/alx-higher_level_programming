#include "lists.h"
#include <stddef.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: the list to check
 *
 * Return: 0 for false || 1 for true
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev = NULL;
	listint_t *current = NULL;
	listint_t *next = NULL;
	listint_t *f_half = NULL;
	listint_t *l_half = NULL;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	/* reverse the last half of the list */
	current = slow;
	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	/* compare first half and last half of list */
	f_half = *head;
	l_half = prev;
	while (l_half != NULL)
	{
		if (f_half->n != l_half->n)
			return (0);
		f_half = f_half->next;
		l_half = l_half->next;
	}

	return (1);
}
