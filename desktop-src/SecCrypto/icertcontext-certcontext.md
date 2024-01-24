---
description: Sets or retrieves the PCCERT\_CONTEXT of a certificate.
ms.assetid: aedd219d-43fa-4722-9af4-36172d2c18b0
title: ICertContext::CertContext property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ICertContext.CertContext
- ICertContext.get_CertContext
- ICertContext.put_CertContext
- CertContext.CertContext
api_type: 
- COM
api_location: 
- Capicom.dll
---

# ICertContext::CertContext property

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP.\]

The **CertContext** property sets or retrieves the PCCERT\_CONTEXT of a certificate.

This property is read/write.

## Syntax


```VB
CertContext.CertContext As Long
```



## Property value

The PCCERT\_CONTEXT of the certificate.

## Error codes

If the property access methods **put\_CertContext** and **get\_CertContext** succeed, they return S\_OK.

Any other **HRESULT** value indicates that the call failed.

## Remarks

You must call either the [**FreeContext**](icertcontext-freecontext.md) method or the [**CertFreeCertificateContext**](/windows/desktop/api/Wincrypt/nf-wincrypt-certfreecertificatecontext) function to free the context.

If you set the **CertContext** property, the state of the entire [**Certificate**](certificate.md) object is reset.

## Requirements



| Requirement | Value |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**ICertContext**](icertcontext.md)
</dt> </dl>

 

 




