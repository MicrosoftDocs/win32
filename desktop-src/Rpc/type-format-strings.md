---
title: Type Format Strings
description: Format characters denote objects of interest to the NDR engine.
ms.assetid: 71117082-07b0-4ba4-a920-09be8d8427ab
ms.topic: article
ms.date: 05/31/2018
---

# Type Format Strings

Format characters denote objects of interest to the NDR engine. There is a format character for each basic type, for various complex types, and for descriptions of pointers, packing, alignment, and other miscellaneous objects. For compound types, several categories of structures and arrays are recognized based on their performance properties. A format string for each category starts with an FC token identifying the particular format string. Format characters for structures and arrays categories may share the in-fixes in the name of the leading FC token shown in the following table.



| Format character | Description                                    |
|------------------|------------------------------------------------|
| C                | Indicates conformance information in the type. |
| V                | Indicates variance information in the type.    |
| P                | Indicates pointers are a part of the type.     |



 

For example, FC\_CSTRUCT and FC\_CARRAY identify the conformant structure and conformant array descriptors, respectively.

The following are format characters with special meanings.



| Format character | Description                                                                         |
|------------------|-------------------------------------------------------------------------------------|
| FC\_PP           | Indicates the beginning of the pointer description section of a structure or array. |



 

RPC NDR type format strings are described in more detail in the following topics:

-   [Simple Types](simple-types-tfs.md)
-   [Pointers](pointers-tfs.md)
-   [Arrays](arrays-tfs.md)
-   [Strings](strings-tfs.md)
-   [Correlation Descriptors](correlation-descriptors-tfs.md)
-   [Structures](structures-tfs.md)
-   [Pointer Layout](pointer-layout-tfs.md)
-   [Unions](unions-tfs.md)
-   [Transmit\_as and Represent\_as](transmit-as-and-represent-as-tfs.md)
-   [User-marshal](user-marshal-tfs.md)

 

 




