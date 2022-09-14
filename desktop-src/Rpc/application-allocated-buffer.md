---
title: Application-Allocated Buffer
description: The ACF attribute \ byte\_count\ directs the stubs to use a preallocated buffer that is not allocated or freed by the client support routines.
ms.assetid: 1b370f74-394e-4e57-9749-83334be50f28
ms.topic: article
ms.date: 05/31/2018
---

# Application-Allocated Buffer

The ACF attribute \[[**byte\_count**](/windows/desktop/Midl/byte-count)\] directs the stubs to use a preallocated buffer that is not allocated or freed by the client support routines. The \[**byte\_count**\] attribute is applied to a pointer or array parameter that points to the buffer. It requires a parameter that specifies the buffer size in bytes.

The client-allocated memory area can contain complex data structures with multiple pointers. Because the memory area is contiguous, the application does not have to make several calls to free each pointer and structure individually. As when using the \[[**allocate(all\_nodes)**](/windows/desktop/Midl/allocate)\] attribute, the memory area can be allocated or freed with one call to the memory-allocation routine or the free routine. However, unlike using the \[**allocate(all\_nodes)**\] attribute, the buffer parameter is not managed by the client stub but by the client application.

The buffer must be an \[[**out**](/windows/desktop/Midl/out-idl)\]-only parameter and the buffer length in bytes must be an \[[**in**](/windows/desktop/Midl/in)\]-only parameter. The \[[**byte\_count**](/windows/desktop/Midl/byte-count)\] attribute can only be applied to pointer types. The \[**byte\_count**\] ACF attribute is a Microsoft extension to DCE IDL and, as such, is not available if you compile using the MIDL [**/osf**](/windows/desktop/Midl/-osf) switch.

In the following example, the parameter *pRoot* uses byte count:

``` syntax
/* function prototype in IDL file (fragment) */
void SortNames(
    [in] short cNames,
    [in, size_is(cNames)] STRINGTYPE pszArray[],
    [in] short cBytes,
    [out, ref] P_TREE_TYPE pRoot  /* tree with sorted data */
);
```

The \[[**byte\_count**](/windows/desktop/Midl/byte-count)\] attribute appears in the ACF as:

``` syntax
/* ACF file (fragment) */
SortNames([byte_count(cBytes)] pRoot);
```

The client stub generated from these IDL and ACF files does not allocate or free the memory for this buffer. The server stub allocates and frees the buffer in a single call using the provided size parameter. If the data is too large for the specified buffer size, an exception is raised.

 

 