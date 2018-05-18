---
title: About Filters
description: About Filters
ms.assetid: 'da6f9df5-2217-44bb-b75d-b516c74ba1cf'
---

# About Filters

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

An Indexing Service filter implements the [**IFilter**](ifilter.md) interface for a specific type of file. The filter extracts text and properties from documents for placement in the Indexing Service index. Once this content is in the index, you can query the index to find occurrences of the requested content in the filtered files.

An Indexing Service filter, also known as a content filter, is a dynamic-link library (DLL) that includes an implementation of the [**IFilter**](ifilter.md) interface for a specific class of files. An Indexing Service filter understands a file format and can extract the text from the content of the file and properties from either the content or associated properties of the file. To filter new file formats, you simply create and install a new filter implementation.

Filters register themselves for a particular file class. For example, an [HTML filter](html-filter.md) can process the class of "htmlfile" files, which include .htm and .html files. For information about filter registration, see [Finding the Filter DLL for a File](finding-the-filter-dll-for-a-file.md).

Content filters also handle embedded or linked objects by having the parent object call the [**IFilter**](ifilter.md) interface methods of the embedded or linked objects. These objects should have their own **IFilter** implementations, supplied by the system or the programmer, which follow the standard COM [containment rules](_com_reusing_objects). [IFilter::Init](ifilter-init.md) accepts a flag to control whether filtering follows links to other objects.

You use a filter for the following two purposes:

-   [Filtering Text and Properties](filtering-text-and-properties.md). A filter performs a full-text search and can also determine properties for a file. A full-text search extracts only the text information from a file, without formatting or graphics information, so that the text can be indexed.
-   [Viewing and Hit-Highlighting](viewing-and-hit-highlighting.md). A filter provides information for viewing and hit-highlighting. Hit-highlighting enables a text viewer to display the query hits and provides the navigation between hits so you can see exactly where query results occur.

 

 




