---
title: IVMNetworkAdapter interface (VPCCOMInterfaces.h)
description: Serves as the interface to a virtual network interface card.
ms.assetid: df050706-09be-47d1-9ae1-1eb0e1836d64
keywords:
- IVMNetworkAdapter interface Virtual PC
- IVMNetworkAdapter interface Virtual PC , described
topic_type:
- apiref
api_name:
- IVMNetworkAdapter
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMNetworkAdapter interface

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Serves as the interface to a virtual network interface card (NIC). It is used to set up how a virtual machine is networked. Network interface cards can be added and removed by using [**IVMVirtualMachine::AddNetworkAdapter**](ivmvirtualmachine-addnetworkadapter.md) and [**IVMVirtualMachine::RemoveNetworkAdapter**](ivmvirtualmachine-removenetworkadapter.md). You can also retrieve an **IVMNetworkAdapter** object from the [**IVMNetworkAdapterCollection**](ivmnetworkadaptercollection.md) collection returned from the [**IVMVirtualMachine::NetworkAdapters**](ivmvirtualmachine-networkadapters.md) or [**IVMVirtualNetwork::NetworkAdapters**](ivmvirtualnetwork-networkadapters.md) properties.

## Members

The **IVMNetworkAdapter** interface inherits from the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface. **IVMNetworkAdapter** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IVMNetworkAdapter** interface has these methods.



| Method                                                                         | Description                                                                 |
|:-------------------------------------------------------------------------------|:----------------------------------------------------------------------------|
| [**\_ID**](ivmnetworkadapter--id.md)                                          | Retrieves the internal identifier of this network interface.<br/>     |
| [**AttachToVirtualNetwork**](ivmnetworkadapter-attachtovirtualnetwork.md)     | Attaches the network interface to the specified virtual network.<br/> |
| [**DetachFromVirtualNetwork**](ivmnetworkadapter-detachfromvirtualnetwork.md) | Detaches the network interface from its virtual network.<br/>         |



 

### Properties

The **IVMNetworkAdapter** interface has these properties.



| Property                                                                                  | Access type           | Description                                                                 |
|:------------------------------------------------------------------------------------------|:----------------------|:----------------------------------------------------------------------------|
| [**EthernetAddress**](ivmnetworkadapter-ethernetaddress.md)<br/>                   | Read/write<br/> | The Ethernet (MAC) address of the network interface.<br/>             |
| [**IsEthernetAddressDynamic**](ivmnetworkadapter-isethernetaddressdynamic.md)<br/> | Read/write<br/> | Indicates whether the Ethernet address is dynamically generated.<br/> |
| [**VirtualMachine**](ivmnetworkadapter-virtualmachine.md)<br/>                     | Read-only<br/>  | The virtual machine associated with this network interface.<br/>      |
| [**VirtualNetwork**](ivmnetworkadapter-virtualnetwork.md)<br/>                     | Read-only<br/>  | The virtual network to which the network interface is attached.<br/>  |



 

## Remarks

The default Ethernet address for a network interface is "00-00-00-00-00-00", which is considered an invalid Ethernet address by most operating systems. If [**IsEthernetAddressDynamic**](ivmnetworkadapter-isethernetaddressdynamic.md) is set to **FALSE**, [**EthernetAddress**](ivmnetworkadapter-ethernetaddress.md) must be initialized with a valid Ethernet network address.

The following procedures explain how to use the **IVMNetworkAdapter** interface.

**To attach a virtual NIC to a host NIC**

-   Virtual (guest) NICs are not attached directly to a host NIC. Instead, the virtual NIC is attached to a virtual network that is attached to a host NIC. For more information about configuring virtual networks, see [**IVMVirtualNetwork**](ivmvirtualnetwork.md). To attach the virtual NIC to a virtual network, use the [**AttachToVirtualNetwork**](ivmnetworkadapter-attachtovirtualnetwork.md) method.

**To disconnect a virtual NIC from the virtual network**

-   The [**DetachFromVirtualNetwork**](ivmnetworkadapter-detachfromvirtualnetwork.md) method will detach the virtual NIC from the virtual network. After this function is called, the [**VirtualNetwork**](ivmnetworkadapter-virtualnetwork.md) property will return a virtual network ID that is not valid.

**To remove a virtual NIC from a virtual machine if you have the virtual NIC object**

1.  Get the virtual machine associated with the virtual NIC by using the [**VirtualMachine**](ivmnetworkadapter-virtualmachine.md) property.
2.  Use the current object as a parameter to the [**IVMVirtualMachine::RemoveNetworkAdapter**](ivmvirtualmachine-removenetworkadapter.md) method.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMNetworkAdapter is defined as e32e4165-22b8-4dc0-8d57-850171ae207a<br/>          |



 

