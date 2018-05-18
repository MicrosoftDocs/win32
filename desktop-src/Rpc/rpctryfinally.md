---
title: RpcTryFinally
description: The RpcTryFinally statement provides structured termination handling.
ms.assetid: 'e9ed748a-db15-4c91-b8a4-b510f99042d8'
keywords: ["RpcTryFinally RPC"]
topic_type:
- apiref
api_name:
- RpcTryFinally
api_location:
- Rpc.h
api_type:
- HeaderDef
---

# RpcTryFinally

The **RpcTryFinally** statement provides structured termination handling. It an exception occurs during the execution statements of the code block associated with the **RpcTryFinally** statement, the statements in the code block associated with the [**RpcFinally**](rpcfinally.md) statement are executed. All **RpcTryFinally** statements must be terminated by an [**RpcEndFinally**](rpcendfinally.md) statement.

For more information, see [**RpcFinally**](rpcfinally.md).

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Rpc.h</dt> </dl> |



## See also

<dl> <dt>

[**RpcFinally**](rpcfinally.md)
</dt> <dt>

[**RpcEndFinally**](rpcendfinally.md)
</dt> </dl>

 

 





