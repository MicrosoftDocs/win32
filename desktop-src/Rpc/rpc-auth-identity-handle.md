---
title: RPC\_AUTH\_IDENTITY\_HANDLE
description: The RPC\_AUTH\_IDENTITY\_HANDLE data type declares a handle that points to a structure containing the clients authentication and authorization credentials specified for remote procedure calls.
ms.assetid: 06e45348-a392-45be-9f8a-e77ef887f26c
keywords:
- RPC_AUTH_IDENTITY_HANDLE
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# RPC\_AUTH\_IDENTITY\_HANDLE

The **RPC\_AUTH\_IDENTITY\_HANDLE** data type declares a handle that points to a structure containing the client's authentication and authorization credentials specified for remote procedure calls.


```C++
typedef void* RPC_AUTH_IDENTITY_HANDLE;
```



## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                |
| Header<br/>                   | <dl> <dt>Rpcdce.h (include Rpc.h)</dt> </dl> |



## See also

<dl> <dt>

[**RpcBindingInqAuthInfo**](/windows/win32/Rpcdce/nf-rpcdce-rpcbindinginqauthinfo?branch=master)
</dt> <dt>

[**RpcBindingSetAuthInfo**](/windows/win32/Rpcdce/nf-rpcdce-rpcbindingsetauthinfo?branch=master)
</dt> </dl>

 

 





