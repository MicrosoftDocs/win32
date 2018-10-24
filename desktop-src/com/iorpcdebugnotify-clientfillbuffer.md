---
title: IOrpcDebugNotify ClientFillBuffer method
description: Sends data from the client debugger to the server debugger.
ms.assetid: d575cf34-34a2-4951-a87e-7835b2c5b7a0
keywords:
- ClientFillBuffer method COM
- ClientFillBuffer method COM , IOrpcDebugNotify interface
- IOrpcDebugNotify interface COM , ClientFillBuffer method
topic_type:
- apiref
api_name:
- IOrpcDebugNotify.ClientFillBuffer
api_location:
- N/A
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IOrpcDebugNotify::ClientFillBuffer method

Sends data from the client debugger to the server debugger.

> [!Note]  
> An import library containing the **ClientFillBuffer** function is not included in the Microsoft Windows Software Development Kit (SDK). An application can use the [**GetProcAddress**](https://msdn.microsoft.com/library/windows/desktop/ms683212) and [**GetModuleHandle**](https://msdn.microsoft.com/library/windows/desktop/ms683199) functions to retrieve a function pointer to [**DllDebugObjectRPCHook**](dlldebugobjectrpchook.md) from oleaut.dll and provide this function via the [**IOrpcDebugNotify**](iorpcdebugnotify.md) interface.

 

## Syntax


```C++
void ClientFillBuffer(
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

[**DllDebugObjectRPCHook**](dlldebugobjectrpchook.md)
</dt> <dt>

[**IOrpcDebugNotify**](iorpcdebugnotify.md)
</dt> </dl>

 

 





