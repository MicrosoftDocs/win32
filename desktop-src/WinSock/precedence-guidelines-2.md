---
description: The two (or more) descriptors that reference a shared socket may be used independently as far as I/O is concerned.
ms.assetid: 25252552-4b62-441a-b564-e7f4a77cf68a
title: Precedence Guidelines
ms.topic: article
ms.date: 05/31/2018
---

# Precedence Guidelines

The two (or more) descriptors that reference a shared socket may be used independently as far as I/O is concerned. However, the Windows Sockets interface does not implement any type of access control, so it is up to the processes involved to coordinate their operations on a shared socket. A typical use for shared sockets is to have one process that is responsible for creating sockets and establishing connections hand off sockets to other processes that are responsible for information exchange.

The general guideline for supporting multiple outstanding operations on shared sockets is that a service provider is encouraged to honor all simultaneous operations on shared sockets, especially the most recent operation on a socket object. If need be, this may occur at the expense of canceling some of the previous but still pending operations, which will return WSAEINTR in this case.

 

 



