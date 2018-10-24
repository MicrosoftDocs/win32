---
title: Impersonation and Asynchronous Calls
description: Impersonation and Asynchronous Calls
ms.assetid: 7eaa0a66-7a80-4831-b0b6-b8eff4abd036
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Impersonation and Asynchronous Calls

The server cannot impersonate the client after the server's call to [**ISynchronize::Signal**](https://msdn.microsoft.com/en-us/library/ms692771(v=VS.85).aspx) completes, even if the Begin\_ method has not yet completed. For example, suppose a client calls the Begin\_ method, the server processes the call immediately, and the server calls **Signal** to indicate it is finished processing. Even if work remains to be done in the Begin\_ method, the server cannot impersonate the client after the call to **Signal** completes.

If the server impersonates the client before it calls [**Signal**](https://msdn.microsoft.com/en-us/library/ms692771(v=VS.85).aspx), the impersonation token will not be removed from the thread until the server calls [**IServerSecurity::RevertToSelf**](https://msdn.microsoft.com/en-us/library/ms680038(v=VS.85).aspx) or until the server's call to Begin\_ returns, whichever comes first.

## Related topics

<dl> <dt>

[Delegation and Impersonation](delegation-and-impersonation.md)
</dt> <dt>

[Making an Asynchronous Call](making-an-asynchronous-call.md)
</dt> </dl>

 

 




