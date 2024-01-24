---
description: The PF\_PARSERINFO structure defines one parser at a time. In the PF\_PARSERINFO structure, a parser is defined by the information about the protocol that the parser detects.
ms.assetid: e1180952-9560-4386-9320-919dfb8171b3
title: PF_PARSERINFO structure (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PF_PARSERINFO
api_type: 
- HeaderDef
api_location: 
- Netmon.h
---

# PF\_PARSERINFO structure

The **PF\_PARSERINFO** structure defines one parser at a time. In the **PF\_PARSERINFO** structure, a parser is defined by the information about the protocol that the parser detects.

## Syntax


```C++
typedef struct _PF_PARSERINFO {
  char           szProtocolName[MAX_PROTOCOL_NAME_LEN];
  char           szComment[MAX_PROTOCOL_COMMENT_LEN];
  char           szHelpFile[MAX_PATH];
  PPF_FOLLOWSET  pWhoCanPrecedeMe;
  PPF_FOLLOWSET  pWhoCanFollowMe;
  PPF_HANDOFFSET pWhoHandsOffToMe;
  PPF_HANDOFFSET pWhoDoIHandOffTo;
} PF_PARSERINFO, *PPF_PARSERINFO;
```



## Members

<dl> <dt>

**szProtocolName**
</dt> <dd>

Name of the protocol that the parser detects.

</dd> <dt>

**szComment**
</dt> <dd>

Brief description of the protocol.

</dd> <dt>

**szHelpFile**
</dt> <dd>

Name of the protocol Help file, if any.

</dd> <dt>

**pWhoCanPrecedeMe**
</dt> <dd>

Pointer to a [PF\_FOLLOWSET](pf-followset.md) structure that lists the protocols that can precede the protocol the **PF\_PARSERINFO** structure describes. Network Monitor adds the parser protocol to the [*follow set*](f.md) of all the protocols in the set.

</dd> <dt>

**pWhoCanFollowMe**
</dt> <dd>

Pointer to a [PF\_FOLLOWSET](pf-followset.md) structure that lists the protocol that can follow the protocol the **PF\_PARSERINFO** structure describes. Network Monitor adds the protocols of the set to the [*follow set*](f.md) of the parser protocol.

</dd> <dt>

**pWhoHandsOffToMe**
</dt> <dd>

Pointer to a [PF\_HANDOFFSET](pf-handoffset.md) structure that hands-off to the protocol that the **PF\_PARSERINFO** structure describes. Network Monitor adds the parser protocol to the [*handoff sets*](h.md) of all the protocols in the set.

</dd> <dt>

**pWhoDoIHandOffTo**
</dt> <dd>

Pointer to a [PF\_HANDOFFSET](pf-handoffset.md) structure that lists the protocols that the parser protocol hands off to. Network Monitor adds the protocols of this set to the [*handoff set*](h.md) of the parser protocol.

</dd> </dl>

## Remarks

The **PF\_PARSERINFO** structure is used in the **PF\_PARSERDLLINFO** structure to provide a description of a parser. Network Monitor uses the parser description to update the [*Parser.ini*](p.md) file, and the INI files of the parsers that precede and follow the protocol described in the **PF\_PARSERINFO** structure.

A follow set specifies the protocols that follow a protocol. Network Monitor uses a follow set when the parser cannot identify the next protocol from the data in a protocol instance. A follow set is stored in the [*Parser.ini*](p.md) file. When the parser is installed for the first time, Network Monitor updates the follow set of the parser protocols that are listed in **pWhoCanPrecedeMe** and **pWhoCanFollowMe**.

A handoff set specifies the protocols that follow a protocol. The parser uses a handoff set only when the parser can identify the next protocol from the data in a protocol instance. A handoff set is stored in the INI files of each parser. When the parser is installed for the first time, Network Monitor updates the handoff set of the parser protocols that are listed in **pWhoHandsOffToMe** and **pWhoDoIHandOffTo**.



| For information on                                               | See                                                                          |
|------------------------------------------------------------------|------------------------------------------------------------------------------|
| What parsers are, and how they work with Network Monitor.        | [Parsers](parsers.md)                                                       |
| What follow sets contain.                                        | [Specifying a Follow Set](specifying-a-follow-set.md)                       |
| What handoff sets contain.                                       | [Specifying a Handoff Set](specifying-a-handoff-set.md)                     |
| What entry points are included in the parser DLL.                | [Parser DLL Architecture](parser-dll-architecture.md)                       |
| How to implement **ParserAutoInstallInfo**  includes an example. | [Implementing ParserAutoInstallInfo](implementing-parserautoinstallinfo.md) |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



## See also

<dl> <dt>

[ParserAutoInstallInfo](parserautoinstallinfo.md)
</dt> <dt>

[PF\_FOLLOWSET](pf-followset.md)
</dt> <dt>

[PF\_HANDOFFSET](pf-handoffset.md)
</dt> <dt>

[PF\_PARSERDLLINFO](pf-parserdllinfo.md)
</dt> </dl>

 

 




