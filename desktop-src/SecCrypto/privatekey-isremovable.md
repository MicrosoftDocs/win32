---
Description: Returns a Boolean value that indicates whether the private key is in removable storage.
ms.assetid: 9371d7cf-65b2-4c0f-a387-195a058d6a8b
title: PrivateKey.IsRemovable method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# PrivateKey.IsRemovable method

\[The **IsRemovable** method is available for use in the operating systems specified in the Requirements section. Instead, use the [**X509Certificate2.PrivateKey Property**](frlrfSystemSecurityCryptographyX509CertificatesX509Certificate2ClassPrivateKeyTopic) in the [**System.Security.Cryptography.X509Certificates**](frlrfSystemSecurityCryptographyX509Certificates) namespace.\]

The **IsRemovable** method returns a Boolean value that indicates whether the private key is in removable storage.

## Syntax


```VB
PrivateKey.IsRemovable()
```



## Parameters

This method has no parameters.

## Return value

If true, the private key is in removable storage.

## Remarks

The return value of this method is dependent on the [*cryptographic service provider*](security.c_gly#-security-cryptographic-service-provider-gly) (CSP) used. This method will return a trustworthy value if a Microsoft CSP is used. If the CSP is not a Microsoft CSP, the return value cannot be trusted to be accurate.

## Requirements



|                            |                                                                                        |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**PrivateKey**](privatekey.md)
</dt> </dl>

 

 




