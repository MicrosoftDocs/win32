---
description: Metrics are used to measure aspects of network and protocol performance.
ms.assetid: ee5faaf6-e230-4084-9829-e8cae8759587
title: Network Terminology (Windows Sockets 2)
ms.topic: article
ms.date: 05/31/2018
---

# Network Terminology (Windows Sockets 2)

Metrics are used to measure aspects of network and protocol performance. The values for such metrics in various scenarios indicate the level of performance of a network application. This section defines terms and metrics used industry-wide for measuring network application performance. These terms are used throughout the rest of this guide.

-   Round Trip Time (RTT)

    Time, in milliseconds, for a request to make a trip from a source computer to a destination computer, and back again. Lower values indicate better performance. Forward and return path times are not necessarily equal.

    RTT values are affected by network infrastructure, distance between nodes, network conditions, and packet size. Packet size, congestion and payload compressibility impact RTT when measured on slow links, such as dial-up connections. Other factors affect RTT, including forward error correction and data compression, which introduce buffers and queues that increase RTT, and therefore decrease performance.

-   Goodput

    Measure of useful application data successfully processed by the receiver, in bits-per-second. Goodput enables the measurement of effective or useful throughput and includes only application data; packet, protocol, and media headers are considered overhead, and are not part of goodput.

-   Protocol Overhead

    Nonapplication bytes, including protocol and media framing, divided by the total number of bytes transmitted. The value is expressed as a percentage. Higher values indicate poorer performance.

    Overhead is calculated for both directions in this guide, but can be calculated for each direction separately.

-   Bandwidth-Delay Product

    Product of the bits-per-second bandwidth of the network, and the RTT (in seconds). This value equates to the number of bits it takes to fill available network bandwidth. When the value for bandwidth-delay product is high, the TCP/IP stack must handle large amounts of unacknowledged data in order to keep the pipeline full. Bandwidth-delay product is a key end-to-end metric for streaming applications.

 

 



