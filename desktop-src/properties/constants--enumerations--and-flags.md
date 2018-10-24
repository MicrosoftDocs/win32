---
Description: This section describes the Windows Property System constants, enumerations, and flags.
ms.assetid: ff735b9c-e444-4e6f-8e80-0b2a5d770386
title: Constants, Enumerations, and Flags
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Constants, Enumerations, and Flags

This section describes the Windows Property System constants, enumerations, and flags.



| Topic                                                                              | Contents                                                                                                                                                                                                                                                                                                                                                                                   |
|------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GETPROPERTYSTOREFLAGS**](/windows/desktop/api/Propsys/ne-propsys-getpropertystoreflags)                             | Indicates flags that modify the property store object retrieved by methods that create a property store, such as [**IShellItem2::GetPropertyStore**](https://msdn.microsoft.com/en-us/library/Bb761124(v=VS.85).aspx) or [**IPropertyStoreFactory::GetPropertyStore**](https://msdn.microsoft.com/library/Bb761447(v=VS.85).aspx).<br/>                                                                                        |
| [**PDOPSTATUS**](https://msdn.microsoft.com/library/Bb762519(v=VS.85).aspx)                                                 | Provides operation status flags.<br/>                                                                                                                                                                                                                                                                                                                                                |
| [**PKA\_FLAGS**](https://msdn.microsoft.com/library/Bb762521(v=VS.85).aspx)                                                  | Describes property change array behavior.<br/>                                                                                                                                                                                                                                                                                                                                       |
| [**PROPDESC\_AGGREGATION\_TYPE**](https://msdn.microsoft.com/library/Bb762522(v=VS.85).aspx)                 | Describes how property values are displayed when multiple items are selected. For a particular property, PROPDESC\_AGGREGATION\_TYPE describes how the property should be displayed when multiple items that have a value for the property are selected, such as whether the values should be summed, or averaged, or just displayed with the default "Multiple Values" string.<br/> |
| [**PROPDESC\_COLUMNINDEX\_TYPE**](https://msdn.microsoft.com/library/Bb762587(v=VS.85).aspx)                 | Indicates whether or how a property can be indexed.<br/>                                                                                                                                                                                                                                                                                                                             |
| [**PROPDESC\_CONDITION\_TYPE**](https://msdn.microsoft.com/library/Bb762523(v=VS.85).aspx)                     | Describes the condition type to use when displaying the property in the query builder UI in Windows Vista, but not in Windows 7 and later.<br/>                                                                                                                                                                                                                                      |
| [**PROPDESC\_ENUMFILTER**](https://msdn.microsoft.com/library/Bb762524(v=VS.85).aspx)                              | Describes the filtered list of property descriptions that is returned.<br/>                                                                                                                                                                                                                                                                                                          |
| [**PROPDESC\_FORMAT\_FLAGS**](https://msdn.microsoft.com/library/Bb762525(v=VS.85).aspx)                         | Used by property description helper functions, such as [**PSFormatForDisplay**](https://msdn.microsoft.com/library/Bb776496(v=VS.85).aspx), to indicate the format of a property string.<br/>                                                                                                                                                                                                                         |
| [**PROPDESC\_RELATIVEDESCRIPTION\_TYPE**](https://msdn.microsoft.com/library/Bb762526(v=VS.85).aspx) | Describes the relative description type for a property description, as determined by the *relativeDescriptionType* attribute of the [displayInfo](https://msdn.microsoft.com/library/Bb773865(v=VS.85).aspx) element.<br/>                                                                                                                                                                                   |
| [**PROPDESC\_SEARCHINFO\_FLAGS**](https://msdn.microsoft.com/library/Bb762588(v=VS.85).aspx)                 | Determines whether and how a property is indexed by Windows Search.<br/>                                                                                                                                                                                                                                                                                                             |
| [**PROPDESC\_TYPE\_FLAGS**](https://msdn.microsoft.com/library/Bb762527(v=VS.85).aspx)                             | Describes attributes of the [typeInfo](https://msdn.microsoft.com/library/Bb773889(v=VS.85).aspx) element in the property's .propdesc file.<br/>                                                                                                                                                                                                                                                                |
| [**PROPDESC\_VIEW\_FLAGS**](https://msdn.microsoft.com/library/Bb762528(v=VS.85).aspx)                             | These flags describe properties in property description list strings.<br/>                                                                                                                                                                                                                                                                                                           |
| [**PROPERTYUI\_FLAGS**](https://msdn.microsoft.com/library/Bb762529(v=VS.85).aspx)                                    | Specifies property features.<br/>                                                                                                                                                                                                                                                                                                                                                    |
| [**PROPVAR\_COMPARE\_UNIT**](https://msdn.microsoft.com/library/Bb762530(v=VS.85).aspx)                           | These flags are associated with certain [**PROPVARIANT**](https://msdn.microsoft.com/en-us/library/Aa380072(v=VS.85).aspx) structure comparisons.<br/>                                                                                                                                                                                                                                                                               |
| [**PSC\_STATE**](https://msdn.microsoft.com/library/Bb762531(v=VS.85).aspx)                                                  | Specifies the state of a property. They are set manually by the code that is hosting the in-memory property store cache.<br/>                                                                                                                                                                                                                                                        |



 

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

 

 




