---
title: About the Microsoft WinSNMP Implementation
description: The Microsoft WinSNMP implementation complies with WinSNMP version 2.0.
ms.assetid: 99e11d30-d159-4d9b-94d0-baa6e49d82cf
ms.topic: article
ms.date: 05/31/2018
---

# About the Microsoft WinSNMP Implementation

The Microsoft WinSNMP implementation complies with WinSNMP version 2.0. It supports all the functions and operations defined in both the WinSNMP version 1.1a specification and the WinSNMP version 2.0 Addendum. The implementation provides the following services for WinSNMP applications:

-   Manages communications to and from management entities. The entity can reside on the local computer or be connected through a local or wide-area network, or the Internet. For more information, see [Levels of SNMP Support](levels-of-snmp-support.md).
-   Hides the details of SNMP protocol, Abstract Syntax Notation One (ASN.1), and the Basic Encoding Rules (BER) for describing transfer syntax.
-   Verifies the correctness of PDUs and rejects invalid PDUs. For more information, see [Working with Protocol Data Units](working-with-protocol-data-units.md).
-   Transforms SNMPv2C PDU types when necessary in accordance with the relevant RFCs.
-   Converts SNMPv1 traps from an SNMPv1 agent to SNMPv2C traps in accordance with RFC 1908, "Coexistence between Version 1 and Version 2 of the Internet-standard Network Management Framework." For more information, see [Translating Traps from SNMPv1 to SNMPv2C](translating-traps-from-snmpv1-to-snmpv2c.md).
-   Supports the application's retransmission policy and provides retransmission execution support. For more information, see [The WinSNMP Database](the-winsnmp-database.md) and [About Retransmission](about-retransmission.md).
-   Provides entity and context translation support for the application. For more information, see [The WinSNMP Database](the-winsnmp-database.md) and [Setting the Entity and Context Translation Mode](setting-the-entity-and-context-translation-mode.md).

For additional information about the relationship between a WinSNMP application and the implementation, see [WinSNMP Data Management Concepts](winsnmp-data-management-concepts.md) and [WinSNMP Sessions](winsnmp-sessions.md).

 

 




