---
Description: Represents a collection of Signer objects.
ms.assetid: 3e28f08a-c4d8-4dd7-953a-e1500eb5bee0
title: Signers object
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Signers
api_type: 
- COM
api_location: 
- Capicom.dll
---

# Signers object

\[The **Signers** object is available for use in the operating systems specified in the Requirements section. Instead, use a collection of CmsSigner objects. For more information, see the [**CmsSigner Class**](https://www.bing.com/search?q=**CmsSigner+Class**) in the [**System.Security.Cryptography.Pkcs**](https://www.bing.com/search?q=**System.Security.Cryptography.Pkcs**) namespace.\]

The **Signers** object represents a collection of [**Signer**](signer.md) objects.

## When to use

The **Signers** object is used to perform the following tasks:

-   Retrieve the number of certificates in the collection.
-   Retrieve a specific **Signers** object from the collection.
-   Iterate through the collection.

## Members

The **Signers** object has these types of members:

-   [Properties](#properties)

### Properties

The **Signers** object has these properties.



| Property                                        | Access type          | Description                                                                                                                                                                                                                     |
|:------------------------------------------------|:---------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**\_NewEnum**](signers-newenum.md)<br/> | Read-only<br/> | Retrieves an [**IEnumVARIANT**](https://msdn.microsoft.com/en-us/library/ms221053(v=VS.71).aspx) interface on an object that can be used to enumerate the collection. This property is hidden within Visual Basic Scripting Edition (VBScript).<br/> |
| [**Count**](signers-count.md)<br/>       | Read-only<br/> | Number of [**Signer**](signer.md) objects in the collection.<br/>                                                                                                                                                        |
| [**Item**](signers-item.md)<br/>         | Read-only<br/> | Retrieves the [**Signer**](signer.md) object that represents the indexed signer. This is the default property.<br/>                                                                                                      |



 

## Remarks

The **Signers** object cannot be created.

## Requirements



|                            |                                                                                        |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**Cryptography Objects**](cryptography-objects.md)
</dt> </dl>

 

 




