---
description: A collection of PolicyInformation objects.
ms.assetid: 2abdd070-82ae-47fd-afbc-6d4361e5a3f1
title: CertificatePolicies object
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- CertificatePolicies
api_type:
- COM
api_location:
- Capicom.dll
---

# CertificatePolicies object

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the [**X509Extension Class**](/dotnet/api/system.security.cryptography.x509certificates.x509extension?view=netcore-3.1) in the [**System.Security.Cryptography.X509Certificates**](/dotnet/api/system.security.cryptography.x509certificates.publickey.-ctor?view=netcore-3.1) namespace by calling the constructor that takes an OID as a parameter, and then use the OID for Certificate Policies to retrieve the certificate policies.\]

The **CertificatePolicies** object represents a collection of [**PolicyInformation**](policyinformation.md) objects. Each [**PolicyInformation**](policyinformation.md) object represents a single certificate policy.

## When to use

The **CertificatePolicies** object is used to perform the following tasks:

-   Retrieve the number of certificate policies in the collection.
-   Retrieve a specific [**PolicyInformation**](policyinformation.md) object from the collection.
-   Iterate through the collection.

## Members

The **CertificatePolicies** object has these types of members:

-   [Properties](#properties)

### Properties

The **CertificatePolicies** object has these properties.



| Property                                                    | Access type          | Description                                                                                                                                                                                                                     |
|:------------------------------------------------------------|:---------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**\_NewEnum**](certificatepolicies-newenum.md)<br/> | Read-only<br/> | Retrieves an [**IEnumVARIANT**](/windows/win32/api/oaidl/nn-oaidl-ienumvariant) interface on an object that can be used to enumerate the collection. This property is hidden within Visual Basic Scripting Edition (VBScript).<br/> |
| [**Count**](certificatepolicies-count.md)<br/>       | Read-only<br/> | Retrieves the number of [**PolicyInformation**](policyinformation.md) objects in the collection.<br/>                                                                                                                    |
| [**Item**](certificatepolicies-item.md)<br/>         | Read-only<br/> | Retrieves a [**PolicyInformation**](policyinformation.md) object that represents the indexed certificate policy of the collection. This is the default property.<br/>                                                    |



 

## Remarks

The **CertificatePolicies** object cannot be created.

## Requirements



| Requirement | Value |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



 

 
