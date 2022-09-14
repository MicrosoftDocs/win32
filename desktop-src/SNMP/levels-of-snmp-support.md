---
title: Levels of SNMP Support
description: The Microsoft WinSNMP implementation provides level 2 SNMP communications support.
ms.assetid: 9874ad9b-4eb9-4d63-816b-fe444c5b4d8a
ms.topic: article
ms.date: 05/31/2018
---

# Levels of SNMP Support

The Microsoft WinSNMP implementation provides level 2 SNMP communications support. Level 2 supports the Internet Engineering Task Force (IETF) standard SNMPv2 protocol as defined in RFCs 1902-1908. It also supports the community-based message wrapper as defined in RFC 1901 (SNMPv2C).

Level 2 communications support includes message encoding and decoding services, previously called Level 0 communications support in WinSNMP version 1.1a. Level 2 also supports all SNMPv1 protocol operations, previously called Level 1 communications support in WinSNMP version 1.1a.

The implementation returns the maximum level of SNMP communications it supports in response to a call by the WinSNMP application to the [**SnmpStartup**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpstartup) function.

If the WinSNMP application uses the implementation for SNMP message encoding and decoding only, the application must perform required transformations that the implementation would have performed. This includes translating SNMPv1 traps returned by a call to the [**SnmpRecvMsg**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmprecvmsg) function, to SNMPv2C traps. It also includes translating PDU types defined by SNMPv1 to the relevant PDU type defined by SNMPv2C, in accordance with RFC 1908.

 

 




