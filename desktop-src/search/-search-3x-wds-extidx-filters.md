---
description: Microsoft Windows Search uses filters to extract the content of items for inclusion in a full-text index.
ms.assetid: 7b86a1b4-c8a9-400d-a9f1-a3b821c0269d
title: Best Practices for Filter Handlers in Windows Search
ms.topic: article
ms.date: 05/31/2018
---

# Best Practices for Creating Filter Handlers in Windows Search

Microsoft Windows Search uses filters to extract the content of items for inclusion in a full-text index. You can extend Windows Search to index new or proprietary file types by writing filter handlers to extract the content, and property handlers to extract the properties of files. Filters are associated with file types, as denoted by file name extensions, MIME types or class identifiers (CLSIDs). While one filter can handle multiple file types, each type works with only one filter.

This topic contains the following sections:

-   [Native Code](#native-code)
-   [Secure Code Practices for Windows Search](#secure-code-practices-for-windows-search)
-   [Additional Resources](#additional-resources)
-   [Related topics](#related-topics)

## Native Code

In Windows 7 and later, filters written in managed code are explicitly blocked. Filters MUST be written in native code due to potential CLR versioning issues with the process that multiple add-ins run in.

## Secure Code Practices for Windows Search

The following are practices for writing secure applications for use with Windows Search.

**For query applications:**

-   When writing search clients, you should choose the API that runs in a security context that allows the user the least privilege. For example, ASP pages can use the IXSSO query object, which runs as a user process.

**For IFilters and Language Resources:**

-   If a new filter handler for a file type is being installed as a replacement for an existing filter registration, the installer should save the current registration and restore it if the new filter handler is uninstalled. There is no mechanism to chain filters. Hence, the new filter handler is responsible for replicating any necessary functionality of the old filter.
-   IFilters, word breakers, and stemmers for Windows Search run in the Local Security context. They should be written to manage buffers and to stack correctly. All string copies must have explicit checks to guard against buffer overruns. You should always verify the allocated size of the buffer and test the size of the data against the size of the buffer. Buffer overruns are a common technique for exploiting code that does not enforce buffer size restrictions.
-   [**IFilter**](/windows/win32/api/filter/nn-filter-ifilter), word breaker and stemmer components should never call the [ExitProcess Function](/windows/win32/api/processthreadsapi/nf-processthreadsapi-exitprocess) function or similar API that terminates a process and all its threads.
-   Do not allocate or free resources in the DllMain entry point. This can lead to failures during low-resource stress tests.
-   Code all objects to be thread-safe. Windows Search calls any one instance of a word breaker or stemmer in one thread at a time, but it may call multiple instances at the same time across multiple threads.
-   Avoid creating temporary files or writing to the registry.
-   If you use the Microsoft Visual C++ compiler, ensure that you compile your application using the **/GS** option. The **/GS** option is used to detect buffer overruns. The /GS option places security checks into the compiled code. For more information, see [DllGetClassObject Function](https://msdn.microsoft.com/library/8dbf701c(vs.71).aspx) /**GS** (Buffer Security Check) in the Visual C++ Compiler Options section of the Platform SDK.

## Additional Resources

-   The [IFilterSample](https://github.com/microsoft/Windows-classic-samples/tree/master/Samples/Win7Samples/winui/WindowsSearch/IFilterSample) sample demonstrates how to create an IFilter base class for implementing the [**IFilter**](/windows/win32/api/filter/nn-filter-ifilter) interface.
-   For an overview of the indexing process, see [The Indexing Process](-search-indexing-process-overview.md).
-   For an overview of file types, see [File Types](../shell/fa-file-types.md).
-   To query file association attributes for a file type, see [PerceivedTypes, SystemFileAssociations, and Application Registration](/previous-versions/windows/desktop/legacy/cc144150(v=vs.85)).

## Related topics

<dl> <dt>

[Developing Filter Handlers](-search-ifilter-conceptual.md)
</dt> <dt>

[About Filter Handlers in Windows Search](-search-ifilter-about.md)
</dt> <dt>

[Returning Properties from a Filter Handler](-search-ifilter-property-filtering.md)
</dt> <dt>

[Filter Handlers that Ship with Windows](-search-ifilter-implementations.md)
</dt> <dt>

[Implementing Filter Handlers in Windows Search](-search-ifilter-constructing-filters.md)
</dt> <dt>

[Registering Filter Handlers](-search-ifilter-registering-filters.md)
</dt> <dt>

[Testing Filter Handlers](-search-ifilter-testing-filters.md)
</dt> </dl>

 

 
