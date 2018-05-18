---
Description: 'The PNRP Namespace Provider API uses the following functions.'
ms.assetid: '7c9f2dd7-8dbc-4bbe-b53c-8036c79faa8a'
title: PNRP Functions
---

# PNRP Functions

The PNRP Namespace Provider API uses the following functions.



| Function                                                             | Description                                                                                                                                                  |
|----------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**PeerNameToPeerHostName**](peernametopeerhostname.md)             | Encodes the supplied peer name as a format that can be used with a subsequent call to the [**getaddrinfo**](https://msdn.microsoft.com/library/windows/desktop/ms738520) Windows Sockets function. |
| [**PeerHostNameToPeerName**](peerhostnametopeername.md)             | Decodes a host name returned by [**PeerNameToPeerHostName**](peernametopeerhostname.md) into the peer name string it represents.                            |
| [**PeerPnrpStartup**](peerpnrpstartup.md)                           | Starts the Peer Name Resolution Protocol (PNRP) service for the calling peer.                                                                                |
| [**PeerPnrpShutdown**](peerpnrpshutdown.md)                         | Shuts down a running instance of the Peer Name Resolution Protocol (PNRP) service and releases all resources associated with it.                             |
| [**PeerPnrpRegister**](peerpnrpregister.md)                         | Registers a peer with a PNRP cloud and returns a handle that can be used for registration updates.                                                           |
| [**PeerPnrpUpdateRegistration**](peerpnrpupdateregistration.md)     | Updates the PNRP registration information for a name.                                                                                                        |
| [**PeerPnrpUnregister**](peerpnrpunregister.md)                     | Deregisters a peer from a PNRP cloud.                                                                                                                        |
| [**PeerPnrpResolve**](peerpnrpresolve.md)                           | Obtains the endpoint address(es) registered for a specific peer name.                                                                                        |
| [**PeerPnrpStartResolve**](peerpnrpstartresolve.md)                 | Starts an asynchronous peer name resolution operation.                                                                                                       |
| [**PeerPnrpGetCloudInfo**](peerpnrpgetcloudinfo.md)                 | Retrieves information on the Peer Name Resolution Protocol (PNRP) clouds in which the calling peer is participating.                                         |
| [**PeerPnrpEndResolve**](peerpnrpendresolve.md)                     | Closes the handle for an asynchronous PNRP resolution operation initiated with a previous call to [**PeerPnrpStartResolve**](peerpnrpstartresolve.md).      |
| [PNRP and WSALookupServiceBegin](pnrp-and-wsalookupservicebegin.md) | Starts the process that allows an application to resolve names and enumerate network clouds.                                                                 |
| [PNRP and WSALookupServiceEnd](pnrp-and-wsalookupserviceend.md)     | Terminates a query initiated in a previous call to [**WSALookupServiceBegin**](winsock-nsp-reference-links.md).                                             |
| [PNRP and WSALookupServiceNext](pnrp-and-wsalookupservicenext.md)   | Matches queries specified in a previous call to [**WSALookupServiceBegin**](winsock-nsp-reference-links.md).                                                |
| [PNRP and WSANSPIoctl](pnrp-and-wsanspioctl.md)                     | Receives notifications about changes to the network cloud list and availability of results of a name resolution request.                                     |
| [PNRP and WSASetService](pnrp-and-wsasetservice.md)                 | Registers or removes [peer names](peer-names.md).                                                                                                           |



 

 

 



