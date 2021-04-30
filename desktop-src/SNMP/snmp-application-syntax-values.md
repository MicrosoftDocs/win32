---
title: SNMP Application Syntax Values (Snmp.h)
description: The SNMP Application Syntax Values are used by management applications that employ the Microsoft SNMP Management API.
ms.assetid: fa269f97-f9d3-49f4-b29b-8c4d71f075d0
topic_type:
- apiref
api_name:
- ASN_IPADDRESS
- ASN_COUNTER32
- ASN_GAUGE32
- ASN_TIMETICKS
- ASN_OPAQUE
- ASN_COUNTER64
- ASN_UINTEGER32
- ASN_RFC2578_UNSIGNED32
api_location:
- Snmp.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# SNMP Application Syntax Values

\[SNMP is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Instead, use [Windows Remote Management](/windows/desktop/WinRM/portal), which is the Microsoft implementation of WS-Man.\]

The SNMP Application Syntax Values are used by management applications that employ the Microsoft SNMP Management API.



| Constant                                                                                                                                                                                  | Description                                                                                                                      |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------|
| <span id="ASN_IPADDRESS"></span><span id="asn_ipaddress"></span><dl> <dt>**ASN\_IPADDRESS**</dt> </dl>                             | Indicates an IP address variable.<br/>                                                                                     |
| <span id="ASN_COUNTER32"></span><span id="asn_counter32"></span><dl> <dt>**ASN\_COUNTER32**</dt> </dl>                             | Indicates a counter variable.<br/>                                                                                         |
| <span id="ASN_GAUGE32"></span><span id="asn_gauge32"></span><dl> <dt>**ASN\_GAUGE32**</dt> </dl>                                   | Indicates a gauge variable. This variable describes an Unsigned32 type in conformance with RFC 1902.<br/>                  |
| <span id="ASN_TIMETICKS"></span><span id="asn_timeticks"></span><dl> <dt>**ASN\_TIMETICKS**</dt> </dl>                             | Indicates a timeticks variable.<br/>                                                                                       |
| <span id="ASN_OPAQUE"></span><span id="asn_opaque"></span><dl> <dt>**ASN\_OPAQUE**</dt> </dl>                                      | Indicates an opaque variable.<br/>                                                                                         |
| <span id="ASN_COUNTER64"></span><span id="asn_counter64"></span><dl> <dt>**ASN\_COUNTER64**</dt> </dl>                             | Indicates a counter variable that increases until it reaches a maximum value of (2^64) - 1.<br/>                           |
| <span id="ASN_UINTEGER32"></span><span id="asn_uinteger32"></span><dl> <dt>**ASN\_UINTEGER32**</dt> </dl>                          | Indicates a 32-bit unsigned integer variable. This variable describes a UInteger32 type in conformance with RFC 1442.<br/> |
| <span id="ASN_RFC2578_UNSIGNED32"></span><span id="asn_rfc2578_unsigned32"></span><dl> <dt>**ASN\_RFC2578\_UNSIGNED32**</dt> </dl> | See ASN\_GAUGE32.<br/>                                                                                                     |



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

 

