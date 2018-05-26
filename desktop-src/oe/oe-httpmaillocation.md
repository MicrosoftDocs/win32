---
title: HTTPMAILLOCATION structure
description: Contains the response information for the CommandCOPY, CommandMOVE, and CommandMKCOL methods.
ms.assetid: 941c816f-ad40-4f42-8d86-120107a6ca75
keywords:
- HTTPMAILLOCATION structure Windows Mail (formerly Outlook Express)
- LPHTTPMAILLOCATION structure pointer Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- HTTPMAILLOCATION
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

# HTTPMAILLOCATION structure

\[**HTTPMAILLOCATION** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Contains the response information for the [**CommandCOPY**](oe-ihttpmailtransport-commandcopy.md), [**CommandMOVE**](oe-ihttpmailtransport-commandmove.md), and [**CommandMKCOL**](oe-ihttpmailtransport-commandmkcol.md) methods.

## Syntax


```C++
typedef struct tagHTTPMAILLOCATION {
  LPSTR pszLocation;
} HTTPMAILLOCATION, *LPHTTPMAILLOCATION;
```



## Members

<dl> <dt>

**pszLocation**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains an **LPSTR** that contains the location of the new or moved resource on the server.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





