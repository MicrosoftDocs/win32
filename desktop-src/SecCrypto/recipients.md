---
Description: Represents a collection of Certificate objects.
ms.assetid: '11d294b5-0a8a-4970-be10-a3b22389d96e'
title: Recipients object
ms.topic: interface
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- Recipients
api_type:
- COM
api_location:
- Capicom.dll
---

# Recipients object

\[The **Recipients** object is available for use in the operating systems specified in the Requirements section. Instead, use the [**CmsRecipientCollection Class**](https://msdn.microsoft.com/library/0y59h9e9(v=VS.100).aspx) in the [**System.Security.Cryptography.Pkcs**](https://msdn.microsoft.com/library/6see7k14(v=VS.100).aspx) namespace.\]

The **Recipients** object represents a collection of [**Certificate**](certificate.md) objects. Each object represents an intended recipient of the enveloped message. Data in an [**EnvelopedData**](envelopeddata.md) object is encrypted with a [*symmetric*](https://msdn.microsoft.com/en-us/library/ms721625(v=VS.85).aspx) session key, and that symmetric session key is then itself encrypted for each recipient by using the public key from that intended recipient's certificate. A recipient with access to the [*private key*](https://msdn.microsoft.com/en-us/library/ms721603(v=VS.85).aspx) associated with a certificate's [*public key*](https://msdn.microsoft.com/en-us/library/ms721603(v=VS.85).aspx) can decrypt the [*session key*](https://msdn.microsoft.com/en-us/library/ms721625(v=VS.85).aspx) and use the decrypted session key to decrypt the actual data.

## When to use

The **Recipients** object is used to perform the following tasks:

-   Add or remove a [**Certificate**](certificate.md) object from the collection.
-   Retrieve the number of certificates in the collection.
-   Retrieve a specific **Recipients** object from the collection.
-   Iterate through the collection.

## Members

The **Recipients** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Recipients** object has these methods.



| Method                              | Description                                                                            |
|:------------------------------------|:---------------------------------------------------------------------------------------|
| [**Add**](recipients-add.md)       | Adds a [**Certificate**](certificate.md) object to the collection.<br/>         |
| [**Clear**](recipients-clear.md)   | Removes all [**Certificate**](certificate.md) objects from the collection.<br/> |
| [**Remove**](recipients-remove.md) | Removes a [**Certificate**](certificate.md) object from the collection.<br/>    |



 

### Properties

The **Recipients** object has these properties.



| Property                                           | Access type          | Description                                                                                                                                                                                                                     |
|:---------------------------------------------------|:---------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**\_NewEnum**](recipients-newenum.md)<br/> | Read-only<br/> | Retrieves an [**IEnumVARIANT**](https://msdn.microsoft.com/en-us/library/ms221053(v=VS.71).aspx) interface on an object that can be used to enumerate the collection. This property is hidden within Visual Basic Scripting Edition (VBScript).<br/> |
| [**Count**](recipients-count.md)<br/>       |                      | The number of objects in the **Recipients** collection.<br/>                                                                                                                                                              |
| [**Item**](recipients-item.md)<br/>         |                      | An indexed object in the collection. This is the default property.<br/>                                                                                                                                                   |



 

## Remarks

The **Recipients** object cannot be created.

## Requirements



|                            |                                                                                        |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**Cryptography Objects**](cryptography-objects.md)
</dt> </dl>

 

 




