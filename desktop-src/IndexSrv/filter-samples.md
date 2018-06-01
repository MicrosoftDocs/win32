---
Description: Filter Samples
ms.assetid: 5b21f96b-52ac-485f-89e7-93d8dc34140b
title: Filter Samples
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Filter Samples

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

This section describes some individual sample filters in the Platform SDK. The following samples are listed in order of increasing complexity.

-   [SmpFilt Sample](smpfilt-sample.md). An example implementation of the [**IFilter**](/windows/desktop/api/Filter/nn-filter-ifilter) interface for unformatted, single-byte-character text files.
-   [IFilter Sample](ifilter-sample.md). An example implementation of the [**IFilter**](/windows/desktop/api/Filter/nn-filter-ifilter) interface that filters both text-type and value-type properties for HTML files.
-   [HtmlProp Sample](htmlprop-sample.md). An example implementation of the [**IFilter**](/windows/desktop/api/Filter/nn-filter-ifilter) interface that specializes the [HTML filter](html-filter.md) (HtmlFilt) implementation of Indexing Service to extract and convert HTML &lt;META&gt; tags to value-type properties.

 

 



