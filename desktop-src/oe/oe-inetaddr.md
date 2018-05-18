---
title: INETADDR structure
description: Contains a single Internet address.
ms.assetid: '28e5f4d5-5a2f-482b-bce8-a3ff12e9e894'
keywords: ["INETADDR structure Windows Mail (formerly Outlook Express)", "LPINETADDR structure pointer Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- INETADDR
api_location:
- Imnxport.h
api_type:
- HeaderDef
---

# INETADDR structure

\[**INETADDR** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Contains a single Internet address.

## Syntax


```C++
typedef struct tagINETADDR {
  INETADDRTYPE addrtype;
  CHAR         szEmail[CCHMAX_EMAIL_ADDRESS];
} INETADDR, *LPINETADDR;
```



## Members

<dl> <dt>

**addrtype**
</dt> <dd>

Type: **[**INETADDRTYPE**](oe-inetaddrtype.md)**

</dd> <dd>

Contains an [**INETADDRTYPE**](oe-inetaddrtype.md) value that indicates whether the address is of the sender or recipient.

</dd> <dt>

**szEmail**
</dt> <dd>

Type: **CHAR\[CCHMAX\_EMAIL\_ADDRESS\]**

</dd> <dd>

Contains the email address.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





