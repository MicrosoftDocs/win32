---
title: Unloading a Server with Outstanding Context Handles
description: Traditionally, unloading a DLL that services RPC calls using context handles, without first stopping the hosting process, has been problematic.
ms.assetid: d3880578-e542-418c-803a-fd00d0bfde7f
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Unloading a Server with Outstanding Context Handles

Traditionally, unloading a DLL that services RPC calls using context handles, without first stopping the hosting process, has been problematic. This is because the run-down routine is no longer valid when the DLL is being unloaded. When a client with a previously open context handle fails, and the RPC run time tries to close the context handle, its attempt to call the run-down routine access violates, and the server crashes.

Beginning with Windows XP, a new API called [**RpcServerUnregisterIfEx**](/windows/win32/Rpcdce/nf-rpcdce-rpcserverunregisterifex?branch=master) has been added. **RpcServerUnregisterIfEx** closes context handles opened by the interface being unregistered; the [**RpcServerUnregisterIf**](/windows/win32/Rpcdce/nf-rpcdce-rpcserverunregisterif?branch=master) function does not. Using **RpcServerUnregisterIfEx** is not necessary when the entire process shuts down, but it is necessary if one or more DLLs hosting the run-down routines is unloaded while outstanding context handles exist.

 

 




