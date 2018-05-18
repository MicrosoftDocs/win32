---
title: BODYLOCATION enumeration
description: Do not use. Specifies the location of a message body in an IMimeMessageTree object.
ms.assetid: '139e5315-d9b7-409f-bc3a-0270e5e37b83'
keywords: ["BODYLOCATION enumeration Windows Mail (formerly Outlook Express)", "ACCESSTYPE enumeration Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- ACCESSTYPE
api_location:
- Mimeole.h
api_type:
- HeaderDef
---

# BODYLOCATION enumeration

Do not use. Specifies the location of a message body in an [**IMimeMessageTree**](oe-imimemessagetree.md) object.

## Syntax


```C++
typedef enum tagBODYLOCATION { 
  IBL_ROOT      = 0,
  IBL_PARENT    = 1,
  IBL_FIRST     = 2,
  IBL_LAST      = 3,
  IBL_NEXT      = 4,
  IBL_PREVIOUS  = 5
} ACCESSTYPE;
```



## Constants

<dl> <dt>

<span id="IBL_ROOT"></span><span id="ibl_root"></span>**IBL\_ROOT**
</dt> <dd>

Indicates the root body of the message.

</dd> <dt>

<span id="IBL_PARENT"></span><span id="ibl_parent"></span>**IBL\_PARENT**
</dt> <dd>

Indicates the parent of the message body.

</dd> <dt>

<span id="IBL_FIRST"></span><span id="ibl_first"></span>**IBL\_FIRST**
</dt> <dd>

Indicates the first child of the message body.

</dd> <dt>

<span id="IBL_LAST"></span><span id="ibl_last"></span>**IBL\_LAST**
</dt> <dd>

Indicates the last child of the message body.

</dd> <dt>

<span id="IBL_NEXT"></span><span id="ibl_next"></span>**IBL\_NEXT**
</dt> <dd>

Indicates the next sibling of the message body.

</dd> <dt>

<span id="IBL_PREVIOUS"></span><span id="ibl_previous"></span>**IBL\_PREVIOUS**
</dt> <dd>

Indicates that previous sibling of the message body.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| Product<br/>                  | Outlook Express 6.0<br/>                                                         |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl> |



 

 





