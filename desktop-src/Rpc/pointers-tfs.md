---
title: Pointers (RPC)
description: Pointers
ms.assetid: 9756E637-BCBB-48F1-B962-25AF2C917921
ms.topic: article
ms.date: 05/31/2018
---

# Pointers (RPC)

## Common Pointers

A common pointer is defined as everything other than interface pointers and byte count pointers.

There are two possible layouts for the description:

``` syntax
pointer_type<1> pointer_attributes<1>
simple_type<1> FC_PAD
```

–or–

``` syntax
pointer_type<1> pointer_attributes<1>
offset_to_complex_description<2>
```

The first format is used if the pointer is a pointer to a simple type or a nonsized string pointer. The second format is used for pointers to all other types. Pointer attributes indicate which description layout it is with the FC\_SIMPLE\_POINTER flag.

pointer\_type<1> is one of the following.



| Format character | Description                              |
|------------------|------------------------------------------|
| FC\_RP           | A reference pointer.                     |
| FC\_UP           | A unique pointer.                        |
| FC\_FP           | A full pointer.                          |
| FC\_OP           | A unique pointer in an object interface. |



 

The reason to distinguish FC\_OP is semantic: in object interfaces, an \[in,out\] pointer should be freed before unmarshaling a new object and assigning a new pointer value.

Pointer\_attributes<1> can have any of the flags shown in the following table.



| Flag | Description              |                                                                                                                                                                                                                                       |
|------|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 01   | FC\_ALLOCATE\_ALL\_NODES | The pointer is a part of an allocate(all\_nodes) allocation scheme.                                                                                                                                                                   |
| 02   | FC\_DONT\_FREE           | An allocate(dont\_free) pointer.                                                                                                                                                                                                      |
| 04   | FC\_ALLOCED\_ON\_STACK   | A pointer whose referent is allocated on the stub's stack.                                                                                                                                                                            |
| 08   | FC\_SIMPLE\_POINTER      | A pointer to a simple type or nonsized conformant string. This flag being set indicates layout of the pointer description as the simple pointer layout described above, otherwise the descriptor format with the offset is indicated. |
| 10   | FC\_POINTER\_DEREF       | A pointer that must be dereferenced before handling the pointer's referent.                                                                                                                                                           |



 

Pointers that have size\_is(), max\_is(), length\_is(), last\_is(), and/or first\_is() applied to them have format string descriptions identical to a pointer to an array of the appropriate type (for example, a conformant array if size\_is() is applied, a conformant varying array if size\_is() and length\_is are applied).

## Interface Pointers

An object interface pointer format string has one of two formats, depending on whether the corresponding IID is known to the compiler.

An interface pointer with a constant IID has the following description:

``` syntax
FC_IP FC_CONSTANT_IID 
iid<16>
```

The iid<16> part is the actual IID for the interface pointer. The iid is written to the format string in a format identical to the GUID data structure: long, short, short, char \[8\].

The description of an interface pointer with iid\_is() applied to it is:

``` syntax
FC_IP FC_PAD 
iid_description<> 
```

The iid\_description<> is a correlation descriptor and has 4 or 6 bytes depending on whether [**/robust**](/windows/desktop/Midl/-robust) is used. The value calculated by the **NdrComputeConformance** function is the IID pointer.

## Byte Count Pointers

Byte count pointers relate to a special optimization attribute called \[**byte\_count**\]. The following formats are used:

``` syntax
FC_BYTE_COUNT_POINTER 
simple_type<1>
byte_count_description<> 
```

–and –

``` syntax
FC_BYTE_COUNT_POINTER 
FC_PAD
byte_count_description<> 
pointee_description<>
```

The byte\_count\_description<> is a correlation descriptor and has 4 or 6 bytes depending on whether [**/robust**](/windows/desktop/Midl/-robust) is used.

The pointee\_description<> is a description of the pointee type.

 

 
