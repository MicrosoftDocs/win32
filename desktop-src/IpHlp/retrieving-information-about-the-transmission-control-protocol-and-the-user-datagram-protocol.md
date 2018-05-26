---
Description: IP Helper makes it possible to access information about network protocols that are used on the local computer.
ms.assetid: 3ae07fbd-0b69-42d6-81ab-cc239c354bbb
title: Retrieving Information About the Transmission Control Protocol and the User Datagram Protocol
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Retrieving Information About the Transmission Control Protocol and the User Datagram Protocol

IP Helper makes it possible to access information about network protocols that are used on the local computer. Use the functions described in the following paragraphs to retrieve information about the Transmission Control Protocol (TCP) and User Datagram Protocol (UDP) on the local computer.

The [**GetTcpStatistics**](/windows/win32/Iphlpapi/nf-iphlpapi-gettcpstatistics?branch=master) function retrieves the current statistics for TCP. For code samples involving **GetTcpStatistics** see [Retrieving Information Using GetTcpStatistics](retrieving-information-using-gettcpstatistics.md).

The [**GetUdpStatistics**](/windows/win32/Iphlpapi/nf-iphlpapi-getudpstatistics?branch=master) function retrieves the current statistics for UDP.

The [**GetTcpTable**](/windows/win32/Iphlpapi/nf-iphlpapi-gettcptable?branch=master) function retrieves the TCP connection table. The [**GetUdpTable**](/windows/win32/Iphlpapi/nf-iphlpapi-getudptable?branch=master) retrieves the UDP listener table.

The [**SetTcpEntry**](/windows/win32/Iphlpapi/nf-iphlpapi-settcpentry?branch=master) function enables a developer to set the state of a specified TCP connection to MIB\_TCP\_STATE\_DELETE\_TCB.

 

 



