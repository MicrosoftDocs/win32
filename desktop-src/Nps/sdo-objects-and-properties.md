---
title: Objects and Properties
description: The characteristics of an object in SDO are determined by the object's properties, and the values associated with those properties.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 9faa7759-cad5-4429-94b0-6cba145cfadb
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Objects and Properties

The characteristics of an object in SDO are determined by the object's properties, and the values associated with those properties. Unlike some other object models, SDO objects themselves do not have methods. However, SDO objects do expose COM interfaces that provide methods.

Objects in SDO expose the [**ISdo**](https://msdn.microsoft.com/library/bb960639) interface that provides methods for manipulating the objects properties. To access the object's properties, obtain an **ISdo** interface for the object, and use the [**GetProperty**](https://msdn.microsoft.com/library/bb960671) and [**PutProperty**](https://msdn.microsoft.com/library/bb960674) interface methods to retrieve and set values for the properties. The topic [Retrieving a User SDO](https://msdn.microsoft.com/library/bb960710) contains sample code that demonstrates obtaining the **ISdo** interface for a User object.

After making changes to the properties of an object, use the [**ISdo::Apply**](https://msdn.microsoft.com/library/bb960670) method to write the changes to persistent storage for the object. You can cancel changes made to an object's properties before you call **ISdo::Apply** by calling the [**ISdo::Restore**](https://msdn.microsoft.com/library/bb960676) method. This method restores the values of an object's properties from persistent storage.

The following table shows the enumeration types that enumerate the properties of some of the objects in SDO.



| Object                                 | Enumeration type                                       |
|----------------------------------------|--------------------------------------------------------|
| All SDO objects                        | [**IASCOMMONPROPERTIES**](https://msdn.microsoft.com/library/bb960631) |
| User Object                            | [**USERPROPERTIES**](https://msdn.microsoft.com/library/bb960719)           |
| Service Object (Network Policy Server) | [**IASPROPERTIES**](https://msdn.microsoft.com/library/bb960636)             |
| Microsoft RADIUS Protocol Object       | [**RADIUSPROPERTIES**](https://msdn.microsoft.com/library/bb960699)       |



 

> [!Note]  
> Internet Authentication Service (IAS) was renamed Network Policy Server (NPS) starting with Windows Server 2008.

 

## Collections

Objects are often grouped into collections. The SDO API provides functionality, through the [**ISdo Collection**](https://msdn.microsoft.com/library/bb960640) interface, to enumerate the objects in a collection and to add and delete objects from a collection.

Access to a collection is obtained by retrieving a collection property on the object that contains the collection. For more information, see the section [Object Model Hierarchy](https://msdn.microsoft.com/library/bb960691).

The data type for all properties that correspond to collections is VT\_DISPATCH.

## Related topics

<dl> <dt>

[SDO Object Model Hierarchy](https://msdn.microsoft.com/library/bb960691)
</dt> <dt>

[SDO Supported Attributes](https://msdn.microsoft.com/library/bb960711)
</dt> </dl>

 

 




