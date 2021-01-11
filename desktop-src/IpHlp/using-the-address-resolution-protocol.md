---
description: You can use IP Helper to perform Address Resolution Protocol (ARP) operations for the local computer. Use the following functions to retrieve and modify the ARP table.
ms.assetid: 2c5dc1f8-590f-4b41-b6bb-f82ab093252f
title: Using the Address Resolution Protocol
ms.topic: article
ms.date: 05/31/2018
---

# Using the Address Resolution Protocol

You can use IP Helper to perform Address Resolution Protocol (ARP) operations for the local computer. Use the following functions to retrieve and modify the ARP table.

The [**GetIpNetTable**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-getipnettable) retrieves the ARP table. The ARP table contains the mapping of IP addresses to physical addresses. Physical addresses are sometimes referred to as Media Access Controller (MAC) addresses.

Use the [**CreateIpNetEntry**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-createipnetentry) and [**DeleteIpNetEntry**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-deleteipnetentry) functions to add or remove particular ARP entries to or from the table. The [**FlushIpNetTable**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-flushipnettable) function deletes all entries from the table.

To create or delete proxy ARP entries, use the [**CreateProxyArpEntry**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-createproxyarpentry) and [**DeleteProxyArpEntry**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-deleteproxyarpentry) functions.

The [**SendARP**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-sendarp) function sends an ARP request to the local network.

 

 



