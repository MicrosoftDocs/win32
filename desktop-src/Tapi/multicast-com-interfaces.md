---
description: The multicast COM interfaces allow access to the networks facility for allocating, renewing, and releasing leases on multicast addresses.
ms.assetid: d4da9616-bdb4-4919-96aa-9e45582b05dd
title: Multicast COM Interfaces
ms.topic: article
ms.date: 05/31/2018
---

# Multicast COM Interfaces

\[ Rendezvous IP Telephony Conferencing controls and interfaces are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The multicast COM interfaces allow access to the network's facility for allocating, renewing, and releasing leases on multicast addresses. They encapsulate a set of function and data structure definitions. The COM interfaces free the programmer from the burden of understanding and manipulating these data structures. Moreover, because TAPI 3 itself is COM-based, these interfaces make multicast address allocation accessible in a way that is consistent with the other facilities provided by TAPI 3. Applications written using Visual Basic, Java, or scripting languages that cannot normally access the Windows API directly are able to use these interfaces.

Multicast address allocation is currently the subject of an IETF working group. To access current information, query on "MDHCP" or "MADCAP" and "Internet draft" using any Internet search engine. In addition to MADCAP, the proposed architecture includes a protocol for server-to-server coordination within a domain or AS, as well as a protocol for interdomain coordination. While this architecture is currently evolving, the client need not concern itself with the details of this scheme.

This component currently supports only IP version 4 addresses.

> [!Note]  
> The protocol used for these interfaces is currently named MADCAP. In previous versions it was known as MDHCP.

 

The multicast object is created by calling **CoCreateInstance** on the [**IMcastAddressAllocation**](/windows/desktop/api/Mdhcp/nn-mdhcp-imcastaddressallocation) interface. The **IMcastAddressAllocation** interface exposes the [**EnumerateScopes**](/windows/desktop/api/Mdhcp/nf-mdhcp-imcastaddressallocation-enumeratescopes) method, which allows an application to get a list of all available multicast scopes.

Once a working scope has been obtained, the [**RequestAddress**](/windows/desktop/api/Mdhcp/nf-mdhcp-imcastaddressallocation-requestaddress) method is used to request a multicast address from the server. If the request is successful, an [**IMcastLeaseInfo**](/windows/desktop/api/Mdhcp/nn-mdhcp-imcastleaseinfo) pointer is returned. The [**EnumerateAddresses**](/windows/desktop/api/Mdhcp/nf-mdhcp-imcastleaseinfo-enumerateaddresses) method exposed by this interface can then be used to obtain the addresses.

Each Media object associated with the conference exposes an [**ITConnection**](itconnection.md) interface. The [**ITConnection::SetAddressInfo**](itconnection-setaddressinfo.md) method allows assignment of the multicast addresses obtained to the media of the conference. The address must be set for each **ITConnection** interface of every Media object associated with the conference.

 

 



