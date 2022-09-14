---
title: Property Set Serialization
description: There are two versions of the property set serialization format.
ms.assetid: 10544118-5e80-47e2-b75b-c1a43be15b2e
ms.topic: article
ms.date: 05/31/2018
---

# Property Set Serialization

There are two versions of the property set serialization format. The original specification describes version 0 of the format. See [Format Version](format-version.md) for more information. Version 1 extends the original version. All version 0 property sets are valid as version 1 property sets. The **Format Version** field in the header of a serialized property set indicates the version.

The following items identify the differences between version 0 and version 1 property set serialization formats.

-   Support for new **VARTYPE** values. For more information about **VARTYPE** values and how to use them, see the topic [IDispatch Data Types and Structures]( /previous-versions/ms221600(v=vs.100)) and the [**PROPVARIANT**](/windows/win32/api/propidlbase/ns-propidlbase-propvariant) structure.

    The following **VARTYPE** values are not supported in version 0 property sets, but are supported in version 1:

    VT_I1

    VT_VECTOR \| VT_I1

    VT_INT

    VT_UINT

    VT_DECIMAL

    Additionally, SafeArrays can be serialized in a property set. The presence of a SafeArray is indicated by the VT_ARRAY bit combined, using an **OR** operation, with the array elements in the **vt** member of the [**PROPVARIANT**](/windows/win32/api/propidlbase/ns-propidlbase-propvariant) structure. For example, a SafeArray of 4-byte signed integers has a type of VT_ARRAY \| VT_I4.

    The following element types are valid for a SafeArray in a serialized property set:

    |<!--tabular list: col headers unnecessary--> &nbsp; |  &nbsp;        |     &nbsp;        |  &nbsp;         | 
    |-------------|----------|-------------|-----------|
    | VT_I1       | VT_UI1   | VT_I2       | VT_UI2    |
    | VT_I4       | VT_UI4   | VT_INT      | VT_UINT   |
    | VT_R4       | VT_R8    | VT_CY       | VT_DATE   |
    | VT_BSTR     | VT_BOOL  | VT_DECIMAL  | VT_ERROR  |
    | VT_VARIANT  |          |             |           |
    |             |          |             |           |

    When the VT_VARIANT data type is specified, it indicates that the SafeArray itself holds [**PROPVARIANT**](/windows/win32/api/propidlbase/ns-propidlbase-propvariant) structures. The types for these elements must be from the preceding list, except they cannot contain nested VT_VARIANT types.
    
    Note that implementations of [**IPropertyStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertystorage) must be able to recover gracefully by returning an error when a new type is encountered; for example, VARENUM types.

-   Case sensitive property names. Property names, for example those specified in the [**IPropertyStorage::WritePropertyNames**](/windows/desktop/api/Propidl/nf-propidl-ipropertystorage-writepropertynames) method, are not case sensitive in version 0 property sets. In version 1 property sets, property names can be case-sensitive depending on the value of the new Behavior property.

    The Behavior property is [Property ID 0x80000003](/windows/desktop/Stg/reserved-property-identifiers) with a type of VT_UI4. If the lowest bit of this value is set, the property set names are case sensitive. Set the PROPSETFLAG_CASE_SENSITIVE flag in the *grfFlags* parameter of the [**IPropertySetStorage::Create**](/windows/desktop/api/Propidl/nf-propidl-ipropertysetstorage-create) method to specify a case-sensitive property set.

-   Long property names. Property names for version 0 property sets must be less than or equal to 256 characters, including the string terminator, for property sets in the Unicode code page. If not in the Unicode code page, they must be less than 256 bytes. Version 1 property sets, on the other hand, can have property names of unlimited length, although they are still limited by the overall property set size limit of 256 kilobytes (KB).

It is recommended that implementations of [**IPropertyStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertystorage) create and maintain version 0 property sets by default. If a caller subsequently requests a feature specific to the version 1 format, only then should the version of the property set be updated. For example, if a property of type VT_ARRAY is written or if a long property name is written, then the implementation should update the property set format to version 1. One exception to this guideline occurs if the PROPSETFLAG_CASE_SENSITIVE enumeration value is specified in the call to [**IPropertySetStorage::Create**](/windows/desktop/api/Propidl/nf-propidl-ipropertysetstorage-create). In this case, the property set must be created as a version 1 property set.

 

 
