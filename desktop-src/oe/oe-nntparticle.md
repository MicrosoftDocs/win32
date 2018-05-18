---
title: NNTPARTICLE structure
description: This structure returns the data from a CommandARTICLE function.
ms.assetid: 'a3daf3bd-5dba-4d3b-bb74-5b3a3cf22f21'
keywords: ["NNTPARTICLE structure Windows Mail (formerly Outlook Express)", "LPNNTPARTICLE structure pointer Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- NNTPARTICLE
api_location:
- Imnxport.h
api_type:
- HeaderDef
---

# NNTPARTICLE structure

\[**NNTPARTICLE** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

This structure returns the data from a [**CommandARTICLE**](oe-inntptransport-commandarticle.md) function. Depending on the size of the article being retrieved, the callback may recieve multiple calls for a single article.

## Syntax


```C++
typedef struct tagNNTPARTICLE {
  DWORD dwArticleNum;
  LPSTR pszMessageId;
  LPSTR pszLines;
  ULONG cbLines;
  ULONG cLines;
  DWORD dwReserved;
} NNTPARTICLE, *LPNNTPARTICLE;
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

</dd> <dt>

**pszLines**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Lines of the message

</dd> <dt>

**cbLines**
</dt> <dd>

Type: **ULONG**

</dd> <dd>

Number of bytes in **pszLines**

</dd> <dt>

**cLines**
</dt> <dd>

Type: **ULONG**

</dd> <dd>

Number of lines in **pszLines**

</dd> <dt>

**dwReserved**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Reserved for system use

</dd> </dl>

## Remarks

When fDone is **TRUE**, then all of the article data has been retrieved. **pszLines** is not accumulated over all of the callbacks, it is the client's responsibility to assemble all of the pszLines that are returned to build the message.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





