---
Description: Microsoft Windows Search uses filters to extract the content of items for inclusion in a full-text index.
ms.assetid: 7b24986b-972d-4674-846b-f856b908edf4
title: Developing Filter Handlers for Windows Search
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Developing Filter Handlers for Windows Search

Microsoft Windows Search uses filters to extract the content of items for inclusion in a full-text index. You can extend Windows Search to index new or proprietary file types by writing filters to extract the content, and property handlers to extract the properties of files.

This section provides the conceptual framework that is necessary for implementing a filter handler (an implementation of the [**IFilter**](https://msdn.microsoft.com/library/Bb266451(v=VS.85).aspx) interface).

-   [Understanding Filter Handlers in Windows Search](-search-ifilter-about.md)
-   [Best Practices for Creating Filter Handlers in Windows Search](-search-3x-wds-extidx-filters.md)
-   [Returning Properties from a Filter Handler](-search-ifilter-property-filtering.md)
-   [Filter Handlers that Ship with Windows](-search-ifilter-implementations.md)
-   [Implementing Filter Handlers in Windows Search](-search-ifilter-constructing-filters.md)
-   [Registering Filter Handlers](-search-ifilter-registering-filters.md)
-   [Testing Filter Handlers](-search-ifilter-testing-filters.md)

## Additional Resources

-   The [IFilterSample](-search-sample-ifiltersample.md) code sample, available on [Code Gallery](http://go.microsoft.com/fwlink/p/?linkid=155654) and the [Windows 7 SDK](http://go.microsoft.com/fwlink/p/?linkid=129787), demonstrates how to create an IFilter base class for implementing the [**IFilter**](https://msdn.microsoft.com/library/Bb266451(v=VS.85).aspx) interface.
-   For an overview of the indexing process, see [The Indexing Process](-search-indexing-process-overview.md).
-   For an overview of file types, see [File Types](http://msdn.microsoft.com/en-us/library/cc144148(VS.85).aspx).
-   To query file association attributes for a file type, see [PerceivedTypes, SystemFileAssociations, and Application Registration](http://msdn.microsoft.com/en-us/library/cc144150(VS.85).aspx).

 

 



