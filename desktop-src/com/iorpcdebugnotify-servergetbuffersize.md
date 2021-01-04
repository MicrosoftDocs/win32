---
title: IOrpcDebugNotify ServerGetBufferSize method
description: Retrieves the RPC buffer size from the server-side debugger.
ms.assetid: 1e9ef194-c85b-4f6d-8b89-1f7ee6941189
keywords:
- ServerGetBufferSize method COM
- ServerGetBufferSize method COM , IOrpcDebugNotify interface
- IOrpcDebugNotify interface COM , ServerGetBufferSize method
topic_type:
- apiref
api_name:
- IOrpcDebugNotify.ServerGetBufferSize
api_location:
- N/A
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IOrpcDebugNotify::ServerGetBufferSize method

Retrieves the RPC buffer size from the server-side debugger.

> [!Note]  
> An import library containing the **ServerGetBufferSize** function is not included in the Microsoft Windows Software Development Kit (SDK). An application can use the [**GetProcAddress**](/windows/desktop/api/libloaderapi/nf-libloaderapi-getprocaddress) and [**GetModuleHandle**](/windows/desktop/api/libloaderapi/nf-libloaderapi-getmodulehandlea) functions to retrieve a function pointer to [**DllDebugObjectRPCHook**](dlldebugobjectrpchook.md) from oleaut.dll and provide this function via the [**IOrpcDebugNotify**](iorpcdebugnotify.md) interface.

 

## Syntax


```C++
void ServerGetBufferSize(
   ORPC_DBG_ALL *lpOrpcDebugAll
);
```



## Parameters

<dl> <dt>

*lpOrpcDebugAll* 
</dt> <dd>

A pointer to a [**ORPC\_DBG\_ALL**](orpc-dbg-all.md) structure that contains notification specific information the COM RPC system passes to the debugger.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                     |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                           |
| Header<br/>                   | <dl> <dt>N/A</dt> </dl> |
| IDL<br/>                      | <dl> <dt>N/A</dt> </dl> |



## See also

<dl> <dt>

[**ORPC\_INIT\_ARGS**](orpc-init-args.md)
</dt> <dt>

[**DllDebugObjectRPCHook**](dlldebugobjectrpchook.md)
</dt> <dt>

[**IOrpcDebugNotify**](iorpcdebugnotify.md)
</dt> </dl>

 

