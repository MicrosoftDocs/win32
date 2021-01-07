---
description: The PATTERNMATCH structure defines pattern elements used to evaluate a frame.
ms.assetid: 3ad27197-92da-49e5-bb0e-daf54de6c54c
title: PATTERNMATCH structure (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PATTERNMATCH
api_type: 
- HeaderDef
api_location: 
- Netmon.h
---

# PATTERNMATCH structure

The **PATTERNMATCH** structure defines pattern elements used to evaluate a frame.

## Syntax


```C++
typedef struct _PATTERNMATCH {
  DWORD        Flags;
  BYTE         OffsetBasis;
  GENERIC_PORT Port;
  WORD         Offset;
  WORD         Length;
  BYTE         PatternToMatch[MAX_PATTERN_LENGTH];
} PATTERNMATCH, *LPPATTERNMATCH;
```



## Members

<dl> <dt>

**Flags**
</dt> <dd>

Pattern match flags:



| Value                                                                                                                                                                                                                                                                                           | Meaning                                                                                           |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| <span id="PATTERN_MATCH_FLAGS_NOT"></span><span id="pattern_match_flags_not"></span><dl> <dt>**PATTERN\_MATCH\_FLAGS\_NOT**</dt> <dt>0x00000001</dt> </dl>                                   | When set, this flag retains frames that lack the specified pattern in the proper spot.<br/> |
| <span id="PATTERN_MATCH_FLAGS_PORT_SPECIFIED"></span><span id="pattern_match_flags_port_specified"></span><dl> <dt>**PATTERN\_MATCH\_FLAGS\_PORT\_SPECIFIED**</dt> <dt>0x00000008</dt> </dl> | Seeks a port number value.<br/>                                                             |



 

</dd> <dt>

**OffsetBasis**
</dt> <dd>

Types of offset, which can be one of the following:



| Value                                                                                                                                                                                                                                                       | Meaning                                                                                |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| <span id="OFFSET_BASIS_RELATIVE_TO_FRAME"></span><span id="offset_basis_relative_to_frame"></span><dl> <dt>**OFFSET\_BASIS\_RELATIVE\_TO\_FRAME**</dt> </dl>                                         | Sets an offset, in bytes, relative to start of the frame.<br/>                   |
| <span id="OFFSET_BASIS_RELATIVE_TO_EFFECTIVE_PROTOCOL"></span><span id="offset_basis_relative_to_effective_protocol"></span><dl> <dt>**OFFSET\_BASIS\_RELATIVE\_TO\_EFFECTIVE\_PROTOCOL**</dt> </dl> | Sets an offset, in bytes, relative to the start of the referenced protocol.<br/> |
| <span id="OFFSET_BASIS_RELATIVE_TO_IPX"></span><span id="offset_basis_relative_to_ipx"></span><dl> <dt>**OFFSET\_BASIS\_RELATIVE\_TO\_IPX**</dt> </dl>                                               | Sets an offset, in bytes, only relative to IPX.<br/>                             |
| <span id="OFFSET_BASIS_RELATIVE_TO_IP"></span><span id="offset_basis_relative_to_ip"></span><dl> <dt>**OFFSET\_BASIS\_RELATIVE\_TO\_IP**</dt> </dl>                                                  | Sets an offset, in bytes, only relative to IP.<br/>                              |



 

</dd> <dt>

**Port**
</dt> <dd>

Port value, if specified.

</dd> <dt>

**Offset**
</dt> <dd>

The offset, in bytes, relative to the **OffsetBasis**.

</dd> <dt>

**Length**
</dt> <dd>

Length of the matched pattern.

</dd> <dt>

**PatternToMatch**
</dt> <dd>

Pattern to match.

</dd> </dl>

## Remarks

This structure is used to construct a capture filter. For more information about implementing this structure, see [Capture Filters](capture-filters.md).

A capture filter can contain up to four **PATTERNMATCH** structures.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



## See also

<dl> <dt>

[CAPTUREFILTER](capturefilter.md)
</dt> </dl>

 

 




