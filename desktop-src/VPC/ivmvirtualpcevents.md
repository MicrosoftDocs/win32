---
title: IVMVirtualPCEvents interface (VPCCOMInterfaces.h)
description: Defines the outgoing event interface for the IVMVirtualPC interface.
ms.assetid: 40ce14d8-43e4-4c72-9729-e5503d882be6
keywords:
- IVMVirtualPCEvents interface Virtual PC
- IVMVirtualPCEvents interface Virtual PC , described
topic_type:
- apiref
api_name:
- IVMVirtualPCEvents
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMVirtualPCEvents interface

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Defines the outgoing event interface for the [**IVMVirtualPC**](ivmvirtualpc.md) interface. The client implements these methods to receive events sent from [**IVMVirtualPC**](ivmvirtualpc.md).

## Members

The **IVMVirtualPCEvents** interface inherits from the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface. **IVMVirtualPCEvents** also has these types of members:

-   [Methods](#methods)

### Methods

The **IVMVirtualPCEvents** interface has these methods.



| Method                                                        | Description                                                                  |
|:--------------------------------------------------------------|:-----------------------------------------------------------------------------|
| [**OnEventLogged**](ivmvirtualpcevents-oneventlogged.md)     | Receives notification that Windows Virtual PC logs an event.<br/>      |
| [**OnVMStateChange**](ivmvirtualpcevents-onvmstatechange.md) | Receives notification that a virtual machine's state has changed.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | DIID\_IVMVirtualPCEvents is defined as efed1ef1-3c09-41f7-a9c2-7e29fa286c9d<br/>        |



 

