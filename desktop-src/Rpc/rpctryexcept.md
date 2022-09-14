---
title: RpcTryExcept (Rpc.h)
description: The RpcTryExcept statement provides structured exception handling for RPC applications.
ms.assetid: 3addb367-4bdc-4c11-bf4d-b5b94da45b26
keywords:
- RpcTryExcept RPC
topic_type:
- apiref
api_name:
- RpcTryExcept
api_location:
- Rpc.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# RpcTryExcept

The **RpcTryExcept** statement provides structured exception handling for RPC applications. If any of the program statements in the **RpcTryExcept** cause an exception, the statements in the [**RpcExcept**](/windows/desktop/api/Rpc/nf-rpc-rpcexcept) code block are executed. All **RpcTryExcept** statements must be terminated by the [**RpcEndExcept**](/previous-versions/aa375629(v=vs.80)) statement.

For more information, see [**RpcExcept**](/windows/desktop/api/Rpc/nf-rpc-rpcexcept).

**Windows Vista and later versions of Windows:**  [**RpcExceptionFilter**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcexceptionfilter) is recommended for structured exception handling for the most common exceptions as an alternative to custom filters with [**RpcExcept**](/windows/desktop/api/Rpc/nf-rpc-rpcexcept).

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Rpc.h</dt> </dl> |



## See also

<dl> <dt>

[**RpcExcept**](/windows/desktop/api/Rpc/nf-rpc-rpcexcept)
</dt> <dt>

[**RpcExceptionFilter**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcexceptionfilter)
</dt> <dt>

[**RpcTryFinally**](rpctryfinally.md)
</dt> </dl>

 

