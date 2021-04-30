---
description: The follow constants are used with Certified Output Protection Protocol (COPP) to specific output protection mechanisms.
ms.assetid: a3cd63d8-22a5-473c-83c2-3499f3d32671
title: COPP Protection Type Flags (Dxva.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- COPP_ProtectionType_Unknown
- COPP_ProtectionType_None
- COPP_ProtectionType_HDCP
- COPP_ProtectionType_ACP
- COPP_ProtectionType_CGMSA
- COPP_ProtectionType_Mask
- COPP_ProtectionType_Reserved
api_type: 
- HeaderDef
api_location: 
- dxva.h
---

# COPP Protection Type Flags

The follow constants are used with Certified Output Protection Protocol (COPP) to specific output protection mechanisms.



| Constant/value                                                                                                                                                                                                                                                                                                             | Description                                                     |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------|
| <span id="COPP_ProtectionType_Unknown"></span><span id="copp_protectiontype_unknown"></span><span id="COPP_PROTECTIONTYPE_UNKNOWN"></span><dl> <dt>**COPP\_ProtectionType\_Unknown**</dt> <dt>0x80000000</dt> </dl>     | Unknown protection mechanism.<br/>                        |
| <span id="COPP_ProtectionType_None"></span><span id="copp_protectiontype_none"></span><span id="COPP_PROTECTIONTYPE_NONE"></span><dl> <dt>**COPP\_ProtectionType\_None**</dt> <dt>0x00000000</dt> </dl>                 | No protection mechanisms.<br/>                            |
| <span id="COPP_ProtectionType_HDCP"></span><span id="copp_protectiontype_hdcp"></span><span id="COPP_PROTECTIONTYPE_HDCP"></span><dl> <dt>**COPP\_ProtectionType\_HDCP**</dt> <dt>0x00000001</dt> </dl>                 | High-Bandwidth Digital Content Protection (HDCP).<br/>    |
| <span id="COPP_ProtectionType_ACP"></span><span id="copp_protectiontype_acp"></span><span id="COPP_PROTECTIONTYPE_ACP"></span><dl> <dt>**COPP\_ProtectionType\_ACP**</dt> <dt>0x00000002</dt> </dl>                     | Analog Copy Protection (ACP).<br/>                        |
| <span id="COPP_ProtectionType_CGMSA"></span><span id="copp_protectiontype_cgmsa"></span><span id="COPP_PROTECTIONTYPE_CGMSA"></span><dl> <dt>**COPP\_ProtectionType\_CGMSA**</dt> <dt>0x00000004</dt> </dl>             | Copy Generation Management System   Analog (CGMS-A).<br/> |
| <span id="COPP_ProtectionType_Mask"></span><span id="copp_protectiontype_mask"></span><span id="COPP_PROTECTIONTYPE_MASK"></span><dl> <dt>**COPP\_ProtectionType\_Mask**</dt> <dt>0x80000007</dt> </dl>                 | Bitmask to isolate valid flags.<br/>                      |
| <span id="COPP_ProtectionType_Reserved"></span><span id="copp_protectiontype_reserved"></span><span id="COPP_PROTECTIONTYPE_RESERVED"></span><dl> <dt>**COPP\_ProtectionType\_Reserved**</dt> <dt>0x7FFFFFF8</dt> </dl> | Reserved. Must be zero.<br/>                              |



## Remarks

Some methods return a single flag from this enumeration type, and some methods return a bitwise **OR** of one or more flags.

These flags are used in the following COPP queries and commands.

-   Global Protection Level
-   Local Protection Level
-   Protection Type
-   Set Protection Level

## Requirements



| Requirement | Value |
|-------------------|-----------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Dxva.h</dt> </dl> |



## See also

<dl> <dt>

[Constants and GUIDs](constants-and-guids.md)
</dt> <dt>

[Using Certified Output Protection Protocol (COPP)](using-certified-output-protection-protocol--copp.md)
</dt> </dl>

 

 




