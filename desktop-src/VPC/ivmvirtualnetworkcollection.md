---
title: IVMVirtualNetworkCollection interface (VPCCOMInterfaces.h)
description: Defines a collection of IVMVirtualNetwork objects. To obtain an IVMVirtualNetworkCollection object, use the IVMVirtualPC VirtualNetworks property.
ms.assetid: 3d595bc3-1a8d-4e09-a809-944d4dcdc675
keywords:
- IVMVirtualNetworkCollection interface Virtual PC
- IVMVirtualNetworkCollection interface Virtual PC , described
topic_type:
- apiref
api_name:
- IVMVirtualNetworkCollection
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMVirtualNetworkCollection interface

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Defines a collection of [**IVMVirtualNetwork**](ivmvirtualnetwork.md) objects. To obtain an **IVMVirtualNetworkCollection** object, use the [**IVMVirtualPC::VirtualNetworks**](ivmvirtualpc-virtualnetworks.md) property.

## Members

The **IVMVirtualNetworkCollection** interface inherits from the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface. **IVMVirtualNetworkCollection** also has these types of members:

-   [Properties](#properties)

### Properties

The **IVMVirtualNetworkCollection** interface has these properties.



| Property                                                             | Access type          | Description                                                                                                   |
|:---------------------------------------------------------------------|:---------------------|:--------------------------------------------------------------------------------------------------------------|
| [**\_NewEnum**](ivmvirtualnetworkcollection--newenum.md)<br/> | Read-only<br/> | An enumerator for the collection.<br/>                                                                  |
| [**Count**](ivmvirtualnetworkcollection-count.md)<br/>        | Read-only<br/> | The number of virtual networks in this collection.<br/>                                                 |
| [**Item**](ivmvirtualnetworkcollection-item.md)<br/>          | Read-only<br/> | The [**IVMVirtualNetwork**](ivmvirtualnetwork.md) object that corresponds to the specified index.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                     |
| Minimum supported server<br/> | None supported<br/>                                                                      |
| End of client support<br/>    | Windows 7<br/>                                                                           |
| Product<br/>                  | Windows Virtual PC<br/>                                                                  |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl>  |
| IID<br/>                      | IID\_IVMVirtualNetworkCollection is defined as 8ed680be-4242-4b2a-a21c-1982d8b0f675<br/> |



 

