---
title: IVMVirtualNetwork interface (VPCCOMInterfaces.h)
description: Defines a virtual network.
ms.assetid: 1ddafc33-05d4-45fb-924d-9830288aa240
keywords:
- IVMVirtualNetwork interface Virtual PC
- IVMVirtualNetwork interface Virtual PC , described
topic_type:
- apiref
api_name:
- IVMVirtualNetwork
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMVirtualNetwork interface

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Defines a virtual network. **IVMVirtualNetwork** objects are returned from [**IVMVirtualPC**](ivmvirtualpc.md) method [**FindVirtualNetwork**](ivmvirtualpc-findvirtualnetwork.md). You can also retrieve an **IVMVirtualNetwork** object from the [**IVMVirtualNetworkCollection**](ivmvirtualnetworkcollection.md) object returned from the [**IVMVirtualPC::VirtualNetworks**](ivmvirtualpc-virtualnetworks.md) property.

A virtual network consists of a virtual switch, which performs all internal routing, and several connections that are "plugged in" to the virtual switch. These connections can be a real external host connection, an "internal network" or shared networking (NAT).

## Members

The **IVMVirtualNetwork** interface inherits from the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface. **IVMVirtualNetwork** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IVMVirtualNetwork** interface has these methods.



| Method                                | Description                                                          |
|:--------------------------------------|:---------------------------------------------------------------------|
| [**\_ID**](ivmvirtualnetwork--id.md) | Retrieves the internal identifier of the virtual network.<br/> |



 

### Properties

The **IVMVirtualNetwork** interface has these properties.



| Property                                                                | Access type          | Description                                                                    |
|:------------------------------------------------------------------------|:---------------------|:-------------------------------------------------------------------------------|
| [**HostAdapter**](ivmvirtualnetwork-hostadapter.md)<br/>         | Read-only<br/> | The name of the adapter to which the virtual network is connected.<br/>  |
| [**MediaType**](/previous-versions/windows/desktop/legacy/dd796707(v=vs.85))<br/>             | Read-only<br/> | Determines whether the virtual network instance is wireless or not.<br/> |
| [**Name**](ivmvirtualnetwork-name.md)<br/>                       | Read-only<br/> | The unique name of the virtual network instance.<br/>                    |
| [**NetworkAdapters**](ivmvirtualnetwork-networkadapters.md)<br/> | Read-only<br/> | An enumerable collection of NICs attached to the virtual network.<br/>   |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMVirtualNetwork is defined as 431cb7a1-2469-4563-b94e-38b987adca63<br/>          |



 

