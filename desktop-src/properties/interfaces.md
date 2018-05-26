---
Description: This section describes the Windows Property System interfaces.
ms.assetid: d81fe8df-9fd6-4ace-a47f-214cbba6f30c
title: Interfaces
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Interfaces

This section describes the Windows Property System interfaces.



| Topic                                                                                        | Contents                                                                                                                                                                                                                                                                                                                                                                                   |
|----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IPropertyChange**](shell.IPropertyChange)                                                 | Exposes a method that encapsulates a change to a single property.                                                                                                                                                                                                                                                                                                                          |
| [**IPropertyChangeArray**](shell.IPropertyChangeArray)                                       | Exposes methods for several multiple change operations that may be passed to [**IFileOperation**](shell.IFileOperation).                                                                                                                                                                                                                                                                   |
| [**IPropertyDescription**](shell.IPropertyDescription)                                       | Exposes methods that enumerate and retrieve individual property description details.                                                                                                                                                                                                                                                                                                       |
| [**IPropertyDescription2**](shell.IPropertyDescription2)                                     | Exposes methods that enumerate and retrieve individual property description details.                                                                                                                                                                                                                                                                                                       |
| [**IPropertyDescriptionAliasInfo**](shell.IPropertyDescriptionAliasInfo)                     | Exposes methods to get the "sort by" columns properties for an item. This interface is used by UI objects that want to retrieve the primary or secondary sort columns for a given property.                                                                                                                                                                                                |
| [**IPropertyDescriptionList**](shell.IPropertyDescriptionList)                               | Exposes methods that extract information from a collection of property descriptions presented as a list.                                                                                                                                                                                                                                                                                   |
| [**IPropertyDescriptionRelatedPropertyInfo**](shell.IPropertyDescriptionRelatedPropertyInfo) | Provides a method that retrives an [**IPropertyDescription**](shell.IPropertyDescription) interface.                                                                                                                                                                                                                                                                                       |
| [**IPropertyDescriptionSearchInfo**](shell.IPropertyDescriptionSearchInfo)                   | Exposes search-related information for a property. The information provided by this interface comes from the [propertyDescription](shell.propdesc_schema_propertyDescription) schema, [searchInfo](shell.propdesc_schema_searchInfo) element for a given property. This information is used by the Windows Search Indexer. Most calling applications will not need to call this interface. |
| [**IPropertyEnumType**](shell.IPropertyEnumType)                                             | Exposes methods that extract data from enumeration information. [**IPropertyEnumType**](shell.IPropertyEnumType) gives access to the [enum](shell.propdesc_schema_enum) and [enumRange](shell.propdesc_schema_enumRange) elements in the [property schema](shell.propdesc_schema_entry) in a programmatic way at run time.                                                                 |
| [**IPropertyEnumType2**](shell.IPropertyEnumType2)                                           | Exposes methods that extract data from enumeration information. [**IPropertyEnumType2**](shell.IPropertyEnumType2) extends [**IPropertyEnumType**](shell.IPropertyEnumType).                                                                                                                                                                                                               |
| [**IPropertyEnumTypeList**](shell.IPropertyEnumTypeList)                                     | Exposes methods that enumerate the possible values for a property.                                                                                                                                                                                                                                                                                                                         |
| [**IPropertyStore**](shell.IPropertyStore)                                                   | Exposes methods for enumerating, getting, and setting property values.                                                                                                                                                                                                                                                                                                                     |
| [**IPropertyStoreCache**](shell.IPropertyStoreCache)                                         | Exposes methods that allow a handler to manage various states for each property.                                                                                                                                                                                                                                                                                                           |
| [**IPropertyStoreCapabilities**](shell.IPropertyStoreCapabilities)                           | Exposes a method that determines whether a property can be edited in the UI by the user.                                                                                                                                                                                                                                                                                                   |
| [**IPropertyStoreFactory**](shell.IPropertyStoreFactory)                                     | Exposes methods to get an [**IPropertyStore**](shell.IPropertyStore) object.                                                                                                                                                                                                                                                                                                               |
| [**IPropertySystem**](shell.IPropertySystem)                                                 | Exposes methods that get property descriptions, register and unregister property schemas, enumerate property descriptions, and format property values in a type-strict way.                                                                                                                                                                                                                |
| [**IPropertyUI**](shell.IPropertyUI)                                                         | Developers should use [**IPropertyDescription**](shell.IPropertyDescription) instead.                                                                                                                                                                                                                                                                                                      |



 

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

 

 



