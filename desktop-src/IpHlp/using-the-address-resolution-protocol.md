---
Description: You can use IP Helper to perform Address Resolution Protocol (ARP) operations for the local computer. Use the following functions to retrieve and modify the ARP table.
ms.assetid: 2c5dc1f8-590f-4b41-b6bb-f82ab093252f
title: Using the Address Resolution Protocol
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using the Address Resolution Protocol

You can use IP Helper to perform Address Resolution Protocol (ARP) operations for the local computer. Use the following functions to retrieve and modify the ARP table.

The [**GetIpNetTable**](/windows/win32/Iphlpapi/nf-iphlpapi-getipnettable?branch=master) retrieves the ARP table. The ARP table contains the mapping of IP addresses to physical addresses. Physical addresses are sometimes referred to as Media Access Controller (MAC) addresses.

Use the [**CreateIpNetEntry**](/windows/win32/Iphlpapi/nf-iphlpapi-createipnetentry?branch=master) and [**DeleteIpNetEntry**](/windows/win32/Iphlpapi/nf-iphlpapi-deleteipnetentry?branch=master) functions to add or remove particular ARP entries to or from the table. The [**FlushIpNetTable**](/windows/win32/Iphlpapi/nf-iphlpapi-flushipnettable?branch=master) function deletes all entries from the table.

To create or delete proxy ARP entries, use the [**CreateProxyArpEntry**](/windows/win32/Iphlpapi/nf-iphlpapi-createproxyarpentry?branch=master) and [**DeleteProxyArpEntry**](/windows/win32/Iphlpapi/nf-iphlpapi-deleteproxyarpentry?branch=master) functions.

The [**SendARP**](/windows/win32/Iphlpapi/nf-iphlpapi-sendarp?branch=master) function sends an ARP request to the local network.

 

 



