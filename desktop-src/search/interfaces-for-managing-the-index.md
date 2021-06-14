---
description: Learn how Windows Search lets you manage the Windows Search index with Search Manager, Catalog Manager, and Crawl Scope Manager.
ms.assetid: 80f0387c-5c91-41b8-9767-5f5e6563c112
title: Interfaces for Managing the Index
ms.topic: article
ms.date: 05/31/2018
---

# Interfaces for Managing the Index

Windows Search enables you to manage the Windows Search index with three main components: Search Manager, Catalog Manager, and Crawl Scope Manager. Some of these management interfaces can be used with standard user privileges, but those that change the state of the index require administrative privileges.

## About the Interfaces for Managing the Index

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Component</th>
<th>Interfaces</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Search Manager</td>
<td><a href="/windows/desktop/api/Searchapi/nn-searchapi-isearchmanager">ISearchManager</a></td>
<td>Provides methods to retrieve and set information about Windows Search:
<ul>
<li>Getting an instance of the Catalog Manager for a specific catalog.</li>
<li>Getting or setting proxy information.</li>
<li>Getting version information about the Windows Search engine.</li>
</ul>
For more information, see <a href="-search-3x-wds-mngidx-searchmanager.md">Using the Search Manager</a>.<br/></td>
</tr>
<tr class="even">
<td>Catalog Manager</td>
<td><a href="/windows/desktop/api/Searchapi/nn-searchapi-isearchcatalogmanager">ISearchCatalogManager</a><br/> <a href="/windows/desktop/api/searchapi/nn-searchapi-isearchcatalogmanager2">ISearchCatalogManager2</a><br/></td>
<td>Provides methods to manage an individual search catalog, such as causing a re-indexing or setting time-outs. This interface manages the catalog in four areas:
<ul>
<li>Catalog contents - ensuring that new data is indexed and that other applications and components work properly by forcing a re-indexing of all or part of the catalog or by resetting the entire catalog.</li>
<li>Catalog properties - setting properties that determine how the catalog manages time-outs when connecting to protocol handlers and how diacritical marks are treated in searches.</li>
<li>Catalog status - getting information about the catalog, including status, size, and current activity state.</li>
<li>Access to other interfaces - retrieving other search-related interfaces required by the Crawl Scope Manager, data change notifications, and the <a href="/windows/desktop/api/Searchapi/nn-searchapi-isearchqueryhelper"><strong>ISearchQueryHelper</strong></a> interface.</li>
</ul>
For more information, see <a href="-search-3x-wds-mngidx-catalog-manager.md">Using the Catalog Manager</a>.<br/></td>
</tr>
<tr class="odd">
<td>Crawl Scope Manager</td>
<td><a href="/windows/desktop/api/Searchapi/nn-searchapi-ienumsearchroots"><strong>IEnumSearchRoots</strong></a><br/> <a href="/windows/desktop/api/searchapi/nn-searchapi-ienumsearchscoperules">IEnumSearchScopeRules</a><br/> <a href="/windows/desktop/api/Searchapi/nn-searchapi-isearchcrawlscopemanager"><strong>ISearchCrawlScopeManager</strong></a><br/> <a href="/windows/desktop/api/searchapi/nn-searchapi-isearchcrawlscopemanager2">ISearchCrawlScopeManager2</a><br/> <a href="/windows/desktop/api/Searchapi/nn-searchapi-isearchroot"><strong>ISearchRoot</strong></a><br/> <a href="/windows/desktop/api/Searchapi/nn-searchapi-isearchscoperule"><strong>ISearchScopeRule</strong></a><br/> <a href="/windows/desktop/search/-search-isearchitem">ISearchItem</a><br/></td>
<td>Provides methods to inform the search engine about containers to crawl or watch, and items under those containers to include or exclude in the index. You can also query the Crawl Scope Manager to see if a particular URL is in the crawl scope. For more information, see <a href="-search-3x-wds-extidx-csm.md">Using the Crawl Scope Manager</a>.<br/></td>
</tr>
</tbody>
</table>

## Related topics

[Managing the Index](-search-3x-wds-mngidx-overview.md)

[Using the Search Manager](-search-3x-wds-mngidx-searchmanager.md)

[Using the Catalog Manager](-search-3x-wds-mngidx-catalog-manager.md)

[Using the Crawl Scope Manager](-search-3x-wds-extidx-csm.md)
