---
title: X509CERTRESULT structure
description: Do not use. Enumerates certificates and their associated states.
ms.assetid: 93aee766-a9c2-4bc4-b599-73c22e9b0ba5
keywords:
- X509CERTRESULT structure Windows Mail (formerly Outlook Express)
- PX509CERTRESULT structure pointer Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- X509CERTRESULT
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

# X509CERTRESULT structure

Do not use. Enumerates certificates and their associated states.

## Syntax


```C++
typedef struct tagX509CERTRESULT {
  DWORD      cEntries;
  CERTSTATE  *rgcs;
  PCX509CERT *rgpCert;
} X509CERTRESULT, *PX509CERTRESULT;
```



## Members

<dl> <dt>

**cEntries**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains the size of the **rgpCert** array. The **rgcs** is the same size.

</dd> <dt>

**rgcs**
</dt> <dd>

Type: **[**CERTSTATE**](oe-certstate.md)\***

</dd> <dd>

Contains a pointer to an array of [**CERTSTATE**](oe-certstate.md) values.

</dd> <dt>

**rgpCert**
</dt> <dd>

Type: **PCX509CERT\***

</dd> <dd>

Contains a pointer to an array of pointers to [CERT\_CONTEXT](http://msdn.microsoft.com/library/seccrypto/security/cert_context.asp) certificate stores.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| Product<br/>                  | Outlook Express 6.0<br/>                                                         |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl> |



 

 





