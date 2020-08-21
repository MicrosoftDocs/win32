---
title: C-Compiler Packing Issues
description: Packing levels affect the memory layout of types for both MIDL and the Microsoft C/C++ compiler in the same way.
ms.assetid: 029e2f68-e68f-4627-bdf0-889939d7d3c6
keywords:
- MIDL compiler MIDL , C-compiler packing issues
- packing MIDL
- memory layout MIDL
ms.topic: article
ms.date: 05/31/2018
---

# C-Compiler Packing Issues

Packing levels affect the memory layout of types for both MIDL and the Microsoft C/C++ compiler in the same way. In Microsoft build environments, such as the build environment defined by VC++ or the Platform Software Development Kit (SDK), the default packing level for MIDL and C/C++ compilers is the same; the default packing level for the 32-bit and 64-bit Windows build environments is 8.

## Natural Alignment

For types in memory, the default alignment is the same as its natural alignment.

-   A base type, such as short, float and \_\_int64, and a pointer is aligned naturally if its representation starts at an address that is modulo its size. All the currently supported base types have sizes of 1, 2, 4 or 8. Pointers have a size of 4 in 32-bit environments and 8 in 64-bit environments.
-   A compound type is aligned naturally if each of its components is aligned naturally relative to the beginning of the type, and if there are no unnecessary gaps (padding) between components. Compound components, such as fields or elements, are recursed to pointer or base type components.

A simple rule to help remember this behavior is that the natural alignment of a type is equal to the biggest alignments of its components.

There is a connection between alignment and memory size of a type in languages like C or C++ and IDL as expressed by the operator **sizeof()**. The size is a multiple of the alignment (the minimal multiple spanning the type). This follows from an array representation in memory.

Natural alignment is important because accessing misaligned data may cause an exception on some systems. Data can be marked for a safe manipulation when misaligned, but typically that involves a speed penalty that may be substantial on some platforms.

> [!Note]  
> In memory, objects of types with a natural alignment of *n* are guaranteed to be aligned properly when placed at addresses that are a multiple of *n*.

 

## Packing versus Alignment

Specifying a packing level larger than the natural alignment of a type does not change the type alignment. Specifying a packing level smaller than the natural alignment reduces the type alignment to the packing level. As a result, the packed types may be placed in memory at addresses that are a multiple of the packing level (the reduced alignment) without causing a misalignment. This affects both simple types and component types. For compound types, the internal layout of the type may be affected, because the reduced alignment of the components may change the size of padding necessary for the proper alignment of the components, thus reducing the size of the type.

A simple rule to help remember this behavior is that the new alignment of a packed type is the smaller of the packing level and its natural alignment. The size of the type is a multiple of the new alignment. The **sizeof()** operator returns the reduced size for packed types.

For example, with packing level 2 a long becomes aligned at 2, and therefore may be placed at any even address, not only at the addresses that are a multiple of 4 as would be the case with natural alignment. A structure with a short and a long, packed at 2, does not need the internal gap between the short and the following long that was necessary for the natural alignment; hence, not only is the structure now aligned at 2, it also has its size reduced from 8 to 6.

As an example, consider a compound type consisting of a 1-byte character, an integer 4 bytes long, and a 1-byte character:

``` syntax
struct mystructtype 
{    
    char c1;  /* requires 1 byte  */
              /* 3 bytes of padding with natural alignment only */
    long l2;  /* requires 4 bytes */
    char c3;  /* requires 1 byte  */
              /* 3 bytes of padding with natural alignment only */
 } mystruct;
```

This structure is naturally aligned at 4 and has the natural size of 12.

For packing level 4 or greater, the structure **mystruct** is aligned at 4 and `sizeof(struct mystructtype)` is equal to 12. The structure will be misaligned if located in memory at an address that is not a multiple of 4.

For packing level 2, the structure is aligned at 2 and its size is 8. The structure packed with level 2 will be misaligned if located in memory at an address that is not a multiple of 2.

For packing level 1, the structure is aligned at 1 and its size is 6. The structure packed with level 1 can be placed anywhere without causing a misalignment fault.

## Related topics

<dl> <dt>


</dt> <dt>

[/Zp](./-zp.md)
</dt> <dt>

[/pack](./-pack.md)
</dt> </dl>

 

 