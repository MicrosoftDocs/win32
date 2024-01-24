---
description: The ISearchManager interface provides methods that make changes across catalogs.
ms.assetid: e6f4432b-03bf-4711-a79e-1bf9242c5683
title: Using the Search Manager
ms.topic: article
ms.date: 05/31/2018
---

# Using the Search Manager

The [**ISearchManager**](/windows/desktop/api/Searchapi/nn-searchapi-isearchmanager) interface provides methods that make changes across catalogs. Changes made at the **ISearchManager** level apply globally to all catalogs used by the indexer, while changes made at the [**ISearchCatalogManager**](/windows/desktop/api/Searchapi/nn-searchapi-isearchcatalogmanager) level apply to specific catalogs. However, currently, Windows Search uses only one catalog, SystemIndex. You can use the Search Manager to do the following:

- Get an instance of the Catalog Manager for the search catalog.
- Get version information about the Windows Search engine.

The following methods of the [**ISearchManager**](/windows/desktop/api/Searchapi/nn-searchapi-isearchmanager) interface can help you manage your search catalog(s):

| Method                                                                      | Description                                                                                                                                                                                                                          |
|-----------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetCatalog**](/windows/desktop/api/Searchapi/nf-searchapi-isearchmanager-getcatalog)                     | Gets a catalog by name and returns an instance of [**ISearchCatalogManager**](/windows/desktop/api/Searchapi/nn-searchapi-isearchcatalogmanager) for that catalog. This enables you to manage an individual search catalog.                                          |
| [**GetIndexerVersion**](/windows/desktop/api/Searchapi/nf-searchapi-isearchmanager-getindexerversion)       | Returns the version of the indexer in two integers: major version and minor version. For example, the major version number for Windows 10 Search is "10" and the minor version number is "0". For Windows Vista Search and Windows Search 3.0 on Windows XP the major version number is "3" and the minor version number is "0". |
| [**GetIndexerVersionStr**](/windows/desktop/api/Searchapi/nf-searchapi-isearchmanager-getindexerversionstr) | Returns the complete version number of the indexer as a string: for example, "10.0.18309.1000". For Windows 10 this will typically match the OS version number. For Windows XP, Vista, and 7 it will be different.                                                                                                                                        |


For more information about these methods, see the [**ISearchManager**](/windows/desktop/api/Searchapi/nn-searchapi-isearchmanager) documentation.

The following [**ISearchManager**](/windows/desktop/api/Searchapi/nn-searchapi-isearchmanager) methods are reserved for future use. They are, however, implemented and do not affect the indexer or catalog, as there is only one catalog for Windows Search at this time.

- **get\_BypassList**
- **get\_LocalBypass**
- **get\_PortNumber**
- **get\_ProxyName**
- **get\_UseProxy**
- **get\_UserAgent**
- **put\_UserAgent**
- **SetProxy**

**GetParameter** and **SetParameter** are also reserved for future use but are not implemented.

## Related topics

[Managing the Index](-search-3x-wds-mngidx-overview.md)

[Interfaces for Managing the Index](interfaces-for-managing-the-index.md)

[Using the Catalog Manager](-search-3x-wds-mngidx-catalog-manager.md)

[Using the Crawl Scope Manager](-search-3x-wds-extidx-csm.md)
