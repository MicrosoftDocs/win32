---
Description: IP Helper provides features to manage network routing. Use the following functions to manage the IP routing table, and to obtain other routing information.
ms.assetid: 879b90e3-aecc-492e-9b22-9ebbf505a610
title: Managing Routing
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Managing Routing

IP Helper provides features to manage network routing. Use the following functions to manage the IP routing table, and to obtain other routing information.

Retrieve the contents of the IP routing table by making a call to the [**GetIpForwardTable**](/windows/win32/Iphlpapi/nf-iphlpapi-getipforwardtable?branch=master) function. Manipulate specific entries in the IP routing table using the [**CreateIpForwardEntry**](/windows/win32/Iphlpapi/nf-iphlpapi-createipforwardentry?branch=master), [**DeleteIpForwardEntry**](/windows/win32/Iphlpapi/nf-iphlpapi-deleteipforwardentry?branch=master), and [**SetIpForwardEntry**](/windows/win32/Iphlpapi/nf-iphlpapi-setipforwardentry?branch=master) functions. Use the **CreateIpForwardEntry** function to add a new routing table entry. Use the **DeleteIpForwardEntry** function to remove an existing entry. The **SetIpForwardEntry** function modifies an existing entry.

The router management capabilities of IP Helper can be used to retrieve information about how datagrams are routed over the network. The [**GetBestRoute**](/windows/win32/Iphlpapi/nf-iphlpapi-getbestroute?branch=master) function retrieves the best route to a specified destination address. The [**GetBestInterface**](/windows/win32/Iphlpapi/nf-iphlpapi-getbestinterface?branch=master) function retrieves the index of the interface used by the best route to a specified destination address. Lastly, the [**GetRTTAndHopCount**](/windows/win32/Iphlpapi/nf-iphlpapi-getrttandhopcount?branch=master) function retrieves the round-trip time (RTT) and number of hops to a specified destination address.

 

 



