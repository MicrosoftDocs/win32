---
title: RANGE structure
description: The range structure allows the caller to provide arguments for commands that allow a range of headers to be retrieved.
ms.assetid: 90f5cc1e-05e5-4b15-985f-af15e8c112e6
keywords:
- RANGE structure Windows Mail (formerly Outlook Express)
- LPRANGE structure pointer Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- RANGE
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

# RANGE structure

\[**RANGE** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

The range structure allows the caller to provide arguments for commands that allow a range of headers to be retrieved. The range structure can be used to specify a single number (ie XOVER 2010), or bounded range (ie XOVER 2000-2010) to request all of the headers within that range \[inclusive\]. Use the idType field to specify which range you are requesting.

## Syntax


```C++
typedef struct tagRANGE {
  RANGETYPE idType;
  DWORD     dwFirst;
  DWORD     dwLast;
} RANGE, *LPRANGE;
```



## Members

<dl> <dt>

**idType**
</dt> <dd>

Type: **[**RANGETYPE**](oe-rangetype.md)**

</dd> <dd></dd> <dt>

**dwFirst**
</dt> <dd>

Type: **DWORD**

</dd> <dd></dd> <dt>

**dwLast**
</dt> <dd>

Type: **DWORD**

</dd> <dd></dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





