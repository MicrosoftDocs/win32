---
title: Server-side Cleanup
description: Server-side cleanup and Remote Procedure Call (RPC).
ms.assetid: 8a48f698-82ae-464b-bdd9-f0245bbc7733
ms.topic: article
ms.date: 05/31/2018
---

# Server-side Cleanup

Imagine the following scenario:

A client opens a context handle, and then either stops or loses connectivity to the server. How does the server detect that the client has failed and the context handle should be run down? There are two subscenarios: one is that the client is shut down in an orderly manner. In such case, it notifies the server that it is shutting down, and the server can clean up, including performing context run downs. If the client does not shut down in an orderly manner or it cannot notify the server, the server uses keep alives to determine whether the client is still available. On the server side, the [**RpcMgmtSetComTimeout**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcmgmtsetcomtimeout) function has no effect. Instead, the server uses the global per machine–keep alive setting, which defaults to approximately two hours. If the client does not respond to the server's keep alives, the connection is closed. When all connections to a given client process are closed, the server cleans up and runs down outstanding context handles.

 

 




