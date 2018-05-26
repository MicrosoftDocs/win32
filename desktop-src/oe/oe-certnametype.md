---
title: CERTNAMETYPE enumeration
description: Do not use. Specifies the returned string type. Each value maps to an equivalent value for the dwStrType parameter of the CertNameToStr function.
ms.assetid: 2d374d7d-5a1e-4f8e-88d3-2c588a8b1e0d
keywords:
- CERTNAMETYPE enumeration Windows Mail (formerly Outlook Express)
- ACCESSTYPE enumeration Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- ACCESSTYPE
api_location:
- Mimeole.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CERTNAMETYPE enumeration

Do not use. Specifies the returned string type. Each value maps to an equivalent value for the *dwStrType* parameter of the [CertNameToStr](http://msdn.microsoft.com/library/seccrypto/security/certnametostr.asp) function.

## Syntax


```C++
typedef enum tagCERTNAMETYPE { 
  SIMPLE  = 0,
  OID     = 1,
  X500    = 2
} ACCESSTYPE;
```



## Constants

<dl> <dt>

<span id="SIMPLE"></span><span id="simple"></span>**SIMPLE**
</dt> <dd>

Equivalent to CERT\_SIMPLE\_NAME\_STR.

</dd> <dt>

<span id="OID"></span><span id="oid"></span>**OID**
</dt> <dd>

Equivalent to CERT\_OID\_NAME\_STR.

</dd> <dt>

<span id="X500"></span><span id="x500"></span>**X500**
</dt> <dd>

Equivalent to CERT\_X500\_NAME\_STR.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| Product<br/>                  | Outlook Express 6.0<br/>                                                         |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl> |



 

 





