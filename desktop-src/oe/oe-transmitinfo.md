---
title: TRANSMITINFO structure
description: Do not use. Holds transmission information about a message body.
ms.assetid: '94d0de66-e432-4096-9d49-a5a993a65a6a'
keywords: ["TRANSMITINFO structure Windows Mail (formerly Outlook Express)", "LPTRANSMITINFO structure pointer Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- TRANSMITINFO
api_location:
- Mimeole.h
api_type:
- HeaderDef
---

# TRANSMITINFO structure

Do not use. Holds transmission information about a message body.

## Syntax


```C++
typedef struct tagTRANSMITINFO {
  ENCODINGTYPE ietCurrent;
  ENCODINGTYPE ietXmitMime;
  ENCODINGTYPE ietXmit822;
  ULONG        cbLongestLine;
  ULONG        cExtended;
  ULONG        ulPercentExt;
  ULONG        cbSize;
  ULONG        cLines;
} TRANSMITINFO, *LPTRANSMITINFO;
```



## Members

<dl> <dt>

**ietCurrent**
</dt> <dd>

Type: **[**ENCODINGTYPE**](oe-encodingtype.md)**

</dd> <dd>

Contains the current [**ENCODINGTYPE**](oe-encodingtype.md) for the body.

</dd> <dt>

**ietXmitMime**
</dt> <dd>

Type: **[**ENCODINGTYPE**](oe-encodingtype.md)**

</dd> <dd>

Contains the suggested [**ENCODINGTYPE**](oe-encodingtype.md) if the message is saved in MIME format.

</dd> <dt>

**ietXmit822**
</dt> <dd>

Type: **[**ENCODINGTYPE**](oe-encodingtype.md)**

</dd> <dd>

Contains the suggested [**ENCODINGTYPE**](oe-encodingtype.md) if the message is saved in [RFC 822](http://www.ietf.org/rfc/rfc822.txt) format.

</dd> <dt>

**cbLongestLine**
</dt> <dd>

Type: **ULONG**

</dd> <dd>

Contains the number of bytes for the longest line in the body. This can determine whether wrapping is needed.

</dd> <dt>

**cExtended**
</dt> <dd>

Type: **ULONG**

</dd> <dd>

Contains the number of 8-bit characters in the body.

</dd> <dt>

**ulPercentExt**
</dt> <dd>

Type: **ULONG**

</dd> <dd>

Contains the percentage of characters that are 8-bit.

</dd> <dt>

**cbSize**
</dt> <dd>

Type: **ULONG**

</dd> <dd>

Contains the number of bytes in the body.

</dd> <dt>

**cLines**
</dt> <dd>

Type: **ULONG**

</dd> <dd>

Contains the number of lines in the body.

</dd> </dl>

## Remarks

This structure is used with the [**GetTransmitInfo**](oe-imimebody-gettransmitinfo.md) method. This structure contains information about the data stored in a message body and suggestions about how to encode the message body for optimal interoperability.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| Product<br/>                  | Outlook Express 6.0<br/>                                                         |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl> |



 

 





