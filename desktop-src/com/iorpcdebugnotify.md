---
title: IOrpcDebugNotify interface
description: Provides remote debugging functionality.
ms.assetid: f91987c0-2e4b-4872-8ed6-e208a23baa49
keywords:
- IOrpcDebugNotify interface COM
- IOrpcDebugNotify interface COM , described
topic_type:
- apiref
api_name:
- IOrpcDebugNotify
api_location:
- N/A
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IOrpcDebugNotify interface

Provides remote debugging functionality.

## When to implement

Implement this interface to enable remote debugging over RPC.

## When to use

This interface should be used for in-process remote debugging when software exceptions should not be used for the COM debugger notifications. It enables in-process debuggers to be notified by direct calls using these methods.

## Members

The **IOrpcDebugNotify** interface inherits from the [**IUnknown**](/windows/desktop/api/Unknwn/nn-unknwn-iunknown) interface. **IOrpcDebugNotify** also has these types of members:

-   [Methods](#methods)

### Methods

The **IOrpcDebugNotify** interface has these methods.



| Method                                                              | Description                                                                    |
|:--------------------------------------------------------------------|:-------------------------------------------------------------------------------|
| [**ClientFillBuffer**](iorpcdebugnotify-clientfillbuffer.md)       | Sends data from the client debugger to the server debugger.<br/>         |
| [**ClientGetBufferSize**](iorpcdebugnotify-clientgetbuffersize.md) | Retrieves the RPC buffer size from the client-side debugger.<br/>        |
| [**ClientNotify**](iorpcdebugnotify-clientnotify.md)               | Informs the client of an outgoing debugger request to the server.<br/>   |
| [**ServerFillBuffer**](iorpcdebugnotify-serverfillbuffer.md)       | Sends data from the server debugger to the client debugger.<br/>         |
| [**ServerGetBufferSize**](iorpcdebugnotify-servergetbuffersize.md) | Retrieves the RPC buffer size from the server-side debugger.<br/>        |
| [**ServerNotify**](iorpcdebugnotify-servernotify.md)               | Informs the server of an incoming debugger request from the client.<br/> |



 

## Remarks

An import library containing the **IOrpcDebugNotify** interface is not included in the Microsoft Windows Software Development Kit (SDK). An application can use the [**GetProcAddress**](/windows/desktop/api/libloaderapi/nf-libloaderapi-getprocaddress) and [**GetModuleHandle**](/windows/desktop/api/libloaderapi/nf-libloaderapi-getmodulehandlea) functions to retrieve a function pointer to [**DllDebugObjectRPCHook**](dlldebugobjectrpchook.md) from oleaut.dll and provide these methods via the **IOrpcDebugNotify** interface.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                     |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                           |
| Header<br/>                   | <dl> <dt>N/A</dt> </dl> |
| IDL<br/>                      | <dl> <dt>N/A</dt> </dl> |



## See also

<dl> <dt>

[**IUnknown**](/windows/desktop/api/Unknwn/nn-unknwn-iunknown)
</dt> <dt>

[**ORPC\_DBG\_ALL**](orpc-dbg-all.md)
</dt> <dt>

[**ORPC\_DBG\_BUFFER**](orpc-dbg-buffer.md)
</dt> <dt>

[**ORPC\_INIT\_ARGS**](orpc-init-args.md)
</dt> <dt>

[**DllDebugObjectRPCHook**](dlldebugobjectrpchook.md)
</dt> </dl>

 

