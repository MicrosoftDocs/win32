---
title: ARTICLEID structure
description: This structure is used to specify an article id to the various NNTP commands that require one (i.e. ARTICLE, BODY, STAT).
ms.assetid: a2d53348-41be-4c89-bbe9-ee5ef3ad960f
keywords:
- ARTICLEID structure Windows Mail (formerly Outlook Express)
- LPARTICLEID structure pointer Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- ARTICLEID
api_location:
- Imnxport.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# ARTICLEID structure

\[**ARTICLEID** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

This structure is used to specify an article id to the various NNTP commands that require one (i.e. ARTICLE, BODY, STAT). These commands accept either a message-id or if the user is current in a the context of a newsgroup the article number within that group.

## Syntax


```C++
typedef struct ARTICLEID {
  ARTICLEIDTYPE idType;
} ARTICLEID, *LPARTICLEID;
```



## Members

<dl> <dt>

**idType**
</dt> <dd>

Type: **[**ARTICLEIDTYPE**](oe-articleidtype.md)**

</dd> <dd></dd> </dl>

## Remarks

When filling in this structure the user should set idType to either AID\_MSGID if pszMessageId is valid, or AID\_ARTICLENUM if dwArticleNum.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





