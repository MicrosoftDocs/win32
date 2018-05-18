---
title: INETADDRLIST structure
description: Contains an Internet address list.
ms.assetid: '5d8b7245-d307-402a-a940-ad6a1ad25bad'
keywords: ["INETADDRLIST structure Windows Mail (formerly Outlook Express)", "LPINETADDRLIST structure pointer Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- INETADDRLIST
api_location:
- Imnxport.h
api_type:
- HeaderDef
---

# INETADDRLIST structure

\[**INETADDRLIST** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Contains an Internet address list.

## Syntax


```C++
typedef struct tagINETADDRLIST {
  ULONG      cAddress;
  LPINETADDR prgAddress;
} INETADDRLIST, *LPINETADDRLIST;
```



## Members

<dl> <dt>

**cAddress**
</dt> <dd>

Type: **ULONG**

</dd> <dd>

Contains a **ULONG** that contains the number of elements in **prgAddress**.

</dd> <dt>

**prgAddress**
</dt> <dd>

Type: **LPINETADDR**

</dd> <dd>

Contains a pointer to an array of [**INETADDR**](oe-inetaddr.md) structures.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





