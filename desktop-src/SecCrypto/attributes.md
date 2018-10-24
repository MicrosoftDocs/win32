---
Description: Represents a collection of Attribute objects.
ms.assetid: 6116e61e-3ec5-4992-90ab-e3c7ced291b6
title: Attributes object
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Attributes object

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, Windows XP. Instead, use the [**CryptographicAttributeObjectCollection Class**](https://msdn.microsoft.com/library/ms147988(v=VS.100).aspx) in the [**System.Security.Cryptography**](https://msdn.microsoft.com/library/9eat8fht(v=VS.100).aspx) namespace.\]

The **Attributes** object represents a collection of [**Attribute**](attribute.md) objects. Each [**Attribute**](attribute.md) object represents a single attribute of a message.

## When to use

The **Attributes** object is used to perform the following tasks:

-   Add or remove a specific [**Attribute**](attribute.md) object from the collection.
-   Clear the collection.
-   Retrieve the number of attributes in the collection.
-   Retrieve a specific [**Attribute**](attribute.md) object from the collection.
-   Iterate through the collection.

## Members

The **Attributes** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Attributes** object has these methods.



| Method                              | Description                                                                       |
|:------------------------------------|:----------------------------------------------------------------------------------|
| [**Add**](attributes-add.md)       | Adds an [**Attribute**](attribute.md) object to the collection.<br/>       |
| [**Clear**](attributes-clear.md)   | Clears all [**Attribute**](attribute.md) objects from the collection.<br/> |
| [**Remove**](attributes-remove.md) | Removes an [**Attribute**](attribute.md) object from the collection.<br/>  |



 

### Properties

The **Attributes** object has these properties.



| Property                                           | Access type          | Description                                                                                                                                                                                                                     |
|:---------------------------------------------------|:---------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**\_NewEnum**](attributes-newenum.md)<br/> | Read-only<br/> | Retrieves an [**IEnumVARIANT**](https://msdn.microsoft.com/en-us/library/ms221053(v=VS.71).aspx) interface on an object that can be used to enumerate the collection. This property is hidden within Visual Basic Scripting Edition (VBScript).<br/> |
| [**Count**](attributes-count.md)<br/>       | Read-only<br/> | Retrieves the number of [**Attribute**](attribute.md) objects in the collection.<br/>                                                                                                                                    |
| [**Item**](attributes-item.md)<br/>         | Read-only<br/> | Retrieves the [**Attribute**](attribute.md) object that represents the indexed attribute. This is the default property.<br/>                                                                                             |



 

## Remarks

The **Attributes** object cannot be created.

## Requirements



|                                  |                                                                                        |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[Cryptography Objects](cryptography-objects.md)
</dt> </dl>

 

 




