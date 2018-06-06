---
Description: Returns a Boolean value that indicates whether the private key belongs to a machine key set.
ms.assetid: ea13ba68-30ae-4aa4-b490-29fd4542c621
title: PrivateKey.IsMachineKeyset method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PrivateKey.IsMachineKeyset method

\[The **IsMachineKeyset** method is available for use in the operating systems specified in the Requirements section. Instead, use the [**X509Certificate2.PrivateKey Property**](https://www.bing.com/search?q=**X509Certificate2.PrivateKey+Property**) in the [**System.Security.Cryptography.X509Certificates**](https://www.bing.com/search?q=**System.Security.Cryptography.X509Certificates**) namespace.\]

The **IsMachineKeyset** method returns a Boolean value that indicates whether the private key belongs to a machine key set.

## Syntax


```VB
PrivateKey.IsMachineKeyset()
```



## Parameters

This method has no parameters.

## Return value

If true, the private key belongs to a machine key set.

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

 

 




