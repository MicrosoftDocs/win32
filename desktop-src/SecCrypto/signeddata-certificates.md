---
description: Retrieves the Certificates collection that is associated with the SignedData object. After being retrieved, the individual Certificate objects in the collection can be enumerated.
ms.assetid: 94741fee-2462-4a18-bc14-c52e9cac374b
title: SignedData.Certificates property
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- SignedData.Certificates
api_type:
- COM
api_location:
- Capicom.dll
---

# SignedData.Certificates property

\[The **Certificates** property is available for use in the operating systems specified in the Requirements section. Instead, use the [**SignedCms Class**](/dotnet/api/system.security.cryptography.pkcs.signedcms?view=dotnet-plat-ext-3.1&preserve-view=true) in the [**System.Security.Cryptography.Pkcs**](/dotnet/api/system.security.cryptography.pkcs?view=dotnet-plat-ext-3.1&preserve-view=true) namespace.\]

The **Certificates** property retrieves the [**Certificates**](certificates.md) collection that is associated with the [**SignedData**](signeddata.md) object. After being retrieved, the individual [**Certificate**](certificate.md) objects in the collection can be enumerated.

## Syntax


```VB
SignedData.Certificates As Certificates
```



## Property value

The [**Certificates**](certificates.md) collection that is associated with the [**SignedData**](signeddata.md) object.

## Requirements



| Requirement | Value |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**SignedData**](signeddata.md)
</dt> </dl>

 

 
