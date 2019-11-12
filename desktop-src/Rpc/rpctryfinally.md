---
title: RpcTryFinally (Rpc.h)
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
ms.topic: reference
ms.date: 05/31/2018
---

# RpcTryFinally

The **RpcTryFinally** statement provides structured termination handling. It an exception occurs during the execution statements of the code block associated with the **RpcTryFinally** statement, the statements in the code block associated with the [**RpcFinally**](https://msdn.microsoft.com/en-US/library/Aa375699(v=VS.80).aspx) statement are executed. All **RpcTryFinally** statements must be terminated by an [**RpcEndFinally**](https://msdn.microsoft.com/en-US/library/Aa375634(v=VS.80).aspx) statement.

For more information, see [**RpcFinally**](https://msdn.microsoft.com/en-US/library/Aa375699(v=VS.80).aspx).

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Rpc.h</dt> </dl> |



## See also

<dl> <dt>

[**RpcFinally**](https://msdn.microsoft.com/en-US/library/Aa375699(v=VS.80).aspx)
</dt> <dt>

[**RpcEndFinally**](https://msdn.microsoft.com/en-US/library/Aa375634(v=VS.80).aspx)
</dt> </dl>

 

 





