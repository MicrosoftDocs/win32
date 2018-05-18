---
title: Filtering Text and Properties
description: Filtering Text and Properties
ms.assetid: '8b73a4e9-6905-40a8-9878-858175eebab9'
---

# Filtering Text and Properties

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Indexing Service uses the [**IFilter**](ifilter.md) interface to scan documents for text and property information. This section includes the following topics:

-   [Filtering Information Chunks](filtering-information-chunks.md). Chunks are the fundamental units of information that can be either contents or properties of an object.
-   [Filtering File Contents](filtering-file-contents.md). A filter extracts chunks of text from the contents of a file to index them.
-   [Filtering File Properties](filtering-file-properties.md). A filter extracts chunks of text from a file's properties to index them.
-   [Filtering Well-Known Properties](filtering-well-known-properties.md). A filter can extract a consistent set of well-known properties for all files.

Several samples of [**IFilter**](ifilter.md) interface implementations can be found in subdirectories of the mssdk\\samples\\winbase\\indexing directory of the Platform SDK. To install the samples, see [Installing the Samples](installing-the-samples.md). For more information about the samples, see [Filter Samples](filter-samples.md).

 

 




