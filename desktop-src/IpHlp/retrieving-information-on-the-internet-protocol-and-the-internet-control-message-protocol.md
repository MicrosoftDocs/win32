---
Description: IP Helper provides information retrieval capabilities that are useful for the network administration of the local computer.
ms.assetid: b50b3927-6c74-4282-b79b-c86d72d93ae3
title: Retrieving Information on the Internet Protocol and the Internet Control Message Protocol
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Retrieving Information on the Internet Protocol and the Internet Control Message Protocol

IP Helper provides information retrieval capabilities that are useful for the network administration of the local computer. The following functions retrieve statistics for the Internet Protocol (IP) and the Internet Control Message Protocol (ICMP). You can also use these functions to set certain configuration parameters for IP.

The [**GetIpStatistics**](/windows/win32/Iphlpapi/nf-iphlpapi-getipstatistics?branch=master) function retrieves the current IP statistics for the local computer. For code samples involving **GetIpStatistics** see [Retrieving Information Using GetIpStatistics](retrieving-information-using-getipstatistics.md).

The [**GetIcmpStatistics**](/windows/win32/Iphlpapi/nf-iphlpapi-geticmpstatistics?branch=master) function retrieves the current ICMP statistics.

Use the [**SetIpStatistics**](/windows/win32/Iphlpapi/nf-iphlpapi-setipstatistics?branch=master) function to enable or disable IP forwarding. This function also makes it possible for you to set the default time-to-live (TTL) for IP datagrams. Alternatively, you can set the TTL by using the [**SetIpTTL**](/windows/win32/Iphlpapi/nf-iphlpapi-setipttl?branch=master) function.

 

 



