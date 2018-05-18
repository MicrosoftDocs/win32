---
title: Windows Deployment Services Server Functions
description: The following functions are used with Windows Deployment Services PXE Server API.
ms.assetid: 'b6089ff9-4d74-4f5d-957f-4a741c09f4b9'
---

# Windows Deployment Services Server Functions

The following functions are used with Windows Deployment Services PXE Server API.



| Function                                                           | Description                                                                                                                    |
|--------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| [**PxeAsyncRecvDone**](pxeasyncrecvdone.md)                       | Returns asynchronous results of client request.                                                                                |
| [**PxeDhcpAppendOption**](pxedhcpappendoption.md)                 | Appends a DHCP option to the reply packet.                                                                                     |
| [**PxeDhcpAppendOptionRaw**](pxedhcpappendoptionraw.md)           | Appends a DHCP option to the reply packet.                                                                                     |
| [**PxeDhcpGetOptionValue**](pxedhcpgetoptionvalue.md)             | Retrieves an option value from a DHCP packet.                                                                                  |
| [**PxeDhcpGetVendorOptionValue**](pxedhcpgetvendoroptionvalue.md) | Retrieves an option value from the Vendor Specific Information field (43) of a DHCP packet.                                    |
| [**PxeDhcpInitialize**](pxedhcpinitialize.md)                     | Initializes a response packet as a DHCP reply packet.                                                                          |
| [**PxeDhcpIsValid**](pxedhcpisvalid.md)                           | Validates that a packet is a DHCP packet.                                                                                      |
| [**PxeGetServerInfo**](pxegetserverinfo.md)                       | Returns information about the PXE server.                                                                                      |
| [**PxePacketAllocate**](pxepacketallocate.md)                     | Allocates a packet to be sent with the [**PxeSendReply**](pxesendreply.md) function.                                          |
| [**PxePacketFree**](pxepacketfree.md)                             | Frees a packet allocated by the [**PxePacketAllocate**](pxepacketallocate.md) function.                                       |
| [**PxeProviderEnumClose**](pxeproviderenumclose.md)               | Closes the enumeration of providers opened by the [**PxeProviderEnumFirst**](pxeproviderenumfirst.md) function.               |
| [**PxeProviderEnumFirst**](pxeproviderenumfirst.md)               | Starts an enumeration of registered providers.                                                                                 |
| [**PxeProviderEnumNext**](pxeproviderenumnext.md)                 | Enumerates registered providers.                                                                                               |
| [**PxeProviderFreeInfo**](pxeproviderfreeinfo.md)                 | Frees memory allocated by the [**PxeProviderEnumNext**](pxeproviderenumnext.md) function.                                     |
| [*PxeProviderInitialize*](pxeproviderinitialize.md)               | An export from a provider dynamic-link library (DLL) that initializes the provider and prepares it to receive client requests. |
| [**PxeProviderQueryIndex**](pxeproviderqueryindex.md)             | Returns the index of the specified provider in the list of registered providers.                                               |
| [*PxeProviderRecvRequest*](pxeproviderrecvrequest.md)             | Called when a request is received from a client.                                                                               |
| [**PxeProviderRegister**](pxeproviderregister.md)                 | Registers a provider with the system.                                                                                          |
| [*PxeProviderServiceControl*](pxeproviderservicecontrol.md)       | Called when a service control code is received by the WDS service.                                                             |
| [**PxeProviderSetAttribute**](pxeprovidersetattribute.md)         | Specifies attributes for the provider.                                                                                         |
| [*PxeProviderShutdown*](pxeprovidershutdown.md)                   | Called to shutdown the provider.                                                                                               |
| [**PxeProviderUnRegister**](pxeproviderunregister.md)             | Removes a provider from the list of registered providers.                                                                      |
| [**PxeRegisterCallback**](pxeregistercallback.md)                 | Registers callback functions for different notification events.                                                                |
| [**PxeSendReply**](pxesendreply.md)                               | Sends a packet to a client request.                                                                                            |
| [**PxeTrace**](pxetrace.md)                                       | Adds a trace entry to the PXE log.                                                                                             |



 

The following is available beginning with Windows 8 and Windows Server 2012.

| Function                                                               | Description                                                                                   |
|------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| [**PxeDhcpv6AppendOption**](pxedhcpv6appendoption.md)                 | Appends a DHCPv6 option to the reply packet.                                                  |
| [**PxeDhcpv6AppendOptionRaw**](pxedhcpv6appendoptionraw.md)           | Appends a DHCPv6 option to the reply packet.                                                  |
| [**PxeDhcpv6GetOptionValue**](pxedhcpv6getoptionvalue.md)             | Retrieves an option value from a DHCPv6 packet.                                               |
| [**PxeDhcpv6GetVendorOptionValue**](pxedhcpv6getvendoroptionvalue.md) | Retrieves option values from the OPTION\_VENDOR\_OPTS (17) field of a DHCPv6 packet.          |
| [**PxeDhcpv6Initialize**](pxedhcpv6initialize.md)                     | Initializes a response packet as a DHCPv6 reply packet.                                       |
| [**PxeDhcpv6IsValid**](pxedhcpv6isvalid.md)                           | Validates that a packet is a valid DHCPv6 packet.                                             |
| [**PxeGetServerInfoEx**](pxegetserverinfoex.md)                       | Returns information about the PXE server.                                                     |
| [**PxeDhcpv6ParseRelayForw**](pxedhcpv6parserelayforw.md)             | Enables a provider to parse RELAY-FORW messages and their nested OPTION\_RELAY\_MSG messages. |
| [**PxeDhcpv6CreateRelayRepl**](pxedhcpv6createrelayrepl.md)           | Generates a RELAY-REPL message.                                                               |



 

 

 




