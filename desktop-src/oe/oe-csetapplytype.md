---
title: CSETAPPLYTYPE enumeration
description: Do not use. Indicates how a character set is to be applied to an object.
ms.assetid: 95413e20-ea94-442c-a430-4f16b43f0c9e
keywords:
- CSETAPPLYTYPE enumeration Windows Mail (formerly Outlook Express)
- ACCESSTYPE enumeration Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- ACCESSTYPE
api_location:
- Mimeole.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CSETAPPLYTYPE enumeration

Do not use. Indicates how a character set is to be applied to an object.

## Syntax


```C++
typedef enum tagCSETAPPLYTYPE { 
  CSET_APPLY_UNTAGGED  = 0,
  CSET_APPLY_ALL       = 1,
  CSET_APPLY_TAG_ALL   = 2
} ACCESSTYPE;
```



## Constants

<dl> <dt>

<span id="CSET_APPLY_UNTAGGED"></span><span id="cset_apply_untagged"></span>**CSET\_APPLY\_UNTAGGED**
</dt> <dd>

Apply the character set to all entities that have an unknown character set.

</dd> <dt>

<span id="CSET_APPLY_ALL"></span><span id="cset_apply_all"></span>**CSET\_APPLY\_ALL**
</dt> <dd>

Apply the character set to all entities and override any existing tagging.

</dd> <dt>

<span id="CSET_APPLY_TAG_ALL"></span><span id="cset_apply_tag_all"></span>**CSET\_APPLY\_TAG\_ALL**
</dt> <dd>

Do not use.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| Product<br/>                  | Outlook Express 6.0<br/>                                                         |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl> |



 

 





