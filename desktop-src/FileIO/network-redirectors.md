---
description: Describes the functionality of a network redirector.
ms.assetid: 3cf36f88-b282-4f75-84fe-8106fea66825
title: Network Redirectors
ms.topic: article
ms.date: 05/31/2018
---

# Network Redirectors

A network redirector is a file system driver (or FSD) that functions in the following manner:

-   As a client in a network I/O operation by sending I/O requests to servers and processing the responses from the servers.
-   As a server in a network I/O operation by receiving I/O requests from servers and processing the requests.

It performs all of the low-level interaction with the server in resolving the file name provided by the application with the location of the resource on the remote server. In this way, the redirector enables the application to access and manipulate resources on remote servers as if they were located on the local machine.

Redirectors operate entirely within kernel mode. This provides the following performance advantages over user-mode alternatives:

-   It can interact with kernel-mode FSDs running on the server, such as the server FSD, without the need for user-to-kernel mode and kernel-to-user mode context switches.
-   It can interact in kernel mode with the cache manager on the server to cache I/O data that the server cache manager sends on the client.
-   API functions custom-made for remote I/O requests, and changes to the standard file I/O functions to provide this functionality, are not necessary.

 

 



