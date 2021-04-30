---
description: This section describes the Windows Property System constants, enumerations, and flags.
ms.assetid: ff735b9c-e444-4e6f-8e80-0b2a5d770386
title: Constants, Enumerations, and Flags (Windows Property System)
ms.topic: article
ms.date: 05/31/2018
---

# Constants, Enumerations, and Flags

This section describes the Windows Property System constants, enumerations, and flags.



| Topic                                                                              | Contents                                                                                                                                                                                                                                                                                                                                                                                   |
|------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GETPROPERTYSTOREFLAGS**](/windows/desktop/api/Propsys/ne-propsys-getpropertystoreflags)                             | Indicates flags that modify the property store object retrieved by methods that create a property store, such as [**IShellItem2::GetPropertyStore**](/windows/win32/api/shobjidl_core/nf-shobjidl_core-ishellitem2-getpropertystore) or [**IPropertyStoreFactory::GetPropertyStore**](/windows/win32/api/propsys/nf-propsys-ipropertystorefactory-getpropertystore).<br/>                                                                                        |
| [**PDOPSTATUS**](/windows/win32/api/shobjidl_core/ne-shobjidl_core-pdopstatus)                                                 | Provides operation status flags.<br/>                                                                                                                                                                                                                                                                                                                                                |
| [**PKA\_FLAGS**](/windows/win32/api/propsys/ne-propsys-pka_flags)                                                  | Describes property change array behavior.<br/>                                                                                                                                                                                                                                                                                                                                       |
| [**PROPDESC\_AGGREGATION\_TYPE**](/windows/win32/api/propsys/ne-propsys-propdesc_aggregation_type)                 | Describes how property values are displayed when multiple items are selected. For a particular property, PROPDESC\_AGGREGATION\_TYPE describes how the property should be displayed when multiple items that have a value for the property are selected, such as whether the values should be summed, or averaged, or just displayed with the default "Multiple Values" string.<br/> |
| [**PROPDESC\_COLUMNINDEX\_TYPE**](/windows/win32/api/propsys/ne-propsys-propdesc_columnindex_type)                 | Indicates whether or how a property can be indexed.<br/>                                                                                                                                                                                                                                                                                                                             |
| [**PROPDESC\_CONDITION\_TYPE**](/windows/win32/api/propsys/ne-propsys-propdesc_condition_type)                     | Describes the condition type to use when displaying the property in the query builder UI in Windows Vista, but not in Windows 7 and later.<br/>                                                                                                                                                                                                                                      |
| [**PROPDESC\_ENUMFILTER**](/windows/win32/api/propsys/ne-propsys-propdesc_enumfilter)                              | Describes the filtered list of property descriptions that is returned.<br/>                                                                                                                                                                                                                                                                                                          |
| [**PROPDESC\_FORMAT\_FLAGS**](/windows/win32/api/propsys/ne-propsys-propdesc_format_flags)                         | Used by property description helper functions, such as [**PSFormatForDisplay**](/windows/win32/api/propsys/nf-propsys-psformatfordisplay), to indicate the format of a property string.<br/>                                                                                                                                                                                                                         |
| [**PROPDESC\_RELATIVEDESCRIPTION\_TYPE**](/windows/win32/api/propsys/ne-propsys-propdesc_relativedescription_type) | Describes the relative description type for a property description, as determined by the *relativeDescriptionType* attribute of the [displayInfo](./propdesc-schema-displayinfo.md) element.<br/>                                                                                                                                                                                   |
| [**PROPDESC\_SEARCHINFO\_FLAGS**](/windows/win32/api/propsys/ne-propsys-propdesc_searchinfo_flags)                 | Determines whether and how a property is indexed by Windows Search.<br/>                                                                                                                                                                                                                                                                                                             |
| [**PROPDESC\_TYPE\_FLAGS**](/windows/win32/api/propsys/ne-propsys-propdesc_type_flags)                             | Describes attributes of the [typeInfo](./propdesc-schema-typeinfo.md) element in the property's .propdesc file.<br/>                                                                                                                                                                                                                                                                |
| [**PROPDESC\_VIEW\_FLAGS**](/windows/win32/api/propsys/ne-propsys-propdesc_view_flags)                             | These flags describe properties in property description list strings.<br/>                                                                                                                                                                                                                                                                                                           |
| [**PROPERTYUI\_FLAGS**](/windows/win32/api/shobjidl_core/ne-shobjidl_core-_propertyui_flags)                                    | Specifies property features.<br/>                                                                                                                                                                                                                                                                                                                                                    |
| [**PROPVAR\_COMPARE\_UNIT**](/windows/win32/api/propvarutil/ne-propvarutil-propvar_compare_unit)                           | These flags are associated with certain [**PROPVARIANT**](/windows/win32/api/propidlbase/ns-propidlbase-propvariant) structure comparisons.<br/>                                                                                                                                                                                                                                                                               |
| [**PSC\_STATE**](/windows/win32/api/propsys/ne-propsys-psc_state)                                                  | Specifies the state of a property. They are set manually by the code that is hosting the in-memory property store cache.<br/>                                                                                                                                                                                                                                                        |



 

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

 

 
