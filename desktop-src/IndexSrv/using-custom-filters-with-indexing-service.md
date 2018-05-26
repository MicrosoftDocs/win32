---
title: Using Custom Filters with Indexing Service
description: Using Custom Filters with Indexing Service
ms.assetid: b3853d90-fe9f-4337-8733-9923bcba995e
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using Custom Filters with Indexing Service

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Indexing Service uses filters to extract content and properties of files for inclusion in a searchable index. Microsoft provides file-format specific filters for several types of files, including [Microsoft Office documents](microsoft-office-document-filter.md) and [HTML files](html-filter.md).

This section describes the use of the [**IFilter**](/windows/win32/Filter/nn-filter-ifilter?branch=master) interface to produce custom filters for other specific file formats. It contains the following sections:

-   [About Filters](about-filters.md) describes how the Indexing Service filter extracts text and properties from a file.
-   [Applying Filters](applying-filters.md) describes how the Indexing Service filtering process determines which filters to use for particular files.
-   [Constructing Filters](constructing-filters.md) describes the construction of several sample filters.
-   [Testing Filters](testing-filters.md) describes how to use the IFilter Test Suite to test filters.
-   [Filter Samples](filter-samples.md) presents details about the sample filters in the Platform Software Development Kit (SDK).

For an overview of how the [**IFilter**](/windows/win32/Filter/nn-filter-ifilter?branch=master) interface regards documents and their properties, see [Properties of Documents](properties-of-documents.md). In particular, for a synopsis and example of how the **IFilter** interface processes a document, see [Property Filtering](property-filtering.md).

 

 




