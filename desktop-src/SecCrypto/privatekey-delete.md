---
Description: Deletes the private key container referenced by the PrivateKey object.
ms.assetid: 80bbe46b-1ec5-4d47-82b0-5a3177f86389
title: PrivateKey.Delete method
ms.topic: article
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- PrivateKey.Delete
api_type:
- COM
api_location:
- Capicom.dll
---

# PrivateKey.Delete method

\[The **Delete** method is available for use in the operating systems specified in the Requirements section. Instead, use the [**X509Certificate2.PrivateKey Property**](https://msdn.microsoft.com/library/ms148460(v=VS.90).aspx) in the [**System.Security.Cryptography.X509Certificates**](https://msdn.microsoft.com/library/73091bzx(v=VS.71).aspx) namespace.\]

The **Delete** method deletes the private key container referenced by the [**PrivateKey**](privatekey.md) object.

## Syntax


```VB
PrivateKey.Delete()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

> [!IMPORTANT]
> This method deletes the private key container referenced by the [**PrivateKey**](privatekey.md) object as well as all private keys in the container. Anything encrypted using the public keys corresponding to the deleted private keys will no longer be able to be decrypted.

 

This method raises CAPICOM\_E\_NOT\_ALLOWED when it is scripted from a web-based application.

## Requirements



|                            |                                                                                        |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



 

 




