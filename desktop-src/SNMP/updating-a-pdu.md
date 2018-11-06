---
title: Updating a PDU
description: A WinSNMP application can retrieve and update selected PDU fields by using the SnmpGetPduData and the SnmpSetPduData functions.
ms.assetid: 001f5252-aa54-490b-8ff0-39a7780baff8
ms.topic: article
ms.date: 05/31/2018
---

# Updating a PDU

A WinSNMP application can retrieve and update selected PDU fields by using the [**SnmpGetPduData**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpgetpdudata) and the [**SnmpSetPduData**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpsetpdudata) functions.

The application can retrieve the PDU type, request identifier, error status, and error index fields from a specific PDU. It can also retrieve the handle to the variable binding list. The application can update the **PDU\_type** and **request\_id** fields.

If the PDU type is equal to SNMP\_PDU\_GETBULK, the application can also update the **non\_repeaters** and the **max\_repetitions** fields of the PDU.

 

 




