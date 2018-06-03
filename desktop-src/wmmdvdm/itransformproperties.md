---
title: ITransformProperties interface
description: The ITransformProperties interface is the collection of child properties (XML elements) of the current property (XML element).
ms.assetid: 38e8d538-3e10-43ba-8718-49323128f599
keywords:
- ITransformProperties interface Windows Movie Maker and DVD Maker
- ITransformProperties interface Windows Movie Maker and DVD Maker , described
topic_type:
- apiref
api_name:
- ITransformProperties
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# ITransformProperties interface

The **ITransformProperties** interface is the collection of child properties (XML elements) of the current property (XML element). Each property, like the XML element it represents, can hold zero or more child properties. **Point** elements are not retrieved in this way, but by calling [**ITransformProperty::get\_Point**](itransformproperty-get-point.md). To get this interface, call **QueryInterface** on an [**ITransformProperty**](itransformproperty.md) interface. If the property has no children, this interface will still be retrieved, but **get\_PropertyCount** will return zero.

## Members

The **ITransformProperties** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **ITransformProperties** also has these types of members:

-   [Methods](#methods)

### Methods

The **ITransformProperties** interface has these methods.



| Method                                                                   | Description                                                                                                           |
|:-------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------|
| [**Clone**](itransformproperties-clone.md)                              | Creates a copy of the current **ITransformProperties** interface.<br/>                                          |
| [**CloneTo**](itransformproperties-cloneto.md)                          | Copies the current **ITransformProperties** interface into a submitted **ITransformProperties** interface.<br/> |
| [**get\_Name**](itransformproperties-get-name.md)                       | Retrieves the name of the current property holding the collection of child properties.<br/>                     |
| [**get\_PropertyByIndex**](itransformproperties-get-propertybyindex.md) | Retrieves a property in the collection by index.<br/>                                                           |
| [**get\_PropertyByName**](itransformproperties-get-propertybyname.md)   | Retrieves a property in the collection by name.<br/>                                                            |
| [**get\_PropertyCount**](itransformproperties-get-propertycount.md)     | Retrieves a count of properties in the collection.<br/>                                                         |



 

## See also

<dl> <dt>

[**Property Management Interfaces**](property-management-interfaces.md)
</dt> </dl>

 

 





