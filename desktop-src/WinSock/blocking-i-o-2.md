---
description: The simplest form of I/O in Windows Sockets 2 is blocking I/O.
ms.assetid: 8ed7e5a8-c577-4b61-9c49-8fd065d84af4
title: Blocking Input/Output
ms.topic: article
ms.date: 05/31/2018
---

# Blocking Input/Output

The simplest form of I/O in Windows Sockets 2 is blocking I/O. As mentioned in [Socket Attribute Flags and Modes](socket-attribute-flags-and-modes-2.md), sockets are created in blocking mode by default. Any I/O operation with a blocking socket will not return until the operation has been fully completed. Thus, any thread can only execute one I/O operation at a time. For example, if a thread issues a receive operation and no data is currently available, the thread will block until data becomes available and is placed into the thread's buffer. Although this is simple, it is not necessarily the most efficient way to do I/O (see [Pseudo Blocking and True Blocking](pseudo-vs--true-blocking-2.md) for more information).

 

 



