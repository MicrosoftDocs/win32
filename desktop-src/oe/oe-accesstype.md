---
title: ACCESSTYPE enumeration
description: Do not use. Flags for specifying the type of access needed when accessing a stream.
ms.assetid: f6950765-c1f4-429b-a6e1-f07b54f7c7c9
keywords:
- ACCESSTYPE enumeration Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- ACCESSTYPE
api_location:
- Directdb.idl
api_type:
- IDLDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# ACCESSTYPE enumeration

Do not use. Flags for specifying the type of access needed when accessing a stream.

## Syntax


```C++
typedef enum  { 
  ACCESS_READ   = 100,
  ACCESS_WRITE  = 200
} ACCESSTYPE;
```



## Constants

<dl> <dt>

<span id="ACCESS_READ"></span><span id="access_read"></span>**ACCESS\_READ**
</dt> <dd>

Database access permission is read access.

</dd> <dt>

<span id="ACCESS_WRITE"></span><span id="access_write"></span>**ACCESS\_WRITE**
</dt> <dd>

Database access permission is write access.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| IDL<br/>                      | <dl> <dt>Directdb.idl</dt> </dl> |



 

 





