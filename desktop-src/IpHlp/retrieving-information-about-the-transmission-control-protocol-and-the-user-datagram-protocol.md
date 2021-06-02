---
description: IP Helper makes it possible to access information about network protocols that are used on the local computer.
ms.assetid: 3ae07fbd-0b69-42d6-81ab-cc239c354bbb
title: Retrieving Information About the Transmission Control Protocol and the User Datagram Protocol
ms.topic: article
ms.date: 05/31/2018
---

# Retrieving Information About the Transmission Control Protocol and the User Datagram Protocol

IP Helper makes it possible to access information about network protocols that are used on the local computer. Use the functions described in the following paragraphs to retrieve information about the Transmission Control Protocol (TCP) and User Datagram Protocol (UDP) on the local computer.

The [**GetTcpStatistics**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-gettcpstatistics) function retrieves the current statistics for TCP. For code samples involving **GetTcpStatistics** see [Retrieving Information Using GetTcpStatistics](retrieving-information-using-gettcpstatistics.md).

The [**GetUdpStatistics**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-getudpstatistics) function retrieves the current statistics for UDP.

The [**GetTcpTable**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-gettcptable) function retrieves the TCP connection table. The [**GetUdpTable**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-getudptable) retrieves the UDP listener table.

The [**SetTcpEntry**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-settcpentry) function enables a developer to set the state of a specified TCP connection to MIB\_TCP\_STATE\_DELETE\_TCB.

 

 



