---
title: Windows Networking Operations
description: An application can use the WNet functions to browse, add, or cancel network connections anywhere in the network hierarchy.
ms.assetid: 8f17af6c-e1b2-4b53-b3f0-698d42beb704
ms.topic: article
ms.date: 05/31/2018
---

# Windows Networking Operations

An application can use the WNet functions to browse, add, or cancel network connections anywhere in the network hierarchy.

A *persistent connection* is a network connection that the system automatically restores when the user logs on. You can call the [**WNetAddConnection2**](/windows/win32/api/winnetwk/nf-winnetwk-wnetaddconnection2a) (or [**WNetAddConnection3**](/windows/win32/api/winnetwk/nf-winnetwk-wnetaddconnection3a)) and [**WNetCancelConnection2**](/windows/win32/api/winnetwk/nf-winnetwk-wnetcancelconnection2a) functions to control whether a network connection is persistent from one session to the next.

To find the default user name or the user name used to establish a network connection, call the [**WNetGetUser**](/windows/win32/api/winnetwk/nf-winnetwk-wnetgetusera) function.

In addition to calling the WNet functions, a process can also use mailslots and named pipes to communicate with another process. For more information, see [Mailslots](/windows/desktop/ipc/mailslots) and [Pipes](/windows/desktop/ipc/pipes).

 

 