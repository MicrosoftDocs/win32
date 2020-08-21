---
title: SNMP Variable Types and Request PDU Types
description: The definitions for some SNMP variable types and request PDU types have changed. The Snmp.h file maps old types to the corresponding new types.
ms.assetid: 2d87aeee-6fcb-4837-b091-6a9def8a9acb
ms.topic: article
ms.date: 05/31/2018
---

# SNMP Variable Types and Request PDU Types

\[SNMP is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Instead, use [Windows Remote Management](/windows/desktop/WinRM/portal), which is the Microsoft implementation of WS-Man.\]

The definitions for some SNMP variable types and request PDU types have changed. The Snmp.h file maps old types to the corresponding new types.

## Modified SNMP Variable Types

You should use the new SNMP variable types listed in the following table when you develop manager applications that use the Microsoft SNMP Management API. The table lists the old SNMP variable types with the corresponding new variable types.

| Old variable type        | New variable type |
|--------------------------|-------------------|
| ASN\_RFC1155\_IPADDRESS  | ASN\_IPADDRESS    |
| ASN\_RFC1155\_COUNTER    | ASN\_COUNTER32    |
| ASN\_RFC1155\_GAUGE      | ASN\_GAUGE32      |
| ASN\_RFC1155\_TIMETICKS  | ASN\_TIMETICKS    |
| ASN\_RFC1155\_OPAQUE     | ASN\_OPAQUE       |
| ASN\_RFC1213\_DISPSTRING | ASN\_OCTETSTRING  |



 

## Modified SNMP PDU Request Types

You should use the new SNMP PDU types listed in the following table when you develop manager applications that use the Microsoft SNMP Management API. The table lists the old SNMP PDU types with the corresponding new PDU types.

| Old PDU type                 | New PDU type        |
|------------------------------|---------------------|
| ASN\_RFC1157\_GETREQUEST     | SNMP\_PDU\_GET      |
| ASN\_RFC1157\_GETNEXTREQUEST | SNMP\_PDU\_GETNEXT  |
| ASN\_RFC1157\_GETRESPONSE    | SNMP\_PDU\_RESPONSE |
| ASN\_RFC1157\_SETREQUEST     | SNMP\_PDU\_SET      |
| ASN\_RFC1157\_TRAP           | SNMP\_PDU\_V1TRAP   |



 

 

 