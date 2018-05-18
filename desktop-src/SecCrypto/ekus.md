---
Description: 'Represents a collection of EKU objects.'
ms.assetid: '04b9f0bf-e1d4-4a2c-be5d-bae7c1090bdb'
title: EKUs object
---

# EKUs object

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the [**X509ExtensionCollection Class**](T:System.Security.Cryptography.X509Certificates.X509ExtensionCollection) in the [**System.Security.Cryptography.X509Certificates**](frlrfSystemSecurityCryptographyX509Certificates) namespace.\]

The **EKUs** object represents a collection of [**EKU**](eku.md) objects. Each [**EKU**](eku.md) object represents a single extended key usage (EKU) property of a certificate.

## When to use

The **EKUs** collection is used to perform the following tasks:

-   Retrieve the number of EKU properties in the collection.
-   Retrieve a specific [**EKU**](eku.md) object from the collection.
-   Iterate through the collection.

## Members

The **EKUs** object has these types of members:

-   [Properties](#properties)

### Properties

The **EKUs** object has these properties.



| Property                                     | Access type          | Description                                                                                                                                                                                                                     |
|:---------------------------------------------|:---------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**\_NewEnum**](ekus-newenum.md)<br/> | Read-only<br/> | Retrieves an [**IEnumVARIANT**](139e3c93-faef-4003-9079-e0e94494db3e) interface on an object that can be used to enumerate the collection. This property is hidden within Visual Basic Scripting Edition (VBScript).<br/> |
| [**Count**](ekus-count.md)<br/>       | Read-only<br/> | Retrieves the number of [**EKU**](eku.md) objects in the collection.<br/>                                                                                                                                                |
| [**Item**](ekus-item.md)<br/>         | Read-only<br/> | Retrieves the [**EKU**](eku.md) object that represents the indexed EKU property. This is the default property.<br/>                                                                                                      |



 

## Remarks

This collection is retrieved by the [**ExtendedKeyUsage.EKUs**](extendedkeyusage-ekus.md) property.

The **EKUs** object cannot be created.

## Requirements



|                                  |                                                                                        |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



 

 




