---
Description: 'This section describes the Windows Property System constants, enumerations, and flags.'
ms.assetid: 'ff735b9c-e444-4e6f-8e80-0b2a5d770386'
title: 'Constants, Enumerations, and Flags'
---

# Constants, Enumerations, and Flags

This section describes the Windows Property System constants, enumerations, and flags.



| Topic                                                                              | Contents                                                                                                                                                                                                                                                                                                                                                                                   |
|------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GETPROPERTYSTOREFLAGS**](getpropertystoreflags.md)                             | Indicates flags that modify the property store object retrieved by methods that create a property store, such as [**IShellItem2::GetPropertyStore**](shell.IShellItem2_GetPropertyStore) or [**IPropertyStoreFactory::GetPropertyStore**](shell.IPropertyStoreFactory_GetPropertyStore).<br/>                                                                                        |
| [**PDOPSTATUS**](shell.PDOPSTATUS)                                                 | Provides operation status flags.<br/>                                                                                                                                                                                                                                                                                                                                                |
| [**PKA\_FLAGS**](shell.PKA_FLAGS)                                                  | Describes property change array behavior.<br/>                                                                                                                                                                                                                                                                                                                                       |
| [**PROPDESC\_AGGREGATION\_TYPE**](shell.PROPDESC_AGGREGATION_TYPE)                 | Describes how property values are displayed when multiple items are selected. For a particular property, PROPDESC\_AGGREGATION\_TYPE describes how the property should be displayed when multiple items that have a value for the property are selected, such as whether the values should be summed, or averaged, or just displayed with the default "Multiple Values" string.<br/> |
| [**PROPDESC\_COLUMNINDEX\_TYPE**](shell.PROPDESC_COLUMNINDEX_TYPE)                 | Indicates whether or how a property can be indexed.<br/>                                                                                                                                                                                                                                                                                                                             |
| [**PROPDESC\_CONDITION\_TYPE**](shell.PROPDESC_CONDITION_TYPE)                     | Describes the condition type to use when displaying the property in the query builder UI in Windows Vista, but not in Windows 7 and later.<br/>                                                                                                                                                                                                                                      |
| [**PROPDESC\_ENUMFILTER**](shell.PROPDESC_ENUMFILTER)                              | Describes the filtered list of property descriptions that is returned.<br/>                                                                                                                                                                                                                                                                                                          |
| [**PROPDESC\_FORMAT\_FLAGS**](shell.PROPDESC_FORMAT_FLAGS)                         | Used by property description helper functions, such as [**PSFormatForDisplay**](shell.PSFormatForDisplay), to indicate the format of a property string.<br/>                                                                                                                                                                                                                         |
| [**PROPDESC\_RELATIVEDESCRIPTION\_TYPE**](shell.PROPDESC_RELATIVEDESCRIPTION_TYPE) | Describes the relative description type for a property description, as determined by the *relativeDescriptionType* attribute of the [displayInfo](shell.propdesc_schema_displayInfo) element.<br/>                                                                                                                                                                                   |
| [**PROPDESC\_SEARCHINFO\_FLAGS**](shell.PROPDESC_SEARCHINFO_FLAGS)                 | Determines whether and how a property is indexed by Windows Search.<br/>                                                                                                                                                                                                                                                                                                             |
| [**PROPDESC\_TYPE\_FLAGS**](shell.PROPDESC_TYPE_FLAGS)                             | Describes attributes of the [typeInfo](shell.propdesc_schema_typeInfo) element in the property's .propdesc file.<br/>                                                                                                                                                                                                                                                                |
| [**PROPDESC\_VIEW\_FLAGS**](shell.PROPDESC_VIEW_FLAGS)                             | These flags describe properties in property description list strings.<br/>                                                                                                                                                                                                                                                                                                           |
| [**PROPERTYUI\_FLAGS**](shell.PROPERTYUI_FLAGS)                                    | Specifies property features.<br/>                                                                                                                                                                                                                                                                                                                                                    |
| [**PROPVAR\_COMPARE\_UNIT**](shell.PROPVAR_COMPARE_UNIT)                           | These flags are associated with certain [**PROPVARIANT**](stg.propvariant) structure comparisons.<br/>                                                                                                                                                                                                                                                                               |
| [**PSC\_STATE**](shell.PSC_STATE)                                                  | Specifies the state of a property. They are set manually by the code that is hosting the in-memory property store cache.<br/>                                                                                                                                                                                                                                                        |



 

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

 

 




