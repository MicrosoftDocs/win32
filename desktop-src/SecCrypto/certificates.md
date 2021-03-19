---
description: Represents a collection of Certificate objects.
ms.assetid: '82011c49-38fb-4261-8fb3-b76859da8a9e'
title: Certificates object
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- Certificates
api_type:
- COM
api_location:
- Capicom.dll
---

# Certificates object

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the [**X509Certificate2Collection Class**](/previous-versions/windows/embedded/hh424013(v=msdn.10)) in the [**System.Security.Cryptography.X509Certificates**](/dotnet/api/system.security.cryptography.x509certificates.publickey.-ctor?view=netcore-3.1) namespace.\]

The **Certificates** object represents a collection of [**Certificate**](certificate.md) objects. Each [**Certificate**](certificate.md) object represents a single [*digital certificate*](../secgloss/d-gly.md).

The **Certificates** object exposes the following interfaces:

-   **ICertificates2**: Introduced in CAPICOM 2.0.
-   **ICertificates**: Introduced in CAPICOM 1.0.

## When to use

The **Certificates** object is used to perform the following tasks:

-   Add or remove a [**Certificate**](certificate.md) object to or from the collection.
-   Generate a subset of the collection by finding a set of certificates or by displaying a dialog box to select the certificates.
-   Clear all the [**Certificate**](certificate.md) objects from the collection.
-   Retrieve the number of certificates in the collection.
-   Retrieve a specific [**Certificate**](certificate.md) object from the collection.
-   Iterate through the collection.

## Members

The **Certificates** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Certificates** object has these methods.



| Method                                | Description                                                                                                                                                           |
|:--------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Add**](certificates-add.md)       | Adds a [**Certificate**](certificate.md) object to the collection.<br/> (Inherited from **CertificatesICertificates2**)                                        |
| [**Clear**](certificates-clear.md)   | Removes all [**Certificate**](certificate.md) objects from the collection.<br/> (Inherited from **CertificatesICertificates2**)                                |
| [**Find**](certificates-find.md)     | Returns a **Certificates** object that contains all certificates that match the specified search criteria.<br/> (Inherited from **CertificatesICertificates2**) |
| [**Remove**](certificates-remove.md) | Removes a single [**Certificate**](certificate.md) object from the collection.<br/> (Inherited from **CertificatesICertificates2**)                            |
| [**Save**](certificates-save.md)     | Saves the certificates to a specified file.<br/> (Inherited from **CertificatesICertificates2**)                                                                |
| [**Select**](certificates-select.md) | Displays a dialog box for selecting certificates and returns a collection of those certificates selected.<br/> (Inherited from **CertificatesICertificates2**)  |



 

### Properties

The **Certificates** object has these properties.



| Property                                             | Access type          | Description                                                                                                                                                                                                                     |
|:-----------------------------------------------------|:---------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**\_NewEnum**](certificates-newenum.md)<br/> | Read-only<br/> | Retrieves an [**IEnumVARIANT**](/windows/win32/api/oaidl/nn-oaidl-ienumvariant) interface on an object that can be used to enumerate the collection. This property is hidden within Visual Basic Scripting Edition (VBScript).<br/> |
| [**Count**](certificates-count.md)<br/>       | Read-only<br/> | Retrieves the number of [**Certificate**](certificate.md) objects in the collection.<br/>                                                                                                                                |
| [**Item**](certificates-item.md)<br/>         | Read-only<br/> | Retrieves a [**Certificate**](certificate.md) object that represents the indexed certificate of the collection. This is the default property.<br/> (Inherited from **CertificatesICertificates2ICertificates**)          |



 

## Remarks

The **Certificates** object can be created, and it is safe for scripting. The ProgID for the **Certificates** object is "CAPICOM.Certificates.2".

**CAPICOM 1.*x*:** The ProgID for the **Certificates** object is "CAPICOM.Certificates.1".

## Requirements



| Requirement | Value |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**Cryptography Objects**](cryptography-objects.md)
</dt> </dl>

 

 
