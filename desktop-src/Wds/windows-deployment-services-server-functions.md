---
title: Windows Deployment Services Server Functions
description: The following functions are used with Windows Deployment Services PXE Server API.
ms.assetid: b6089ff9-4d74-4f5d-957f-4a741c09f4b9
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Windows Deployment Services Server Functions

The following functions are used with Windows Deployment Services PXE Server API.



| Function                                                           | Description                                                                                                                    |
|--------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| [**PxeAsyncRecvDone**](/windows/win32/WdsPxe/nf-wdspxe-pxeasyncrecvdone?branch=master)                       | Returns asynchronous results of client request.                                                                                |
| [**PxeDhcpAppendOption**](/windows/win32/WdsPxe/nf-wdspxe-pxedhcpappendoption?branch=master)                 | Appends a DHCP option to the reply packet.                                                                                     |
| [**PxeDhcpAppendOptionRaw**](/windows/win32/WdsPxe/nf-wdspxe-pxedhcpappendoptionraw?branch=master)           | Appends a DHCP option to the reply packet.                                                                                     |
| [**PxeDhcpGetOptionValue**](/windows/win32/WdsPxe/nf-wdspxe-pxedhcpgetoptionvalue?branch=master)             | Retrieves an option value from a DHCP packet.                                                                                  |
| [**PxeDhcpGetVendorOptionValue**](/windows/win32/WdsPxe/nf-wdspxe-pxedhcpgetvendoroptionvalue?branch=master) | Retrieves an option value from the Vendor Specific Information field (43) of a DHCP packet.                                    |
| [**PxeDhcpInitialize**](/windows/win32/WdsPxe/nf-wdspxe-pxedhcpinitialize?branch=master)                     | Initializes a response packet as a DHCP reply packet.                                                                          |
| [**PxeDhcpIsValid**](/windows/win32/WdsPxe/nf-wdspxe-pxedhcpisvalid?branch=master)                           | Validates that a packet is a DHCP packet.                                                                                      |
| [**PxeGetServerInfo**](/windows/win32/WdsPxe/nf-wdspxe-pxegetserverinfo?branch=master)                       | Returns information about the PXE server.                                                                                      |
| [**PxePacketAllocate**](/windows/win32/WdsPxe/nf-wdspxe-pxepacketallocate?branch=master)                     | Allocates a packet to be sent with the [**PxeSendReply**](/windows/win32/WdsPxe/nf-wdspxe-pxesendreply?branch=master) function.                                          |
| [**PxePacketFree**](/windows/win32/WdsPxe/nf-wdspxe-pxepacketfree?branch=master)                             | Frees a packet allocated by the [**PxePacketAllocate**](/windows/win32/WdsPxe/nf-wdspxe-pxepacketallocate?branch=master) function.                                       |
| [**PxeProviderEnumClose**](/windows/win32/WdsPxe/nf-wdspxe-pxeproviderenumclose?branch=master)               | Closes the enumeration of providers opened by the [**PxeProviderEnumFirst**](/windows/win32/WdsPxe/nf-wdspxe-pxeproviderenumfirst?branch=master) function.               |
| [**PxeProviderEnumFirst**](/windows/win32/WdsPxe/nf-wdspxe-pxeproviderenumfirst?branch=master)               | Starts an enumeration of registered providers.                                                                                 |
| [**PxeProviderEnumNext**](/windows/win32/WdsPxe/nf-wdspxe-pxeproviderenumnext?branch=master)                 | Enumerates registered providers.                                                                                               |
| [**PxeProviderFreeInfo**](/windows/win32/WdsPxe/nf-wdspxe-pxeproviderfreeinfo?branch=master)                 | Frees memory allocated by the [**PxeProviderEnumNext**](/windows/win32/WdsPxe/nf-wdspxe-pxeproviderenumnext?branch=master) function.                                     |
| [*PxeProviderInitialize*](pxeproviderinitialize.md)               | An export from a provider dynamic-link library (DLL) that initializes the provider and prepares it to receive client requests. |
| [**PxeProviderQueryIndex**](/windows/win32/WdsPxe/nf-wdspxe-pxeproviderqueryindex?branch=master)             | Returns the index of the specified provider in the list of registered providers.                                               |
| [*PxeProviderRecvRequest*](pxeproviderrecvrequest.md)             | Called when a request is received from a client.                                                                               |
| [**PxeProviderRegister**](/windows/win32/WdsPxe/nf-wdspxe-pxeproviderregister?branch=master)                 | Registers a provider with the system.                                                                                          |
| [*PxeProviderServiceControl*](pxeproviderservicecontrol.md)       | Called when a service control code is received by the WDS service.                                                             |
| [**PxeProviderSetAttribute**](/windows/win32/WdsPxe/nf-wdspxe-pxeprovidersetattribute?branch=master)         | Specifies attributes for the provider.                                                                                         |
| [*PxeProviderShutdown*](pxeprovidershutdown.md)                   | Called to shutdown the provider.                                                                                               |
| [**PxeProviderUnRegister**](/windows/win32/WdsPxe/nf-wdspxe-pxeproviderunregister?branch=master)             | Removes a provider from the list of registered providers.                                                                      |
| [**PxeRegisterCallback**](/windows/win32/WdsPxe/nf-wdspxe-pxeregistercallback?branch=master)                 | Registers callback functions for different notification events.                                                                |
| [**PxeSendReply**](/windows/win32/WdsPxe/nf-wdspxe-pxesendreply?branch=master)                               | Sends a packet to a client request.                                                                                            |
| [**PxeTrace**](/windows/win32/WdsPxe/nf-wdspxe-pxetrace?branch=master)                                       | Adds a trace entry to the PXE log.                                                                                             |



 

The following is available beginning with Windows 8 and Windows Server 2012.

| Function                                                               | Description                                                                                   |
|------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| [**PxeDhcpv6AppendOption**](/windows/win32/WdsPxe/nf-wdspxe-pxedhcpv6appendoption?branch=master)                 | Appends a DHCPv6 option to the reply packet.                                                  |
| [**PxeDhcpv6AppendOptionRaw**](/windows/win32/WdsPxe/nf-wdspxe-pxedhcpv6appendoptionraw?branch=master)           | Appends a DHCPv6 option to the reply packet.                                                  |
| [**PxeDhcpv6GetOptionValue**](/windows/win32/WdsPxe/nf-wdspxe-pxedhcpv6getoptionvalue?branch=master)             | Retrieves an option value from a DHCPv6 packet.                                               |
| [**PxeDhcpv6GetVendorOptionValue**](/windows/win32/WdsPxe/nf-wdspxe-pxedhcpv6getvendoroptionvalue?branch=master) | Retrieves option values from the OPTION\_VENDOR\_OPTS (17) field of a DHCPv6 packet.          |
| [**PxeDhcpv6Initialize**](/windows/win32/WdsPxe/nf-wdspxe-pxedhcpv6initialize?branch=master)                     | Initializes a response packet as a DHCPv6 reply packet.                                       |
| [**PxeDhcpv6IsValid**](/windows/win32/WdsPxe/nf-wdspxe-pxedhcpv6isvalid?branch=master)                           | Validates that a packet is a valid DHCPv6 packet.                                             |
| [**PxeGetServerInfoEx**](/windows/win32/WdsPxe/nf-wdspxe-pxegetserverinfoex?branch=master)                       | Returns information about the PXE server.                                                     |
| [**PxeDhcpv6ParseRelayForw**](/windows/win32/WdsPxe/nf-wdspxe-pxedhcpv6parserelayforw?branch=master)             | Enables a provider to parse RELAY-FORW messages and their nested OPTION\_RELAY\_MSG messages. |
| [**PxeDhcpv6CreateRelayRepl**](/windows/win32/WdsPxe/nf-wdspxe-pxedhcpv6createrelayrepl?branch=master)           | Generates a RELAY-REPL message.                                                               |



 

 

 




