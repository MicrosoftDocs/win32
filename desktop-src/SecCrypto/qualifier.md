---
description: Represents a Certification Practice Statement (CPS) pointer or user notice qualifier.
ms.assetid: 857af3d6-aa7b-429a-a056-72573232f72c
title: Qualifier object
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- Qualifier
api_type:
- COM
api_location:
- Capicom.dll
---

# Qualifier object

\[The **Qualifier** object is available for use in the operating systems specified in the Requirements section. Instead, use the [**X509Extension Class**](/dotnet/api/system.security.cryptography.x509certificates.x509extension?view=netcore-3.1) in the [**System.Security.Cryptography.X509Certificates**](/dotnet/api/system.security.cryptography.x509certificates.publickey.-ctor?view=netcore-3.1) namespace by calling the constructor that takes an OID as a parameter, and then use the OID for Certificate Policies to process qualifiers that are part of the policy information in the Certificate Policies extension.\]

The **Qualifier** object represents a Certification Practice Statement (CPS) pointer or user notice qualifier.

## When to use

The **Qualifier** object is used to perform the following tasks:

-   Retrieve the object identifier of the qualifier.
-   Retrieve the Uniform Resource Identifier (URI) that points to a CPS published by the [*certification authority*](../secgloss/c-gly.md) (CA).
-   Retrieve the name of the organization associated with the qualifier.
-   Retrieve the name and content of a user notice.

## Members

The **Qualifier** object has these types of members:

-   [Properties](#properties)

### Properties

The **Qualifier** object has these properties.



| Property                                                          | Access type          | Description                                                                                                                         |
|:------------------------------------------------------------------|:---------------------|:------------------------------------------------------------------------------------------------------------------------------------|
| [**CPSPointer**](qualifier-cpspointer.md)<br/>             | Read-only<br/> | Retrieves a string that contains the URI that points to a CPS published by the CA.<br/>                                       |
| [**ExplicitText**](qualifier-explicittext.md)<br/>         | Read-only<br/> | Retrieves a string that contains the content of the user notice. This property may be empty.<br/>                             |
| [**NoticeNumbers**](qualifier-noticenumbers.md)<br/>       | Read-only<br/> | Retrieves a **NoticeNumbers** object that contains the collection of user notice numbers. This property may be empty.<br/>    |
| [**OID**](qualifier-oid.md)<br/>                           | Read-only<br/> | Retrieves an [**OID**](oid.md) object that identifies the qualifier. This is the default property.<br/>                      |
| [**OrganizationName**](qualifier-organizationname.md)<br/> | Read-only<br/> | Retrieves a string that contains the name of the organization associated with the qualifier. This property may be empty.<br/> |



 

## Remarks

The **Qualifier** object cannot be created.

## Requirements



| Requirement | Value |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



 

 
