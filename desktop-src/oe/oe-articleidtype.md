---
title: ARTICLEIDTYPE enumeration
description: Defined as part of INNTPTransport.
ms.assetid: 38684d7d-b4ac-48eb-b4ba-c10028ca0120
keywords:
- ARTICLEIDTYPE enumeration Windows Mail (formerly Outlook Express)
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

# ARTICLEIDTYPE enumeration

\[**ARTICLEIDTYPE** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Defined as part of [**INNTPTransport**](oe-inntptransport.md).

## Syntax


```C++
typedef enum tagARTICLEIDTYPE { 
  AID_MSGID       = 0,
  AID_ARTICLENUM  = 1
} ACCESSTYPE;
```



## Constants

<dl> <dt>

<span id="AID_MSGID"></span><span id="aid_msgid"></span>**AID\_MSGID**
</dt> <dd></dd> <dt>

<span id="AID_ARTICLENUM"></span><span id="aid_articlenum"></span>**AID\_ARTICLENUM**
</dt> <dd></dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





