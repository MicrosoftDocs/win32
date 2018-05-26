---
title: POP3TOP structure
description: Contains the response data from the TOP command.
ms.assetid: 507ccfeb-28ec-4ddf-a185-5107abc6b889
keywords:
- POP3TOP structure Windows Mail (formerly Outlook Express)
- LPPOP3TOP structure pointer Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- POP3TOP
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

# POP3TOP structure

\[**POP3TOP** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Contains the response data from the TOP command.

## Syntax


```C++
typedef struct tagPOP3TOP {
  BOOL  fHeader;
  BOOL  fBody;
  DWORD dwPopId;
  DWORD cPreviewLines;
  DWORD cbSoFar;
  LPSTR pszLines;
  ULONG cbLines;
} POP3TOP, *LPPOP3TOP;
```



## Members

<dl> <dt>

**fHeader**
</dt> <dd>

Type: **BOOL**

</dd> <dd>

Contains a **BOOL** that indicates whether the header has been downloaded.

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

**cPreviewLines**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains a **DWORD** that holds the number of lines to be previewed.

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

Contains an **LPSTR** that holds the header and body lines.

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



 

 





