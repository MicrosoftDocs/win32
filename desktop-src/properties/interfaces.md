---
Description: This section describes the Windows Property System interfaces.
ms.assetid: d81fe8df-9fd6-4ace-a47f-214cbba6f30c
title: Interfaces
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Interfaces

This section describes the Windows Property System interfaces.



| Topic                                                                                        | Contents                                                                                                                                                                                                                                                                                                                                                                                   |
|----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IPropertyChange**](https://msdn.microsoft.com/library/Bb775244(v=VS.85).aspx)                                                 | Exposes a method that encapsulates a change to a single property.                                                                                                                                                                                                                                                                                                                          |
| [**IPropertyChangeArray**](https://msdn.microsoft.com/library/Bb775223(v=VS.85).aspx)                                       | Exposes methods for several multiple change operations that may be passed to [**IFileOperation**](https://msdn.microsoft.com/en-us/library/Bb775771(v=VS.85).aspx).                                                                                                                                                                                                                                                                   |
| [**IPropertyDescription**](https://msdn.microsoft.com/library/Bb761561(v=VS.85).aspx)                                       | Exposes methods that enumerate and retrieve individual property description details.                                                                                                                                                                                                                                                                                                       |
| [**IPropertyDescription2**](https://msdn.microsoft.com/library/Dd378278(v=VS.85).aspx)                                     | Exposes methods that enumerate and retrieve individual property description details.                                                                                                                                                                                                                                                                                                       |
| [**IPropertyDescriptionAliasInfo**](https://msdn.microsoft.com/library/Bb761517(v=VS.85).aspx)                     | Exposes methods to get the "sort by" columns properties for an item. This interface is used by UI objects that want to retrieve the primary or secondary sort columns for a given property.                                                                                                                                                                                                |
| [**IPropertyDescriptionList**](https://msdn.microsoft.com/library/Bb761511(v=VS.85).aspx)                               | Exposes methods that extract information from a collection of property descriptions presented as a list.                                                                                                                                                                                                                                                                                   |
| [**IPropertyDescriptionRelatedPropertyInfo**](https://msdn.microsoft.com/library/Dd378276(v=VS.85).aspx) | Provides a method that retrives an [**IPropertyDescription**](https://msdn.microsoft.com/library/Bb761561(v=VS.85).aspx) interface.                                                                                                                                                                                                                                                                                       |
| [**IPropertyDescriptionSearchInfo**](https://msdn.microsoft.com/library/Bb761505(v=VS.85).aspx)                   | Exposes search-related information for a property. The information provided by this interface comes from the [propertyDescription](https://msdn.microsoft.com/library/Bb773880(v=VS.85).aspx) schema, [searchInfo](https://msdn.microsoft.com/library/Bb773885(v=VS.85).aspx) element for a given property. This information is used by the Windows Search Indexer. Most calling applications will not need to call this interface. |
| [**IPropertyEnumType**](https://msdn.microsoft.com/library/Bb761495(v=VS.85).aspx)                                             | Exposes methods that extract data from enumeration information. [**IPropertyEnumType**](https://msdn.microsoft.com/library/Bb761495(v=VS.85).aspx) gives access to the [enum](https://msdn.microsoft.com/library/Bb773869(v=VS.85).aspx) and [enumRange](https://msdn.microsoft.com/library/Bb773873(v=VS.85).aspx) elements in the [property schema](https://msdn.microsoft.com/library/Bb773879(v=VS.85).aspx) in a programmatic way at run time.                                                                 |
| [**IPropertyEnumType2**](https://msdn.microsoft.com/library/Dd378274(v=VS.85).aspx)                                           | Exposes methods that extract data from enumeration information. [**IPropertyEnumType2**](https://msdn.microsoft.com/library/Dd378274(v=VS.85).aspx) extends [**IPropertyEnumType**](https://msdn.microsoft.com/library/Bb761495(v=VS.85).aspx).                                                                                                                                                                                                               |
| [**IPropertyEnumTypeList**](https://msdn.microsoft.com/library/Bb761483(v=VS.85).aspx)                                     | Exposes methods that enumerate the possible values for a property.                                                                                                                                                                                                                                                                                                                         |
| [**IPropertyStore**](https://msdn.microsoft.com/library/Bb761474(v=VS.85).aspx)                                                   | Exposes methods for enumerating, getting, and setting property values.                                                                                                                                                                                                                                                                                                                     |
| [**IPropertyStoreCache**](https://msdn.microsoft.com/library/Bb761466(v=VS.85).aspx)                                         | Exposes methods that allow a handler to manage various states for each property.                                                                                                                                                                                                                                                                                                           |
| [**IPropertyStoreCapabilities**](https://msdn.microsoft.com/library/Bb761452(v=VS.85).aspx)                           | Exposes a method that determines whether a property can be edited in the UI by the user.                                                                                                                                                                                                                                                                                                   |
| [**IPropertyStoreFactory**](https://msdn.microsoft.com/library/Bb761450(v=VS.85).aspx)                                     | Exposes methods to get an [**IPropertyStore**](https://msdn.microsoft.com/library/Bb761474(v=VS.85).aspx) object.                                                                                                                                                                                                                                                                                                               |
| [**IPropertySystem**](https://msdn.microsoft.com/library/Bb761437(v=VS.85).aspx)                                                 | Exposes methods that get property descriptions, register and unregister property schemas, enumerate property descriptions, and format property values in a type-strict way.                                                                                                                                                                                                                |
| [**IPropertyUI**](https://msdn.microsoft.com/library/Dd758082(v=VS.85).aspx)                                                         | Developers should use [**IPropertyDescription**](https://msdn.microsoft.com/library/Bb761561(v=VS.85).aspx) instead.                                                                                                                                                                                                                                                                                                      |



 

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

 

 



