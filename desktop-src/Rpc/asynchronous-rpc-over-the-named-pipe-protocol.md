---
title: Asynchronous RPC over the Named-Pipe Protocol
description: If you use named pipes (ncacn\_np) as your transport protocol, you should avoid allowing a large number of idle pending calls on the server.
ms.assetid: a1d0f758-91bc-4821-9a82-64ba6ce575ad
ms.topic: article
ms.date: 05/31/2018
---

# Asynchronous RPC over the Named-Pipe Protocol

If you use named pipes ([**ncacn\_np**](/windows/desktop/Midl/ncacn-np)) as your transport protocol, you should avoid allowing a large number of idle pending calls on the server. With named pipes, each client waiting for a reply will have a pending named pipe read on the server, each of which requires a certain amount of kernel memory.

For example, you would not want to use a notification call for new e-mail with the named-pipe transport, because such a call would remain pending even when clients are idle, and kernel memory could be depleted. Note that this is not a problem with the other connection-oriented protocols, such as [**ncacn\_ip\_tcp**](/windows/desktop/Midl/ncacn-ip-tcp).

Since named pipes are a transport protocol, your application can use them by specifying [**ncacn\_np**](/windows/desktop/Midl/ncacn-np) as the protocol in a string binding. For more information on named pipes, see [Named Pipes](/windows/desktop/ipc/named-pipes). For details on creating string bindings, see [Using String Bindings](finding-server-host-systems.md).

 

 