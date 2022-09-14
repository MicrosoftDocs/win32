---
title: Translating Traps from SNMPv1 to SNMPv2C
description: When the Microsoft WinSNMP implementation receives traps from an entity operating under the SNMPv1 framework, it translates the traps to the SNMPv2C format.
ms.assetid: 472f67ba-05d5-46f7-a2f1-1cef6182574e
ms.topic: article
ms.date: 05/31/2018
---

# Translating Traps from SNMPv1 to SNMPv2C

When the Microsoft WinSNMP implementation receives traps from an entity operating under the SNMPv1 framework, it translates the traps to the SNMPv2C format. Therefore, when [**SnmpRecvMsg**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmprecvmsg) delivers a trap it is always in the SNMPv2C format. RFC 1908, "Coexistence between Version 1 and Version 2 of the Internet-standard Network Management Framework," specifies the rules for translating from the SNMPv1 to the SNMPv2C trap format.

A WinSNMP application can check the last variable binding entry in a variable binding list to determine if the entry is a trap translated from the SNMPv1 to the SNMPv2C format. If so, the last variable binding will always be equal to the value "snmpTrapEnterpriseOID.0".

For more information, see [Managing Traps and Notifications](managing-traps-and-notifications.md).

 

 




