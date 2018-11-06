---
title: Translating Message Requests
description: This topic describes the process of translating SNMPv1 requests into SNMPv2 requests.
ms.assetid: 7671ae36-99b1-47b1-930a-f376021d56a2
ms.topic: article
ms.date: 05/31/2018
---

# Translating Message Requests

This topic describes the process of translating SNMPv1 requests into SNMPv2 requests.

If a WinSNMP application requests functionality that is available under the SNMP version 2C framework (SNMPv2C), but the target entity supports only the SNMP version 1 framework (SNMPv1), the Microsoft WinSNMP implementation attempts to translate the request to the SNMPv1 format. To do this, the implementation uses the procedures defined in RFC 1908, "Coexistence Between Version 1 and Version 2 of the Internet-Standard Network Management Framework." If translation is not possible, the [**SnmpSendMsg**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpsendmsg) function fails with the extended error code SNMPAPI\_OPERATION\_INVALID.

 

 




