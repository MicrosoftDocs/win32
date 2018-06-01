---
title: IVMVirtualNetwork interface
description: The IVMVirtualNetwork interface defines a virtual network.
ms.assetid: 88975844-7ee3-44a8-ba03-9d23655ce66a
keywords:
- IVMVirtualNetwork interface Virtual Server
- IVMVirtualNetwork interface Virtual Server , described
topic_type:
- apiref
api_name:
- IVMVirtualNetwork
api_location:
- VsComInterfaces.h
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IVMVirtualNetwork interface

The **IVMVirtualNetwork** interface defines a virtual network. **IVMVirtualNetwork** objects are returned from [**IVMVirtualServer**](ivmvirtualserver.md) methods [**IVMVirtualServer::CreateVirtualNetwork**](ivmvirtualserver-createvirtualnetwork.md) and [**IVMVirtualServer::FindVirtualNetwork**](ivmvirtualserver-findvirtualnetwork.md). You can also retrieve an **IVMVirtualNetwork** object from the [**IVMVirtualNetworkCollection**](ivmvirtualnetworkcollection.md) object returned from the [**IVMVirtualServer::VirtualNetworks**](ivmvirtualserver-virtualnetworks.md) property.

## When to use

A virtual network consists of a virtual switch, which performs all internal routing, and several connections that are "plugged in" to the virtual switch. These connections can be a real external host connection, a virtual Ethernet NIC or a "virtual network server". Currently, the only "virtual network server" is the DHCP virtual network server.

## Members

The **IVMVirtualNetwork** interface inherits from the [**IDispatch**](https://msdn.microsoft.com/windows/desktop/ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IVMVirtualNetwork** also has these types of members:

-   [Properties](#properties)

### Properties

The **IVMVirtualNetwork** interface has these properties.



| Property                                                                                  | Access type           | Description                                                                                                             |
|:------------------------------------------------------------------------------------------|:----------------------|:------------------------------------------------------------------------------------------------------------------------|
| [**\_ID**](ivmvirtualnetwork--id.md)<br/>                                          | Read-only<br/>  | The internal ID of this virtual network.<br/>                                                                     |
| [**BytesDropped**](ivmvirtualnetwork-bytesdropped.md)<br/>                         | Read-only<br/>  | The current number of bytes dropped per second by this virtual network.<br/>                                      |
| [**BytesDroppedHistory**](ivmvirtualnetwork-bytesdroppedhistory.md)<br/>           | Read-only<br/>  | The recent number of bytes dropped by this virtual network (as an array of number of bytes).<br/>                 |
| [**BytesReceived**](ivmvirtualnetwork-bytesreceived.md)<br/>                       | Read-only<br/>  | The current number of bytes received per second by this virtual network.<br/>                                     |
| [**BytesReceivedHistory**](ivmvirtualnetwork-bytesreceivedhistory.md)<br/>         | Read-only<br/>  | The recent number of bytes received per second by this virtual network (as an array of number of bytes).<br/>     |
| [**BytesSent**](ivmvirtualnetwork-bytessent.md)<br/>                               | Read-only<br/>  | The current number of bytes sent per second by this virtual network.<br/>                                         |
| [**BytesSentHistory**](ivmvirtualnetwork-bytessenthistory.md)<br/>                 | Read-only<br/>  | The recent number of bytes sent per second this virtual network (as an array of number of bytes).<br/>            |
| [**DHCPVirtualNetworkServer**](ivmvirtualnetwork-dhcpvirtualnetworkserver.md)<br/> | Read-only<br/>  | The DHCP virtual network server attached to this virtual network.<br/>                                            |
| [**File**](ivmvirtualnetwork-file.md)<br/>                                         | Read-only<br/>  | The full path to the virtual network's configuration file.<br/>                                                   |
| [**HostAdapter**](ivmvirtualnetwork-hostadapter.md)<br/>                           | Read/write<br/> | The name of the host Ethernet adapter to which the virtual network is connected.<br/>                             |
| [**Name**](ivmvirtualnetwork-name.md)<br/>                                         | Read/write<br/> | The unique name of this virtual network.<br/>                                                                     |
| [**NetworkAdapters**](ivmvirtualnetwork-networkadapters.md)<br/>                   | Read-only<br/>  | An enumerable collection of NICs attached to the virtual network.<br/>                                            |
| [**Notes**](ivmvirtualnetwork-notes.md)<br/>                                       | Read/write<br/> | The notes for this virtual network.<br/>                                                                          |
| [**PacketsDropped**](ivmvirtualnetwork-packetsdropped.md)<br/>                     | Read-only<br/>  | The current number of packets dropped per second by this virtual network.<br/>                                    |
| [**PacketsDroppedHistory**](ivmvirtualnetwork-packetsdroppedhistory.md)<br/>       | Read-only<br/>  | The recent number of packets dropped per second by this virtual network (as an array of number of bytes).<br/>    |
| [**PacketsReceived**](ivmvirtualnetwork-packetsreceived.md)<br/>                   | Read-only<br/>  | The current number of packets received per second by this virtual network.<br/>                                   |
| [**PacketsReceivedHistory**](ivmvirtualnetwork-packetsreceivedhistory.md)<br/>     | Read-only<br/>  | The recent number of packets received per second by this virtual network (as an array of number of packets).<br/> |
| [**PacketsSent**](ivmvirtualnetwork-packetssent.md)<br/>                           | Read-only<br/>  | The current number of packets sent per second by this virtual network.<br/>                                       |
| [**PacketsSentHistory**](ivmvirtualnetwork-packetssenthistory.md)<br/>             | Read-only<br/>  | The recent number of packets sent per second by this virtual network (as an array of number of packets).<br/>     |
| [**Security**](ivmvirtualnetwork-security.md)<br/>                                 | Read/write<br/> | The [**IVMSecurity**](ivmsecurity.md) object associated with the virtual network.<br/>                           |



 

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



 

 





