---
title: Stopping the Server Application
description: A server application can stop listening for clients by calling RpcMgmtStopServerListening and RpcServerUnregisterIf, or by simply exiting the host process.
ms.assetid: 9d310cfb-72ad-448f-a66a-db6ac2478824
keywords:
- Remote Procedure Call RPC , tasks, stopping the server application
ms.topic: article
ms.date: 05/31/2018
---

# Stopping the Server Application

A server application can stop listening for clients by calling [**RpcMgmtStopServerListening**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcmgmtstopserverlistening) and [**RpcServerUnregisterIf**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverunregisterif), or by simply exiting the host process. Both methods are acceptable. If the server follows the first approach, it should implement the following steps:

The server function [**RpcServerListen**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverlisten) does not return to the calling program until an exception occurs or until a call to [**RpcMgmtStopServerListening**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcmgmtstopserverlistening) occurs. By default, only another server thread is allowed to halt the RPC server by using **RpcMgmtStopServerListening**. Clients who try to halt the server will receive the error RPC\_S\_ACCESS\_DENIED. However, it is possible to configure RPC to allow some or all clients to stop the server. See **RpcMgmtStopServerListening** for details.

You can also have the client application make a remote procedure call to a shutdown routine on the server. The shutdown routine calls [**RpcMgmtStopServerListening**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcmgmtstopserverlistening) and [**RpcServerUnregisterIf**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverunregisterif). This tutorial example program application uses this approach by adding a new remote function, **Shutdown**, to the file Hellop.c.

In the **Shutdown** function, the single null parameter to [**RpcMgmtStopServerListening**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcmgmtstopserverlistening) indicates that the local application should stop listening for remote procedure calls. The two null parameters to [**RpcServerUnregisterIf**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverunregisterif) are wildcards, indicating that all interfaces should be unregistered. The **FALSE** parameter indicates that the interface should be removed from the registry immediately, rather than waiting for pending calls to complete.


```C++
/* add this function to hellop.c */
void Shutdown(void)
{
    RPC_STATUS status;
 
    status = RpcMgmtStopServerListening(NULL);
 
    if (status) 
    {
       exit(status);
    }
 
    status = RpcServerUnregisterIf(NULL, NULL, FALSE);
 
    if (status) 
    {
       exit(status);
    }
} //end Shutdown
```



 

 




