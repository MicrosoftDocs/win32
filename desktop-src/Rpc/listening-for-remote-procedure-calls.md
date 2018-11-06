---
title: Listening for Remote Procedure Calls
description: After a server program registers its binding information and advertises its presence in a name service database, it can begin listening to the endpoint for remote procedure calls.
ms.assetid: 1c116e44-03a4-4b86-ae37-0b9187981e53
ms.topic: article
ms.date: 05/31/2018
---

# Listening for Remote Procedure Calls

After a server program registers its binding information and advertises its presence in a name service database, it can begin listening to the endpoint for remote procedure calls. Server programs call the [**RpcServerListen**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverlisten) function to monitor endpoints for client invocations of remote procedures.

The DCE specification of [**RpcServerListen**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverlisten) indicates that it should not return until a function in the server program calls [**RpcMgmtStopServerListening**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcmgmtstopserverlistening). The Microsoft RPC implementation of **RpcServerListen** uses two parameters that do not appear in the DCE specification: *DontWait* and *MinimumCallThreads*. Your server program can pass a nonzero value for the *DontWait* parameter. If it does, the **RpcServerListen** function will return immediately. Use the [**RpcMgmtWaitServerListen**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcmgmtwaitserverlisten) routine to perform the wait operation usually associated with **RpcServerListen**.

 

 




