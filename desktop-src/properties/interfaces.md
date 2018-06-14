---
Description: This section describes the Windows Property System interfaces.
ms.assetid: d81fe8df-9fd6-4ace-a47f-214cbba6f30c
title: Interfaces
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Interfaces

This section describes the Windows Property System interfaces.



| Topic                                                                                        | Contents                                                                                                                                                                                                                                                                                                                                                                                   |
|----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IPropertyChange**](https://www.bing.com/search?q=**IPropertyChange**)                                                 | Exposes a method that encapsulates a change to a single property.                                                                                                                                                                                                                                                                                                                          |
| [**IPropertyChangeArray**](https://www.bing.com/search?q=**IPropertyChangeArray**)                                       | Exposes methods for several multiple change operations that may be passed to [**IFileOperation**](https://msdn.microsoft.com/en-us/library/Bb775771(v=VS.85).aspx).                                                                                                                                                                                                                                                                   |
| [**IPropertyDescription**](https://www.bing.com/search?q=**IPropertyDescription**)                                       | Exposes methods that enumerate and retrieve individual property description details.                                                                                                                                                                                                                                                                                                       |
| [**IPropertyDescription2**](https://www.bing.com/search?q=**IPropertyDescription2**)                                     | Exposes methods that enumerate and retrieve individual property description details.                                                                                                                                                                                                                                                                                                       |
| [**IPropertyDescriptionAliasInfo**](https://www.bing.com/search?q=**IPropertyDescriptionAliasInfo**)                     | Exposes methods to get the "sort by" columns properties for an item. This interface is used by UI objects that want to retrieve the primary or secondary sort columns for a given property.                                                                                                                                                                                                |
| [**IPropertyDescriptionList**](https://www.bing.com/search?q=**IPropertyDescriptionList**)                               | Exposes methods that extract information from a collection of property descriptions presented as a list.                                                                                                                                                                                                                                                                                   |
| [**IPropertyDescriptionRelatedPropertyInfo**](https://www.bing.com/search?q=**IPropertyDescriptionRelatedPropertyInfo**) | Provides a method that retrives an [**IPropertyDescription**](https://www.bing.com/search?q=**IPropertyDescription**) interface.                                                                                                                                                                                                                                                                                       |
| [**IPropertyDescriptionSearchInfo**](https://www.bing.com/search?q=**IPropertyDescriptionSearchInfo**)                   | Exposes search-related information for a property. The information provided by this interface comes from the [propertyDescription](https://www.bing.com/search?q=propertyDescription) schema, [searchInfo](https://www.bing.com/search?q=searchInfo) element for a given property. This information is used by the Windows Search Indexer. Most calling applications will not need to call this interface. |
| [**IPropertyEnumType**](https://www.bing.com/search?q=**IPropertyEnumType**)                                             | Exposes methods that extract data from enumeration information. [**IPropertyEnumType**](https://www.bing.com/search?q=**IPropertyEnumType**) gives access to the [enum](https://www.bing.com/search?q=enum) and [enumRange](https://www.bing.com/search?q=enumRange) elements in the [property schema](https://www.bing.com/search?q=property+schema) in a programmatic way at run time.                                                                 |
| [**IPropertyEnumType2**](https://www.bing.com/search?q=**IPropertyEnumType2**)                                           | Exposes methods that extract data from enumeration information. [**IPropertyEnumType2**](https://www.bing.com/search?q=**IPropertyEnumType2**) extends [**IPropertyEnumType**](https://www.bing.com/search?q=**IPropertyEnumType**).                                                                                                                                                                                                               |
| [**IPropertyEnumTypeList**](https://www.bing.com/search?q=**IPropertyEnumTypeList**)                                     | Exposes methods that enumerate the possible values for a property.                                                                                                                                                                                                                                                                                                                         |
| [**IPropertyStore**](https://www.bing.com/search?q=**IPropertyStore**)                                                   | Exposes methods for enumerating, getting, and setting property values.                                                                                                                                                                                                                                                                                                                     |
| [**IPropertyStoreCache**](https://www.bing.com/search?q=**IPropertyStoreCache**)                                         | Exposes methods that allow a handler to manage various states for each property.                                                                                                                                                                                                                                                                                                           |
| [**IPropertyStoreCapabilities**](https://www.bing.com/search?q=**IPropertyStoreCapabilities**)                           | Exposes a method that determines whether a property can be edited in the UI by the user.                                                                                                                                                                                                                                                                                                   |
| [**IPropertyStoreFactory**](https://www.bing.com/search?q=**IPropertyStoreFactory**)                                     | Exposes methods to get an [**IPropertyStore**](https://www.bing.com/search?q=**IPropertyStore**) object.                                                                                                                                                                                                                                                                                                               |
| [**IPropertySystem**](https://www.bing.com/search?q=**IPropertySystem**)                                                 | Exposes methods that get property descriptions, register and unregister property schemas, enumerate property descriptions, and format property values in a type-strict way.                                                                                                                                                                                                                |
| [**IPropertyUI**](https://www.bing.com/search?q=**IPropertyUI**)                                                         | Developers should use [**IPropertyDescription**](https://www.bing.com/search?q=**IPropertyDescription**) instead.                                                                                                                                                                                                                                                                                                      |



 

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

 

 



