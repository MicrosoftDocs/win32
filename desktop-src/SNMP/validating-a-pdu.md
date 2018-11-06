---
title: Validating a PDU
description: When the WinSNMP application calls the SnmpSendMsg function or the SnmpEncodeMsg function, the Microsoft WinSNMP implementation verifies the validity of the PDU and the other function parameters.
ms.assetid: 0f5754ff-3688-465b-a1ad-bf7d89d7dbd8
ms.topic: article
ms.date: 05/31/2018
---

# Validating a PDU

When the WinSNMP application calls the [**SnmpSendMsg**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpsendmsg) function or the [**SnmpEncodeMsg**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpencodemsg) function, the Microsoft WinSNMP implementation verifies the validity of the PDU and the other function parameters.

The value of one PDU data component (or field) can be valid individually, but it may be invalid in combination with values for other fields. For example, unless the **PDU\_type** field of the PDU is SNMP\_PDU\_GETBULK or SNMP\_PDU\_RESPONSE, both the **error\_status** and **error\_index** fields must be equal to zero. Any other value combination constitutes an invalid PDU.

The implementation rejects invalid PDUs and returns the error status SNMPAPI\_FAILURE. It sets an extended error code equal to SNMPAPI\_PDU\_INVALID.

 

 




