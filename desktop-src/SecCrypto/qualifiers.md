---
description: Represents a collection of qualifiers.
ms.assetid: '2f51404d-b26e-4153-b206-ab6b413363a1'
title: Qualifiers object (Iads.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- Qualifiers
api_type:
- COM
api_location:
- Capicom.dll
---

# Qualifiers object

\[The **Qualifiers** object is available for use in the operating systems specified in the Requirements section. Instead, use the [**X509Extension Class**](/dotnet/api/system.security.cryptography.x509certificates.x509extension?view=netcore-3.1) in the [**System.Security.Cryptography.X509Certificates**](/dotnet/api/system.security.cryptography.x509certificates.publickey.-ctor?view=netcore-3.1) namespace by calling the constructor that takes an OID as a parameter, and then use the OID for Certificate Policies to process qualifiers that are part of the policy information in the Certificate Policies extension.\]

The **Qualifiers** object represents a collection of qualifiers.

## When to use

The **Qualifiers** object is used to perform the following tasks:

-   Retrieve a specific extended property from the collection.
-   Retrieve the number of extended properties in the collection.
-   Iterate through the collection.

## Members

The **Qualifiers** object has these types of members:

-   [Properties](#properties)

### Properties

The **Qualifiers** object has these properties.



| Property                                           | Access type          | Description                                                                                                                                                                                                                     |
|:---------------------------------------------------|:---------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**\_NewEnum**](qualifiers-newenum.md)<br/> | Read-only<br/> | Retrieves an [**IEnumVARIANT**](/windows/win32/api/oaidl/nn-oaidl-ienumvariant) interface on an object that can be used to enumerate the collection. This property is hidden within Visual Basic Scripting Edition (VBScript).<br/> |
| [**Count**](qualifiers-count.md)<br/>       | Read-only<br/> | Retrieves the number of qualifiers in the collection.<br/>                                                                                                                                                                |
| [**Item**](qualifiers-item.md)<br/>         | Read-only<br/> | Retrieves a [**Qualifier**](qualifier.md) object that represents the indexed qualifier of the collection. This is the default property.<br/>                                                                             |



 

## Remarks

The **Qualifiers** object cannot be created.

The [**PolicyInformation.Qualifiers**](policyinformation-qualifiers.md) CAPICOM object property returns a **Qualifiers** object.

## Requirements



| Requirement | Value |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| Header<br/>          | <dl> <dt>Iads.h</dt> </dl>      |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



 

 
