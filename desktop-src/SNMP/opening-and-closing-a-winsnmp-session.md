---
title: Opening and Closing a WinSNMP Session
description: To open a session, an application calls the SnmpCreateSession function.
ms.assetid: 76650231-509b-45be-b156-09752b817854
ms.topic: article
ms.date: 05/31/2018
---

# Opening and Closing a WinSNMP Session

To open a session, an application calls the [**SnmpCreateSession**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpcreatesession) function. If the function completes successfully, the Microsoft WinSNMP implementation opens a session, and the function returns a session identifier in the form of an **HSNMP\_SESSION** handle. All WinSNMP functions that return handle variables include the session identifier as an input parameter. This enables the implementation to use the handle to efficiently manage resources at the session level.

An application can have multiple sessions open at one time. Multiple sessions within an application can share handle variables.

If the implementation cannot open a session because of resource limitations, it returns SNMPAPI\_FAILURE when the application calls [**SnmpCreateSession**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpcreatesession). If the application then calls the [**SnmpGetLastError**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpgetlasterror) function, it returns SNMPAPI\_ALLOC\_ERROR.

A call to the [**SnmpClose**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpclose) function enables the implementation to free any remaining resources and to close the session.

For more information, see [Resource Handle Objects](resource-handle-objects.md) and [WinSNMP Sessions](winsnmp-sessions.md).

 

 




