---
description: Releases a PCCERT\_CONTEXT acquired through the CertContext property.
ms.assetid: fcb9e885-d26c-4866-a35d-1c940bfe8162
title: ICertContext::FreeContext method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ICertContext.FreeContext
- CertContext.FreeContext
api_type: 
- COM
api_location: 
- Capicom.dll
---

# ICertContext::FreeContext method

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP.\]

The **FreeContext** method releases a PCCERT\_CONTEXT acquired through the [**CertContext**](icertcontext-certcontext.md) property.

## Syntax


```VB
CertContext.FreeContext( _
  ByVal pCertContext _
)
```



## Parameters

<dl> <dt>

*pCertContext* \[in\]
</dt> <dd>

The PCCERT\_CONTEXT to be released.

</dd> </dl>

## Return value

The return value is an **HRESULT**. A value of S\_OK indicates success. Any other value indicates that the operation failed.

## Remarks

This method does not release the PCCERT\_CONTEXT contained within a [**Certificate**](certificate.md) object. It should be used only to release a PCCERT\_CONTEXT acquired through the [**CertContext**](icertcontext-certcontext.md) property.

## Requirements



| Requirement | Value |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**ICertContext**](icertcontext.md)
</dt> </dl>

 

 




