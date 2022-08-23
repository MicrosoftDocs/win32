---
description: Represents a single digital certificate.
ms.assetid: 'da95312b-cc9f-44f0-9517-0b28c5fcfb61'
title: Certificate object
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- Certificate
api_type:
- COM
api_location:
- Capicom.dll
---

# Certificate object

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the [**X509Certificate2 Class**](/previous-versions/windows/embedded/hh424017(v=msdn.10)) in the [**System.Security.Cryptography.X509Certificates**](/dotnet/api/system.security.cryptography.x509certificates.publickey.-ctor) namespace.\]

The **Certificate** object represents a single [*digital certificate*](../secgloss/d-gly.md).

The **Certificate** object exposes the following interfaces:

-   **ICertificate** — Introduced in CAPICOM 1.0.
-   **ICertificate2** — Introduced in CAPICOM 2.0.

## When to use

The **Certificate** object is used to perform the following tasks:

-   Load certificate data, including the private key, from a file.
-   Get information from the certificate.
-   Return basic constraints, EKU, extended properties, extensions, key usage, public key, and template objects associated with the certificate.
-   Determine whether the certificate is valid and check the access availability of the certificate subject's private key.
-   Display the certificate.
-   Import and export the certificate.
-   Save the certificate to a file.
-   Retrieve or set properties that describe the certificate.

## Members

The **Certificate** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Certificate** object has these methods.



| Method                                                       | Description                                                                                                                                                                                                                                              |
|:-------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**BasicConstraints**](certificate-basicconstraints.md)     | Returns a [**BasicConstraints**](basicconstraints.md) object that represents the basic constraints extension of the certificate.<br/> (Inherited from **CertificateICertificate2ICertificate**)                                                   |
| [**Display**](certificate-display.md)                       | Displays a certificate.<br/> (Inherited from **CertificateICertificate2ICertificate**)                                                                                                                                                             |
| [**Export**](certificate-export.md)                         | Copies a certificate to an encoded string. The encoded string can be written to a file or imported into a new **Certificate** object.<br/> (Inherited from **CertificateICertificate2ICertificate**)                                               |
| [**ExtendedKeyUsage**](certificate-extendedkeyusage.md)     | Returns an [**ExtendedKeyUsage**](extendedkeyusage.md) object that indicates the valid extended key uses of the certificate.<br/> (Inherited from **CertificateICertificate2ICertificate**)                                                       |
| [**ExtendedProperties**](certificate-extendedproperties.md) | Returns a collection of the extended properties of the certificate.<br/> (Inherited from **CertificateICertificate2**)                                                                                                                             |
| [**Extensions**](certificate-extensions.md)                 | Returns a collection of the extensions associated with the certificate.<br/> (Inherited from **CertificateICertificate2**)                                                                                                                         |
| [**GetInfo**](certificate-getinfo.md)                       | Retrieves information from the certificate.<br/> (Inherited from **CertificateICertificate2ICertificate**)                                                                                                                                         |
| [**HasPrivateKey**](certificate-hasprivatekey.md)           | Determines whether the certificate has a [*private key*](../secgloss/p-gly.md) associated with it.<br/> (Inherited from **CertificateICertificate2ICertificate**)                                    |
| [**Import**](certificate-import.md)                         | Imports a previously encoded certificate from a string into the **Certificate** object.<br/> (Inherited from **CertificateICertificate2ICertificate**)                                                                                             |
| [**IsValid**](certificate-isvalid.md)                       | Builds a certificate verification chain for a certificate and returns a [**CertificateStatus**](certificatestatus.md) object that contains the validity status of the certificate.<br/> (Inherited from **CertificateICertificate2ICertificate**) |
| [**KeyUsage**](certificate-keyusage.md)                     | Returns a [**KeyUsage**](keyusage.md) object that indicates the valid key usage of the certificate.<br/> (Inherited from **CertificateICertificate2ICertificate**)                                                                                |
| [**Load**](certificate-load.md)                             | Imports a certificate from a file.<br/> (Inherited from **CertificateICertificate2**)                                                                                                                                                              |
| [**PublicKey**](certificate-publickey.md)                   | Returns a [**PublicKey**](publickey.md) object.<br/> (Inherited from **CertificateICertificate2**)                                                                                                                                                |
| [**Save**](certificate-save.md)                             | Saves the certificate to a file.<br/> (Inherited from **CertificateICertificate2**)                                                                                                                                                                |
| [**Template**](certificate-template.md)                     | Returns the template associated with the certificate.<br/> (Inherited from **CertificateICertificate2**)                                                                                                                                           |



 

### Properties

The **Certificate** object has these properties.



| Property                                                      | Access type           | Description                                                                                                                                          |
|:--------------------------------------------------------------|:----------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Archived**](certificate-archived.md)<br/>           | Read/write<br/> | Sets or retrieves a Boolean value that indicates whether the certificate is archived.<br/> (Inherited from **CertificateICertificate2**)       |
| [**IssuerName**](certificate-issuername.md)<br/>       | Read-only<br/>  | Retrieves a string that contains the name of the certificate issuer.<br/> (Inherited from **CertificateICertificate2ICertificate**)            |
| [**PrivateKey**](certificate-privatekey.md)<br/>       | Read/write<br/> | Sets or retrieves the private key associated with the certificate.<br/> (Inherited from **CertificateICertificate2**)                          |
| [**SerialNumber**](certificate-serialnumber.md)<br/>   | Read-only<br/>  | Retrieves a string that contains the certificate serial number.<br/> (Inherited from **CertificateICertificate2ICertificate**)                 |
| [**SubjectName**](certificate-subjectname.md)<br/>     | Read-only<br/>  | Retrieves a string that contains the name of the certificate subject.<br/> (Inherited from **CertificateICertificate2ICertificate**)           |
| [**Thumbprint**](certificate-thumbprint.md)<br/>       | Read-only<br/>  | Retrieves a hexadecimal string that contains the SHA-1 hash of the certificate.<br/> (Inherited from **CertificateICertificate2ICertificate**) |
| [**ValidFromDate**](certificate-validfromdate.md)<br/> | Read-only<br/>  | Retrieves the beginning date for the validity of the certificate.<br/> (Inherited from **CertificateICertificate2ICertificate**)               |
| [**ValidToDate**](certificate-validtodate.md)<br/>     | Read-only<br/>  | Retrieves the ending date for the validity of the certificate.<br/> (Inherited from **CertificateICertificate2ICertificate**)                  |
| [**Version**](certificate-version.md)<br/>             | Read-only<br/>  | Retrieves the version number of the certificate.<br/> (Inherited from **CertificateICertificate2ICertificate**)                                |



 

## Remarks

The **Certificate** object can be created, and it is safe for scripting. The ProgID for the **Certificate** object is "CAPICOM.Certificate.2".

**CAPICOM 1.*x*:** The ProgID for the **Certificate** object is "CAPICOM.Certificate.1".

## Requirements



| Requirement | Value |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



 

 
