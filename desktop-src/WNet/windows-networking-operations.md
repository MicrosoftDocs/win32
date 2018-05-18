---
title: Windows Networking Operations
description: An application can use the WNet functions to browse, add, or cancel network connections anywhere in the network hierarchy.
ms.assetid: '8f17af6c-e1b2-4b53-b3f0-698d42beb704'
---

# Windows Networking Operations

An application can use the WNet functions to browse, add, or cancel network connections anywhere in the network hierarchy.

A *persistent connection* is a network connection that the system automatically restores when the user logs on. You can call the [**WNetAddConnection2**](wnetaddconnection2.md) (or [**WNetAddConnection3**](wnetaddconnection3.md)) and [**WNetCancelConnection2**](wnetcancelconnection2.md) functions to control whether a network connection is persistent from one session to the next.

To find the default user name or the user name used to establish a network connection, call the [**WNetGetUser**](wnetgetuser.md) function.

In addition to calling the WNet functions, a process can also use mailslots and named pipes to communicate with another process. For more information, see [Mailslots](https://msdn.microsoft.com/library/windows/desktop/aa365576) and [Pipes](https://msdn.microsoft.com/library/windows/desktop/aa365780).

 

 




