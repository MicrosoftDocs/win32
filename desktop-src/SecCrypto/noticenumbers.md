---
description: NoticeNumbers object - Represents a collection of Extension objects.
ms.assetid: b0d69df9-12c4-4872-b883-b029c4350502
title: NoticeNumbers object
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- NoticeNumbers
api_type: 
- COM
api_location: 
- Capicom.dll
---

# NoticeNumbers object

\[The **NoticeNumbers** object is available for use in the operating systems specified in the Requirements section. For more information, see [**Qualifier**](qualifier.md).\]

The **NoticeNumbers** object represents a collection of [**Extension**](extension.md) objects. Each [**Extension**](extension.md) object represents a user notice number.

## When to use

The **NoticeNumbers** object is used to perform the following tasks:

-   Retrieve the number of [**Extension**](extension.md) objects in the collection.
-   Retrieve a specific [**Extension**](extension.md) object from the collection.
-   Iterate through the collection.

## Members

The **NoticeNumbers** object has these types of members:

-   [Properties](#properties)

### Properties

The **NoticeNumbers** object has these properties.



| Property                                              | Access type          | Description                                                                                                                                                                                                                     |
|:------------------------------------------------------|:---------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**\_NewEnum**](noticenumbers-newenum.md)<br/> | Read-only<br/> | Retrieves an [**IEnumVARIANT**](/windows/win32/api/oaidl/nn-oaidl-ienumvariant) interface on an object that can be used to enumerate the collection. This property is hidden within Visual Basic Scripting Edition (VBScript).<br/> |
| [**Count**](noticenumbers-count.md)<br/>       | Read-only<br/> | Retrieves the number of [**Extension**](extension.md) objects in the collection.<br/>                                                                                                                                    |
| [**Item**](noticenumbers-item.md)<br/>         | Read-only<br/> | Retrieves the [**Extension**](extension.md) object that represents the indexed notice number of the collection.<br/> This is the default property.<br/>                                                            |



 

## Remarks

The **NoticeNumbers** object cannot be created.

The NoticeNumbers object is used in the [**Qualifier.NoticeNumbers**](qualifier-noticenumbers.md) property.

## Requirements



| Requirement | Value |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



 

 
