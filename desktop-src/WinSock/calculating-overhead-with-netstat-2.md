---
description: Calculating Overhead with Netstat
ms.assetid: d96a8fba-8d76-443f-be49-81a8ad7050fa
title: Calculating Overhead with Netstat
ms.topic: article
ms.date: 05/31/2018
---

# Calculating Overhead with Netstat

Calculating overhead with Netstat should be performed on a quiet network to avoid other network traffic from skewing the data, such as broadcast or multicast traffic.

**To calculate an application's network overhead using Netstat**

1.  Retrieve the current interface statistics using Netstat.
2.  Execute the application.
3.  Get the interface statistics, again using Netstat.
4.  Calculate the number of bytes received between the two Netstat measurements.

## Example

The following example demonstrates these steps, using TTCP to send 10 bytes of data, one byte at a time.

First, a theoretical overhead for the application is calculated. For this test, all packets are 60 bytes (the Ethernet minimum). This transfer requires three packets to set up the connection, 10 data packets, 10 acknowledgment packets (delayed ACK is triggered nearly every time), and four packets to close the connection gracefully.

This equates to 27 packets of 60 bytes each, or 1620 bytes (3+4+10+10)\*60=1620). Since only 10 bytes of data are transferred, the overhead is 1610 bytes, which is over 99% protocol overhead.

### Commands

**netstat -e**

``` syntax
Interface Statistics
                     Received     Sent
Bytes                392291400    444684566
Unicast packets      487627       570086
Non-unicast packets  1159163      11300
Discards             0            0
Errors               0            0
Unknown protocols    52812
```

**ttcp -t -h0 -D -l1 -n10 -p9 172.31.71.99**

``` syntax
ttcp-t: 10 bytes in 2168 real milliseconds = 0 KB/sec
ttcp-t: 10 I/O calls, msec/call = 216, calls/sec = 4, bytes/call = 1
```

**netstat -e**

``` syntax
Interface Statistics
                      Received     Sent
Bytes                 39229207     444685382
Unicast packets       487641       570100
Non-unicast packets   1159164      11301
Discards              0            0
Errors                0            0
Unknown protocols     52812
```

### Calculations

**Sent:** 816 bytes

**Received:** 674 bytes

**Total bytes:** 1490

**User bytes:** 10

**Overhead:** 1480/1490 = 99.3%

**Goodput:  **= 5 bytes/second (or 40 bits/s)

> [!Note]  
> Actual bytes transferred do not match the theoretical values due to padding bytes not being accounted for in the Netstat values.

 

## Related topics

<dl> <dt>

[Application Behavior](application-behavior-2.md)
</dt> <dt>

[High-performance Windows Sockets Applications](high-performance-windows-sockets-applications-2.md)
</dt> </dl>

 

 



