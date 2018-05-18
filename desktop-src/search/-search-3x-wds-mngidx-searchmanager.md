---
Description: 'The ISearchManager interface provides methods that make changes across catalogs.'
ms.assetid: 'e6f4432b-03bf-4711-a79e-1bf9242c5683'
title: Using the Search Manager
---

# Using the Search Manager

The [**ISearchManager**](-search-isearchmanager.md) interface provides methods that make changes across catalogs. Changes made at the **ISearchManager** level apply globally to all catalogs used by the indexer, while changes made at the [**ISearchCatalogManager**](-search-isearchcatalogmanager.md) level apply to specific catalogs. However, currently, Windows Search uses only one catalog, SystemIndex. You can use the Search Manager to do the following:

-   Get an instance of the Catalog Manager for the search catalog.
-   Get version information about the Windows Search engine.

The following methods of the [**ISearchManager**](-search-isearchmanager.md) interface can help you manage your search catalog(s):



| Method                                                                      | Description                                                                                                                                                                                                                          |
|-----------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetCatalog**](-search-isearchmanager-getcatalog.md)                     | Gets a catalog by name and returns an instance of [**ISearchCatalogManager**](-search-isearchcatalogmanager.md) for that catalog. This enables you to manage an individual search catalog.                                          |
| [**GetIndexerVersion**](-search-isearchmanager-getindexerversion.md)       | Returns the version of the indexer in two integers: major version and minor version. For example, the major version number for Windows Vista Search and Windows Search 3.0 on Windows XP is "3" and the minor version number is "0". |
| [**GetIndexerVersionStr**](-search-isearchmanager-getindexerversionstr.md) | Returns the complete version number of the indexer as a string: for example, "03.00.5824.280".                                                                                                                                       |



 

For more information about these methods, see the [**ISearchManager**](-search-isearchmanager.md) documentation.

The following [**ISearchManager**](-search-isearchmanager.md) methods are reserved for future use. They are, however, implemented and do not affect the indexer or catalog, as there is only one catalog for Windows Search at this time.

-   **get\_BypassList**
-   **get\_LocalBypass**
-   **get\_PortNumber**
-   **get\_ProxyName**
-   **get\_UseProxy**
-   **get\_UserAgent**
-   **put\_UserAgent**
-   **SetProxy**

**GetParameter** and **SetParameter** are also reserved for future use but are not implemented.

## Related topics

<dl> <dt>

[Managing the Index](-search-3x-wds-mngidx-overview.md)
</dt> <dt>

[Interfaces for Managing the Index](interfaces-for-managing-the-index.md)
</dt> <dt>

[Using the Catalog Manager](-search-3x-wds-mngidx-catalog-manager.md)
</dt> <dt>

[Using the Crawl Scope Manager](-search-3x-wds-extidx-csm.md)
</dt> </dl>

 

 



