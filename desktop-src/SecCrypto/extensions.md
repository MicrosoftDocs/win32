---
description: Represents a collection of Extension objects.
ms.assetid: 'f2a6854d-1831-489f-adf6-31a0b26511e3'
title: Extensions object
ms.topic: article
ms.date: 05/31/2018
---

# Extensions object

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the [**X509ExtensionCollection Class**](/dotnet/api/system.security.cryptography.x509certificates.x509extensioncollection) in the [**System.Security.Cryptography.X509Certificates**](/dotnet/api/system.security.cryptography.x509certificates.publickey.-ctor) namespace.\]

The **Extensions** object represents a collection of [**Extension**](extension.md) objects. Each [**Extension**](extension.md) object represents a single certificate extension.

## When to use

The **Extensions** object is used to perform the following tasks:

-   Retrieve the number of certificate extensions in the collection.
-   Retrieve a specific [**Extension**](extension.md) object from the collection.
-   Iterate through the collection.

## Members

The **Extensions** object has these types of members:

-   [Properties](#properties)

### Properties

The **Extensions** object has these properties.



| Property                                           | Access type          | Description                                                                                                                                                                                                                     |
|:---------------------------------------------------|:---------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**\_NewEnum**](extensions-newenum.md)<br/> | Read-only<br/> | Retrieves an [**IEnumVARIANT**](/windows/win32/api/oaidl/nn-oaidl-ienumvariant) interface on an object that can be used to enumerate the collection. This property is hidden within Visual Basic Scripting Edition (VBScript).<br/> |
| [**Count**](extensions-count.md)<br/>       | Read-only<br/> | Retrieves the number of [**Extension**](extension.md) objects in the collection.<br/>                                                                                                                                    |
| [**Item**](extensions-item.md)<br/>         | Read-only<br/> | Retrieves the [**Extension**](extension.md) object that represents the indexed certificate extension of the collection. This is the default property.<br/>                                                               |



 

## Remarks

The **Extensions** object is returned by the [**Certificate.Extensions**](certificate-extensions.md) method.

The **Extensions** object cannot be created.

## Requirements



| Requirement | Value |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



 

 
