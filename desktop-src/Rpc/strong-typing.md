---
title: Strong Typing
description: C is a weakly typed language, that is, the compiler allows operations such as assignment and comparison among variables of different types.
ms.assetid: 5f52adcc-22b9-4b4f-b921-5996d278b10e
keywords:
- Remote Procedure Call RPC , described, data typing
ms.topic: article
ms.date: 05/31/2018
---

# Strong Typing

C is a weakly typed language, that is, the compiler allows operations such as assignment and comparison among variables of different types. For example, C allows the value of a variable to be cast to another type. The ability to use variables of different types in the same expression promotes flexibility as well as efficiency.

A strongly typed language imposes restrictions on operations among variables of different types. In those cases, the compiler issues an error prohibiting the operation. These strict guidelines regarding data types are designed to avoid potential errors.

The difficulty with using a weakly typed language such as C for remote procedure calls is that distributed applications can run on several different computers with different C compilers and different architectures. When an application runs on only one computer, you don't have to be concerned with the internal data format because the data is handled in a consistent manner. However, in a distributed computing environment, different computers can use different definitions for their base data types. For example, some computers define the **int** type, so its internal representation is 16 bits, while other computers use 32 bits. One computer architecture, known as "little endian," assigns the least significant byte of data to the lowest memory address and the most significant byte to the highest address. Another architecture, known as "big endian," assigns the least significant byte to the highest memory address associated with that data.

Remote procedure calls require strict control over parameter types. To handle data transmission and conversion over the network, MIDL strictly enforces type restrictions for data transferred over the network. For this reason, MIDL includes a set of well-defined [base types](base-types.md). MIDL enforces strong typing by mandating the use of keywords that unambiguously define the size and type of data. The most visible effect of strong typing is that MIDL does not allow variables of the type **void \***.

In the following topics, this section discusses the MIDL language features that enforce strong data typing:

-   [Base Types](base-types.md)
-   [Signed and Unsigned Types](signed-and-unsigned-types.md)
-   [Wide-Character Types](wide-character-types.md)
-   [Structures](structures.md)
-   [Unions](unions.md)
-   [Enumerated Types](enumerated-types.md)
-   [Arrays](arrays.md)
-   [Function Attributes](function-attributes.md)
-   [Field Attributes](field-attributes.md)
-   [Three Pointer Types](three-pointer-types.md)
-   [Type Attributes](type-attributes.md)

 

 




