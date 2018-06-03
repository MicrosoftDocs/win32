---
title: HTTPMEMBERERROR structure
description: Contains the error response information.
ms.assetid: 0aee66ee-f033-4313-b970-30dfbbfd35eb
keywords:
- HTTPMEMBERERROR structure Windows Mail (formerly Outlook Express)
- LPHTTPMEMBERERROR structure pointer Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- HTTPMEMBERERROR
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

# HTTPMEMBERERROR structure

\[**HTTPMEMBERERROR** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Contains the error response information.

## Syntax


```C++
typedef struct tagHTTPMEMBERERROR {
  LPSTR   pszHref;
  HRESULT hrResult;
} HTTPMEMBERERROR, *LPHTTPMEMBERERROR;
```



## Members

<dl> <dt>

**pszHref**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains an **LPSTR** that contains the URL to the resource being reported.

</dd> <dt>

**hrResult**
</dt> <dd>

Type: **HRESULT**

</dd> <dd>

Contains an **HRESULT** that contains the error information.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





