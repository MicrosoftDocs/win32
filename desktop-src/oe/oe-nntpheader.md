---
title: NNTPHEADER structure
description: This structure contains the parsed information for a single header returned from the GetHeaders command.
ms.assetid: bcecfea2-8b0b-4b92-a2f6-9acf12461a3b
keywords:
- NNTPHEADER structure Windows Mail (formerly Outlook Express)
- LPNNTPHEADER structure pointer Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- NNTPHEADER
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

# NNTPHEADER structure

\[**NNTPHEADER** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

This structure contains the parsed information for a single header returned from the [**GetHeaders**](oe-inntptransport-getheaders.md) command. An array of these headers is contained in the [**NNTPHEADERRESP**](oe-nntpheaderresp.md) struct.

## Syntax


```C++
typedef struct tagNNTPHEADER {
  DWORD dwArticleNum;
  LPSTR pszSubject;
  LPSTR pszFrom;
  LPSTR pszDate;
  LPSTR pszMessageId;
  LPSTR pszReferences;
  DWORD dwBytes;
  DWORD dwLines;
  LPSTR pszXref;
} NNTPHEADER, *LPNNTPHEADER;
```



## Members

<dl> <dt>

**dwArticleNum**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Article number

</dd> <dt>

**pszSubject**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Article subject

</dd> <dt>

**pszFrom**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Who the article is from

</dd> <dt>

**pszDate**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Date the article was posted

</dd> <dt>

**pszMessageId**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Message id

</dd> <dt>

**pszReferences**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

References

</dd> <dt>

**dwBytes**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Size of the message in bytes (might not be filled in)

</dd> <dt>

**dwLines**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Size of the message in lines

</dd> <dt>

**pszXref**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

XREF: header for cross post managment

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





