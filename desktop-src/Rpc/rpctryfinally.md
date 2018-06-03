---
title: RpcTryFinally
description: The RpcTryFinally statement provides structured termination handling.
ms.assetid: e9ed748a-db15-4c91-b8a4-b510f99042d8
keywords:
- RpcTryFinally RPC
topic_type:
- apiref
api_name:
- RpcTryFinally
api_location:
- Rpc.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RpcTryFinally

The **RpcTryFinally** statement provides structured termination handling. It an exception occurs during the execution statements of the code block associated with the **RpcTryFinally** statement, the statements in the code block associated with the [**RpcFinally**](/windows/desktop/api/Rpc/) statement are executed. All **RpcTryFinally** statements must be terminated by an [**RpcEndFinally**](/windows/desktop/api/Rpc/) statement.

For more information, see [**RpcFinally**](/windows/desktop/api/Rpc/).

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Rpc.h</dt> </dl> |



## See also

<dl> <dt>

[**RpcFinally**](/windows/desktop/api/Rpc/)
</dt> <dt>

[**RpcEndFinally**](/windows/desktop/api/Rpc/)
</dt> </dl>

 

 





