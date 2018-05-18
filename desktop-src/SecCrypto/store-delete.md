---
Description: 'Deletes the certificate store that is represented by the current Store object.'
ms.assetid: '274914ee-27a0-4bd6-8510-af897aab3a2d'
title: 'Store.Delete method'
---

# Store.Delete method

\[The **Delete** method is available for use in the operating systems specified in the Requirements section. Instead, use the [**X509Store Class**](T:System.Security.Cryptography.X509Certificates.X509Store) in the [**System.Security.Cryptography.X509Certificates**](frlrfSystemSecurityCryptographyX509Certificates) namespace.\]

The **Delete** method deletes the [*certificate store*](security.c_gly#-security-certificate-store-gly) that is represented by the current [**Store**](certificate.md) object. This method deletes only nonsystem stores.

## Syntax


```VB
Store.Delete()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

The following stores are system stores and cannot be deleted:

-   My
-   Root
-   Trust
-   CA
-   UserDS
-   TrustedPublisher
-   Disallowed
-   AuthRoot
-   TrustedPeople

The **Delete** method returns an error if called from a web script.

## Requirements



|                            |                                                                                        |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.1 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**Store**](store.md)
</dt> <dt>

[**Cryptography Objects**](cryptography-objects.md)
</dt> </dl>

 

 




