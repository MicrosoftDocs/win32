---
title: Objects and Properties
description: The characteristics of an object in SDO are determined by the object's properties, and the values associated with those properties.
ms.assetid: 9faa7759-cad5-4429-94b0-6cba145cfadb
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Objects and Properties

The characteristics of an object in SDO are determined by the object's properties, and the values associated with those properties. Unlike some other object models, SDO objects themselves do not have methods. However, SDO objects do expose COM interfaces that provide methods.

Objects in SDO expose the [**ISdo**](/windows/desktop/api/sdoias/nn-sdoias-isdo) interface that provides methods for manipulating the objects properties. To access the object's properties, obtain an **ISdo** interface for the object, and use the [**GetProperty**](/windows/desktop/api/sdoias/nf-sdoias-isdo-getproperty) and [**PutProperty**](/windows/desktop/api/sdoias/nf-sdoias-isdo-putproperty) interface methods to retrieve and set values for the properties. The topic [Retrieving a User SDO](/windows/desktop/Nps/sdo-retrieving-a-user-sdo) contains sample code that demonstrates obtaining the **ISdo** interface for a User object.

After making changes to the properties of an object, use the [**ISdo::Apply**](/windows/desktop/api/sdoias/nf-sdoias-isdo-apply) method to write the changes to persistent storage for the object. You can cancel changes made to an object's properties before you call **ISdo::Apply** by calling the [**ISdo::Restore**](/windows/desktop/api/sdoias/nf-sdoias-isdo-restore) method. This method restores the values of an object's properties from persistent storage.

The following table shows the enumeration types that enumerate the properties of some of the objects in SDO.



| Object                                 | Enumeration type                                       |
|----------------------------------------|--------------------------------------------------------|
| All SDO objects                        | [**IASCOMMONPROPERTIES**](/windows/desktop/api/sdoias/ne-sdoias-iascommonproperties) |
| User Object                            | [**USERPROPERTIES**](/windows/desktop/api/sdoias/ne-sdoias-userproperties)           |
| Service Object (Network Policy Server) | [**IASPROPERTIES**](/windows/desktop/api/sdoias/ne-sdoias-iasproperties)             |
| Microsoft RADIUS Protocol Object       | [**RADIUSPROPERTIES**](/windows/desktop/api/sdoias/ne-sdoias-radiusproperties)       |



 

> [!Note]  
> Internet Authentication Service (IAS) was renamed Network Policy Server (NPS) starting with Windows Server 2008.

 

## Collections

Objects are often grouped into collections. The SDO API provides functionality, through the [**ISdo Collection**](/windows/desktop/api/sdoias/nn-sdoias-isdocollection) interface, to enumerate the objects in a collection and to add and delete objects from a collection.

Access to a collection is obtained by retrieving a collection property on the object that contains the collection. For more information, see the section [Object Model Hierarchy](/windows/desktop/Nps/sdo-object-model-hierarchy).

The data type for all properties that correspond to collections is VT\_DISPATCH.

## Related topics

<dl> <dt>

[SDO Object Model Hierarchy](/windows/desktop/Nps/sdo-object-model-hierarchy)
</dt> <dt>

[SDO Supported Attributes](/windows/desktop/Nps/sdo-sdo-supported-attributes)
</dt> </dl>

 

 