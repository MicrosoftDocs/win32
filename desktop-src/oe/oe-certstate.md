---
title: CERTSTATE enumeration
description: Do not use. Defines the state of a certificate in secure messaging.
ms.assetid: 71b8ab6a-1f62-4829-abcb-2542a53fec61
keywords:
- CERTSTATE enumeration Windows Mail (formerly Outlook Express)
- ACCESSTYPE enumeration Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- ACCESSTYPE
api_location:
- Mimeole.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# CERTSTATE enumeration

Do not use. Defines the state of a certificate in secure messaging.

## Syntax


```C++
typedef enum tagCERTSTATE { 
  CERTIFICATE_OK              = 0,
  CERTIFICATE_NOT_PRESENT     = 1,
  CERTIFICATE_EXPIRED         = 2,
  CERTIFICATE_CHAIN_TOO_LONG  = 3,
  CERTIFICATE_MISSING_ISSUER  = 4,
  CERTIFICATE_CRL_LISTED      = 5,
  CERTIFICATE_NOT_TRUSTED     = 6,
  CERTIFICATE_INVALID         = 7,
  CERTIFICATE_ERROR           = 8,
  CERTIFICATE_NOPRINT         = 9,
  CERTIFICATE_UNKNOWN         = 10
} ACCESSTYPE;
```



## Constants

<dl> <dt>

<span id="CERTIFICATE_OK"></span><span id="certificate_ok"></span>**CERTIFICATE\_OK**
</dt> <dd>

Indicates that the certificate has no errors.

</dd> <dt>

<span id="CERTIFICATE_NOT_PRESENT"></span><span id="certificate_not_present"></span>**CERTIFICATE\_NOT\_PRESENT**
</dt> <dd>

Indicates that no certificate is present.

</dd> <dt>

<span id="CERTIFICATE_EXPIRED"></span><span id="certificate_expired"></span>**CERTIFICATE\_EXPIRED**
</dt> <dd>

Indicates that the certificate has expired.

</dd> <dt>

<span id="CERTIFICATE_CHAIN_TOO_LONG"></span><span id="certificate_chain_too_long"></span>**CERTIFICATE\_CHAIN\_TOO\_LONG**
</dt> <dd>

Indicates that the certificate trust chain is too long.

</dd> <dt>

<span id="CERTIFICATE_MISSING_ISSUER"></span><span id="certificate_missing_issuer"></span>**CERTIFICATE\_MISSING\_ISSUER**
</dt> <dd>

Indicates that the certificate is missing an issuer.

</dd> <dt>

<span id="CERTIFICATE_CRL_LISTED"></span><span id="certificate_crl_listed"></span>**CERTIFICATE\_CRL\_LISTED**
</dt> <dd>

Indicates that the CRL of the certificate is listed.

</dd> <dt>

<span id="CERTIFICATE_NOT_TRUSTED"></span><span id="certificate_not_trusted"></span>**CERTIFICATE\_NOT\_TRUSTED**
</dt> <dd>

Indicates that the certificate is not trusted.

</dd> <dt>

<span id="CERTIFICATE_INVALID"></span><span id="certificate_invalid"></span>**CERTIFICATE\_INVALID**
</dt> <dd>

Indicates that the certificate is invalid.

</dd> <dt>

<span id="CERTIFICATE_ERROR"></span><span id="certificate_error"></span>**CERTIFICATE\_ERROR**
</dt> <dd>

Indicates that the certificate has an error.

</dd> <dt>

<span id="CERTIFICATE_NOPRINT"></span><span id="certificate_noprint"></span>**CERTIFICATE\_NOPRINT**
</dt> <dd>

Indicates that the certificate cannot be printed.

</dd> <dt>

<span id="CERTIFICATE_UNKNOWN"></span><span id="certificate_unknown"></span>**CERTIFICATE\_UNKNOWN**
</dt> <dd>

Indicates that the state of the certificate is unknown.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| Product<br/>                  | Outlook Express 6.0<br/>                                                         |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl> |



 

 





