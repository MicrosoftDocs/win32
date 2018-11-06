---
title: Format Strings
description: A format string is an interpreted token that the NDR engine understands. Format strings are often referred to as MOPs; this documentation uses the term format string throughout.
ms.assetid: 548283bd-023a-41dd-b1d0-661305d019e9
ms.topic: article
ms.date: 05/31/2018
---

# Format Strings

A format string is an interpreted token that the NDR engine understands. Format strings are often referred to as MOPs; this documentation uses the term format string throughout.

To be more precise, a format character is an individual (atomic) interpretable token. Each format character is one byte in size. A format string is a sequence of format characters or format characters and numerical data. The term descriptor is also used for naming common sequences; for example, a parameter format string or a parameter descriptor is a format string used to describe a parameter of a routine.

Format characters have suggestive symbolic names like FC\_LONG or FC\_STRUCT. All format string characters used by MIDL and the NDR engine are defined in the Ndrtypes.h file.

## Format String Tables

Two primary format string tables are used by the engine: the procedure format string table, **\_\_MIDL\_ProcFormatString**, that keeps the procedure descriptors; and the type format string table, **\_\_MIDL\_TypeFormatString**, that keeps the data type descriptors. The compiler generates both into the main stub files (\*\_c.c, \*\_s.c, \*\_p.c). The procedure format string table is used mostly by various interpreters but it is also used for the buffer conversion regardless of the compiler mode. The type format string table is used when calling the core NDR engine to indicate specific data types to be worked on.

## Format String Notation

The notation used in this document follows common programming description guidelines, with a bar ( \| ) used to denote alternative constructs and square brackets ( \[ \] ) used to indicate optional elements. Format strings are frequently stacked up for readability (accountability). Throughout this document, FC denotes a single format character. Format characters are presented in all CAPS, using their actual symbolic names. Other arbitrary fields are represented by a name and a size.

Angle brackets ( <> ) are used to denote sizes of the descriptors. The conventions shown in the following table are employed.



| Notation     | Meaning                                                   |
|--------------|-----------------------------------------------------------|
| <*n*>  | The size of descriptor is n bytes.                        |
| <>     | The size of descriptor varies.                            |
| {<>}\* | The descriptor is repeated any number of times (0,1,2 …). |



 

The following format characters have a special meaning.



| Character | Meaning                                   |
|-----------|-------------------------------------------|
| FC\_END   | Indicates the end of some format strings. |
| FC\_PAD   | Uninterpreted pad character.              |



 

 

 




