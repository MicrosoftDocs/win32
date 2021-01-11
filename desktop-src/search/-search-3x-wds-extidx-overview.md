---
description: You can extend Windows Search to index the contents and properties of new file formats, and data stores using data add-in interfaces.
ms.assetid: 69edf316-77a8-4cc5-9af8-fb89f440c9ea
title: Extending the Index (Windows Search)
ms.topic: article
ms.date: 05/31/2018
---

# Extending the Index (Windows Search)

You can extend Windows Search to index the contents and properties of new file formats, and data stores using [data add-in interfaces](./-search-data-addins-interfaces-entry-page.md). To create Windows Search add-ins, third-party developers must first implement a Shell data store, and then develop a protocol handler so that Windows Search can access the data for indexing. If you have a custom file format, you must develop a filter handler to index file contents, and a property handler for every file type to index properties.

Windows Search currently supports the indexing of over 200 types of items (such as .txt, .html, and .xml file formats) and can work with multiple types of data stores (such as the NTFS file system and Microsoft Outlook). Windows Search uses filter and protocol handler technology similar to SharePoint Server. Hence, if you already have implementations for your file format, you can update the implementations to be initialized with a stream by using [IPersistStream](/windows/win32/api/objidl/nn-objidl-ipersiststream) so that the filter will work with Windows Search.

> [!Note]  
> Filter handlers, property handlers, and protocol handlers must be written in native code. This is due to potential common language runtime (CLR) versioning issues with the process that multiple add-ins run in.

 

This section on extending the index with add-ins contains the following topics:

-   [Developing Filter Handlers](-search-ifilter-conceptual.md)
-   [Developing Property Handlers for Windows Search](-search-3x-wds-extidx-propertyhandlers.md)
-   [Developing Protocol Handlers](-search-3x-wds-phaddins.md)

## Additional Resources

For related code samples, see [Windows Search Code Samples](-search-samples-ovw.md).

## Related topics

<dl> <dt>

[Windows Search Development Guide](-search-developers-guide-entry-page.md)
</dt> <dt>

[Managing the Index](-search-3x-wds-mngidx-overview.md)
</dt> <dt>

[Querying the Index Programmatically](-search-3x-wds-qryidx-overview.md)
</dt> <dt>

[Extending Language Resources](extending-language-resources-in-windows-search.md)
</dt> </dl>

 

 
