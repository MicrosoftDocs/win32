---
Description: This section describes the Windows Property System constants, enumerations, and flags.
ms.assetid: ff735b9c-e444-4e6f-8e80-0b2a5d770386
title: Constants, Enumerations, and Flags
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Constants, Enumerations, and Flags

This section describes the Windows Property System constants, enumerations, and flags.



| Topic                                                                              | Contents                                                                                                                                                                                                                                                                                                                                                                                   |
|------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GETPROPERTYSTOREFLAGS**](/windows/desktop/api/Propsys/ne-propsys-getpropertystoreflags)                             | Indicates flags that modify the property store object retrieved by methods that create a property store, such as [**IShellItem2::GetPropertyStore**](https://msdn.microsoft.com/windows/desktop/706b2551-a9b0-4368-babb-e54cea6d297e) or [**IPropertyStoreFactory::GetPropertyStore**](https://www.bing.com/search?q=**IPropertyStoreFactory::GetPropertyStore**).<br/>                                                                                        |
| [**PDOPSTATUS**](https://www.bing.com/search?q=**PDOPSTATUS**)                                                 | Provides operation status flags.<br/>                                                                                                                                                                                                                                                                                                                                                |
| [**PKA\_FLAGS**](https://www.bing.com/search?q=**PKA\_FLAGS**)                                                  | Describes property change array behavior.<br/>                                                                                                                                                                                                                                                                                                                                       |
| [**PROPDESC\_AGGREGATION\_TYPE**](https://www.bing.com/search?q=**PROPDESC\_AGGREGATION\_TYPE**)                 | Describes how property values are displayed when multiple items are selected. For a particular property, PROPDESC\_AGGREGATION\_TYPE describes how the property should be displayed when multiple items that have a value for the property are selected, such as whether the values should be summed, or averaged, or just displayed with the default "Multiple Values" string.<br/> |
| [**PROPDESC\_COLUMNINDEX\_TYPE**](https://www.bing.com/search?q=**PROPDESC\_COLUMNINDEX\_TYPE**)                 | Indicates whether or how a property can be indexed.<br/>                                                                                                                                                                                                                                                                                                                             |
| [**PROPDESC\_CONDITION\_TYPE**](https://www.bing.com/search?q=**PROPDESC\_CONDITION\_TYPE**)                     | Describes the condition type to use when displaying the property in the query builder UI in Windows Vista, but not in Windows 7 and later.<br/>                                                                                                                                                                                                                                      |
| [**PROPDESC\_ENUMFILTER**](https://www.bing.com/search?q=**PROPDESC\_ENUMFILTER**)                              | Describes the filtered list of property descriptions that is returned.<br/>                                                                                                                                                                                                                                                                                                          |
| [**PROPDESC\_FORMAT\_FLAGS**](https://www.bing.com/search?q=**PROPDESC\_FORMAT\_FLAGS**)                         | Used by property description helper functions, such as [**PSFormatForDisplay**](https://www.bing.com/search?q=**PSFormatForDisplay**), to indicate the format of a property string.<br/>                                                                                                                                                                                                                         |
| [**PROPDESC\_RELATIVEDESCRIPTION\_TYPE**](https://www.bing.com/search?q=**PROPDESC\_RELATIVEDESCRIPTION\_TYPE**) | Describes the relative description type for a property description, as determined by the *relativeDescriptionType* attribute of the [displayInfo](https://www.bing.com/search?q=displayInfo) element.<br/>                                                                                                                                                                                   |
| [**PROPDESC\_SEARCHINFO\_FLAGS**](https://www.bing.com/search?q=**PROPDESC\_SEARCHINFO\_FLAGS**)                 | Determines whether and how a property is indexed by Windows Search.<br/>                                                                                                                                                                                                                                                                                                             |
| [**PROPDESC\_TYPE\_FLAGS**](https://www.bing.com/search?q=**PROPDESC\_TYPE\_FLAGS**)                             | Describes attributes of the [typeInfo](https://www.bing.com/search?q=typeInfo) element in the property's .propdesc file.<br/>                                                                                                                                                                                                                                                                |
| [**PROPDESC\_VIEW\_FLAGS**](https://www.bing.com/search?q=**PROPDESC\_VIEW\_FLAGS**)                             | These flags describe properties in property description list strings.<br/>                                                                                                                                                                                                                                                                                                           |
| [**PROPERTYUI\_FLAGS**](https://www.bing.com/search?q=**PROPERTYUI\_FLAGS**)                                    | Specifies property features.<br/>                                                                                                                                                                                                                                                                                                                                                    |
| [**PROPVAR\_COMPARE\_UNIT**](https://www.bing.com/search?q=**PROPVAR\_COMPARE\_UNIT**)                           | These flags are associated with certain [**PROPVARIANT**](https://msdn.microsoft.com/windows/desktop/e86cc279-826d-4767-8d96-fc8280060ea1) structure comparisons.<br/>                                                                                                                                                                                                                                                                               |
| [**PSC\_STATE**](https://www.bing.com/search?q=**PSC\_STATE**)                                                  | Specifies the state of a property. They are set manually by the code that is hosting the in-memory property store cache.<br/>                                                                                                                                                                                                                                                        |



 

## Related topics

<dl> <dt>

[Windows Properties](props.md)
</dt> <dt>

[Property Description Schema](property-description-schema.md)
</dt> <dt>

[Property Sets](property-sets.md)
</dt> <dt>

[Interfaces](interfaces.md)
</dt> <dt>

[Functions](functions.md)
</dt> <dt>

[Structures](structures.md)
</dt> </dl>

 

 




