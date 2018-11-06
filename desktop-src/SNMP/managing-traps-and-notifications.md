---
title: Managing Traps and Notifications
description: The WinSNMP application must register to receive traps and notifications by calling the SnmpRegister function with SNMPAPI\_ON. The application can unregister and disable traps and notifications by calling the function with SNMPAPI\_OFF.
ms.assetid: 2bccba35-bf5c-4e5c-94e4-59980f2b9776
ms.topic: article
ms.date: 05/31/2018
---

# Managing Traps and Notifications

The WinSNMP application must register to receive traps and notifications by calling the [**SnmpRegister**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpregister) function with SNMPAPI\_ON. The application can unregister and disable traps and notifications by calling the function with SNMPAPI\_OFF.

Several options are available when the application calls **SnmpRegister**. The application can register or unregister for the following traps and notifications:

-   One type of trap or notification
-   All traps and notifications
-   All sources of trap and notification requests
-   Traps and notifications from all management entities
-   Traps and notifications for every context

To register and receive a predefined trap or notification type, the application must define an object identifier (an [**smiOID**](/windows/desktop/api/Winsnmp/ns-winsnmp-smioid) structure) for each predefined type. The structure must contain a pattern-matching sequence for the type of trap or notification. RFC 1907, "Management Information Base for Version 2 of the Simple Network Management Protocol (SNMPv2)," defines trap and notification object identifiers.

To retrieve outstanding trap data and notifications for a WinSNMP session, a WinSNMP application must call the [**SnmpRecvMsg**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmprecvmsg) function with the session handle returned by the [**SnmpCreateSession**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpcreatesession) function.

For more information, see [Sending SNMP Messages](sending-snmp-messages.md) and [Receiving SNMP Messages](receiving-snmp-messages.md). For additional information about allocation and deallocation of resources for traps and notifications, see [Allocating WinSNMP Memory Objects](allocating-winsnmp-memory-objects.md).

 

 




