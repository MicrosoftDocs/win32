---
title: NNTPXHDR structure
description: An array of these structures will be returned in the NNTPXHDRRESP structure.
ms.assetid: e8f72fd5-5f9e-4b12-911b-9a179ad0ff5e
keywords:
- NNTPXHDR structure Windows Mail (formerly Outlook Express)
- LPNNTPXHDR structure pointer Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- NNTPXHDR
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

# NNTPXHDR structure

\[**NNTPXHDR** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

An array of these structures will be returned in the [**NNTPXHDRRESP**](oe-nntpxhdrresp.md) structure.

## Syntax


```C++
typedef struct tagNNTPXHDR {
  DWORD dwArticleNum;
  LPSTR pszHeader;
} NNTPXHDR, *LPNNTPXHDR;
```



## Members

<dl> <dt>

**dwArticleNum**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Article number this header is for

</dd> <dt>

**pszHeader**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Requested article header for this article

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





