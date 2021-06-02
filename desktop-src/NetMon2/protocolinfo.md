---
description: The PROTOCOLINFO structure describes a protocol.
ms.assetid: '7f936c93-a942-4591-9abc-59872df0964e'
title: PROTOCOLINFO structure (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PROTOCOLINFO
api_type: 
- HeaderDef
api_location: 
- Netmon.h
---

# PROTOCOLINFO structure

The **PROTOCOLINFO** structure describes a protocol.

## Syntax


```C++
typedef struct _PROTOCOLINFO {
  DWORD              ProtocolID;
  LPPROPERTYDATABASE PropertyDatabase;
  BYTE               ProtocolName[16];
  BYTE               HelpFile[16];
  BYTE               Comment[128];
} PROTOCOLINFO, *LPPROTOCOLINFO;
```



## Members

<dl> <dt>

**ProtocolID**
</dt> <dd>

System-assigned protocol identifier of the specified run session.

</dd> <dt>

**PropertyDatabase**
</dt> <dd>

Property database of the specified protocol.

</dd> <dt>

**ProtocolName**
</dt> <dd>

Abbreviated protocol name.

</dd> <dt>

**HelpFile**
</dt> <dd>

Optional Help file name associated with the protocol.

</dd> <dt>

**Comment**
</dt> <dd>

A comment describing the protocol.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



 

 




