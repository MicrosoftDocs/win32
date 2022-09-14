---
title: Trap Formats
description: The format of trap PDUs is different than that of other PDUs. The format of SNMPv1 traps and SNMPv2C traps is also different.
ms.assetid: 2d2b4520-28b7-4a2e-8dee-456e17d9d6f6
ms.topic: article
ms.date: 05/31/2018
---

# Trap Formats

The format of trap PDUs is different than that of other PDUs. The format of SNMPv1 traps and SNMPv2C traps is also different.

Under the SNMPv2C framework, the PDU trap format is a variable binding list of *n* variable binding entries organized in the following manner:

-   The first variable binding entry contains a time-stamp.
-   The second variable binding entry is an object identifier that identifies the trap.
-   The third through *n* variable binding entries, if present, contain additional information associated with the trap.

Under the SNMPv1 framework, the PDU trap format is as follows.

| Field                      | Description                                                      |
|----------------------------|------------------------------------------------------------------|
| enterprise                 | Identifies the type of device that generated the trap.           |
| agent-addr                 | Identifies the IP address of the device that generated the trap. |
| generic-trap/specific-trap | Identifies a predefined trap type.                               |
| time-stamp                 | Identifies when the trap was generated.                          |
| variable-bindings          | Contains additional information associated with the trap.        |



 

The [**SnmpRecvMsg**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmprecvmsg) function always returns a message in the SNMPv2C format. If the message contains the operation type **SNMP\_PDU\_TRAP**, the application can read the variable binding entries of the message and retrieve the information associated with the trap.

 

 




