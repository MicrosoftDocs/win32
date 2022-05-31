---
description: The PublicKey object represents a public key in a Certificate object.
title: PublicKey object
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- PublicKey
api_type:
- COM
api_location:
- Capicom.dll
---

# PublicKey object

\[The **PublicKey** object is available for use in the operating systems specified in the Requirements section. Instead, use the [**X509Certificate2.PublicKey Property**](/dotnet/api/system.security.cryptography.x509certificates.x509certificate2.publickey?view=netcore-3.1&preserve-view=true) in the [**System.Security.Cryptography.X509Certificates**](/dotnet/api/system.security.cryptography.x509certificates.publickey.-ctor?view=netcore-3.1&preserve-view=true) namespace.\]

The **PublicKey** object represents a public key in a [**Certificate**](certificate.md) object.

## When to use

The **PublicKey** object is used to retrieve data about the public key.

## Members

The **PublicKey** object has these types of members:

-   [Properties](#properties)

### Properties

The **PublicKey** object has these properties.



| Property                                                            | Access type          | Description                                                                                                                            |
|:--------------------------------------------------------------------|:---------------------|:---------------------------------------------------------------------------------------------------------------------------------------|
| [**Algorithm**](publickey-algorithm.md)<br/>                 | Read-only<br/> | Retrieves the [**OID**](oid.md) object that identifies the algorithm used by the public key. This is the default property.<br/> |
| [**EncodedKey**](publickey-encodedkey.md)<br/>               | Read-only<br/> | Retrieves an [**EncodedData**](encodeddata.md) object that provides access to the value of the public key.<br/>                 |
| [**EncodedParameters**](publickey-encodedparameters.md)<br/> | Read-only<br/> | Retrieves an [**EncodedData**](encodeddata.md) object that provides access to the parameters of the public key algorithm.<br/>  |
| [**Length**](publickey-length.md)<br/>                       | Read-only<br/> | Retrieves the length of the public key in bits.<br/>                                                                             |



 

## Remarks

The **PublicKey** object cannot be created.

The **PublicKey** object is used by the [**Certificate.PublicKey**](certificate-publickey.md) method.

## Requirements



| Requirement | Value |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



 

 
