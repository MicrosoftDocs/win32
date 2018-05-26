---
title: POP3RETR structure
description: Contains the response data from the RETR command.
ms.assetid: 84c1d9ee-3b96-4d06-8dcd-6f0d05483ac9
keywords:
- POP3RETR structure Windows Mail (formerly Outlook Express)
- LPPOP3RETR structure pointer Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- POP3RETR
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

# POP3RETR structure

\[**POP3RETR** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Contains the response data from the RETR command.

## Syntax


```C++
typedef struct tagPOP3RETR {
  BOOL  fHeader;
  BOOL  fBody;
  DWORD dwPopId;
  DWORD cbSoFar;
  LPSTR pszLines;
  ULONG cbLines;
} POP3RETR, *LPPOP3RETR;
```



## Members

<dl> <dt>

**fHeader**
</dt> <dd>

Type: **BOOL**

</dd> <dd>

Contains a **BOOL** that indicates whether the full header has been downloaded.

</dd> <dt>

**fBody**
</dt> <dd>

Type: **BOOL**

</dd> <dd>

Contains a **BOOL** that indicates whether the body has been downloaded.

</dd> <dt>

**dwPopId**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains a **DWORD** that holds the message ID.

</dd> <dt>

**cbSoFar**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains a **DWORD** that holds the number of bytes downloaded since start of download.

</dd> <dt>

**pszLines**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains an **LPSTR** that holds the message lines. Do not free this pointer.

</dd> <dt>

**cbLines**
</dt> <dd>

Type: **ULONG**

</dd> <dd>

Contains a **ULONG** that holds the number of bytes in **pszLines**.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





