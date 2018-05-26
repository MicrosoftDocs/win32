---
title: Receiving Cancellations
description: The server application can call RpcServerTestCancel with the binding handle of the call in question to find out if the client has requested cancellation of the asynchronous call. It will return RPC\_S\_OK if the client canceled the call.
ms.assetid: ac7d7a50-a788-40a9-b57d-1f528bdbd7df
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Receiving Cancellations

The server application can call [**RpcServerTestCancel**](/windows/win32/Rpcdce/nf-rpcdce-rpcservertestcancel?branch=master) with the binding handle of the call in question to find out if the client has requested cancellation of the asynchronous call. It will return RPC\_S\_OK if the client canceled the call.

 

 




