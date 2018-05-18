---
Description: 'IP Helper provides information retrieval capabilities that are useful for the network administration of the local computer.'
ms.assetid: 'b50b3927-6c74-4282-b79b-c86d72d93ae3'
title: Retrieving Information on the Internet Protocol and the Internet Control Message Protocol
---

# Retrieving Information on the Internet Protocol and the Internet Control Message Protocol

IP Helper provides information retrieval capabilities that are useful for the network administration of the local computer. The following functions retrieve statistics for the Internet Protocol (IP) and the Internet Control Message Protocol (ICMP). You can also use these functions to set certain configuration parameters for IP.

The [**GetIpStatistics**](getipstatistics.md) function retrieves the current IP statistics for the local computer. For code samples involving **GetIpStatistics** see [Retrieving Information Using GetIpStatistics](retrieving-information-using-getipstatistics.md).

The [**GetIcmpStatistics**](geticmpstatistics.md) function retrieves the current ICMP statistics.

Use the [**SetIpStatistics**](setipstatistics.md) function to enable or disable IP forwarding. This function also makes it possible for you to set the default time-to-live (TTL) for IP datagrams. Alternatively, you can set the TTL by using the [**SetIpTTL**](setipttl.md) function.

 

 



