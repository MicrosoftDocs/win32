---
title: SNMP Simple Syntax Values (Snmp.h)
description: The SNMP Simple Syntax Values are used to indicate an SNMP variable type.
ms.assetid: 42b681e5-721d-4d41-bc1a-c9f0005cde87
topic_type:
- apiref
api_name:
- ASN_INTEGER
- ASN_BITS
- ASN_OCTETSTRING
- ASN_NULL
- ASN_OBJECTIDENTIFIER
- ASN_INTEGER32
api_location:
- Snmp.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# SNMP Simple Syntax Values

\[SNMP is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Instead, use [Windows Remote Management](/windows/desktop/WinRM/portal), which is the Microsoft implementation of WS-Man.\]

The SNMP Simple Syntax Values are used to indicate an SNMP variable type.



| Constant                                                                                                                                                                           | Description                                                           |
|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------|
| <span id="ASN_INTEGER"></span><span id="asn_integer"></span><dl> <dt>**ASN\_INTEGER**</dt> </dl>                            | Indicates a 32-bit signed integer variable.<br/>                |
| <span id="ASN_BITS"></span><span id="asn_bits"></span><dl> <dt>**ASN\_BITS**</dt> </dl>                                     | Indicates a variable that is an enumeration of named bits.<br/> |
| <span id="ASN_OCTETSTRING"></span><span id="asn_octetstring"></span><dl> <dt>**ASN\_OCTETSTRING**</dt> </dl>                | Indicates an octet string variable.<br/>                        |
| <span id="ASN_NULL"></span><span id="asn_null"></span><dl> <dt>**ASN\_NULL**</dt> </dl>                                     | Indicates a **NULL** value.<br/>                                |
| <span id="ASN_OBJECTIDENTIFIER"></span><span id="asn_objectidentifier"></span><dl> <dt>**ASN\_OBJECTIDENTIFIER**</dt> </dl> | Indicates an object identifier variable.<br/>                   |
| <span id="ASN_INTEGER32"></span><span id="asn_integer32"></span><dl> <dt>**ASN\_INTEGER32**</dt> </dl>                      | Indicates a 32-bit signed integer value.<br/>                   |



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

 

