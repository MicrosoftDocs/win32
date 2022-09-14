---
title: Listening for Client Calls
description: After your server application has registered its interfaces, created the necessary binding information, and registered its endpoints, it is ready to begin listening for remote procedure calls from client programs.
ms.assetid: ca9d24ed-0acc-45de-bbb2-761c56745a58
keywords:
- Remote Procedure Call RPC , tasks, listening for client calls
ms.topic: article
ms.date: 05/31/2018
---

# Listening for Client Calls

After your server application has registered its interfaces, created the necessary binding information, and registered its endpoints, it is ready to begin listening for remote procedure calls from client programs.

To listen for remote procedure calls, your server program must call [**RpcServerListen**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverlisten), as shown in the following code fragment:


```C++
RPC_STATUS status;
status = RpcServerListen(
    1,
    RPC_C_LISTEN_MAX_CALLS_DEFAULT,
    0);
```



An RPC Server has one or more threads that pick up client calls and deliver them to the routines in the registered interfaces. The first parameter to the [**RpcServerListen**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverlisten) function is the minimum number of threads to create. The parameter is only a hint; the RPC run time may chose to ignore it.

The second parameter to [**RpcServerListen**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverlisten) is the maximum number of concurrent remote procedure calls to handle. If you want your application to use the default maximum value, pass RPC\_C\_LISTEN\_MAX\_CALLS\_DEFAULT as the value for this parameter.

The DCE specification calls for [**RpcServerListen**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverlisten) to keep running until it receives a signal to stop. One Microsoft extension to this function is to enable it to begin listening and return immediately. If you want your application to use the default DCE behavior, set the third parameter to zero. See [**RpcServerListen**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverlisten), [**RpcMgmtStopServerListening**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcmgmtstopserverlistening), and [**RpcMgmtWaitServerListen**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcmgmtwaitserverlisten) for details.

 

 




