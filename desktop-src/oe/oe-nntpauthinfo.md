---
title: NNTPAUTHINFO structure
description: This structure is used to specify the type of authentication to use in the CommandAUTHINFO command.
ms.assetid: c6d591d1-bb73-4ae1-9055-a3fd4d9a28e4
keywords:
- NNTPAUTHINFO structure Windows Mail (formerly Outlook Express)
- LPNNTPAUTHINFO structure pointer Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- NNTPAUTHINFO
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

# NNTPAUTHINFO structure

\[**NNTPAUTHINFO** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

This structure is used to specify the type of authentication to use in the [**CommandAUTHINFO**](oe-inntptransport-commandauthinfo.md) command. For **AUTHTYPE\_USERPASS** and **AUTHTYPE\_SIMPLE**, **pszUser** and **pszPass** are the user name and password to send with the command.

## Syntax


```C++
typedef struct tagNNTPAUTHINFO {
  AUTHTYPE authtype;
  LPSTR    pszUser;
  LPSTR    pszPass;
} NNTPAUTHINFO, *LPNNTPAUTHINFO;
```



## Members

<dl> <dt>

**authtype**
</dt> <dd>

Type: **[**AUTHTYPE**](oe-authtype.md)**

</dd> <dd></dd> <dt>

**pszUser**
</dt> <dd>

Type: **LPSTR**

</dd> <dd></dd> <dt>

**pszPass**
</dt> <dd>

Type: **LPSTR**

</dd> <dd></dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





