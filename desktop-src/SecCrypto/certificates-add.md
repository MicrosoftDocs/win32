---
Description: 'Adds a Certificate object to the collection.'
ms.assetid: '0973018d-1e83-41b4-a250-7dd5be2fb664'
title: 'ICertificates2::Add method'
---

# ICertificates2::Add method

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the [**X509Certificate2Collection Class**](T:System.Security.Cryptography.X509Certificates.X509Certificate2Collection) in the [**System.Security.Cryptography.X509Certificates**](frlrfSystemSecurityCryptographyX509Certificates) namespace.\]

The **Add** method adds a [**Certificate**](certificate.md) object to the collection. This method is introduced in CAPICOM 2.0.

## Syntax


```VB
Certificates.Add( _
  ByVal Certificate _
)
```



## Parameters

<dl> <dt>

*Certificate* \[in\]
</dt> <dd>

The [**Certificate**](certificate.md) object to be added to the collection.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                                  |                                                                                        |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



 

 




