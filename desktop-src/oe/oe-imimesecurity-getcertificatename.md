---
title: IMimeSecurity GetCertificateName method
description: Gets the name of the specified certificate.
ms.assetid: 270049d0-e4fa-4345-b9cf-b26b1438fdf8
keywords:
- GetCertificateName method Windows Mail (formerly Outlook Express)
- GetCertificateName method Windows Mail (formerly Outlook Express) , IMimeSecurity interface
- IMimeSecurity interface Windows Mail (formerly Outlook Express) , GetCertificateName method
topic_type:
- apiref
api_name:
- IMimeSecurity.GetCertificateName
api_location:
- Inetcomm.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IMimeSecurity::GetCertificateName method

Gets the name of the specified certificate.

## Syntax


```C++
HRESULT GetCertificateName(
  [in]  const PCX509CERT   pX509Cert,
  [in]  const CERTNAMETYPE cn,
  [out]       LPSTR        *ppszName
);
```



## Parameters

<dl> <dt>

*pX509Cert* \[in\]
</dt> <dd>

Type: **const PCX509CERT**

Specifies a pointer to the [CERT\_CONTEXT](http://msdn.microsoft.com/library/seccrypto/security/cert_context.asp) structure for which to get the name.

</dd> <dt>

*cn* \[in\]
</dt> <dd>

Type: **const [**CERTNAMETYPE**](oe-certnametype.md)**

Specifies the [**CERTNAMETYPE**](oe-certnametype.md) of the name to return.

</dd> <dt>

*ppszName* \[out\]
</dt> <dd>

Type: **LPSTR\***

Receives a pointer to a **LPSTR** that contains the name of the certificate. The client is responsible for freeing this pointer.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                                                                                                            |
|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates success. <br/>                                                                                                         |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates that *pX509Cert* or *ppszName* is **NULL**, or that *cn* is not a valid [**CERTNAMETYPE**](oe-certnametype.md). <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





