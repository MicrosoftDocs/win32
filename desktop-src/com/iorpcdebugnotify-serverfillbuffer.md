---
title: IOrpcDebugNotify ServerFillBuffer method
description: Sends data from the server debugger to the client debugger.
ms.assetid: 58813f28-6e32-478c-8b12-8cf0ebe01973
keywords:
- ServerFillBuffer method COM
- ServerFillBuffer method COM , IOrpcDebugNotify interface
- IOrpcDebugNotify interface COM , ServerFillBuffer method
topic_type:
- apiref
api_name:
- IOrpcDebugNotify.ServerFillBuffer
api_location:
- N/A
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IOrpcDebugNotify::ServerFillBuffer method

Sends data from the server debugger to the client debugger.

> [!Note]  
> An import library containing the **ServerFillBuffer** function is not included in the Microsoft Windows Software Development Kit (SDK). An application can use the [**GetProcAddress**](https://msdn.microsoft.com/library/windows/desktop/ms683212) and [**GetModuleHandle**](https://msdn.microsoft.com/library/windows/desktop/ms683199) functions to retrieve a function pointer to [**DllDebugObjectRPCHook**](dlldebugobjectrpchook.md) from oleaut.dll and provide this function via the [**IOrpcDebugNotify**](iorpcdebugnotify.md) interface.

 

## Syntax


```C++
void ServerFillBuffer(
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



|                                     |                                                                                |
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

 

 





