#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - Entry point
 * Description: 'infinite'
 * Parameters: no input returns an int
 * Return: Always 0 (Success)
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
 * main - Entry point
 * Description: 'main'
 * Parameters: no input returns an int
 * Return: Always 0 (Success)
 */
int main(void)
{
	int i;
	pid_t pid;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid == 0)
		{
			exit(0);
		}
		else
		{
			printf("Zombie process created, PID: %d\n", pid);
		}
	}

	infinite_while();

	return (0);
}
