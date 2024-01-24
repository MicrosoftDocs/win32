---
description: IP Helper provides information retrieval capabilities that are useful for the network administration of the local computer.
ms.assetid: b50b3927-6c74-4282-b79b-c86d72d93ae3
title: Retrieving Information on the Internet Protocol and the Internet Control Message Protocol
ms.topic: article
ms.date: 05/31/2018
---

# Retrieving Information on the Internet Protocol and the Internet Control Message Protocol

IP Helper provides information retrieval capabilities that are useful for the network administration of the local computer. The following functions retrieve statistics for the Internet Protocol (IP) and the Internet Control Message Protocol (ICMP). You can also use these functions to set certain configuration parameters for IP.

The [**GetIpStatistics**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-getipstatistics) function retrieves the current IP statistics for the local computer. For code samples involving **GetIpStatistics** see [Retrieving Information Using GetIpStatistics](retrieving-information-using-getipstatistics.md).

The [**GetIcmpStatistics**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-geticmpstatistics) function retrieves the current ICMP statistics.

Use the [**SetIpStatistics**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-setipstatistics) function to enable or disable IP forwarding. This function also makes it possible for you to set the default time-to-live (TTL) for IP datagrams. Alternatively, you can set the TTL by using the [**SetIpTTL**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-setipttl) function.

 

 



