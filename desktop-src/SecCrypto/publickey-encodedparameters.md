---
Description: Retrieves the parameters of the public key algorithm.
ms.assetid: 1d12f72e-0144-4b7b-b468-d2f35bf253d3
title: PublicKey.EncodedParameters property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# PublicKey.EncodedParameters property

\[The **EncodedParameters** property is available for use in the operating systems specified in the Requirements section. Instead, use the [**X509Certificate2.PublicKey Property**](frlrfSystemSecurityCryptographyX509CertificatesX509Certificate2ClassPublicKeyTopic) in the [**System.Security.Cryptography.X509Certificates**](frlrfSystemSecurityCryptographyX509Certificates) namespace.\]

The **EncodedParameters** property retrieves the parameters of the public key algorithm.

## Syntax


```VB
PublicKey.EncodedParameters As EncodedData
```



## Property value

An [**EncodedData**](encodeddata.md) object that provides access to the parameters of the public key algorithm.

## Requirements



|                            |                                                                                        |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**PublicKey**](publickey.md)
</dt> </dl>

 

 




