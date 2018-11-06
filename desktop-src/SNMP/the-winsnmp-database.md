---
title: The WinSNMP Database
description: The Microsoft WinSNMP implementation maintains a store of administrative information in a database.
ms.assetid: 0a0d9731-d800-4eaa-8230-25469a0b0285
ms.topic: article
ms.date: 05/31/2018
---

# The WinSNMP Database

The Microsoft WinSNMP implementation maintains a store of administrative information in a database. The database includes the following information:

-   Network and version properties.

    The implementation uses these properties to determine which network transport protocol and SNMP version framework to use to complete transmission requests. For more information, see [About SNMP Versions](about-snmp-versions.md).

-   Entity and context translation mode.

    The implementation uses this mode to interpret user-friendly names for SNMP entities and contexts. For more information, see [Setting the Entity and Context Translation Mode](setting-the-entity-and-context-translation-mode.md).

-   Retransmission policy setting.

    The implementation uses this setting to determine whether or not it should execute the application's retransmission policy. The implementation stores a time-out value and a retry count for each destination entity. For more information, see [About Retransmission](about-retransmission.md) and [Managing the Retransmission Policy](managing-the-retransmission-policy.md).

 

 




