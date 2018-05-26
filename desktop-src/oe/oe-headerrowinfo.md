---
title: HEADERROWINFO structure
description: Do not use. Holds information about a row in an IMimeHeaderTable object.
ms.assetid: a8600fac-89ff-4d01-9645-0c4557ffb0a9
keywords:
- HEADERROWINFO structure Windows Mail (formerly Outlook Express)
- LPHEADERROWINFO structure pointer Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- HEADERROWINFO
api_location:
- Mimeole.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# HEADERROWINFO structure

Do not use. Holds information about a row in an [**IMimeHeaderTable**](oe-imimeheadertable.md) object.

## Syntax


```C++
typedef struct tagHEADERROWINFO {
  DWORD dwRowNumber;
  ULONG cboffStart;
  ULONG cboffColon;
  ULONG cboffEnd;
} HEADERROWINFO, *LPHEADERROWINFO;
```



## Members

<dl> <dt>

**dwRowNumber**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains the relative position of the header row in the header. Row numbers increase from top to bottom of the header table.

</dd> <dt>

**cboffStart**
</dt> <dd>

Type: **ULONG**

</dd> <dd>

Contains the byte offset in the message where the header row starts.

</dd> <dt>

**cboffColon**
</dt> <dd>

Type: **ULONG**

</dd> <dd>

Contains the byte offset of the colon (":") in the message between the header name and the header data.

</dd> <dt>

**cboffEnd**
</dt> <dd>

Type: **ULONG**

</dd> <dd>

Contains the byte offset in the message where the header row ends. This is the byte offset of the character immediately following the last line feed for the header.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| Product<br/>                  | Outlook Express 6.0<br/>                                                         |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl> |



 

 





