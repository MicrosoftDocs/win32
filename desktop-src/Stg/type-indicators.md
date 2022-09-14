---
title: Type Indicators
description: The actual properties follow the table of Property Identifiers/Offset Pairs property set values. Each property is stored as a DWORD, followed by the data type value.
ms.assetid: 8523458b-8b1b-4e9f-8f96-d7601e57675c
ms.topic: article
ms.date: 05/31/2018
---

# Type Indicators

The actual properties follow the table of Property Identifiers/Offset Pairs property set values. Each property is stored as a **DWORD**, followed by the data type value.

Type indicators and their associated values are described in the [**PROPVARIANT**](/windows/win32/api/propidlbase/ns-propidlbase-propvariant) structure.

All Type/Value pairs must begin on a 32-bit boundary. Thus, values may be followed with null bytes to align the subsequent pair on a 32-bit boundary.

The following example code calculates how many bytes are required to align on a 32-bit boundary, given a count of bytes.


```C++
cbAdd = (((cbCurrent + 3) >> 2) << 2) - cbCurrent ;
```



Within a vector of values, each repetition of a simple scalar value smaller than 32 bits must align with its natural alignment rather than with a 32-bit alignment. In practice, this is only significant for types **VT\_UI1**, **VT\_UI2**, **VT\_I2**, and **VT\_BOOL** (which have one-byte or two-byte natural alignment). All other types have four-byte natural alignment. Some types, for example, **VT\_R8**, actually have 8-byte natural alignment, but are stored as if they have four-byte alignment.

A property value with type indicator **VT\_I2** \| **VT\_VECTOR** would include:

-   A **DWORD** element count.
-   A sequence of packed two-byte integers with no null padding between them.

> [!IMPORTANT]
> Any 32-bit counts or property types that are stored as a part of a vector property element must also be 32-bit aligned.

 

A property value of type identifier **VT\_LPSTR** \| **VT\_VECTOR** would include:

-   A **DWORD** element count (**DWORD** *cElems*).
-   A sequence of strings (**char** *rgch\[\]*), each preceded by a length-count **DWORD** and possibly followed by null padding to round to a 32-bit boundary.

 

 