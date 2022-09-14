---
title: Structures (RPC)
description: Description of various types of structures in Remote Procedure Call (RPC).
ms.assetid: edaf547d-d3d1-443c-93dd-8e036bc42944
ms.topic: article
ms.date: 05/31/2018
---

# Structures (RPC)

There are several categories of structures, progressively more complicated in terms of actions required for marshaling. They begin with a simple structure that can be block-copied as a whole, and continue to a complex structure that has to be serviced field by field.

-   [Simple Structure](#simple-structure)
-   [Simple Structure with Pointers](#simple-structure-with-pointers)
-   [Conformant Structure](#conformant-structure)
-   [Conformant Structure with Pointers](#conformant-structure-with-pointers)
-   [Conformant Varying Structure (with or without Pointers)](#conformant-varying-structure-with-or-without-pointers)
-   [Hard Structure](#hard-structure)
-   [Complex Structure](#complex-structure)
-   [Structure Member Layout Description](#structure-member-layout-description)

> [!Note]  
> When compared to array categories, it becomes clear that only structures up to 64k in size can be described (the size is for the flat part of the structure), that is there is no equivalent of SM and LG arrays.

 

**Members Common to Structures**

-   **alignment**

    The necessary alignment of the buffer before unmarshaling the structure. Valid values are 0, 1, 3, and 7 (the actual alignment minus 1).

-   **memory\_size**

    Size of the structure in memory in bytes; for conformant structures this size does not include the array's size.

-   **offset\_to\_array\_description**

    Offset from the current format string pointer to the description of the conformant array contained in a structure.

-   **member\_layout**

    Description of each element of the structure. The NDR routines only need to examine this portion of a type's format string if endian transformation is needed or if the type is a complex structure.

-   **pointer\_layout**

    See the [Pointer Layout](pointer-layout-tfs.md) section.

## Simple Structure

A simple structure contains only base types, fixed arrays, and other simple structures. The main feature of the simple structure is that it can be block-copied as a whole.

``` syntax
FC_STRUCT alignment<1> 
memory_size<2> 
member_layout<> 
FC_END
```

## Simple Structure with Pointers

A simple structure with pointers contains only base types, pointers, fixed arrays, simple structures, and other simple structures with pointers. Because the layout<> will only have to be visited when doing an endianess conversion, it is placed at the end of the description.

``` syntax
FC_PSTRUCT alignment<1> 
memory_size<2> 
pointer_layout<> 
member_layout<> 
FC_END
```

## Conformant Structure

A conformant structure contains only base types, fixed arrays, and simple structures, and must contain either a conformant string or a conformant array. This array could actually be contained in another conformant structure or conformant structure with pointers which is embedded in this structure.

``` syntax
FC_CSTRUCT alignment<1> 
memory_size<2> 
offset_to_array_description<2> 
member_layout<> 
FC_END
```

## Conformant Structure with Pointers

A conformant structure with pointers contains only base types, pointers, fixed arrays, simple structures, and simple structures with pointers; a conformant structure must contain a conformant array. This array could actually be contained in another conformant structure or conformant structure with pointers that is embedded in this structure.

``` syntax
FC_CPSTRUCT alignment<1> 
memory_size<2> 
offset_to_array_description<2> 
pointer_layout<> 
member_layout<> FC_END
```

## Conformant Varying Structure (with or without Pointers)

A conformant varying structure contains only simple types, pointers, fixed arrays, simple structures, and simple structures with pointers; a conformant varying structure must contain either a conformant string or a conformant-varying array. The conformant string or array can actually be contained in another conformant structure or conformant structure with pointers that is embedded in this structure.

``` syntax
FC_CVSTRUCT alignment<1> 
memory_size<2> 
offset_to_array_description<2> 
[pointer_layout<>] 
layout<> 
FC_END
```

## Hard Structure

The hard structure was a concept aimed at eliminating steep penalties related to processing complex structures. It is derived from an observation that a complex structure typically has only one or two conditions that prevent block-copying, and therefore spoil its performance compared to a simple structure. The culprits are usually unions or enumeration fields.

A hard structure is a structure that has an enum16, end-padding in memory, or a union as the last member. These three elements prevent the structure from falling into one of the previous structure categories, which enjoy small interpretation overhead and maximum optimization potential, but do not force it into the very costly complex structure category.

The enum16 must not cause the memory and wire sizes of the structure to differ. The structure cannot have any conformant array, nor any pointers (unless part of the union); the only other members allowed are base types, fixed arrays, and simple structures.

``` syntax
FC_HARD_STRUCTURE alignment<1> 
memory_size<2> 
reserved<4> 
enum_offset<2> 
copy_size<2> 
mem_copy_incr<2> 
union_description_offset<2>
member_layout<> 
FC_END
```

The enum\_offset<2> field provides the offset from the beginning of the structure in memory to an enum16 if it contains one; otherwise the enum\_offset<2> field is –1.

The copy\_size<2> field provides the total number of bytes in the structure, which may be block-copied into/from the buffer. This total does not include any trailing union nor any end-padding in memory. This value is also the amount the buffer pointer should be incremented following the copy.

The mem\_copy\_incr<2> field is the number of bytes the memory pointer should be incremented following the block-copy before handling any trailing union. Incrementing by this amount (not by copy\_size<2> bytes) yields a proper memory pointer to any trailing union.

## Complex Structure

A complex structure is any structure containing one or more fields that either prevent the structure from being block-copied, or for which additional checking must be performed during marshaling or unmarshaling (for example, bound checks on an enumeration). The following NDR types fall in this category:

-   [simple types](simple-types-tfs.md): ENUM16, \_\_INT3264 (on 64-bit platforms only), an integral with \[[**range**](/windows/desktop/Midl/range)\]
-   alignment padding at the end of the structure
-   interface pointers (they go using an embedded complex)
-   ignored pointers (that is related to \[[**ignore**](/windows/desktop/Midl/ignore)\] attribute and FC\_IGNORE token)
-   complex arrays, varying arrays, string arrays
-   multidimensional conformant arrays with at least one nonfixed dimension
-   unions
-   elements defined with \[[**transmit\_as**](/windows/desktop/Midl/transmit-as)\], \[[**represent\_as**](/windows/desktop/Midl/represent-as)\], \[[**wire\_marshal**](/windows/desktop/Midl/wire-marshal)\], \[[**user\_marshal**](/windows/desktop/Midl/user-marshal)\]
-   embedded complex structures
-   padding at the end of the structure

A complex structure has the following format description:

``` syntax
FC_BOGUS_STRUCT alignment<1> 
memory_size<2> 
offset_to_conformant_array_description<2> 
offset_to_pointer_layout<2> 
member_layout<> 
FC_END 
[pointer_layout<>]
```

The memory\_size<2> field is the size of the structure in memory, in bytes.

If the structure contains a conformant array, the offset\_to\_conformant\_array\_description<2> field provides the offset to the conformant array's description, otherwise it is zero.

If the structure has pointers, the offset\_to\_pointer\_layout<2> field provides the offset past the structure's layout to the pointer layout, otherwise this field is zero.

The pointer\_layout<> field of a complex structure is handled somewhat differently than for other structures. The pointer\_layout<> field of a complex structure only contains descriptions of actual pointer fields in the structure itself. Any pointers contained within any embedded arrays, unions, or structures are not described in the complex structure's pointer\_layout<> field.

> [!Note]  
> This is in contrast to other structures, which duplicate the description of any pointers contained in embedded arrays or structures in their own pointer \_layout<> field as well.

 

The format of a complex structure's pointer layout is also radically different. Because it only contains descriptions of actual pointer members and because a complex structure is marshaled and unmarshaled one field at a time, the pointer\_layout<> field simply contains the pointer description of all pointer members. There is no beginning FC\_PP, and none of the usual pointer\_layout<> information.

## Structure Member Layout Description

A structure's layout description contains one or more of the following format characters:

-   Any of the base type characters, like FC\_CHAR, and so on
-   Alignment directives. There are three format characters specifying alignment of the memory pointer: FC\_ALIGNM2, FC\_ALIGNM4, and FC\_ALIGNM8.
    > [!Note]  
    > There are also buffer alignment tokens, FC\_ALIGNB2 through FC\_ALIGNM8; these are not used.

     

-   Memory padding. These occur only at the end of a structure's description and denote the number of bytes of padding in memory before the conformant array in the structure: FC\_STRUCTPADn, where n is the number of bytes of padding.
-   Any embedded nonbase type (note, however, that a conformant array never occurs in the structure layout). This has a 4-byte description:

    ``` syntax
    FC_EMBEDDED_COMPLEX memory_pad<1> 
    offset_to_description<2>,
    ```

    where the offset is not guaranteed to be 2-byte aligned.

    memory\_pad<1> is a padding needed in memory before the complex field.

    offset\_to\_description<2> is a relative type offset to the embedded type.

There may also be an FC\_PAD before the terminating FC\_END if needed to ensure that the format string will be aligned at a 2-byte boundary following the FC\_END.

 

 