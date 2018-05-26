---
title: NNTPNEXT structure
description: This structure will be used for the response from CommandNEXT, CommandLAST, and CommandSTAT.
ms.assetid: 9fa6f68d-5270-4de6-a474-c8538c4c255e
keywords:
- NNTPNEXT structure Windows Mail (formerly Outlook Express)
- LPNNTPNEXT structure pointer Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- NNTPNEXT
api_location:
- Imnxport.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# NNTPNEXT structure

\[**NNTPNEXT** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

This structure will be used for the response from [**CommandNEXT**](oe-inntptransport-commandnext.md), [**CommandLAST**](oe-inntptransport-commandlast.md), and [**CommandSTAT**](oe-inntptransport-commandstat.md). The data returned is the article number and message id for the article that is selected by the command that was issued.

## Syntax


```C++
typedef struct tagNNTPNEXT {
  DWORD dwArticleNum;
  LPSTR pszMessageId;
} NNTPNEXT, *LPNNTPNEXT;
```



## Members

<dl> <dt>

**dwArticleNum**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Article number

</dd> <dt>

**pszMessageId**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Message ID

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





