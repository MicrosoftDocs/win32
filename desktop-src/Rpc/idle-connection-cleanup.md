---
title: Idle Connection Cleanup
description: By default, connections in the thread pool are not closed until the whole association is shut down.
ms.assetid: e3d6c89b-0ec5-429d-96d9-1396cce10750
ms.topic: article
ms.date: 05/31/2018
---

# Idle Connection Cleanup

By default, connections in the thread pool are not closed until the whole association is shut down. This policy enables clients with a large number of threads or security identities to make RPC calls to the server in an efficient manner. The drawback is that an inordinate amount of resources may be committed to maintaining those connections. To manage the process, RPC provides the [**RpcMgmtEnableIdleCleanup**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcmgmtenableidlecleanup) function. This function enables idle connection cleanup; the client periodically scans the connection pool and closes connections that have not been recently used. If the association has maintained context handles, the idle connection cleanup closes all idle connections, but makes sure at least one connection is left open, even if the connection is idle (otherwise the server gets context handle run downs). If the association has not maintained context handles, idle connection cleanup closes all idle connections, even if doing so leaves no connections in the pool.

On Windows XP, the RPC run time keeps track of the number of open connections in an association, and automatically turns on idle connection cleanup if the number of connections in any association exceeds a certain threshold.

 

 




