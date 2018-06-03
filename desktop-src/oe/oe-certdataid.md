---
title: CERTDATAID enumeration
description: Do not use. Used to identify a request by GetCertData.
ms.assetid: 031aab68-503d-426e-a4da-ad46a982e978
keywords:
- CERTDATAID enumeration Windows Mail (formerly Outlook Express)
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

# CERTDATAID enumeration

Do not use. Used to identify a request by [**GetCertData**](oe-imimesecurity-getcertdata.md).

## Syntax


```C++
typedef enum tagCERTDATAID { 
  CDID_EMAIL      = 0,
  CDID_ALT_EMAIL  = 1,
  CDID_MAX        = 2
} ACCESSTYPE;
```



## Constants

<dl> <dt>

<span id="CDID_EMAIL"></span><span id="cdid_email"></span>**CDID\_EMAIL**
</dt> <dd>

Indicates the data to get from the certificate.

</dd> <dt>

<span id="CDID_ALT_EMAIL"></span><span id="cdid_alt_email"></span>**CDID\_ALT\_EMAIL**
</dt> <dd>

Indicates the data to get from the certificate's alternate subject field.

</dd> <dt>

<span id="CDID_MAX"></span><span id="cdid_max"></span>**CDID\_MAX**
</dt> <dd>

Indicates the total number of values in this enumeration.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| Product<br/>                  | Outlook Express 6.0<br/>                                                         |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl> |



 

 





