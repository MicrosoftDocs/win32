---
title: HTTPMAILBCOPYMOVE structure
description: Contains the response information for the CommandBCOPY and CommandBMOVE methods.
ms.assetid: 532b2bdd-c1ed-4359-8f00-37036383f2ad
keywords:
- HTTPMAILBCOPYMOVE structure Windows Mail (formerly Outlook Express)
- LPHTTPMAILBCOPYMOVE structure pointer Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- HTTPMAILBCOPYMOVE
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

# HTTPMAILBCOPYMOVE structure

\[**HTTPMAILBCOPYMOVE** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Contains the response information for the [**CommandBCOPY**](oe-ihttpmailtransport-commandbcopy.md) and [**CommandBMOVE**](oe-ihttpmailtransport-commandbmove.md) methods.

## Syntax


```C++
typedef struct tagHTTPMAILBCOPYMOVE {
  LPSTR   pszHref;
  LPSTR   pszLocation;
  HRESULT hrResult;
} HTTPMAILBCOPYMOVE, *LPHTTPMAILBCOPYMOVE;
```



## Members

<dl> <dt>

**pszHref**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains an **LPCSTR** that contains the URL to the collection resource that contains the target resources.

</dd> <dt>

**pszLocation**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains an **LPCSTR** that contains the URL to the collection resource that contains the destination resources.

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



 

 





