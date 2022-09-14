---
title: User-marshal
description: User-marshal in Remote Procedure Call (RPC).
ms.assetid: 5119e959-d8b8-4fca-8910-568bb9063a9d
ms.topic: article
ms.date: 05/31/2018
---

# User-marshal

User marshal has a format string that is similar to transmit\_as:

``` syntax
FC_USER_MARSHAL
flags<1>
quadruple_index<2>
user_type_memory_size<2>
transmitted_type_buffer size<2>
offset_to_the_transmitted_type<2>
```

The flags<1> byte consists of the upper flag nibble and the lower alignment nibble.

The upper 2 bits of the flag nibble are used to describe whether the wire type is defined as a unique pointer, reference pointer or no pointer (it cannot be a ptr). The following manifests have been defined to set/get the flags:

``` syntax
#define USER_MARSHAL_UNIQUE         0x80
#define USER_MARSHAL_REF            0x40
#define USER_MARSHAL_POINTER        0xc0  /* unique or ref */
#define USER_MARSHAL_IID            0x20  /* JIT compiler only */
```

The alignment nibble of the flag word keeps the wire alignment of the transmitted type.

The quadruple\_index<2> is an index of the callback routine quadruple of the user marshal functions. The routine positions are as follow: sizing, marshaling, unmarshaling, and freeing routine.

The user\_type\_memory\_size<2> provides a size for the user specific type, including unknown types.

The transmitted\_type\_buffer\_size<2> is either zero when the size is varying, or the actual fixed size. This is an optimization that enables MIDL to skip callbacks when sizing the buffer, and also when freeing.

## Range

The \[range\] checking provides additional means for argument validation at the NDR layer. The \[range\] descriptor has the following format:

``` syntax
FC_RANGE,   flags_type <1>
low value<4>
high value<4>
```

The flags take the upper nibble and the type the lower nibble of the second byte. The low and high values depend on the type of the variable to be checked.

The flags are meant as an expansion vehicle; the compiler has been setting the nibble to zero.

 

 




