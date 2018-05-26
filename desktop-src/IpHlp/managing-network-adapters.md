---
Description: IP Helper provides capabilities for managing network adapters. There is a one-to-one correspondence between the interfaces and adapters on a given computer. An interface is an IP-level abstraction, whereas an adapter is a datalink-level abstraction.
ms.assetid: fbb32941-2add-4f74-90c4-1dc1bfebd64c
title: Managing Network Adapters
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Managing Network Adapters

IP Helper provides capabilities for managing network adapters. There is a one-to-one correspondence between the interfaces and adapters on a given computer. An interface is an IP-level abstraction, whereas an adapter is a datalink-level abstraction.

Use the functions described in the following paragraphs to retrieve information about the network adapters in the local computer.

The [**GetAdaptersInfo**](/windows/win32/Iphlpapi/nf-iphlpapi-getadaptersinfo?branch=master) function returns an array of [**IP\_ADAPTER\_INFO**](/windows/win32/Iptypes/ns-iptypes-_ip_adapter_info?branch=master) structures, one for each adapter in the local computer. The [**GetPerAdapterInfo**](/windows/win32/Iphlpapi/nf-iphlpapi-getperadapterinfo?branch=master) function returns additional information about a specific adapter. The **GetPerAdapterInfo** function requires the caller to specify the index of the adapter. To obtain the adapter index from the adapter name, use the [**GetAdapterIndex**](/windows/win32/Iphlpapi/nf-iphlpapi-getadapterindex?branch=master) function.

Some applications use adapters that receive datagrams, but cannot transmit them. To obtain information about these adapters, use the [**GetUniDirectionalAdapterInfo**](/windows/win32/Iphlpapi/nf-iphlpapi-getunidirectionaladapterinfo?branch=master) function.

The [**GetAdaptersAddresses**](/windows/win32/Iphlpapi/nf-iphlpapi-getadaptersaddresses?branch=master) function enables you to retrieve the IP addresses associated with a particular adapter. This function supports both IPv4 and IPv6 addressing.

-   For code samples involving [**GetAdaptersInfo**](/windows/win32/Iphlpapi/nf-iphlpapi-getadaptersinfo?branch=master) see [Managing Network Adapters Using GetAdaptersInfo](managing-network-adapters-using-getadaptersinfo.md).

 

 



