---
title: RASCONNTYPE enumeration
description: RAS connection type.
ms.assetid: '81350d25-5c00-4311-8e53-c0d5434cca34'
keywords: ["RASCONNTYPE enumeration Windows Mail (formerly Outlook Express)", "ACCESSTYPE enumeration Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- ACCESSTYPE
api_location:
- Imnxport.h
api_type:
- HeaderDef
---

# RASCONNTYPE enumeration

\[**RASCONNTYPE** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

RAS connection type.

## Syntax


```C++
typedef enum tagRASCONNTYPE { 
  RAS_CONNECT_LAN     = 0,
  RAS_CONNECT_MANUAL  = 1,
  RAS_CONNECT_RAS     = 2
} ACCESSTYPE;
```



## Constants

<dl> <dt>

<span id="RAS_CONNECT_LAN"></span><span id="ras_connect_lan"></span>**RAS\_CONNECT\_LAN**
</dt> <dd></dd> <dt>

<span id="RAS_CONNECT_MANUAL"></span><span id="ras_connect_manual"></span>**RAS\_CONNECT\_MANUAL**
</dt> <dd></dd> <dt>

<span id="RAS_CONNECT_RAS"></span><span id="ras_connect_ras"></span>**RAS\_CONNECT\_RAS**
</dt> <dd></dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





