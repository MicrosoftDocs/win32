---
Description: Represents a collection of qualifiers.
ms.assetid: aa5e2225-0a39-40bc-868c-d96f5953edaa
title: Qualifiers object
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
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

\[The **Qualifiers** object is available for use in the operating systems specified in the Requirements section. Instead, use the [**X509Extension Class**](https://www.bing.com/search?q=**X509Extension+Class**) in the [**System.Security.Cryptography.X509Certificates**](https://www.bing.com/search?q=**System.Security.Cryptography.X509Certificates**) namespace by calling the constructor that takes an OID as a parameter, and then use the OID for Certificate Policies to process qualifiers that are part of the policy information in the Certificate Policies extension.\]

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
| [**\_NewEnum**](qualifiers-newenum.md)<br/> | Read-only<br/> | Retrieves an [**IEnumVARIANT**](https://msdn.microsoft.com/en-us/library/ms221053(v=VS.71).aspx) interface on an object that can be used to enumerate the collection. This property is hidden within Visual Basic Scripting Edition (VBScript).<br/> |
| [**Count**](qualifiers-count.md)<br/>       | Read-only<br/> | Retrieves the number of qualifiers in the collection.<br/>                                                                                                                                                                |
| [**Item**](qualifiers-item.md)<br/>         | Read-only<br/> | Retrieves a [**Qualifier**](qualifier.md) object that represents the indexed qualifier of the collection. This is the default property.<br/>                                                                             |



 

## Remarks

The **Qualifiers** object cannot be created.

The [**PolicyInformation.Qualifiers**](policyinformation-qualifiers.md) CAPICOM object property returns a **Qualifiers** object.

## Requirements



|                            |                                                                                        |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| Header<br/>          | <dl> <dt>Iads.h</dt> </dl>      |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



 

 




