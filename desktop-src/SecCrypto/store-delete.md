---
description: Deletes the certificate store that is represented by the current Store object.
ms.assetid: 274914ee-27a0-4bd6-8510-af897aab3a2d
title: Store.Delete method
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- Store.Delete
api_type:
- COM
api_location:
- Capicom.dll
---

# Store.Delete method

\[The **Delete** method is available for use in the operating systems specified in the Requirements section. Instead, use the [**X509Store Class**](/previous-versions/windows/embedded/hh424027(v=msdn.10)) in the [**System.Security.Cryptography.X509Certificates**](/dotnet/api/system.security.cryptography.x509certificates.publickey.-ctor) namespace.\]

The **Delete** method deletes the [*certificate store*](../secgloss/c-gly.md) that is represented by the current [**Store**](certificate.md) object. This method deletes only nonsystem stores.

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



| Requirement | Value |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.1 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**Store**](store.md)
</dt> <dt>

[**Cryptography Objects**](cryptography-objects.md)
</dt> </dl>

 

 
