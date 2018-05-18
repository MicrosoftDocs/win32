---
title: Constructing Filters
description: Constructing Filters
ms.assetid: 'f1243f67-6ae1-4e0a-96d8-38c255bb3b1c'
---

# Constructing Filters

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

This section describes the construction of filters for Indexing Service. The following topics discuss the significant aspects of realizing the required dynamic-link library (DLL) structure for an [IFilter](ifilter.md) interface implementation.

-   [Describing the Filter Structure](describing-the-filter-structure.md)
-   [Implementing and Exporting the DLL Entry Points](implementing-and-exporting-the-dll-entry-points.md)
-   [Implementing the Filter Class and Class Factory](implementing-the-filter-class-and-class-factory.md)
-   [Inheriting the COM Interfaces](inheriting-the-com-interfaces.md)
-   [Implementing the COM Interface Methods](implementing-the-com-interface-methods.md)

> \[!Caution\]  
> IFilters for Indexing Service run in the Local System security context. They should be written to manage buffers and to stack correctly. All string copies must have explicit checks to guard against buffer overruns. You should always verify the allocated size of the buffer. You should always test the size of the data against the size of the buffer.

 

## Related topics

<dl> <dt>

[Secure Code Practices](secure-code-practices.md)
</dt> </dl>

 

 




