---
title: Network Transport Errors
description: The Microsoft WinSNMP implementation can detect a network transport error after it transmits an SNMP message.
ms.assetid: 2ff535b1-76cb-42aa-baeb-14c1a1bc41ce
ms.topic: article
ms.date: 05/31/2018
---

# Network Transport Errors

\[SNMP is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Instead, use [Windows Remote Management](/windows/desktop/WinRM/portal), which is the Microsoft implementation of WS-Man.\]

The Microsoft WinSNMP implementation can detect a network transport error after it transmits an SNMP message. When this occurs, the implementation sends a data receipt notification to the WinSNMP session that initiated the communication request. The implementation also returns SNMPAPI\_FAILURE on the next call to the [**SnmpRecvMsg**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmprecvmsg) function for the session. The **SnmpRecvMsg** function fails with an extended error code that indicates a network transport layer error.

For a list of specific transport layer errors, see the reference pages for the [**SnmpRegister**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpregister), [**SnmpSendMsg**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpsendmsg), and [**SnmpRecvMsg**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmprecvmsg) functions.

 

 