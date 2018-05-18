---
Description: 'IP Helper makes it possible to access information about network protocols that are used on the local computer.'
ms.assetid: '3ae07fbd-0b69-42d6-81ab-cc239c354bbb'
title: Retrieving Information About the Transmission Control Protocol and the User Datagram Protocol
---

# Retrieving Information About the Transmission Control Protocol and the User Datagram Protocol

IP Helper makes it possible to access information about network protocols that are used on the local computer. Use the functions described in the following paragraphs to retrieve information about the Transmission Control Protocol (TCP) and User Datagram Protocol (UDP) on the local computer.

The [**GetTcpStatistics**](gettcpstatistics.md) function retrieves the current statistics for TCP. For code samples involving **GetTcpStatistics** see [Retrieving Information Using GetTcpStatistics](retrieving-information-using-gettcpstatistics.md).

The [**GetUdpStatistics**](getudpstatistics.md) function retrieves the current statistics for UDP.

The [**GetTcpTable**](gettcptable.md) function retrieves the TCP connection table. The [**GetUdpTable**](getudptable.md) retrieves the UDP listener table.

The [**SetTcpEntry**](settcpentry.md) function enables a developer to set the state of a specified TCP connection to MIB\_TCP\_STATE\_DELETE\_TCB.

 

 



