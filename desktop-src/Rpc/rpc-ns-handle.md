---
title: RPC\_NS\_HANDLE
description: The data type RPC\_NS\_HANDLE defines a name-service handle.
ms.assetid: 'd9c2a376-4972-4f16-aa8d-f0e43d5ddb8d'
keywords: ["RPC_NS_HANDLE"]
---

# RPC\_NS\_HANDLE

The data type **RPC\_NS\_HANDLE** defines a name-service handle.


```C++
typedef void* RPC_NS_HANDLE;
```



## Remarks

A name-service handle is an opaque variable containing information the RPC run-time library uses to return the following RPC data from the name-service database:

-   Server-binding handles
-   UUIDs of resources offered by server profile members
-   Group members

The scope of a name-service handle is from a "Begin" routine through the corresponding "Done" routine.

Applications are responsible for concurrency control of name-service handles across threads.

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                |
| Header<br/>                   | <dl> <dt>Rpcnsi.h (include Rpc.h)</dt> </dl> |



## See also

<dl> <dt>

[**RpcNsBindingImportBegin**](rpcnsbindingimportbegin.md)
</dt> <dt>

[**RpcNsBindingImportDone**](rpcnsbindingimportdone.md)
</dt> <dt>

[**RpcNsBindingImportNext**](rpcnsbindingimportnext.md)
</dt> <dt>

[**RpcNsBindingLookupBegin**](rpcnsbindinglookupbegin.md)
</dt> <dt>

[**RpcNsBindingLookupDone**](rpcnsbindinglookupdone.md)
</dt> <dt>

[**RpcNsBindingLookupNext**](rpcnsbindinglookupnext.md)
</dt> </dl>

 

 





