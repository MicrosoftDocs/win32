---
description: 'There are two ways to implement multitasking: as a single process with multiple threads or as multiple processes, each with one or more threads.'
ms.assetid: ac0a8163-1498-4274-acfc-6a36b4c02a27
title: When to Use Multitasking
ms.topic: article
ms.date: 05/31/2018
---

# When to Use Multitasking

There are two ways to implement multitasking: as a single process with multiple threads or as multiple processes, each with one or more threads. An application can put each thread that requires a private address space and private resources into its own process, to protect it from the activities of other process threads.

A multithreaded process can manage mutually exclusive tasks with threads, such as providing a user interface and performing background calculations. Creating a multithreaded process can also be a convenient way to structure a program that performs several similar or identical tasks concurrently. For example, a named pipe server can create a thread for each client process that attaches to the pipe. This thread manages the communication between the server and the client. Your process could use multiple threads to accomplish the following tasks:

-   Manage input for multiple windows.
-   Manage input from several communications devices.
-   Distinguish tasks of varying priority. For example, a high-priority thread manages time-critical tasks, and a low-priority thread performs other tasks.
-   Allow the user interface to remain responsive, while allocating time to background tasks.

It is typically more efficient for an application to implement multitasking by creating a single, multithreaded process, rather than creating multiple processes, for the following reasons:

-   The system can perform a context switch more quickly for threads than processes, because a process has more overhead than a thread does (the process context is larger than the thread context).
-   All threads of a process share the same address space and can access the process's global variables, which can simplify communication between threads.
-   All threads of a process can share open handles to resources, such as files and pipes.

There are other techniques you can use in the place of multithreading. The most significant of these are as follows: asynchronous input and output (I/O), I/O completion ports, asynchronous procedure calls (APC), and the ability to wait for multiple events.

A single thread can initiate multiple time-consuming I/O requests that can run concurrently using asynchronous I/O. Asynchronous I/O can be performed on files, pipes, and serial communication devices. For more information, see [Synchronization and Overlapped Input and Output](../sync/synchronization-and-overlapped-input-and-output.md).

A single thread can block its own execution while waiting for any one or all of several events to occur. This is more efficient than using multiple threads, each waiting for a single event, and more efficient than using a single thread that consumes processor time by continually checking for events to occur. For more information, see [Wait Functions](../sync/wait-functions.md).

 

 
