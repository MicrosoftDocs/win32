---
description: Contains information about how to construct a certificate trust chain.
ms.assetid: 120cd79e-7c9b-45f3-8596-091b674e73d8
title: CertificateStatus object
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- CertificateStatus
api_type:
- COM
api_location:
- Capicom.dll
---

# CertificateStatus object

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the [**X509ChainStatus Structure**](/dotnet/api/system.security.cryptography.x509certificates.x509chainstatus) in the [**System.Security.Cryptography.X509Certificates**](/dotnet/api/system.security.cryptography.x509certificates.publickey.-ctor) namespace.\]

The **CertificateStatus** object contains information about how to construct a certificate trust chain.

## Members

The **CertificateStatus** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **CertificateStatus** object has these methods.



| Method                                                               | Description                                                                                                                                  |
|:---------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------|
| [**ApplicationPolicies**](certificatestatus-applicationpolicies.md) | Returns an [**OIDs**](oids.md) collection that represents the application policy OIDs.<br/>                                           |
| [**CertificatePolicies**](certificatestatus-certificatepolicies.md) | Returns an [**OIDs**](oids.md) collection that represents the certificate policy OIDs used during chain building.<br/>                |
| [**EKU**](certificatestatus-eku.md)                                 | Returns the [**EKU**](eku.md) object used to set the EKU elements to be checked in establishing a certificate's validity status.<br/> |



 

### Properties

The **CertificateStatus** object has these properties.



| Property                                                                        | Access type           | Description                                                                                                                                                                                                                                                       |
|:--------------------------------------------------------------------------------|:----------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Certificates**](certificatestatus-certificates.md)<br/>               | Read/write<br/> | Sets or retrieves the collection of certificates that can be used to build the certificate chain.<br/> **CAPICOM 2.0.0.3 and earlier:** The [**Certificates**](certificatestatus-certificates.md) property is not supported.<br/>                    |
| [**CheckFlag**](certificatestatus-checkflag.md)<br/>                     | Read/write<br/> | Validity check flag. Values can be joined by using a logical **OR** operator. The default check flag is [**CAPICOM\_CHECK\_ONLINE\_ALL**](capicom-check-flag.md).<br/>                                                                                     |
| [**Result**](certificatestatus-result.md)<br/>                           | Read-only<br/>  | Indicates whether the certificate is valid. The certificate's validity is checked using the current setting of the [**CheckFlag**](certificatestatus-checkflag.md) property and the policy settings of the certificate. This is the default property.<br/> |
| [**UrlRetrievalTimeout**](certificatestatus-urlretrievaltimeout.md)<br/> | Read/write<br/> | Sets or retrieves the length of time before a URL is determined to be unreachable.<br/>                                                                                                                                                                     |
| [**VerificationTime**](certificatestatus-verificationtime.md)<br/>       | Read/write<br/> | Sets or retrieves the time that the certificate was verified.<br/>                                                                                                                                                                                          |



 

## Remarks

The **CertificateStatus** object cannot be created.

The **CertificateStatus** object is returned by the [**Certificate.IsValid**](certificate-isvalid.md) method.

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
</dt> <dt>

[**Chain**](chain.md)
</dt> </dl>

 

 
