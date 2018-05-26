---
title: RpcTryExcept
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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# RpcTryExcept

The **RpcTryExcept** statement provides structured exception handling for RPC applications. If any of the program statements in the **RpcTryExcept** cause an exception, the statements in the [**RpcExcept**](/windows/win32/Rpc/nf-rpc-rpcexcept?branch=master) code block are executed. All **RpcTryExcept** statements must be terminated by the [**RpcEndExcept**](/windows/win32/Rpc/?branch=master) statement.

For more information, see [**RpcExcept**](/windows/win32/Rpc/nf-rpc-rpcexcept?branch=master).

**Windows Vista and later versions of Windows:  **[**RpcExceptionFilter**](/windows/win32/Rpcdce/nf-rpcdce-rpcexceptionfilter?branch=master) is recommended for structured exception handling for the most common exceptions as an alternative to custom filters with [**RpcExcept**](/windows/win32/Rpc/nf-rpc-rpcexcept?branch=master).

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Rpc.h</dt> </dl> |



## See also

<dl> <dt>

[**RpcExcept**](/windows/win32/Rpc/nf-rpc-rpcexcept?branch=master)
</dt> <dt>

[**RpcExceptionFilter**](/windows/win32/Rpcdce/nf-rpcdce-rpcexceptionfilter?branch=master)
</dt> <dt>

[**RpcTryFinally**](rpctryfinally.md)
</dt> </dl>

 

 





