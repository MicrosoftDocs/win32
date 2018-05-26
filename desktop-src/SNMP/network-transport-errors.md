---
title: Network Transport Errors
description: The Microsoft WinSNMP implementation can detect a network transport error after it transmits an SNMP message.
ms.assetid: 2ff535b1-76cb-42aa-baeb-14c1a1bc41ce
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Network Transport Errors

\[SNMP is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Instead, use [Windows Remote Management](https://msdn.microsoft.com/library/aa384426), which is the Microsoft implementation of WS-Man.\]

The Microsoft WinSNMP implementation can detect a network transport error after it transmits an SNMP message. When this occurs, the implementation sends a data receipt notification to the WinSNMP session that initiated the communication request. The implementation also returns SNMPAPI\_FAILURE on the next call to the [**SnmpRecvMsg**](/windows/win32/Winsnmp/nf-winsnmp-snmprecvmsg?branch=master) function for the session. The **SnmpRecvMsg** function fails with an extended error code that indicates a network transport layer error.

For a list of specific transport layer errors, see the reference pages for the [**SnmpRegister**](/windows/win32/Winsnmp/nf-winsnmp-snmpregister?branch=master), [**SnmpSendMsg**](/windows/win32/Winsnmp/nf-winsnmp-snmpsendmsg?branch=master), and [**SnmpRecvMsg**](/windows/win32/Winsnmp/nf-winsnmp-snmprecvmsg?branch=master) functions.

 

 




