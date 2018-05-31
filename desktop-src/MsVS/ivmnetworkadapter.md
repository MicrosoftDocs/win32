---
title: IVMNetworkAdapter interface
description: The IVMNetworkAdapter interface is the interface to a virtual network interface card (NIC).
ms.assetid: 60f1db1e-54ba-4f35-bc12-de87257687d4
keywords:
- IVMNetworkAdapter interface Virtual Server
- IVMNetworkAdapter interface Virtual Server , described
topic_type:
- apiref
api_name:
- IVMNetworkAdapter
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMNetworkAdapter interface

The **IVMNetworkAdapter** interface is the interface to a virtual network interface card (NIC). It is used to set up how a virtual machine is networked. Network interface cards can be added and removed by using [**IVMVirtualMachine::AddNetworkAdapter**](ivmvirtualmachine-addnetworkadapter.md) and [**IVMVirtualMachine::RemoveNetworkAdapter**](ivmvirtualmachine-removenetworkadapter.md). You can also retrieve an **IVMNetworkAdapter** object from the [**IVMNetworkAdapterCollection**](ivmnetworkadaptercollection.md) collection returned from the [**IVMVirtualMachine::NetworkAdapters**](ivmvirtualmachine-networkadapters.md) property.

## When to use

The following procedures explain how to use the **IVMNetworkAdapter** interface.

**To attach a virtual NIC to a host NIC**

-   Virtual (guest) NICs are not attached directly to a host NIC. Instead, the virtual NIC is attached to a virtual network that is attached to a host NIC. For more information about configuring virtual networks, see [**IVMVirtualNetwork**](ivmvirtualnetwork.md). To attach the virtual NIC to a virtual network, use the [**AttachToVirtualNetwork**](ivmnetworkadapter-attachtovirtualnetwork.md) method.

**To disconnect a virtual NIC from the virtual network**

-   The [**DetachFromVirtualNetwork**](ivmnetworkadapter-detachfromvirtualnetwork.md) method will detach the virtual NIC from the virtual network. After this function is called, the [**VirtualNetwork**](ivmnetworkadapter-virtualnetwork.md) property will return a virtual network ID that is not valid.

**To remove a virtual NIC from a virtual machine if you have the virtual NIC object**

1.  Get the virtual machine associated with the virtual NIC by using the [**VirtualMachine**](ivmnetworkadapter-virtualmachine.md) property.
2.  Use the current object as a parameter to the [**IVMVirtualMachine::RemoveNetworkAdapter**](ivmvirtualmachine-removenetworkadapter.md) method.
    > [!Note]  
    > The default Ethernet address for a network interface is "00-00-00-00-00-00", which is considered an invalid Ethernet address by most operating systems. If [**IsEthernetAddressDynamic**](ivmnetworkadapter-isethernetaddressdynamic.md) is set to **FALSE**, use [**EthernetAddress**](ivmnetworkadapter-ethernetaddress.md) to specify a valid Ethernet address.

     

## Members

The **IVMNetworkAdapter** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IVMNetworkAdapter** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IVMNetworkAdapter** interface has these methods.



| Method                                                                         | Description                                                                                             |
|:-------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------|
| [**AttachToVirtualNetwork**](ivmnetworkadapter-attachtovirtualnetwork.md)     | Attaches the virtual NIC to the specified virtual network by using the virtual network's ID.<br/> |
| [**DetachFromVirtualNetwork**](ivmnetworkadapter-detachfromvirtualnetwork.md) | Detaches the virtual NIC from its virtual network.<br/>                                           |



 

### Properties

The **IVMNetworkAdapter** interface has these properties.



| Property                                                                                  | Access type           | Description                                                                 |
|:------------------------------------------------------------------------------------------|:----------------------|:----------------------------------------------------------------------------|
| [**\_ID**](ivmnetworkadapter--id.md)<br/>                                          | Read-only<br/>  | The internal ID of this network adapter.<br/>                         |
| [**EthernetAddress**](ivmnetworkadapter-ethernetaddress.md)<br/>                   | Read/write<br/> | The Ethernet (MAC/Physical/Network) address of the virtual NIC.<br/>  |
| [**IsEthernetAddressDynamic**](ivmnetworkadapter-isethernetaddressdynamic.md)<br/> | Read/write<br/> | Indicates whether the Ethernet address is dynamically generated.<br/> |
| [**VirtualMachine**](ivmnetworkadapter-virtualmachine.md)<br/>                     | Read-only<br/>  | The virtual machine associated with this virtual NIC.<br/>            |
| [**VirtualNetwork**](ivmnetworkadapter-virtualnetwork.md)<br/>                     | Read-only<br/>  | The virtual network to which the virtual NIC is attached.<br/>        |



 

## Remarks

The default Ethernet address for a network interface is "00-00-00-00-00-00", which is considered an invalid Ethernet address by most operating systems. If [**IsEthernetAddressDynamic**](ivmnetworkadapter-isethernetaddressdynamic.md) is set to **FALSE**, [**EthernetAddress**](ivmnetworkadapter-ethernetaddress.md) must be initialized with a valid Ethernet network address.

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5)
</dt> <dt>

[Virtual Server Interfaces](interfaces.md)
</dt> <dt>

[IVMNetwork Methods](ivmnetworkadapter-methods.md)
</dt> <dt>

[IVMNetwork Properties](ivmnetworkadapter-properties.md)
</dt> </dl>

 

 





