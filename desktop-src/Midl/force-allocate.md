---
title: force_allocate attribute
description: The ACF attribute \ force\_allocate\ forces a pointer parameter to be allocated using midl\_user\_allocate instead of optimizing away the allocation.
ms.assetid: 40e3a7d9-7e4f-4e3d-8c82-fb6ef567f293
keywords:
- force_allocate attribute MIDL
topic_type:
- apiref
api_name:
- force_allocate
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# force\_allocate attribute

The ACF attribute \[**force\_allocate**\] forces a pointer parameter to be allocated using [**midl\_user\_allocate**](midl-user-allocate-1.md) instead of optimizing away the allocation.

``` syntax
[ [function-attribute-list <>] ] type-specifier <> [pointer- <>declarator <>] function-name <>( [ force_allocate [ , parameter-attribute-list <> ] ] type-specifier <> [declarator <>] , ...);
```

## Parameters

This attribute has no parameters.

## Remarks

RPC attempts to minimize memory allocations on the server by supplying pointers to internal memory buffers. This approach can cause problems for applications that attempt to directly call [**midl\_user\_free**](midl-user-free-1.md) on RPC-supplied pointers, because a pointer that has been optimized cannot be freed. Marking a parameter with **\[force\_allocate\]** will prevent this optimization for all pointers deriving it.

Another common use for **\[force\_allocate\]** is to guarantee the alignment of the memory being pointed to if an application requires an alignment greater than that of the memory pointed to. For example, applications often pass data in a generic array of bytes rather than using the actual type, but a byte is only guaranteed to be aligned at 1, which may cause problems for applications that assume a larger alignment. By marking the parameter with **\[force\_allocate\]**, the application can guarantee all memory pointed to will have an alignment equal to that guaranteed by [**midl\_user\_allocate**](midl-user-allocate-1.md).

## Examples

``` syntax
/* IDL file */
void Func1([in, out, string] char **ppstr);
void Func2([in] long s, [in, size_is(s)] byte *pData);

/* ACF file */

/* e.g. The application wishes to call midl_user_free on *ppstr and supply a new pointer */
Func1([force_allocate] pstr);

/* e.g. pData really points to a structure that needs an alignment greater than 1 */
Func2([force_allocate] pData);
```

## See also

<dl> <dt>

[Avoiding Information Hiding](/windows/desktop/WinProg64/avoiding-information-hiding)
</dt> <dt>

[Designing 64-bit-Compatible Interfaces](/windows/desktop/WinProg64/designing-64-bit-compatible-interfaces)
</dt> <dt>

[**midl\_user\_allocate**](midl-user-allocate-1.md)
</dt> <dt>

[**midl\_user\_free**](midl-user-free-1.md)
</dt> <dt>

[**allocate**](allocate.md)
</dt> </dl>

 

 