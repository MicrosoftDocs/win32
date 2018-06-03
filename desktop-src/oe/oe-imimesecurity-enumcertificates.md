---
title: IMimeSecurity EnumCertificates method
description: Enumerates the certificates from the specified store.
ms.assetid: 74dfcd2a-25ad-4106-b2a8-3af863c6d5c0
keywords:
- EnumCertificates method Windows Mail (formerly Outlook Express)
- EnumCertificates method Windows Mail (formerly Outlook Express) , IMimeSecurity interface
- IMimeSecurity interface Windows Mail (formerly Outlook Express) , EnumCertificates method
topic_type:
- apiref
api_name:
- IMimeSecurity.EnumCertificates
api_location:
- Inetcomm.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IMimeSecurity::EnumCertificates method

Enumerates the certificates from the specified store.

## Syntax


```C++
HRESULT EnumCertificates(
  [in]  HCAPICERTSTORE hc,
  [in]  DWORD          dwUsage,
  [in]  PCX509CERT     pPrev,
  [out] PCX509CERT     *ppCert
);
```



## Parameters

<dl> <dt>

*hc* \[in\]
</dt> <dd>

Type: **HCAPICERTSTORE**

Specifies the handle to the certificate store.

</dd> <dt>

*dwUsage* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies the thumbprint type. A value of zero indicates that the caller is checking whether any certificates exist.

<dl> <dt>

<span id="ITT_SIGNING"></span><span id="itt_signing"></span>**ITT\_SIGNING** (0x00000001)
</dt> <dt>

<span id="ITT_ENCRYPTION"></span><span id="itt_encryption"></span>**ITT\_ENCRYPTION** (0x00000002)
</dt> </dl> </dd> <dt>

*pPrev* \[in\]
</dt> <dd>

Type: **PCX509CERT**

Specifies a pointer to the last [CERT\_CONTEXT](http://msdn.microsoft.com/library/seccrypto/security/cert_context.asp) structure enumerated by this method. Use **NULL** to indicate that the *ppCert* should receive the first certificate in the enumeration.

</dd> <dt>

*ppCert* \[out\]
</dt> <dd>

Type: **PCX509CERT\***

Receives a pointer to the next [CERT\_CONTEXT](http://msdn.microsoft.com/library/seccrypto/security/cert_context.asp) structure in the enumeration.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                         | Description                                                                 |
|-----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                | Indicates success. <br/>                                              |
| <dl> <dt>**S\_FALSE**</dt> </dl>             | Indicates that *dwUsage* is zero and there are no certificates. <br/> |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>        | Indicates that *hc* or *ppCert* is **NULL**. <br/>                    |
| <dl> <dt>**CRYPT\_E\_NOT\_FOUND**</dt> </dl> | Indicates that there are no more certificates. <br/>                  |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





