---
title: Key Acquisition Functions
description: By default, the SSP supplies encryption keys to server programs that request them. Each SSP implements its own system of generating keys. The format of the keys that the SSP generates are specific to the SSP.
ms.assetid: 0ba7212c-6ee8-4a92-94d0-f09f84b05bf3
ms.topic: article
ms.date: 05/31/2018
---

# Key Acquisition Functions

By default, the SSP supplies encryption keys to server programs that request them. Each SSP implements its own system of generating keys. The format of the keys that the SSP generates are specific to the SSP.

RPC provides you with the ability to override the default method of generating encryption keys. Your application can call the [**RpcServerRegisterAuthInfo**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterauthinfo) function and pass it a pointer to a key acquisition function. You can write the key acquisition function so that it generates keys using any method you choose. However, the key it passes to the server program must match the format that the SSP requires.

> [!Note]  
> Most applications do not need to use key acquisition functions, and can simply supply **NULL** to all parameters where a key acquisition function is requested.

 

 

 




