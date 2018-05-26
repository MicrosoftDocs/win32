---
title: BODYOFFSETS structure
description: Do not use. Holds information about the byte offsets for a body.
ms.assetid: e44507e1-857e-48df-8f7f-c5aa282b19f8
keywords:
- BODYOFFSETS structure Windows Mail (formerly Outlook Express)
- LPBODYOFFSETS structure pointer Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- BODYOFFSETS
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

# BODYOFFSETS structure

Do not use. Holds information about the byte offsets for a body.

## Syntax


```C++
typedef struct tagBODYOFFSETS {
  DWORD cbBoundaryStart;
  DWORD cbHeaderStart;
  DWORD cbBodyStart;
  DWORD cbBodyEnd;
} BODYOFFSETS, *LPBODYOFFSETS;
```



## Members

<dl> <dt>

**cbBoundaryStart**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains the byte offset of the starting boundary for the body.

</dd> <dt>

**cbHeaderStart**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains the byte offset to the header of the body.

</dd> <dt>

**cbBodyStart**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains the byte offset to where the body data starts.

</dd> <dt>

**cbBodyEnd**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains the byte offset to where the body data ends.

</dd> </dl>

## Remarks

The byte offsets are relative to the source message with which the body is associated. A body does not have offsets unless the body has been saved to a message or the body was loaded from a message. To get the offsets for a body, a client would call [**GetOffsets**](oe-imimebody-getoffsets.md) or [**GetBodyOffsets**](oe-imimemessagetree-getbodyoffsets.md). For MIME and [RFC 822](http://www.ietf.org/rfc/rfc822.txt) messages, the offsets have a subtly different meaning because an [RFC 822](http://www.ietf.org/rfc/rfc822.txt) message does not have boundaries or headers for attachments.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| Product<br/>                  | Outlook Express 6.0<br/>                                                         |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl> |



 

 





