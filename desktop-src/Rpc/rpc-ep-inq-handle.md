---
title: RPC\_EP\_INQ\_HANDLE
description: The RPC\_EP\_INQ\_HANDLE data type declares a handle for an inquiry context. RPC applications use it to view server address information stored in the endpoint map.
ms.assetid: e18ce800-0110-4450-9a1b-a3f777d00f2d
keywords:
- RPC_EP_INQ_HANDLE
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# RPC\_EP\_INQ\_HANDLE

The **RPC\_EP\_INQ\_HANDLE** data type declares a handle for an inquiry context. RPC applications use it to view server address information stored in the endpoint map.


```C++
typedef I_RPC_HANDLE* RPC_EP_INQ_HANDLE;
```



## Requirements



|                                     |                                                                                                       |
|-------------------------------------|-------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                  |
| Header<br/>                   | <dl> <dt>Rpcasync.h (include Rpc.h)</dt> </dl> |



## See also

<dl> <dt>

[**RpcMgmtEpEltInqBegin**](/windows/win32/Rpcdce/nf-rpcdce-rpcmgmtepeltinqbegin?branch=master)
</dt> <dt>

[**RpcMgmtEpEltInqNext**](/windows/win32/Rpcdce/nf-rpcdce-rpcmgmtepeltinqnext?branch=master)
</dt> <dt>

[**RpcMgmtEpEltInqDone**](/windows/win32/Rpcdce/nf-rpcdce-rpcmgmtepeltinqdone?branch=master)
</dt> </dl>

 

 





