---
title: Arrays (RPC) (TFS)
description: Remote Procedure Call (RPC) array categories include fixed-size, conformant, conformant varying, varying, and complex.
ms.assetid: 7144ec87-90f2-463a-80e4-28cb4771325f
ms.topic: article
ms.date: 05/31/2018
---

# Arrays (RPC)

Several array categories have been defined based on their performance characteristics, primarily whether the array can be block-copied.

For some categories, such as a fixed-size array, two types of array descriptors exist; they are indicated by an in-fix in the name of the leading FC token.



| Format character | Description                                                           |
|------------------|-----------------------------------------------------------------------|
| SM               | The type's total size can be represented in a 16-bit unsigned int.    |
| LG               | The type's total size needs a 32-bit unsigned long to be represented. |



 

Fields common to arrays:

-   total\_size

    Total size of the array in memory, in bytes. This is the same as wire size after alignment. The total size is calculated for categories for which the padding issue does not exist and the size is actual array size.

-   element\_size

    Total size in memory of a single element of the array, including padding (this may happen for complex arrays only).

-   element\_description

    Description of the array element type.

-   pointer\_layout

    See the [Pointer Layout](pointer-layout-tfs.md) topic for more information.

## Fixed-sized Arrays

A fixed-sized array format string is generated for arrays that have a known size, and therefore may be block-copied to the marshaling buffer. The two fixed array descriptor formats are as follows.

``` syntax
FC_SMFARRAY alignment<1> 
total_size<2> 
[pointer_layout<>]  
element_description<> 
FC_END
```

and

``` syntax
FC_LGFARRAY alignment<1> 
total_size<4> 
[pointer_layout<>] 
element_description<> 
FC_END
```

## Conformant Array

A conformant array can be block-copied once the size of the array is known.

``` syntax
FC_CARRAY alignment<1>
element_size<2> 
conformance_description<> 
[pointer_layout<>] 
element_description<> 
FC_END
```

The conformance\_description<> is a correlation descriptor and has 4 or 6 bytes depending on whether [**/robust**](/windows/desktop/Midl/-robust) is used.

## Conformant Varying Array

A conformant varying array can also be block-copied.

``` syntax
FC_CVARRAY alignment<1> 
element_size<2> 
conformance_description<> 
variance_description<>  
[pointer_layout<>] 
element_description<> 
FC_END
```

The conformance\_description<> and variance\_description<> is a correlation descriptor and has 4 or 6 bytes depending on whether [**/robust**](/windows/desktop/Midl/-robust) is used.

## Varying Array

The varying arrays have two possibilities depending on the size of the array.

``` syntax
FC_SMVARRAY alignment<1>
total_size<2>  
number_elements<2> 
element_size<2> 
variance_description<> 
[pointer_layout<>] 
element_description<> 
FC_END

FC_LGVARRAY alignment<1>
total_size<4>  
number_elements<4> 
element_size<2> 
variance_description<4>
[pointer_layout<>] 
element_description<> 
FC_END
```

The variance\_description<> is a correlation descriptor and has 4 or 6 bytes depending on the [**/robust**](/windows/desktop/Midl/-robust) being used.

For varying arrays embedded inside of a structure, the offset<2> field of the variance\_description<> is a relative offset from the varying array's position in the structure to the variance describing field. The offset is typically relative to the beginning of the structure.

## Complex Arrays

A complex array is any array with an element that prevents it from being block-copied, and as such, additional action needs to be taken. These elements make an array complex:

-   simple types: ENUM16, \_\_INT3264 (on 64-bit platforms only), an integral with \[[**range**](/windows/desktop/Midl/range)\]
-   reference and interface pointers (all pointers on 64-bit platforms)
-   unions
-   complex structures (see the Complex Structure Description topic for a full list of reasons for a structure to be complex)
-   elements defined with \[[**transmit\_as**](/windows/desktop/Midl/transmit-as)\], \[[**user\_marshal**](/windows/desktop/Midl/user-marshal)\]
-   All multidimensional arrays with at least one conformant and/or varying dimension are complex regardless of the underlying element type.

The complex array description is as follows:

``` syntax
FC_BOGUS_ARRAY alignment<1> 
number_of_elements<2> 
conformance_description<> 
variance_description<> 
element_description<> 
FC_END
```

The number\_of\_elements<2> field is zero if the array is conformant.

The conformance\_description<> and variance\_description<> is a correlation descriptor and has 4 or 6 bytes depending on whether [**/robust**](/windows/desktop/Midl/-robust) is used. If the array has conformance and/or variance then the conformance\_description<> and/or variance\_description<> field(s) have valid descriptions, otherwise the first 4 bytes of the correlation descriptor are set to 0xFFFFFFFF. The flags, when present, are set to zero.

 

 
