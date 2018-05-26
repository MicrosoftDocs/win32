---
title: MIMEPARAMINFO structure
description: Do not use. Holds the name and value of a MIME parameter.
ms.assetid: 155ce438-b138-4f0e-aef4-e0247dc9db2d
keywords:
- MIMEPARAMINFO structure Windows Mail (formerly Outlook Express)
- LPMIMEPARAMINFO structure pointer Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- MIMEPARAMINFO
api_location:
- Mimeole.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MIMEPARAMINFO structure

Do not use. Holds the name and value of a MIME parameter.

## Syntax


```C++
typedef struct tagMIMEPARAMINFO {
  LPSTR pszName;
  LPSTR pszData;
} MIMEPARAMINFO, *LPMIMEPARAMINFO;
```



## Members

<dl> <dt>

**pszName**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains the parameter name.

</dd> <dt>

**pszData**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains the parameter value.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| Product<br/>                  | Outlook Express 6.0<br/>                                                         |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl> |



 

 





