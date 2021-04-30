---
title: IVMVirtualPCEvents OnEventLogged method (VPCCOMInterfaces.h)
description: Receives notification that Windows Virtual PC logs an event.
ms.assetid: 89439e8e-e9bf-409e-a129-525b9feb8fdd
keywords:
- OnEventLogged method Virtual PC
- OnEventLogged method Virtual PC , IVMVirtualPCEvents interface
- IVMVirtualPCEvents interface Virtual PC , OnEventLogged method
topic_type:
- apiref
api_name:
- IVMVirtualPCEvents.OnEventLogged
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMVirtualPCEvents::OnEventLogged method

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Receives notification that Windows Virtual PC logs an event.

## Syntax


```C++
HRESULT OnEventLogged(
  [in] long logMessageID
);
```



## Parameters

<dl> <dt>

*logMessageID* \[in\]
</dt> <dd>

The message identifier of the event log message that was logged.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

This method is called when Windows Virtual PC logs a message to the Windows event log. The client program must implement this interface method to receive notification of the **vmVirtualPCEvent\_EventLogged** event originating from [**IVMVirtualPC**](ivmvirtualpc.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | DIID\_IVMVirtualPCEvents is defined as efed1ef1-3c09-41f7-a9c2-7e29fa286c9d<br/>        |



## See also

<dl> <dt>

[**IVMVirtualPCEvents**](ivmvirtualpcevents.md)
</dt> </dl>

 

