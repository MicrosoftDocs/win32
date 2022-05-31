---
description: Retrieves the name of the certificate store that this object represents.
ms.assetid: db61b464-0e8e-4b19-be12-04e00d6bba53
title: Store.Name property
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- Store.Name
api_type:
- COM
api_location:
- Capicom.dll
---

# Store.Name property

\[The [**Name**](store-location.md) property is available for use in the operating systems specified in the Requirements section. Instead, use the [**X509Store Class**](/dotnet/api/system.security.cryptography.x509certificates.x509store?view=netcore-3.1&preserve-view=true) in the [**System.Security.Cryptography.X509Certificates**](/dotnet/api/system.security.cryptography.x509certificates.publickey.-ctor?view=netcore-3.1&preserve-view=true) namespace.\]

The [**Name**](store-location.md) property retrieves the name of the certificate store that this object represents.

## Syntax


```VB
Store.Name As String
```



## Property value

The **String** value that represents the name of the certificate store.

## Remarks

Examples of certificate store names include My and Root.

The value of the [**Name**](store-location.md) property is the same as the value supplied for the *StoreName* parameter of the [**Open**](store-open.md) method when the store was opened.

## Requirements



| Requirement | Value |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.1 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**Store**](store.md)
</dt> </dl>

 

 
