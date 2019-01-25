---
Description: Represents a collection of ExtendedProperty objects.
ms.assetid: '9de25994-9f0b-47a0-b4c8-781aec782f88'
title: ExtendedProperties object
ms.topic: interface
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ExtendedProperties
api_type: 
- COM
api_location: 
- Capicom.dll
---

# ExtendedProperties object

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use Platform Invocation Services (PInvoke) to call the Win32 API function [**CertGetCertificateContextProperty**](/windows/desktop/api/Wincrypt/nf-wincrypt-certgetcertificatecontextproperty) and obtain the properties. For information about PInvoke, see [Platform Invoke Tutorial](https://go.microsoft.com/fwlink/p/?linkid=119531). The [.NET and CryptoAPI via P/Invoke: Part 1](https://go.microsoft.com/fwlink/p/?linkid=119533) and [.NET and CryptoAPI via P/Invoke: Part 2](https://go.microsoft.com/fwlink/p/?linkid=119534) subsections of [Extending .NET Cryptography with CAPICOM and P/Invoke](https://go.microsoft.com/fwlink/p/?linkid=119532) may also be helpful.\]

The **ExtendedProperties** object represents a collection of [**ExtendedProperty**](extendedproperty.md) objects. Each object represents a single extended property.

## When to use

The **ExtendedProperties** object is used to perform the following tasks:

-   Add or remove an [**ExtendedProperty**](extendedproperty.md) object from the collection.
-   Retrieve the number of extended properties in the collection.
-   Retrieve a specific [**ExtendedProperty**](extendedproperty.md) object from the collection.
-   Iterate through the collection.

## Members

The **ExtendedProperties** object has these types of members:

-   [Methods](#methods)
-   [Properties](#extendedproperties-object)

### Methods

The **ExtendedProperties** object has these methods.



| Method                                      | Description                                                                                    |
|:--------------------------------------------|:-----------------------------------------------------------------------------------------------|
| [**Add**](extendedproperties-add.md)       | Adds an [**ExtendedProperty**](extendedproperty.md) object to the collection.<br/>      |
| [**Remove**](extendedproperties-remove.md) | Removes an [**ExtendedProperty**](extendedproperty.md) object from the collection.<br/> |



 

### Properties

The **ExtendedProperties** object has these properties.



| Property                                                   | Access type          | Description                                                                                                                                                                                                                     |
|:-----------------------------------------------------------|:---------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**\_NewEnum**](extendedproperties-newenum.md)<br/> | Read-only<br/> | Retrieves an [**IEnumVARIANT**](https://msdn.microsoft.com/en-us/library/ms221053(v=VS.71).aspx) interface on an object that can be used to enumerate the collection. This property is hidden within Visual Basic Scripting Edition (VBScript).<br/> |
| [**Count**](extendedproperties-count.md)<br/>       | Read-only<br/> | Retrieves the number of [**ExtendedProperty**](extendedproperty.md) objects in the collection.<br/>                                                                                                                      |
| [**Item**](extendedproperties-item.md)<br/>         | Read-only<br/> | Retrieves an [**ExtendedProperty**](extendedproperty.md) object that represents the indexed extended property of the collection. This is the default property.<br/>                                                      |



 

## Remarks

The **ExtendedProperties** object cannot be created.

## Requirements



|                                  |                                                                                        |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



 

 




