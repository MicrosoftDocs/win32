---
title: Variant Manipulation Functions
description: These functions are provided to allow applications to manipulate VARIANTARG variables.
ms.assetid: f0940eea-077f-4b68-9dac-d49e3fc62e43
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Variant Manipulation Functions

These functions are provided to allow applications to manipulate VARIANTARG variables. Applications that implement [**IDispatch**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-idispatch) should test each VARIANTARG for all permitted types by attempting to coerce the variant to each type using [**VariantChangeType**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-variantchangetype) or [**VariantChangeTypeEx**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-variantchangetypeex). If objects are allowed, the application should always test for object types before other types. If an object type is expected, the application must use **IUnknown::QueryInterface** to test whether the object is the desired type.

Although applications can access and interpret the VARIANTARGs without these functions, using them ensures uniform conversion and coercion rules for all implementers of [**IDispatch**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-idispatch). For example, these functions automatically coerce numeric arguments to strings, and vice versa, when necessary.

Because variants can contain strings, references to scalars, objects, and arrays, all data ownership rules must be followed. All variant manipulation functions should conform to the following rules:

-   Before use, all VARIANTARGs must be initialized by [**VariantInit**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-variantinit).

-   For the types VT\_UI1, VT\_I2, VT\_I4, VT\_R4, VT\_R8, VT\_BOOL, VT\_ERROR, VT\_CY, VT\_DECIMAL, and VT\_DATE, data is stored within the VARIANT structure. Any pointers to the data become invalid when the type of the variant is changed.

-   For VT\_BYREF \| any type, the memory pointed to by the variant is owned and freed by the caller of the function.

-   For VT\_BSTR, there is only one owner for the string. All strings in variants must be allocated with the [**SysAllocString**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-sysallocstring) function. When releasing or changing the type of a variant with the VT\_BSTR type, [**SysFreeString**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-sysfreestring) is called on the contained string.

-   For VT\_ARRAY \| any type, the rule is analogous to the rule for VT\_BSTR. All arrays in variants must be allocated with [**SafeArrayCreate**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-safearraycreate). When releasing or changing the type of a variant with the VT\_ARRAY flag set, [**SafeArrayDestroy**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-safearraydestroy) is called.

-   For VT\_DISPATCH and VT\_UNKNOWN, the objects that are pointed to have reference counts that are incremented when they are placed in a variant. When releasing or changing the type of the variant, **Release** is called on the object that is pointed to.

## In this section



| Topic                                                         | Description                                                                                                                                                       |
|---------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**VariantChangeType**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-variantchangetype)<br/>     | Converts a variant from one type to another.<br/>                                                                                                           |
| [**VariantChangeTypeEx**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-variantchangetypeex)<br/> | Converts a variant from one type to another, using an LCID.<br/>                                                                                            |
| [**VariantClear**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-variantclear)<br/>               | Clears a variant.<br/>                                                                                                                                      |
| [**VariantCopy**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-variantcopy)<br/>                 | Frees the destination variant and makes a copy of the source variant.<br/>                                                                                  |
| [**VariantCopyInd**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-variantcopyind)<br/>           | Frees the destination variant and makes a copy of the source variant, performing the necessary indirection if the source is specified to be VT\_BYREF.<br/> |
| [**VariantInit**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-variantinit)<br/>                 | Initializes a variant.<br/>                                                                                                                                 |



 

> [!Note]  
> If these functions are passed NULL pointers, there will be an access violation and the program will crash. It is your responsibility to protect these functions against NULL pointers.

 

## Related topics

<dl> <dt>

[Conversion and Manipulation Functions](conversion-and-manipulation-functions.md)
</dt> </dl>

 

 





