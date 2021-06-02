---
description: The PF\_PARSERDLLINFO structure defines the parsers located in the parser DLL.
ms.assetid: a7473b58-7767-4224-be3b-e96132d98adf
title: PF_PARSERDLLINFO structure (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PF_PARSERDLLINFO
api_type: 
- HeaderDef
api_location: 
- Netmon.h
---

# PF\_PARSERDLLINFO structure

The **PF\_PARSERDLLINFO** structure defines the parsers located in the parser DLL.

## Syntax


```C++
typedef struct _PF_PARSERDLLINFO {
  DWORD         nParsers;
  PF_PARSERINFO ParserInfo[];
} PF_PARSERDLLINFO, *PPF_PARSERDLLINFO;
```



## Members

<dl> <dt>

**nParsers**
</dt> <dd>

Number of parsers in the parser DLL.

</dd> <dt>

**ParserInfo**
</dt> <dd>

Array of [PF\_PARSERINFO](pf-parserinfo.md) structures that describe each parser in the parser DLL.

</dd> </dl>

## Remarks

The **PF\_PARSERDLLINFO** structure is returned by the [ParserAutoInstallInfo](parserautoinstallinfo.md) export function that is implemented in the parser DLL. The **ParserAutoInstallInfo** function identifies the number of parsers in the DLL, and uses an array of [PF\_PARSERINFO](pf-parserinfo.md) structures to describe each parser.

The PF\_PARSERDLLINFO structure must be allocated using **HeapAlloc**.



| For information on                                               | See                                                                         |
|------------------------------------------------------------------|-----------------------------------------------------------------------------|
| What parsers are, and how they work with Network Monitor.        | [Parsers](parsers.md)                                                      |
| Which entry points are included in the parser DLL.               | [Parser DLL Architecture](parser-dll-architecture.md)                      |
| How to implement **ParserAutoInstallInfo**  includes an example. | [Implementing ParserAutoIstallInfo](implementing-parserautoinstallinfo.md) |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



## See also

<dl> <dt>

[PF\_PARSERINFO](pf-parserinfo.md)
</dt> <dt>

[ParserAutoInstallInfo](parserautoinstallinfo.md)
</dt> </dl>

 

 




