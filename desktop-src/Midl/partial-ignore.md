---
title: partial_ignore attribute
description: The ACF attribute \ partial\_ignore\ defines a specialized version of \ unique\ pointers that provides optional-out semantics.
ms.assetid: 8a8f88b0-4a12-496d-bf77-ee57241b577b
keywords:
- partial_ignore attribute MIDL
topic_type:
- apiref
api_name:
- partial_ignore
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# partial\_ignore attribute

The ACF attribute **\[partial\_ignore\]** defines a specialized version of **\[unique\]** pointers that provides optional-out semantics.

``` syntax
[ [function-attribute-list <>] ] type-specifier <> [pointer- <>declarator <>] function-name <>( [ partial_ignore [ , parameter-attribute-list <> ] ] type-specifier <> [declarator <>] , ...);
```

## Remarks

When creating a function, it is common to allow users to specify a non-**NULL** pointer to optional return data, often referred to as an optional-out pointer. The memory pointed to by the user is not typically required to be initialized. This technique represents a problem when the function is used over RPC.

If the optional-out pointer is valid, but points to uninitialized data, RPC attempts to marshal that data and send it to the server, which can cause the marshaling to fail and abort the call. Even if the marshaling succeeds, a potentially large amount of useless data is sent to the server.

These problems are solved by marking the pointer as **\[in, out, unique, partial\_ignore\]**. All four attributes must be present. When a **\[partial\_ignore\]** pointer is marshaled on the client side, the only data sent to the server is an indicator showing whether the pointer is **NULL**. If the pointer is non-**NULL**, the server-side routine receives a valid pointer to a block of memory that has been initialized with zeros. If the pointer is **NULL**, the server-side routine receives a **NULL** pointer.

In this situation, the maximum size of the pointer must be well defined either at compile time or based on input parameters, because the server needs to allocate space for the memory location being pointed to. For example, a simple **\[string\]** pointer does not have a well defined size because the string is implicitly terminated by a NULL character. In this case, specifying the maximum size of the string by adding a **\[size\_is\]** attribute would achieve the well defined size requirement.

## Examples

``` syntax
/* The MoveLeft function will move one position to the left and optionally return the previous position */
void MoveLeft([in, out, unique, partial_ignore] long *pPrevPosition);
```

## See also

<dl> <dt>

[**unique**](unique.md)
</dt> </dl>

 

 




