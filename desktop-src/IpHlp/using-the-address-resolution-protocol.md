---
Description: 'You can use IP Helper to perform Address Resolution Protocol (ARP) operations for the local computer. Use the following functions to retrieve and modify the ARP table.'
ms.assetid: '2c5dc1f8-590f-4b41-b6bb-f82ab093252f'
title: Using the Address Resolution Protocol
---

# Using the Address Resolution Protocol

You can use IP Helper to perform Address Resolution Protocol (ARP) operations for the local computer. Use the following functions to retrieve and modify the ARP table.

The [**GetIpNetTable**](getipnettable.md) retrieves the ARP table. The ARP table contains the mapping of IP addresses to physical addresses. Physical addresses are sometimes referred to as Media Access Controller (MAC) addresses.

Use the [**CreateIpNetEntry**](createipnetentry.md) and [**DeleteIpNetEntry**](deleteipnetentry.md) functions to add or remove particular ARP entries to or from the table. The [**FlushIpNetTable**](flushipnettable.md) function deletes all entries from the table.

To create or delete proxy ARP entries, use the [**CreateProxyArpEntry**](createproxyarpentry.md) and [**DeleteProxyArpEntry**](deleteproxyarpentry.md) functions.

The [**SendARP**](sendarp.md) function sends an ARP request to the local network.

 

 



