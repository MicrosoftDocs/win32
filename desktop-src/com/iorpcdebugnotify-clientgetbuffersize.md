---
title: IOrpcDebugNotify ClientGetBufferSize method
description: Retrieves the RPC buffer size from the client-side debugger.
ms.assetid: 05475156-1508-4eb2-82a6-bb1701839fbd
keywords:
- ClientGetBufferSize method COM
- ClientGetBufferSize method COM , IOrpcDebugNotify interface
- IOrpcDebugNotify interface COM , ClientGetBufferSize method
topic_type:
- apiref
api_name:
- IOrpcDebugNotify.ClientGetBufferSize
api_location:
- N/A
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IOrpcDebugNotify::ClientGetBufferSize method

Retrieves the RPC buffer size from the client-side debugger.

> [!Note]  
> An import library containing the **ClientGetBufferSize** function is not included in the Microsoft Windows Software Development Kit (SDK). An application can use the [**GetProcAddress**](/windows/desktop/api/libloaderapi/nf-libloaderapi-getprocaddress) and [**GetModuleHandle**](/windows/desktop/api/libloaderapi/nf-libloaderapi-getmodulehandlea) functions to retrieve a function pointer to [**DllDebugObjectRPCHook**](dlldebugobjectrpchook.md) from oleaut.dll and provide this function via the [**IOrpcDebugNotify**](iorpcdebugnotify.md) interface.

 

## Syntax


```C++
void ClientGetBufferSize(
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

 

