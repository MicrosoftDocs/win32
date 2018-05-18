---
Description: 'IP Helper provides features to manage network routing. Use the following functions to manage the IP routing table, and to obtain other routing information.'
ms.assetid: '879b90e3-aecc-492e-9b22-9ebbf505a610'
title: Managing Routing
---

# Managing Routing

IP Helper provides features to manage network routing. Use the following functions to manage the IP routing table, and to obtain other routing information.

Retrieve the contents of the IP routing table by making a call to the [**GetIpForwardTable**](getipforwardtable.md) function. Manipulate specific entries in the IP routing table using the [**CreateIpForwardEntry**](createipforwardentry.md), [**DeleteIpForwardEntry**](deleteipforwardentry.md), and [**SetIpForwardEntry**](setipforwardentry.md) functions. Use the **CreateIpForwardEntry** function to add a new routing table entry. Use the **DeleteIpForwardEntry** function to remove an existing entry. The **SetIpForwardEntry** function modifies an existing entry.

The router management capabilities of IP Helper can be used to retrieve information about how datagrams are routed over the network. The [**GetBestRoute**](getbestroute.md) function retrieves the best route to a specified destination address. The [**GetBestInterface**](getbestinterface.md) function retrieves the index of the interface used by the best route to a specified destination address. Lastly, the [**GetRTTAndHopCount**](getrttandhopcount.md) function retrieves the round-trip time (RTT) and number of hops to a specified destination address.

 

 



