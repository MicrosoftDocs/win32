---
Description: Windows Search enables you to manage the Windows Search index with three main components Search Manager, Catalog Manager, and Crawl Scope Manager.
ms.assetid: 80f0387c-5c91-41b8-9767-5f5e6563c112
title: Interfaces for Managing the Index
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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
<td>Search?Manager</td>
<td>[ISearchManager](/windows/win32/Searchapi/nn-searchapi-isearchmanager?branch=master)</td>
<td>Provides methods to retrieve and set information about Windows Search:
<ul>
<li>Getting an instance of the Catalog Manager for a specific catalog.</li>
<li>Getting or setting proxy information.</li>
<li>Getting version information about the Windows Search engine.</li>
</ul>
For more information, see [Using the Search Manager](-search-3x-wds-mngidx-searchmanager.md).<br/></td>
</tr>
<tr class="even">
<td>Catalog?Manager</td>
<td>[ISearchCatalogManager](/windows/win32/Searchapi/nn-searchapi-isearchcatalogmanager?branch=master)<br/> [ISearchCatalogManager2](http://msdn.microsoft.com/en-us/library/cc142932(VS.85).aspx)<br/></td>
<td>Provides methods to manage an individual search catalog, such as causing a re-indexing or setting time-outs. This interface manages the catalog in four areas:
<ul>
<li>Catalog contents - ensuring that new data is indexed and that other applications and components work properly by forcing a re-indexing of all or part of the catalog or by resetting the entire catalog.</li>
<li>Catalog properties - setting properties that determine how the catalog manages time-outs when connecting to protocol handlers and how diacritical marks are treated in searches.</li>
<li>Catalog status - getting information about the catalog, including status, size, and current activity state.</li>
<li>Access to other interfaces - retrieving other search-related interfaces required by the Crawl Scope Manager, data change notifications, and the [<strong>ISearchQueryHelper</strong>](/windows/win32/Searchapi/nn-searchapi-isearchqueryhelper?branch=master) interface.</li>
</ul>
For more information, see [Using the Catalog Manager](-search-3x-wds-mngidx-catalog-manager.md).<br/></td>
</tr>
<tr class="odd">
<td>Crawl?Scope?Manager</td>
<td>[<strong>IEnumSearchRoots</strong>](/windows/win32/Searchapi/nn-searchapi-ienumsearchroots?branch=master)<br/> [IEnumSearchScopeRules](http://msdn.microsoft.com/en-us/library/bb266499(VS.85).aspx)<br/> [<strong>ISearchCrawlScopeManager</strong>](/windows/win32/Searchapi/nn-searchapi-isearchcrawlscopemanager?branch=master)<br/> [ISearchCrawlScopeManager2](http://msdn.microsoft.com/en-us/library/dd797832(VS.85).aspx)<br/> [<strong>ISearchRoot</strong>](/windows/win32/Searchapi/nn-searchapi-isearchroot?branch=master)<br/> [<strong>ISearchScopeRule</strong>](/windows/win32/Searchapi/nn-searchapi-isearchscoperule?branch=master)<br/> [ISearchItem](http://msdn.microsoft.com/en-us/library/dd756722(VS.85).aspx)<br/></td>
<td>Provides methods to inform the search engine about containers to crawl or watch, and items under those containers to include or exclude in the index. You can also query the Crawl Scope Manager to see if a particular URL is in the crawl scope. For more information, see [Using the Crawl Scope Manager](-search-3x-wds-extidx-csm.md).<br/></td>
</tr>
</tbody>
</table>



 

## Related topics

<dl> <dt>

[Managing the Index](-search-3x-wds-mngidx-overview.md)
</dt> <dt>

[Using the Search Manager](-search-3x-wds-mngidx-searchmanager.md)
</dt> <dt>

[Using the Catalog Manager](-search-3x-wds-mngidx-catalog-manager.md)
</dt> <dt>

[Using the Crawl Scope Manager](-search-3x-wds-extidx-csm.md)
</dt> </dl>

 

 




