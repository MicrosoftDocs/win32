---
title: BSTR and Vector Conversion Functions
description: Automation supports conversion between an array of bytes and a BSTR through the two low-level conversion functions VectorFromBstr and BstrFromVector, and by performing the appropriate conversions in VariantChangeType, ITypeInfo Invoke, DispInvoke, and other relevant locations.
ms.assetid: '482c0e05-2841-446a-a2d0-015ae55c806e'
---

# BSTR and Vector Conversion Functions

Automation supports conversion between an array of bytes and a BSTR through the two low-level conversion functions [**VectorFromBstr**](vectorfrombstr.md) and [**BstrFromVector**](bstrfromvector.md), and by performing the appropriate conversions in [**VariantChangeType**](variantchangetype.md), [**ITypeInfo::Invoke**](itypeinfo-invoke.md), [**DispInvoke**](dispinvoke.md), and other relevant locations.

BSTRs are wide, double-byte (Unicode) strings on 32-bit Windows platforms, and narrow, single-byte strings on 16-bit Windows and the Apple PowerMac. These functions do not perform any special string handling. They simply move bytes from one location to another, so the width of strings does not affect these API functions.

## In this section



| Topic                                               | Description                                                                                    |
|-----------------------------------------------------|------------------------------------------------------------------------------------------------|
| [**BstrFromVector**](bstrfromvector.md)<br/> | Returns a BSTR, assigning each element of the vector to a character in the BSTR.<br/>    |
| [**SetOaNoCache**](setoanocache.md)<br/>     | Disables the **BSTR** caching in OleAut32.dll. <br/>                                     |
| [**VarBstrCat**](varbstrcat.md)<br/>         | Concatenates two variants of type BSTR and returns the resulting BSTR.<br/>              |
| [**VarBstrCmp**](varbstrcmp.md)<br/>         | Compares two variants of type BSTR.<br/>                                                 |
| [**VectorFromBstr**](vectorfrombstr.md)<br/> | Returns a vector, assigning each character in the BSTR to an element of the vector.<br/> |



 

> [!Note]  
> If these functions are passed NULL pointers, there will be an access violation and the program will crash. It is your responsibility to protect these functions against NULL pointers.

 

## Related topics

<dl> <dt>

[Conversion and Manipulation Functions](conversion-and-manipulation-functions.md)
</dt> </dl>

 

 





