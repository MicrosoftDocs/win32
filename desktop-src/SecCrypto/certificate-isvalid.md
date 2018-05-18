---
Description: 'Builds a certificate verification chain for a certificate and returns a CertificateStatus object that contains the validity status of the certificate.'
ms.assetid: '4463e4ac-60a5-4845-93b3-35d2f83bd86e'
title: 'ICertificate2::IsValid method'
---

# ICertificate2::IsValid method

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the [**X509Certificate2 Class**](T:System.Security.Cryptography.X509Certificates.X509Certificate2) in the [**System.Security.Cryptography.X509Certificates**](frlrfSystemSecurityCryptographyX509Certificates) namespace.\]

The **IsValid** method builds a certificate verification chain for a certificate and returns a [**CertificateStatus**](certificatestatus.md) object that contains the validity status of the certificate.

## Syntax


```VB
Certificate.IsValid()
```



## Parameters

This method has no parameters.

## Requirements



|                                  |                                                                                        |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[Cryptography Objects](cryptography-objects.md)
</dt> <dt>

[**Certificate**](certificate.md)
</dt> </dl>

 

 




