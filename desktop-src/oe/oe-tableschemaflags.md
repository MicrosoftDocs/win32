---
title: TABLESCHEMAFLAGS enumeration
description: Do not use.
ms.assetid: 8f909874-9c35-4aa2-b245-f0c86565966b
keywords:
- TABLESCHEMAFLAGS enumeration Windows Mail (formerly Outlook Express)
- ACCESSTYPE enumeration Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- ACCESSTYPE
api_location:
- Directdb.idl
api_type:
- IDLDef
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# TABLESCHEMAFLAGS enumeration

Do not use.

## Syntax


```C++
typedef enum  { 
  TSF_RESETIFBADVERSION  = 0x00000001,
  TSF_HASSTREAMS         = 0x00000002
} ACCESSTYPE;
```



## Constants

<dl> <dt>

<span id="TSF_RESETIFBADVERSION"></span><span id="tsf_resetifbadversion"></span>**TSF\_RESETIFBADVERSION**
</dt> <dd>

Resets the database header if there is a file version mismatch.

</dd> <dt>

<span id="TSF_HASSTREAMS"></span><span id="tsf_hasstreams"></span>**TSF\_HASSTREAMS**
</dt> <dd>

The table has stream values.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| IDL<br/>                      | <dl> <dt>Directdb.idl</dt> </dl> |



 

 





