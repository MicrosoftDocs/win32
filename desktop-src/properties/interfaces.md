---
description: This section describes the Windows Property System interfaces.
ms.assetid: d81fe8df-9fd6-4ace-a47f-214cbba6f30c
title: Interfaces (Windows Property System)
ms.topic: article
ms.date: 05/31/2018
---

# Interfaces (Windows Property System)

This section describes the Windows Property System interfaces.



| Topic                                                                                        | Contents                                                                                                                                                                                                                                                                                                                                                                                   |
|----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IPropertyChange**](/windows/win32/api/propsys/nn-propsys-ipropertychange)                                                 | Exposes a method that encapsulates a change to a single property.                                                                                                                                                                                                                                                                                                                          |
| [**IPropertyChangeArray**](/windows/win32/api/propsys/nn-propsys-ipropertychangearray)                                       | Exposes methods for several multiple change operations that may be passed to [**IFileOperation**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ifileoperation).                                                                                                                                                                                                                                                                   |
| [**IPropertyDescription**](/windows/win32/api/propsys/nn-propsys-ipropertydescription)                                       | Exposes methods that enumerate and retrieve individual property description details.                                                                                                                                                                                                                                                                                                       |
| [**IPropertyDescription2**](/windows/win32/api/propsys/nn-propsys-ipropertydescription2)                                     | Exposes methods that enumerate and retrieve individual property description details.                                                                                                                                                                                                                                                                                                       |
| [**IPropertyDescriptionAliasInfo**](/windows/win32/api/propsys/nn-propsys-ipropertydescriptionaliasinfo)                     | Exposes methods to get the "sort by" columns properties for an item. This interface is used by UI objects that want to retrieve the primary or secondary sort columns for a given property.                                                                                                                                                                                                |
| [**IPropertyDescriptionList**](/windows/win32/api/propsys/nn-propsys-ipropertydescriptionlist)                               | Exposes methods that extract information from a collection of property descriptions presented as a list.                                                                                                                                                                                                                                                                                   |
| [**IPropertyDescriptionRelatedPropertyInfo**](/windows/win32/api/propsys/nn-propsys-ipropertydescriptionrelatedpropertyinfo) | Provides a method that retrives an [**IPropertyDescription**](/windows/win32/api/propsys/nn-propsys-ipropertydescription) interface.                                                                                                                                                                                                                                                                                       |
| [**IPropertyDescriptionSearchInfo**](/windows/win32/api/propsys/nn-propsys-ipropertydescriptionsearchinfo)                   | Exposes search-related information for a property. The information provided by this interface comes from the [propertyDescription](./propdesc-schema-propertydescription.md) schema, [searchInfo](./propdesc-schema-searchinfo.md) element for a given property. This information is used by the Windows Search Indexer. Most calling applications will not need to call this interface. |
| [**IPropertyEnumType**](/windows/win32/api/propsys/nn-propsys-ipropertyenumtype)                                             | Exposes methods that extract data from enumeration information. [**IPropertyEnumType**](/windows/win32/api/propsys/nn-propsys-ipropertyenumtype) gives access to the [enum](./propdesc-schema-enum.md) and [enumRange](./propdesc-schema-enumrange.md) elements in the [property schema](./propdesc-schema-entry.md) in a programmatic way at run time.                                                                 |
| [**IPropertyEnumType2**](/windows/win32/api/propsys/nn-propsys-ipropertyenumtype2)                                           | Exposes methods that extract data from enumeration information. [**IPropertyEnumType2**](/windows/win32/api/propsys/nn-propsys-ipropertyenumtype2) extends [**IPropertyEnumType**](/windows/win32/api/propsys/nn-propsys-ipropertyenumtype).                                                                                                                                                                                                               |
| [**IPropertyEnumTypeList**](/windows/win32/api/propsys/nn-propsys-ipropertyenumtypelist)                                     | Exposes methods that enumerate the possible values for a property.                                                                                                                                                                                                                                                                                                                         |
| [**IPropertyStore**](/windows/win32/api/propsys/nn-propsys-ipropertystore)                                                   | Exposes methods for enumerating, getting, and setting property values.                                                                                                                                                                                                                                                                                                                     |
| [**IPropertyStoreCache**](/windows/win32/api/propsys/nn-propsys-ipropertystorecache)                                         | Exposes methods that allow a handler to manage various states for each property.                                                                                                                                                                                                                                                                                                           |
| [**IPropertyStoreCapabilities**](/windows/win32/api/propsys/nn-propsys-ipropertystorecapabilities)                           | Exposes a method that determines whether a property can be edited in the UI by the user.                                                                                                                                                                                                                                                                                                   |
| [**IPropertyStoreFactory**](/windows/win32/api/propsys/nn-propsys-ipropertystorefactory)                                     | Exposes methods to get an [**IPropertyStore**](/windows/win32/api/propsys/nn-propsys-ipropertystore) object.                                                                                                                                                                                                                                                                                                               |
| [**IPropertySystem**](/windows/win32/api/propsys/nn-propsys-ipropertysystem)                                                 | Exposes methods that get property descriptions, register and unregister property schemas, enumerate property descriptions, and format property values in a type-strict way.                                                                                                                                                                                                                |
| [**IPropertyUI**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ipropertyui)                                                         | Developers should use [**IPropertyDescription**](/windows/win32/api/propsys/nn-propsys-ipropertydescription) instead.                                                                                                                                                                                                                                                                                                      |



 

## Related topics

<dl> <dt>

[Windows Properties](props.md)
</dt> <dt>

[Property Description Schema](property-description-schema.md)
</dt> <dt>

[Property Sets](property-sets.md)
</dt> <dt>

[Functions](functions.md)
</dt> <dt>

[Structures](structures.md)
</dt> <dt>

[Constants, Enumerations, and Flags](constants--enumerations--and-flags.md)
</dt> </dl>

 

 
