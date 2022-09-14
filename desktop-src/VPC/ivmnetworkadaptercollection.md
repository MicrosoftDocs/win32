---
title: IVMNetworkAdapterCollection interface (VPCCOMInterfaces.h)
description: Defines a collection of virtual network interface cards. To obtain an IVMNetworkAdapterCollection object, use the IVMVirtualMachine NetworkAdapters, IVMVirtualNetwork NetworkAdapters, and IVMVirtualPC UnconnectedNetworkAdapters properties.
ms.assetid: cfb03a7c-a568-488c-9284-798b7e21027a
keywords:
- IVMNetworkAdapterCollection interface Virtual PC
- IVMNetworkAdapterCollection interface Virtual PC , described
topic_type:
- apiref
api_name:
- IVMNetworkAdapterCollection
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMNetworkAdapterCollection interface

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Defines a collection of virtual network interface cards. To obtain an IVMNetworkAdapterCollection object, use the [**IVMVirtualMachine::NetworkAdapters**](ivmvirtualmachine-networkadapters.md), [**IVMVirtualNetwork::NetworkAdapters**](ivmvirtualnetwork-networkadapters.md), and [**IVMVirtualPC::UnconnectedNetworkAdapters**](ivmvirtualpc-unconnectednetworkadapters.md) properties.

## Members

The **IVMNetworkAdapterCollection** interface inherits from the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface. **IVMNetworkAdapterCollection** also has these types of members:

-   [Properties](#properties)

### Properties

The **IVMNetworkAdapterCollection** interface has these properties.



| Property                                                             | Access type          | Description                                                                                                   |
|:---------------------------------------------------------------------|:---------------------|:--------------------------------------------------------------------------------------------------------------|
| [**\_NewEnum**](ivmnetworkadaptercollection--newenum.md)<br/> | Read-only<br/> | An enumerator for the collection.<br/>                                                                  |
| [**Count**](ivmnetworkadaptercollection-count.md)<br/>        | Read-only<br/> | The number of network interfaces in this collection.<br/>                                               |
| [**Item**](ivmnetworkadaptercollection-item.md)<br/>          | Read-only<br/> | The [**IVMNetworkAdapter**](ivmnetworkadapter.md) object that corresponds to the specified index.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                     |
| Minimum supported server<br/> | None supported<br/>                                                                      |
| End of client support<br/>    | Windows 7<br/>                                                                           |
| Product<br/>                  | Windows Virtual PC<br/>                                                                  |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl>  |
| IID<br/>                      | IID\_IVMNetworkAdapterCollection is defined as ebaeafe9-ebcd-47cf-866e-ad87d735e479<br/> |



## See also

<dl> <dt>

[**IVMNetworkAdapter**](ivmnetworkadapter.md)
</dt> <dt>

[**IVMVirtualMachine::NetworkAdapters**](ivmvirtualmachine-networkadapters.md)
</dt> <dt>

[**IVMVirtualNetwork::NetworkAdapters**](ivmvirtualnetwork-networkadapters.md)
</dt> <dt>

[**IVMVirtualPC::UnconnectedNetworkAdapters**](ivmvirtualpc-unconnectednetworkadapters.md)
</dt> </dl>

 

