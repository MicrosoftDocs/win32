---
title: ADDRESSPROPS structure
description: Do not use. Holds information about a message sender or recipient \ 8212;for example, a message address.
ms.assetid: 7e52cbfe-ee24-405c-acd4-bfbb21477550
keywords:
- ADDRESSPROPS structure Windows Mail (formerly Outlook Express)
- LPADDRESSPROPS structure pointer Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- ADDRESSPROPS
api_location:
- Mimeole.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# ADDRESSPROPS structure

Do not use. Holds information about a message sender or recipient for example, a message address.

## Syntax


```C++
typedef struct tagADDRESSPROPS {
  DWORD        dwProps;
  HADDRESS     hAddress;
  ENCODINGTYPE ietFriendly;
  HCHARSET     hCharset;
  DWORD        dwAdrType;
  LPSTR        pszFriendly;
  LPWSTR       pszFriendlyW;
  LPSTR        pszEmail;
  CERTSTATE    certstate;
  THUMBBLOB    tbSigning;
  THUMBBLOB    tbEncryption;
  DWORD        dwCookie;
  DWORD        dwReserved1;
  DWORD        dwReserved2;
} ADDRESSPROPS, *LPADDRESSPROPS;
```



## Members

<dl> <dt>

**dwProps**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains a bitmask that indicates the valid fields in this structure.



| Value                                                                                                                                                                                                                                               | Meaning                                                                |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| <span id="IAP_CHARSET"></span><span id="iap_charset"></span><dl> <dt>**IAP\_CHARSET**</dt> <dt>0x00000001</dt> </dl>                             | Indicates that **hCharset** is valid. <br/>                      |
| <span id="IAP_HANDLE"></span><span id="iap_handle"></span><dl> <dt>**IAP\_HANDLE**</dt> <dt>0x00000002</dt> </dl>                                | Indicates that **hAddress** is valid. <br/>                      |
| <span id="IAP_ADRTYPE"></span><span id="iap_adrtype"></span><dl> <dt>**IAP\_ADRTYPE**</dt> <dt>0x00000004</dt> </dl>                             | Indicates that **dwAdrType** is valid. <br/>                     |
| <span id="IAP_FRIENDLYA"></span><span id="iap_friendlya"></span><dl> <dt>**IAP\_FRIENDLYA**</dt> <dt>0x00000008</dt> </dl>                       | Indicates that **pszFriendly** is valid. <br/>                   |
| <span id="IAP_EMAIL"></span><span id="iap_email"></span><dl> <dt>**IAP\_EMAIL**</dt> <dt>0x00000020</dt> </dl>                                   | Indicates that **pszEmail** is valid. <br/>                      |
| <span id="IAP_CERTSTATE"></span><span id="iap_certstate"></span><dl> <dt>**IAP\_CERTSTATE**</dt> <dt>0x00000100</dt> </dl>                       | Indicates that **certstate** is valid. <br/>                     |
| <span id="IAP_SIGNING_PRINT"></span><span id="iap_signing_print"></span><dl> <dt>**IAP\_SIGNING\_PRINT**</dt> <dt>0x00000200</dt> </dl>          | Indicates that **tbSigning** is valid. <br/>                     |
| <span id="IAP_ENCRYPTION_PRINT"></span><span id="iap_encryption_print"></span><dl> <dt>**IAP\_ENCRYPTION\_PRINT**</dt> <dt>0x00000400</dt> </dl> | Indicates that **tbEncryption** is valid. <br/>                  |
| <span id="IAP_ENCODING"></span><span id="iap_encoding"></span><dl> <dt>**IAP\_ENCODING**</dt> <dt>0x00000800</dt> </dl>                          | Indicates that **ietFriendly** is valid. <br/>                   |
| <span id="IAP_COOKIE"></span><span id="iap_cookie"></span><dl> <dt>**IAP\_COOKIE**</dt> <dt>0x00001000</dt> </dl>                                | Indicates that **dwCookie** is valid. <br/>                      |
| <span id="IAP_FRIENDLYW"></span><span id="iap_friendlyw"></span><dl> <dt>**IAP\_FRIENDLYW**</dt> <dt>0x00002000</dt> </dl>                       | Indicates that **pszFriendlyW** is valid. <br/>                  |
| <span id="IAP_ALL"></span><span id="iap_all"></span><dl> <dt>**IAP\_ALL**</dt> <dt>0xffffffff</dt> </dl>                                         | Indicates that all the fields of this structure are valid. <br/> |



 

</dd> <dt>

**hAddress**
</dt> <dd>

Type: **HADDRESS**

</dd> <dd>

Contains the handle of this address in the [**IMimeAddressTable**](oe-imimeaddresstable.md). (IAP\_HANDLE)

</dd> <dt>

**ietFriendly**
</dt> <dd>

Type: **[**ENCODINGTYPE**](oe-encodingtype.md)**

</dd> <dd>

Contains the encoding type of the friendly name. (IAP\_ENCODING)

</dd> <dt>

**hCharset**
</dt> <dd>

Type: **HCHARSET**

</dd> <dd>

Contains the character set for the friendly name. (IAP\_CHARSET)

</dd> <dt>

**dwAdrType**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains a bitmask that indicates the type of address. (IAP\_ADRTYPE)



| Value                                                                                                                                                                                                                                                                               | Meaning                                                                           |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| <span id="IAT_UNKNOWN"></span><span id="iat_unknown"></span><dl> <dt>**IAT\_UNKNOWN**</dt> <dt>0x00000000</dt> </dl>                                                             | Indicates an unknown address type. <br/>                                    |
| <span id="IAT_FROM"></span><span id="iat_from"></span><dl> <dt>**IAT\_FROM**</dt> <dt>0x00000001</dt> </dl>                                                                      | Indicates the From address header. <br/>                                    |
| <span id="IAT_SENDER"></span><span id="iat_sender"></span><dl> <dt>**IAT\_SENDER**</dt> <dt>0x00000002</dt> </dl>                                                                | Indicates the Sender address header. <br/>                                  |
| <span id="IAT_TO"></span><span id="iat_to"></span><dl> <dt>**IAT\_TO**</dt> <dt>0x00000004</dt> </dl>                                                                            | Indicates the To address header. <br/>                                      |
| <span id="IAT_CC"></span><span id="iat_cc"></span><dl> <dt>**IAT\_CC**</dt> <dt>0x00000008</dt> </dl>                                                                            | Indicates the CC address header. <br/>                                      |
| <span id="IAT_BCC"></span><span id="iat_bcc"></span><dl> <dt>**IAT\_BCC**</dt> <dt>0x00000010</dt> </dl>                                                                         | Indicates the BCC address header. <br/>                                     |
| <span id="IAT_REPLYTO"></span><span id="iat_replyto"></span><dl> <dt>**IAT\_REPLYTO**</dt> <dt>0x00000020</dt> </dl>                                                             | Indicates the Reply-To address header. <br/>                                |
| <span id="IAT_RETURNPATH"></span><span id="iat_returnpath"></span><dl> <dt>**IAT\_RETURNPATH**</dt> <dt>0x00000040</dt> </dl>                                                    | Indicates the Return-Path address header. <br/>                             |
| <span id="IAT_RETRCPTTO"></span><span id="iat_retrcptto"></span><dl> <dt>**IAT\_RETRCPTTO**</dt> <dt>0x00000080</dt> </dl>                                                       | Indicates the Return-Receipt address header. <br/>                          |
| <span id="IAT_RR"></span><span id="iat_rr"></span><dl> <dt>**IAT\_RR**</dt> <dt>0x00000100</dt> </dl>                                                                            |                                                                                   |
| <span id="IAT_APPARTO"></span><span id="iat_apparto"></span><dl> <dt>**IAT\_APPARTO**</dt> <dt>0x00000200</dt> </dl>                                                             | Indicates the Apparently-To address header. <br/>                           |
| <span id="IAT_DISP_NOTIFICATION_TO"></span><span id="iat_disp_notification_to"></span><dl> <dt>**IAT\_DISP\_NOTIFICATION\_TO**</dt> <dt>0x00000400</dt> </dl>                    |                                                                                   |
| <span id="IAT_ALL"></span><span id="iat_all"></span><dl> <dt>**IAT\_ALL**</dt> <dt>0xFFFFFFFF</dt> </dl>                                                                         | Indicates all address types. <br/>                                          |
| <span id="IAT_KNOWN"></span><span id="iat_known"></span><dl> <dt>**IAT\_KNOWN**</dt> <dt>(IAT\_FROM \| IAT\_TO \| IAT\_CC \| IAT\_BCC \| IAT\_REPLYTO \| IAT\_SENDER)</dt> </dl> | Indicates the From, To, CC, BCC, Reply-To, or Sender address headers. <br/> |
| <span id="IAT_RECIPS"></span><span id="iat_recips"></span><dl> <dt>**IAT\_RECIPS**</dt> <dt>(IAT\_TO \| IAT\_CC \| IAT\_BCC)</dt> </dl>                                          | Indicates the To, CC, or BCC address headers. <br/>                         |



 

</dd> <dt>

**pszFriendly**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains the friendly name of the address. (IAP\_FRIENDLY)

</dd> <dt>

**pszFriendlyW**
</dt> <dd>

Type: **LPWSTR**

</dd> <dd>

Contains the wide character friendly name of the address. (IAP\_FRIENDLYW)

</dd> <dt>

**pszEmail**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains the email address. (IAP\_EMAIL)

</dd> <dt>

**certstate**
</dt> <dd>

Type: **[**CERTSTATE**](oe-certstate.md)**

</dd> <dd>

Contains the certificate state. (IAP\_CERTSTATE)

</dd> <dt>

**tbSigning**
</dt> <dd>

Type: **THUMBBLOB**

</dd> <dd>

Contains the thumbprint to be used for signing. (IAP\_SIGNING\_PRINT)

</dd> <dt>

**tbEncryption**
</dt> <dd>

Type: **THUMBBLOB**

</dd> <dd>

Contains the thumbprint to be used for encryption. (IAP\_ENCRYPTION\_PRINT)

</dd> <dt>

**dwCookie**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Do not use. (IAP\_COOKIE)

</dd> <dt>

**dwReserved1**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Do not use.

</dd> <dt>

**dwReserved2**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Do not use.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| Product<br/>                  | Outlook Express 6.0<br/>                                                         |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl> |



 

 





