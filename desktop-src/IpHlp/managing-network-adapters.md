---
Description: 'IP Helper provides capabilities for managing network adapters. There is a one-to-one correspondence between the interfaces and adapters on a given computer. An interface is an IP-level abstraction, whereas an adapter is a datalink-level abstraction.'
ms.assetid: 'fbb32941-2add-4f74-90c4-1dc1bfebd64c'
title: Managing Network Adapters
---

# Managing Network Adapters

IP Helper provides capabilities for managing network adapters. There is a one-to-one correspondence between the interfaces and adapters on a given computer. An interface is an IP-level abstraction, whereas an adapter is a datalink-level abstraction.

Use the functions described in the following paragraphs to retrieve information about the network adapters in the local computer.

The [**GetAdaptersInfo**](getadaptersinfo.md) function returns an array of [**IP\_ADAPTER\_INFO**](ip-adapter-info.md) structures, one for each adapter in the local computer. The [**GetPerAdapterInfo**](getperadapterinfo.md) function returns additional information about a specific adapter. The **GetPerAdapterInfo** function requires the caller to specify the index of the adapter. To obtain the adapter index from the adapter name, use the [**GetAdapterIndex**](getadapterindex.md) function.

Some applications use adapters that receive datagrams, but cannot transmit them. To obtain information about these adapters, use the [**GetUniDirectionalAdapterInfo**](getunidirectionaladapterinfo.md) function.

The [**GetAdaptersAddresses**](getadaptersaddresses.md) function enables you to retrieve the IP addresses associated with a particular adapter. This function supports both IPv4 and IPv6 addressing.

-   For code samples involving [**GetAdaptersInfo**](getadaptersinfo.md) see [Managing Network Adapters Using GetAdaptersInfo](managing-network-adapters-using-getadaptersinfo.md).

 

 



