---
title: IVMDHCPVirtualNetworkServer interface
description: The IVMDHCPVirtualNetworkServer interface defines the DHCP virtual network server.
ms.assetid: 773f3aae-8c1a-40fa-9d5b-9d129e48b7ed
keywords:
- IVMDHCPVirtualNetworkServer interface Virtual Server
- IVMDHCPVirtualNetworkServer interface Virtual Server , described
topic_type:
- apiref
api_name:
- IVMDHCPVirtualNetworkServer
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

# IVMDHCPVirtualNetworkServer interface

The **IVMDHCPVirtualNetworkServer** interface defines the DHCP virtual network server.

## When to use

This interface configures the virtual DHCP attached to a virtual network. It is used to provide DHCP services to a guest operating system. You can retrieve the **IVMDHCPVirtualNetworkServer** interface from the [**IVMVirtualNetwork::DHCPVirtualNetworkServer**](ivmvirtualnetwork-dhcpvirtualnetworkserver.md) property.

## Members

The **IVMDHCPVirtualNetworkServer** interface inherits from the [**IDispatch**](https://msdn.microsoft.com/windows/desktop/ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IVMDHCPVirtualNetworkServer** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IVMDHCPVirtualNetworkServer** interface has these methods.



| Method                                                                                 | Description                                                                              |
|:---------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------|
| [**ConfigureDHCPLeaseTimes**](ivmdhcpvirtualnetworkserver-configuredhcpleasetimes.md) | Sets the lease time parameters for leases managed by the virtual DHCP server.<br/> |
| [**ConfigureDHCPServer**](ivmdhcpvirtualnetworkserver-configuredhcpserver.md)         | Sets the parameters for the virtual network DHCP server.<br/>                      |



 

### Properties

The **IVMDHCPVirtualNetworkServer** interface has these properties.



| Property                                                                                      | Access type           | Description                                                                                                                                                                  |
|:----------------------------------------------------------------------------------------------|:----------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DefaultGatewayAddress**](ivmdhcpvirtualnetworkserver-defaultgatewayaddress.md)<br/> | Read/write<br/> | The TCP/IP address of the default gateway.<br/>                                                                                                                        |
| [**DNSServers**](ivmdhcpvirtualnetworkserver-dnsservers.md)<br/>                       | Read/write<br/> | A comma-separated list of the TCP/IP address representing DNS servers.<br/>                                                                                            |
| [**EndingIPAddress**](ivmdhcpvirtualnetworkserver-endingipaddress.md)<br/>             | Read-only<br/>  | The last TCP/IP address that the DHCP server can dynamically assign to a client on the Virtual Network.<br/>                                                           |
| [**IsEnabled**](ivmdhcpvirtualnetworkserver-isenabled.md)<br/>                         | Read/write<br/> | Indicates whether the DHCP virtual network server is enabled.<br/>                                                                                                     |
| [**LeaseRebindingTime**](ivmdhcpvirtualnetworkserver-leaserebindingtime.md)<br/>       | Read-only<br/>  | The time in seconds after which the client virtual machine should rebind if the virtual DHCP server has not responded.<br/>                                            |
| [**LeaseRenewalTime**](ivmdhcpvirtualnetworkserver-leaserenewaltime.md)<br/>           | Read-only<br/>  | The time in seconds after which the client virtual machine should renew its TCP/IP address lease.<br/>                                                                 |
| [**LeaseTime**](ivmdhcpvirtualnetworkserver-leasetime.md)<br/>                         | Read-only<br/>  | The time in seconds after which leases granted by the virtual DHCP server expire.<br/>                                                                                 |
| [**Network**](ivmdhcpvirtualnetworkserver-network.md)<br/>                             | Read-only<br/>  | The base TCP/IP address of the range.<br/>                                                                                                                             |
| [**NetworkMask**](ivmdhcpvirtualnetworkserver-networkmask.md)<br/>                     | Read-only<br/>  | The mask used to calculate the base TCP/IP address for the given network.<br/>                                                                                         |
| [**ServerIPAddress**](ivmdhcpvirtualnetworkserver-serveripaddress.md)<br/>             | Read-only<br/>  | The TCP/IP address of the DHCP server.<br/>                                                                                                                            |
| [**StartingIPAddress**](ivmdhcpvirtualnetworkserver-startingipaddress.md)<br/>         | Read-only<br/>  | The first TCP/IP address that the server can dynamically assign to a client on the Virtual Network.<br/>                                                               |
| [**WINSServers**](ivmdhcpvirtualnetworkserver-winsservers.md)<br/>                     | Read/write<br/> | A comma-separated list of the TCP/IP address representing WINS servers. The list of WINS servers is returned to the DHCP client as part of the server's response.<br/> |



 

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IDispatch**](https://msdn.microsoft.com/windows/desktop/ebbff4bc-36b2-4861-9efa-ffa45e013eb5)
</dt> </dl>

 

 





