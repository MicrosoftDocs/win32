---
title: ITransformPropertiesConfig interface
description: The ITransformPropertiesConfig interface is used to create, add, and remove properties from a collection. To get this interface, query ITransformProperty or ITransformProperties.
ms.assetid: 'b94c1a44-495d-4446-aa9e-b9479079f44c'
keywords: ["ITransformPropertiesConfig interface Windows Movie Maker and DVD Maker", "ITransformPropertiesConfig interface Windows Movie Maker and DVD Maker , described"]
topic_type:
- apiref
api_name:
- ITransformPropertiesConfig
api_type:
- COM
---

# ITransformPropertiesConfig interface

The **ITransformPropertiesConfig** interface is used to create, add, and remove properties from a collection. To get this interface, query [**ITransformProperty**](itransformproperty.md) or [**ITransformProperties**](itransformproperties.md).

## Members

The **ITransformPropertiesConfig** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **ITransformPropertiesConfig** also has these types of members:

-   [Methods](#methods)

### Methods

The **ITransformPropertiesConfig** interface has these methods.



| Method                                                                            | Description                                                                       |
|:----------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|
| [**AddProperty**](itransformpropertiesconfig-addproperty.md)                     | Adds a previously created property to the current collection.<br/>          |
| [**CreateProperty**](itransformpropertiesconfig-createproperty.md)               | Creates a new property and adds it to the current property collection.<br/> |
| [**RemoveAllProperties**](itransformpropertiesconfig-removeallproperties.md)     | Clears all properties from the current collection.<br/>                     |
| [**RemovePropertyByIndex**](itransformpropertiesconfig-removepropertybyindex.md) | Removes a property from the current collection by index number.<br/>        |
| [**RemovePropertyByName**](itransformpropertiesconfig-removepropertybyname.md)   | Removes a property from the current property collection by name.<br/>       |
| [**SetPropertyValue**](itransformpropertiesconfig-setpropertyvalue.md)           | Assigns a property with a time point to a collection.<br/>                  |



 

## See also

<dl> <dt>

[**Property Management Interfaces**](property-management-interfaces.md)
</dt> </dl>

 

 





