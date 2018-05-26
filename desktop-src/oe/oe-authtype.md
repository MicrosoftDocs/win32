---
title: AUTHTYPE enumeration
description: Defined as part of INNTPTransport.
ms.assetid: 43b8b6aa-a915-40dd-9e27-3e2192ae3a20
keywords:
- AUTHTYPE enumeration Windows Mail (formerly Outlook Express)
- ACCESSTYPE enumeration Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- ACCESSTYPE
api_location:
- Imnxport.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# AUTHTYPE enumeration

\[**AUTHTYPE** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Defined as part of [**INNTPTransport**](oe-inntptransport.md).

## Syntax


```C++
typedef enum tagAUTHTYPE { 
  AUTHTYPE_USERPASS,
  AUTHTYPE_SIMPLE,
  AUTHTYPE_SASL
} ACCESSTYPE;
```



## Constants

<dl> <dt>

<span id="AUTHTYPE_USERPASS"></span><span id="authtype_userpass"></span>**AUTHTYPE\_USERPASS**
</dt> <dd></dd> <dt>

<span id="AUTHTYPE_SIMPLE"></span><span id="authtype_simple"></span>**AUTHTYPE\_SIMPLE**
</dt> <dd></dd> <dt>

<span id="AUTHTYPE_SASL"></span><span id="authtype_sasl"></span>**AUTHTYPE\_SASL**
</dt> <dd></dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





