---
title: Transmit_as and Represent_as
description: Transmit\_as and represent\_as share the same layout except for the leading token; the token reads FC\_TRANSMIT\_AS or FC\_REPRESENT\_AS, but the underlying code is common.
ms.assetid: 70fbb4bf-0892-4c26-9790-9fc21ff8c0dd
ms.topic: article
ms.date: 05/31/2018
---

# Transmit\_as and Represent\_as

Transmit\_as and represent\_as share the same layout except for the leading token; the token reads FC\_TRANSMIT\_AS or FC\_REPRESENT\_AS, but the underlying code is common.

The description has the following layout:

``` syntax
FC_TRANSMIT_AS | FC_REPRESENT_AS
flags<1>
quintuple_index<2>
presented_type_memory_size<2>
transmitted_type_buffer_size<2>
transmitted_type_offset<2>
```

The flags<1> byte consists of the upper flag nibble and the lower alignment nibble.

The alignment nibble keeps the wire alignment of the transmitted type. This is needed when buffer sizing and using the transmitted type size from the format code.

The flag nibble can have the following flags:

``` syntax
#define PRESENTED_TYPE_IS_ARRAY     0x10
#define PRESENTED_TYPE_ALIGN_4      0x20
#define PRESENTED_TYPE_ALIGN_8      0x40
```

The PRESENTED\_TYPE\_IS\_ARRAY flag marks a top-level transmit as (or represent as) argument being an array of something and passed-by value. The [**–Oi**](/windows/desktop/Midl/-oi) interpreter uses this flag to step over such an argument (which is actually a pointer on stack, not the array). The other two flags are also used only in previous interpreters to step correctly over a presented type on the stack.

The quintuple\_index<2> is an index of the callback routine quintuple (this is actually a quadruple) of functions. The table is common to both transmit as and represent as and there is an obvious mapping for the position of the routines, as the same entry points service transmit as and represent as codes. The mapping is from\_local => to\_xmit, to\_local => from\_xmit, free\_inst => free\_xmit, free\_local => free\_inst.

The presented\_type\_memory\_size<2> always provides a size for the presented/local type, including unknown represent as types.

The transmitted\_type\_buffer\_size<2> is either zero, when the size is varying, or the actual fixed size. This is an optimization that enables skipping some callbacks when sizing the buffer.

The transmitted\_type\_offset<2> is the usual relative type offset to the transmitted type format string.

 

 