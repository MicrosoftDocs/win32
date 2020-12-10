---
title: IOrpcDebugNotify ServerNotify method
description: Informs the server of an incoming debugger request from the client.
ms.assetid: 6c868b9e-f25b-4d27-80ff-697d0c005b8d
keywords:
- ServerNotify method COM
- ServerNotify method COM , IOrpcDebugNotify interface
- IOrpcDebugNotify interface COM , ServerNotify method
topic_type:
- apiref
api_name:
- IOrpcDebugNotify.ServerNotify
api_location:
- N/A
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IOrpcDebugNotify::ServerNotify method

Informs the server of an incoming debugger request from the client.

> [!Note]  
> An import library containing the **ServerNotify** function is not included in the Microsoft Windows Software Development Kit (SDK). An application can use the [**GetProcAddress**](/windows/desktop/api/libloaderapi/nf-libloaderapi-getprocaddress) and [**GetModuleHandle**](/windows/desktop/api/libloaderapi/nf-libloaderapi-getmodulehandlea) functions to retrieve a function pointer to [**DllDebugObjectRPCHook**](dlldebugobjectrpchook.md) from oleaut.dll and provide this function via the [**IOrpcDebugNotify**](iorpcdebugnotify.md) interface.

 

## Syntax


```C++
void ServerNotify(
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

 

