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

-   Support for new **VARTYPE** values. For more information about **VARTYPE** values and how to use them, see the topic [IDispatch Data Types and Structures]( https://go.microsoft.com/fwlink/p/?linkid=124543) and the [**PROPVARIANT**](https://msdn.microsoft.com/library/Aa380072(v=VS.85).aspx) structure.

    The following **VARTYPE** values are not supported in version 0 property sets, but are supported in version 1:

    VT\_I1

    VT\_VECTOR \| VT\_I1

    VT\_INT

    VT\_UINT

    VT\_DECIMAL

    Additionally, SafeArrays can be serialized in a property set. The presence of a SafeArray is indicated by the VT\_ARRAY bit combined, using an **OR** operation, with the array elements in the **vt** member of the [**PROPVARIANT**](https://msdn.microsoft.com/library/Aa380072(v=VS.85).aspx) structure. For example, a SafeArray of 4-byte signed integers has a type of VT\_ARRAY \| VT\_I4.

    The following element types are valid for a SafeArray in a serialized property set:



|             |          |             |           |
|-------------|----------|-------------|-----------|
| VT\_I1      | VT\_UI1  | VT\_I2      | VT\_UI2   |
| VT\_I4      | VT\_UI4  | VT\_INT     | VT\_UINT  |
| VT\_R4      | VT\_R8   | VT\_CY      | VT\_DATE  |
| VT\_BSTR    | VT\_BOOL | VT\_DECIMAL | VT\_ERROR |
| VT\_VARIANT |          |             |           |



 

When the VT\_VARIANT data type is specified, it indicates that the SafeArray itself holds [**PROPVARIANT**](https://msdn.microsoft.com/library/Aa380072(v=VS.85).aspx) structures. The types for these elements must be from the preceding list, except they cannot contain nested VT\_VARIANT types.

Note that implementations of [**IPropertyStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertystorage) must be able to recover gracefully by returning an error when a new type is encountered; for example, VARENUM types.

-   Case sensitive property names. Property names, for example those specified in the [**IPropertyStorage::WritePropertyNames**](/windows/desktop/api/Propidl/nf-propidl-ipropertystorage-writepropertynames) method, are not case sensitive in version 0 property sets. In version 1 property sets, property names can be case-sensitive depending on the value of the new Behavior property.

    The Behavior property is [Property ID 0x80000003](https://docs.microsoft.com/windows/desktop/Stg/reserved-property-identifiers) with a type of VT\_UI4. If the lowest bit of this value is set, the property set names are case sensitive. Set the PROPSETFLAG\_CASE\_SENSITIVE flag in the *grfFlags* parameter of the [**IPropertySetStorage::Create**](/windows/desktop/api/Propidl/nf-propidl-ipropertysetstorage-create) method to specify a case-sensitive property set.

-   Long property names. Property names for version 0 property sets must be less than or equal to 256 characters, including the string terminator, for property sets in the Unicode code page. If not in the Unicode code page, they must be less than 256 bytes. Version 1 property sets, on the other hand, can have property names of unlimited length, although they are still limited by the overall property set size limit of 256 kilobytes (KB).

It is recommended that implementations of [**IPropertyStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertystorage) create and maintain version 0 property sets by default. If a caller subsequently requests a feature specific to the version 1 format, only then should the version of the property set be updated. For example, if a property of type VT\_ARRAY is written or if a long property name is written, then the implementation should update the property set format to version 1. One exception to this guideline occurs if the PROPSETFLAG\_CASE\_SENSITIVE enumeration value is specified in the call to [**IPropertySetStorage::Create**](/windows/desktop/api/Propidl/nf-propidl-ipropertysetstorage-create). In this case, the property set must be created as a version 1 property set.

 

 




