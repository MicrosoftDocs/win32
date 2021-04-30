---
title: PDU Type Values (Snmp.h)
description: The PDU type values are used in the pdu\_type field of the PDU to describe its type.
ms.assetid: 9d7a3f1c-7940-428b-a4e0-3c9e61dd755f
topic_type:
- apiref
api_name:
- SNMP_PDU_GET
- SNMP_PDU_GETNEXT
- SNMP_PDU_RESPONSE
- SNMP_PDU_SET
- SNMP_PDU_V1TRAP
- SNMP_PDU_GETBULK
- SNMP_PDU_INFORM
- SNMP_PDU_TRAP
api_location:
- Snmp.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# PDU Type Values

\[SNMP is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Instead, use [Windows Remote Management](/windows/desktop/WinRM/portal), which is the Microsoft implementation of WS-Man.\]

The PDU type values are used in the **pdu\_type** field of the PDU to describe its type.



| Constant                                                                                                                                                                   | Description                                                                                                  |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------|
| <span id="SNMP_PDU_GET"></span><span id="snmp_pdu_get"></span><dl> <dt>**SNMP\_PDU\_GET**</dt> </dl>                | Search and retrieve a value from a specified SNMP variable.<br/>                                       |
| <span id="SNMP_PDU_GETNEXT"></span><span id="snmp_pdu_getnext"></span><dl> <dt>**SNMP\_PDU\_GETNEXT**</dt> </dl>    | Search and retrieve the value of an SNMP variable without knowing the exact name of the variable.<br/> |
| <span id="SNMP_PDU_RESPONSE"></span><span id="snmp_pdu_response"></span><dl> <dt>**SNMP\_PDU\_RESPONSE**</dt> </dl> | Reply to an SNMP\_PDU\_GET or an SNMP\_PDU\_GETNEXT request.<br/>                                      |
| <span id="SNMP_PDU_SET"></span><span id="snmp_pdu_set"></span><dl> <dt>**SNMP\_PDU\_SET**</dt> </dl>                | Store a value in a specified SNMP variable.<br/>                                                       |
| <span id="SNMP_PDU_V1TRAP"></span><span id="snmp_pdu_v1trap"></span><dl> <dt>**SNMP\_PDU\_V1TRAP**</dt> </dl>       | Indicates that the PDU trap is formatted to conform with the SNMPv1 standard.<br/>                     |
| <span id="SNMP_PDU_GETBULK"></span><span id="snmp_pdu_getbulk"></span><dl> <dt>**SNMP\_PDU\_GETBULK**</dt> </dl>    | Search and retrieve multiple values with a single request.<br/>                                        |
| <span id="SNMP_PDU_INFORM"></span><span id="snmp_pdu_inform"></span><dl> <dt>**SNMP\_PDU\_INFORM**</dt> </dl>       | Indicates an inform request PDU.<br/>                                                                  |
| <span id="SNMP_PDU_TRAP"></span><span id="snmp_pdu_trap"></span><dl> <dt>**SNMP\_PDU\_TRAP**</dt> </dl>             | Alerts the management system to an extraordinary event under SNMPv2C.<br/>                             |



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                        |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                              |
| Header<br/>                   | <dl> <dt>Snmp.h</dt> </dl> |



## See also

<dl> <dt>

[Simple Network Management Protocol (SNMP) Overview](simple-network-management-protocol-snmp-.md)
</dt> <dt>

[SNMP Reference](snmp-reference.md)
</dt> <dt>

[SNMP Constants](snmp-constants.md)
</dt> </dl>

 

