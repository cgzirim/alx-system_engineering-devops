#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>

/**
 * infinite_while - Run a while loop indefinitely.
 *
 * Return: Always 0.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Creates five zombie processes.
 *
 * Return: Always 0.
 */
int main(void)
{

	int i;

	for (i = 0; i < 5; i++)
	{
		pid_t child_pid = fork();

		if (child_pid > 0)
		{
			printf("Zombie process created, PID: %d\n", child_pid);
			sleep(1);
		}

		else
			exit(0);
	}

	infinite_while();

	return (EXIT_SUCCESS);
}
