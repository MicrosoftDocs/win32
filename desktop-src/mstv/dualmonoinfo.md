---
title: DualMonoInfo structure
description: Specifies the languages for an MPEG-2 dual-mono audio stream.
ms.assetid: dd3b702b-1017-4963-91ba-516a3bbb3b60
keywords:
- DualMonoInfo structure Microsoft TV Technologies
topic_type:
- apiref
api_name:
- DualMonoInfo
api_location:
- bdamedia.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# DualMonoInfo structure

Specifies the languages for an MPEG-2 dual-mono audio stream.

## Syntax


```C++
typedef struct _DualMonoInfo {
  LANGID LangID1;
  LANGID LangID2;
  LONG   lISOLangCode1;
  LONG   lISOLangCode2;
} DualMonoInfo;
```



## Members

<dl> <dt>

**LangID1**
</dt> <dd>

A locale identifier (LCID) that specifies the first language.

</dd> <dt>

**LangID2**
</dt> <dd>

An LCID that specifies the second language.

</dd> <dt>

**lISOLangCode1**
</dt> <dd>

The ISO 639 language code for the first language.

</dd> <dt>

**lISOLangCode2**
</dt> <dd>

The ISO 639 language code for the second language.

</dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Bdamedia.h</dt> </dl> |



 

 





