---
title: Pointer Layout
description: Pointer layout describes pointers of a structure or an array.
ms.assetid: 1a4984c1-97b9-4e95-a17e-851b67fa94a3
ms.topic: article
ms.date: 05/31/2018
---

# Pointer Layout

Pointer layout describes pointers of a structure or an array.

## pointer\_layout<>

A pointer\_layout<> field consists of the format characters FC\_PP FC\_PAD followed by one or more pointer descriptions, as described later, and terminating with an FC\_END format character:

``` syntax
FC_PP
FC_PAD
{ pointer_instance_layout<> }*
FC_END
```

A pointer\_instance\_layout<> field is a format string describing single or multiple instances of pointers. The following fields are used in these descriptors:

-   offset\_in\_memory

    The signed offset to the pointer's location in memory. For a pointer residing in a structure, this offset is a negative offset from the end of the structure (the end of the nonconformant portion of conformant structures); for arrays, the offset is from the beginning of the array.

-   offset\_in\_buffer

    The signed offset to the pointer's location in the buffer. For a pointer residing in a structure, this offset is a negative offset from the end of the structure (the end of the nonconformant portion of conformant structures): for arrays, the offset is from the beginning of the array.

-   offset\_to\_array

    Offset from an enclosing structure to the embedded array whose pointers are being handled. For top-level arrays, this field will always be zero.

-   iterations

    Total number of pointers that have the same layout<> described.

-   increment

    Increment between successive pointers during a REPEAT.

-   number\_of\_pointers

    Number of different pointers in a repeat instance.

-   pointer\_description

    Pointer description.

All pointer instance layouts use the following single pointer\_instance<8>:

``` syntax
offset_to_pointer_in_memory<2> 
offset_to_pointer_in_buffer<2> 
pointer_description<4>
```

The following are instance descriptors:

**Single instance of a pointer to a simple type:**

``` syntax
FC_NO_REPEAT FC_PAD 
pointer_instance<8>
```

**Fixed repeat pointer:**

``` syntax
FC_FIXED_REPEAT FC_PAD 
iterations<2> 
increment<2> 
offset_to_array<2> 
number_of_pointers<2>
{ pointer_instance<8> }*
```

**Variable repeat pointer:**

``` syntax
FC_VARIABLE_REPEAT (FC_FIXED_OFFSET | FC_VARIABLE_OFFSET) 
increment<2> 
offset_to_array<2> 
number_of_pointers<2> 
{ pointer_instance<8> }*
```

For fixed repeat and variable repeat pointer instances there is a set of offset and pointer descriptions for each pointer in the repeat instance.

## Pointers Layout Design Issues

This section addresses issues related to processing conformant structures and embedded pointers. The issue is that the compiler generates pointer layouts for structures and arrays with some redundancy. This is beneficial, because the information is useful and as such, for example, a conformant structure can walk one pointer layout to service all the pointers from the structure and from the conformant array being part of the conformant structure. However, some embedded situations exist that require the NDR engine to perform additional work to process all the pointer layouts in the proper sequence, processing each pointer exactly once.

## What the Compiler Generates

Every object discussed in this section has pointers, so for example, a conformant structure has pointers in the structure part as well as in the array elements. The element is a simple structure with a pointer.

1.  Conformant structure, single level

    The conformant descriptor has a PP part where all the pointers are described, both from the structure and from the array. The member list has FC\_LONG in lieu of a pointer. The CARRAY array descriptor has elements through the use of an embedded\_complex and no pointer descriptors at all. The element still has its single pointer descriptor. Pointer layout precedes the member layout in a conformant structure and simple structure descriptors.

2.  Conformant structure, two or more levels

    The PP description has pointers from all levels. It reuses the same array description as the internal conformant structure. The member list has FC\_LONG in lieu of a pointer. An embedded structure comes through the use of an embedded complex. The conformant structure descriptor is reused as-is. The size of the flat portion of the structure comes out complete as well, meaning that the top-level structure size would include embedded structure's flat size.

3.  Complex structure, single level

    Pointer members are marked by FC\_POINTER. Pointer layout is simplified such that there is a pointer descriptor (4 bytes) for each FC\_POINTER entry on the list. Pointer layout is walked in parallel with a member walk, that is, an FC\_POINTER causes the next pointer description to be processed. The CARRAY array has pointer layout with all the descriptors of the array, and then element, through the use of an embedded complex. The element descriptor is reused. The size of the flat portion of the structure comes out complete; in other words, the top-level structure's flat size includes the embedded structure's flat size. The member layout precedes the pointer layout for complex structures.

    Hence, the conformant array description generation is different depending on whether it is an array inside of a conformant structure or inside a complex structure.

4.  Complex structure, 2 or more levels, complex in complex

    Top-level complex structure has its member pointers, embedded complex structure has its member pointers. The conformant structure descriptor is reused. The array descriptor from the top is the reused array from the embedded structure.

5.  Complex structure with an embedded conformant structure

    Top=level conformant structure has its member pointers. The conformant structure descriptor is reused as-is. The array descriptor is reused from the embedded conformant structure; in other words, it does not have any pointers at the array descriptor. The element has its pointer descriptor.

6.  Arrays of structures with pointers

    An array of simple structures with pointers is generated as an SMFARRAY or CARRAY depending whether the array is sized, but in both cases it has a pointer layout that is complete (FIXED\_REPEAT or VARIABLE\_REPEAT). The pointer layout comes before the member layout.

    An array of complex structures with pointers is generated as BOGUS\_ARRAY regardless whether it is fixed or sized, and in both cases, does not have any pointer layout.

## What the NDR Engine Does

This section describes the NDR engine behavior.

**The marshaling pass**

1.  Conformant structures and embedded conformant structure.

    The top-level structure behaves like a single-level structure.

2.  Embedded complex structure with conformant array

    Any complex structure forces the outer structure to be a complex structure. Embedded structure never marshals its array. Every structure always goes through embedded pointers by simply marshaling members and a member happening to be an FC\_POINTER.

3.  Complex structure with conformant structure

    The top-most embedded conformant structure marshals the conformant array and all the pointees. The NDR engine never descends to deeper nested conformant structures if there are any; this simplifies the solution, as a conformant structure is a leaf object as far as the marshaling of embedded objects is concerned. The top-level complex structure skips the array marshaling.

**Unmarshaling, bufsizing and freeing passes**

Unmarshaling is symmetrical to marshaling; the first operation it performs for complex structures is to find out the pointees' location in the buffer by means of calling the **NdrComplexStructBufferSize** function. It then unmarshals pointees in parallel, enabling the same scheme for unmarshaling the pointees correctly to be used. There should be no confusion about sized objects and unions; the memory image should not be used for sized objects and unions, just for the buffer contents.

The flags used to perform marshaling and unmarshaling correctly are used in the same way in bufsizing and freeing to make sure that pointees are walked exactly once.

**Endianess pass**

At first, the endianess pass is somewhat similar to marshaling/unmarshaling; two passes are required to process complex structures. First pass converts the flat part and finds the pointees' location in the buffer similar to how bufsizing performs this operation for unmarshaling. The second pass then converts the pointees.

Endianess passes differ in the following manner: every structure and every member has to be stepped until the leaf member or element is a simple type. This is different from unmarshaling; in unmarshaling, for example, there is never a need to process conformant structures embedded in conformant structures, or any member of the conformant structure, for that matter. Another issue is that the conversion is not an idempotent operation—hence the unmarshaling pass could redo unmarshaling of some pieces without harm, while conversion has to be performed on a strictly once-per-any-simple-type basis.

Hence, the endianess algorithm can be summarized as the following. NDR has a notion of the top-level conformant structure and a flag to mark that, as appropriate. When walking the first time, such as to convert the flat portion and to obtain the location of the pointees, this notion would not be used. NDR would descend through the flat parts of all levels of structures and never venture into pointer processing. Finally, NDR would flat convert the array at the top-level.

When walking the second time, the flag would be used to mark the embedded pointer's pass to avoid entering deeper levels of the conformant structures, then the top-most conformant structure. In this way, the flag would force the common marshaling/unmarshaling behavior, which is to avoid descending into deeper levels of conformant structures.

The second pass for complex structures with conformant arrays works as follows: the complex structures work the common way; which means deeper levels would never look at or skip their conformant size or their conformant arrays, and would rather simply walk their members without touching the array.

For complex structures with conformant structures, the conformant structure must be aware whether it is top level, and whether it is in a complex structure. The flat portion of the array is processed by the top-most conformant structure. On the second pass, the top-most conformant structure would skip the flat portion and go through the pointer layout and return. The top-most complex structure would skip its flat portion, and would also skip the pointer layout.

**The robust aspect of the endianess walks**

The endianess walk checks for the usual out-of-the-buffer conditions and performs other checks of an uncorrelated nature. The checks aimed at correlated values (such as the sizing argument versus the conformant size) cannot be performed using this step; they are performed later, when unmarshaling.

 

 




