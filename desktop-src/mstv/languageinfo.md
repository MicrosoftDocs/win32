---
title: LanguageInfo structure
description: Specifies the language for an MPEG-2 audio stream.
ms.assetid: 25c936a7-b4d6-4af9-a8cc-7af5aed5b23e
keywords:
- LanguageInfo structure Microsoft TV Technologies
topic_type:
- apiref
api_name:
- LanguageInfo
api_location:
- bdamedia.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# LanguageInfo structure

Specifies the language for an MPEG-2 audio stream.

## Syntax


```C++
typedef struct _LanguageInfo {
  LANGID LangID;
  LONG   lISOLangCode;
} LanguageInfo;
```



## Members

<dl> <dt>

**LangID**
</dt> <dd>

A locale identifier (LCID) that specifies the language.

</dd> <dt>

**lISOLangCode**
</dt> <dd>

The ISO 639 language code for the language.

</dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Bdamedia.h</dt> </dl> |



 

 





