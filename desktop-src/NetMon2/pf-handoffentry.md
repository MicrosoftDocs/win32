---
description: The PF\_HANDOFFENTRY structure defines a protocol that Network Monitor adds to the handoff set of a parser.
ms.assetid: c26bee6e-7dbf-4994-a0a7-a280cf4838be
title: PF_HANDOFFENTRY structure (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PF_HANDOFFENTRY
api_type: 
- HeaderDef
api_location: 
- Netmon.h
---

# PF\_HANDOFFENTRY structure

The **PF\_HANDOFFENTRY** structure defines a protocol that Network Monitor adds to the handoff set of a parser.

## Syntax


```C++
typedef struct _PF_HANDOFFENTRY {
  char                      szIniFile[MAX_PATH];
  char                      szIniSection[MAX_PATH];
  char                      szProtocol[MAX_PROTOCOL_NAME_LEN];
  DWORD                     dwHandOffValue;
  PF_HANDOFFVALUEFORMATBASE ValueFormatBase;
} PF_HANDOFFENTRY, *PPF_HANDOFFENTRY;
```



## Members

<dl> <dt>

**szIniFile**
</dt> <dd>

Name of the INI file associated with the protocol.

</dd> <dt>

**szIniSection**
</dt> <dd>

Section label within the INI file.

</dd> <dt>

**szProtocol**
</dt> <dd>

Name of the protocol.

</dd> <dt>

**dwHandOffValue**
</dt> <dd>

Value associated with the protocol.

</dd> <dt>

**ValueFormatBase**
</dt> <dd>

Numeric base of the protocol value that is specified in **dwHandOffValue**. The **ValueFormatBase** function must be set to one of the following:



| Value                                                                                                                                                                                                                        | Meaning                     |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|
| <span id="HANDOFF_VALUE_FORMAT_BASE_UNKNOWN"></span><span id="handoff_value_format_base_unknown"></span><dl> <dt>**HANDOFF\_VALUE\_FORMAT\_BASE\_UNKNOWN**</dt> </dl> | Unknown base<br/>     |
| <span id="HANDOFF_VALUE_FORMAT_BASE_DECIMAL"></span><span id="handoff_value_format_base_decimal"></span><dl> <dt>**HANDOFF\_VALUE\_FORMAT\_BASE\_DECIMAL**</dt> </dl> | Decimal base<br/>     |
| <span id="HANDOFF_VALUE_FORMAT_BASE_HEX"></span><span id="handoff_value_format_base_hex"></span><dl> <dt>**HANDOFF\_VALUE\_FORMAT\_BASE\_HEX**</dt> </dl>             | Hexadecimal base<br/> |



 

</dd> </dl>

## Remarks

An array of the **PF\_HANDOFFENTRY** structures is used in the [PF\_HANDOFFSET](pf-handoffset.md) structure.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



## See also

<dl> <dt>

[PF\_HANDOFFSET](pf-handoffset.md)
</dt> </dl>

 

 




