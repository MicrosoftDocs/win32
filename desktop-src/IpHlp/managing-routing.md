---
description: IP Helper provides features to manage network routing. Use the following functions to manage the IP routing table, and to obtain other routing information.
ms.assetid: 879b90e3-aecc-492e-9b22-9ebbf505a610
title: Managing Routing
ms.topic: article
ms.date: 05/31/2018
---

# Managing Routing

IP Helper provides features to manage network routing. Use the following functions to manage the IP routing table, and to obtain other routing information.

Retrieve the contents of the IP routing table by making a call to the [**GetIpForwardTable**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-getipforwardtable) function. Manipulate specific entries in the IP routing table using the [**CreateIpForwardEntry**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-createipforwardentry), [**DeleteIpForwardEntry**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-deleteipforwardentry), and [**SetIpForwardEntry**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-setipforwardentry) functions. Use the **CreateIpForwardEntry** function to add a new routing table entry. Use the **DeleteIpForwardEntry** function to remove an existing entry. The **SetIpForwardEntry** function modifies an existing entry.

The router management capabilities of IP Helper can be used to retrieve information about how datagrams are routed over the network. The [**GetBestRoute**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-getbestroute) function retrieves the best route to a specified destination address. The [**GetBestInterface**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-getbestinterface) function retrieves the index of the interface used by the best route to a specified destination address. Lastly, the [**GetRTTAndHopCount**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-getrttandhopcount) function retrieves the round-trip time (RTT) and number of hops to a specified destination address.

 

 



