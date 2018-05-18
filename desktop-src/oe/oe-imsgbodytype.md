---
title: IMSGBODYTYPE enumeration
description: Do not use. Indicates message body types for verification.
ms.assetid: 'af21a17b-84f9-41b6-b28b-bb55b32f40b3'
keywords: ["IMSGBODYTYPE enumeration Windows Mail (formerly Outlook Express)", "ACCESSTYPE enumeration Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- ACCESSTYPE
api_location:
- Mimeole.h
api_type:
- HeaderDef
---

# IMSGBODYTYPE enumeration

Do not use. Indicates message body types for verification.

## Syntax


```C++
typedef enum tagIMSGBODYTYPE { 
  IBT_SECURE      = 0,
  IBT_ATTACHMENT  = 1,
  IBT_EMPTY       = 2,
  IBT_CSETTAGGED  = 3,
  IBT_AUTOATTACH  = 4
} ACCESSTYPE;
```



## Constants

<dl> <dt>

<span id="IBT_SECURE"></span><span id="ibt_secure"></span>**IBT\_SECURE**
</dt> <dd>

Verify that the body is secure.

</dd> <dt>

<span id="IBT_ATTACHMENT"></span><span id="ibt_attachment"></span>**IBT\_ATTACHMENT**
</dt> <dd>

Verify that the body is considered an attachment by MimeOLE.

</dd> <dt>

<span id="IBT_EMPTY"></span><span id="ibt_empty"></span>**IBT\_EMPTY**
</dt> <dd>

Verify that the body is empty.

</dd> <dt>

<span id="IBT_CSETTAGGED"></span><span id="ibt_csettagged"></span>**IBT\_CSETTAGGED**
</dt> <dd>

Verify that the body is tagged with a character set.

</dd> <dt>

<span id="IBT_AUTOATTACH"></span><span id="ibt_autoattach"></span>**IBT\_AUTOATTACH**
</dt> <dd>

Verify that the body was marked as an attachment by MimeOLE.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| Product<br/>                  | Outlook Express 6.0<br/>                                                         |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl> |



 

 





