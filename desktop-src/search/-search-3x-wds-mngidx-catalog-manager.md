---
description: The ISearchCatalogManager and ISearchCatalogManager2 interfaces provide methods to manage a search catalog, such as causing re-indexing or setting time-outs.
ms.assetid: 8dad7012-d610-4398-8e86-cd319db8c360
title: Using the Catalog Manager
ms.topic: article
ms.date: 05/31/2018
---

# Using the Catalog Manager

The [**ISearchCatalogManager**](/windows/desktop/api/Searchapi/nn-searchapi-isearchcatalogmanager) and [**ISearchCatalogManager2**](/windows/desktop/api/Searchapi/nn-searchapi-isearchcatalogmanager2) interfaces provide methods to manage a search catalog, such as causing re-indexing or setting time-outs. While Windows Search currently uses only one catalog, this interface was designed to give you greater control for managing multiple catalogs independently. The interface manages the catalog in the following ways:

- Access to other interfaces — retrieving other search-related interfaces required by the Crawl Scope Manager, data change notifications, and the [**ISearchQueryHelper**](/windows/desktop/api/Searchapi/nn-searchapi-isearchqueryhelper) interface.
- Catalog contents — ensuring that new data is indexed and that other applications and components work properly by forcing a re-indexing of all or part of the catalog or by resetting the entire catalog.
- Catalog properties — setting properties that determine how the catalog manages time-outs when connecting to protocol handlers and how diacritical marks are treated in searches.
- Catalog status — getting information about the catalog, including status, size, and current activity state.

This topic is organized as follows:

- [Accessing Related Interfaces](#accessing-related-interfaces)
- [Managing the Catalog Contents](#managing-the-catalog-contents)
- [Managing Catalog Status](#managing-catalog-status)
- [Managing Catalog Properties](#managing-catalog-properties)
- [Running in Elevated Mode](#running-in-elevated-mode)
- [Related topics](#related-topics)

## Accessing Related Interfaces

Some useful interfaces in the Windows Search platform require an instance of the Catalog Manager before they can be used. To create a Catalog Manager for a specified catalog, call the [**ISearchManager::GetCatalog**](/windows/desktop/api/Searchapi/nf-searchapi-isearchmanager-getcatalog) method. The methods of the Catalog Manager can then be used to instantiate and return interfaces that are based on the specified catalog.

| Method                                                                                               | Description                                                                                                                                                                                                                                                                                                                                                                        |
|------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetQueryHelper**](/windows/desktop/api/Searchapi/nf-searchapi-isearchcatalogmanager-getqueryhelper)                               | Gets an instance of the [**ISearchQueryHelper**](/windows/desktop/api/Searchapi/nn-searchapi-isearchqueryhelper) interface for the current catalog, to enable you to build queries easily.                                                                                                                                                                                                                         |
| [**GetCrawlScopeManager**](/windows/desktop/api/Searchapi/nf-searchapi-isearchcatalogmanager-getcrawlscopemanager)                   | Gets an instance of [**ISearchCrawlScopeManager**](/windows/desktop/api/Searchapi/nn-searchapi-isearchcrawlscopemanager) for this search catalog, to enable developers to modify the crawl scope of the Windows Search Indexer.                                                                                                                                                                                    |
| [**GetItemsChangedSink**](/windows/desktop/api/Searchapi/nf-searchapi-isearchcatalogmanager-getitemschangedsink)                     | Gets an instance of the [**ISearchItemsChangedSink**](/windows/desktop/api/Searchapi/nn-searchapi-isearchitemschangedsink) interface, which client applications use to notify the indexer of changes when the client wants indexing status information about the item to support provider-managed notifications. See [Notifying the Index of Changes](-search-3x-wds-notifyingofchanges.md) for more information. |
| [**GetPersistentItemsChangedSink**](/windows/desktop/api/Searchapi/nf-searchapi-isearchcatalogmanager-getpersistentitemschangedsink) | Gets an instance of [**ISearchPersistentItemsChangedSink**](/windows/desktop/api/Searchapi/nn-searchapi-isearchpersistentitemschangedsink), which client applications use to notify the indexer of changes when the client does not want indexing status information (indexer-managed notifications). See [Notifying the Index of Changes](-search-3x-wds-notifyingofchanges.md) for more information.            |

## Managing the Catalog Contents

There are two primary tasks involved in managing the catalog: re-indexing all or some of the URLs in the indexer's crawl scope, and resetting the entire underlying catalog. When you re-index URLs, old data remains in the catalog until or unless it is replaced by new data. When you reset the catalog, the entire catalog is rebuilt and all URLs in the crawl scope are re-indexed. This process can take a lot of time and should be used only as a last resort for solving issues such as a possibly corrupted index.

When you install a new application, protocol handler, or filter, the setup application should add its directory or root to the crawl scope to ensure that the indexer includes the location of that application's data. If the data does not appear in the catalog after the indexer has crawled its crawl scope, then you should first ensure that the location of the data is included in the crawl scope. You can add it by using the user interface for Windows Search options or the [Crawl Scope Manager](-search-3x-wds-extidx-csm.md). If the location appears to be in the crawl scope, you can manually force a re-indexing of all URLs in the indexer's crawl scope or a subset, by using the following methods of the [**ISearchCatalogManager**](/windows/desktop/api/Searchapi/nn-searchapi-isearchcatalogmanager) interface.

| Re-indexing method                                                                                                                                                                                                                | Description                                                                                                                                                                                                                                                          |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ISearchCatalogManager::Reindex**](/windows/desktop/api/Searchapi/nf-searchapi-isearchcatalogmanager-reindex)                                                                                                                                                   | Re-indexes all URLs in the catalog. The old information will remain until it is replaced by new information.                                                                                                                                                         |
| [**ISearchCatalogManager::ReindexMatchingURLs**](/windows/desktop/api/Searchapi/nf-searchapi-isearchcatalogmanager-reindexmatchingurls)<br/> [**ISearchCatalogManager::ReindexSearchRoot**](/windows/desktop/api/Searchapi/nf-searchapi-isearchcatalogmanager-reindexsearchroot)<br/> | Re-indexes URLs that match the pattern or start at a particular root (for example, file:///C:\\Foldername\\Subfoldername\\). This is useful for recrawling everything in a particular directory or with a particular extension, as when an application is installed. |
| [**PrioritizeMatchingURLs**](/windows/desktop/api/Searchapi/nf-searchapi-isearchcatalogmanager2-prioritizematchingurls)                                                                                                                                           | Instructs the indexer to prioritize indexing items with URLs that match a specified pattern over completing other indexing tasks.                                                                                                                                    |

**Resetting the Index.** You can reset the entire index with a call to [**ISearchCatalogManager::Reset**](/windows/desktop/api/Searchapi/nf-searchapi-isearchcatalogmanager-reset). This resets the underlying catalog by rebuilding the databases and performing a full index of all URLs in the crawl scope. This process can take a lot of time and should be used only as a last resort for solving issues such as a possibly corrupted index.

> [!IMPORTANT]
> Because of the slowdown in indexing that these methods can cause, they should be used carefully when you are trying to identify indexing or catalog problems. First, make sure your search roots and scope rules are added in the Crawl Scope Manager, and then make sure that the FANCI bit (File Attribute Not Content Indexed) is set properly for files and folders. If you have confirmed that these are correct, try ReindexSearchRoot first and Reindex last. If neither of these work, then try Reset as a last resort.

For related information, see [Notifying the Index of Changes](-search-3x-wds-notifyingofchanges.md), and [Querying the Index with ISearchQueryHelper](-search-3x-wds-qryidx-searchqueryhelper.md)

## Managing Catalog Status

The Catalog Manager can be used to get the status of the catalog for applications that want to customize how the catalog is managed (for example, a custom "Catalog Status" monitoring application). But the Catalog Manager is not typically required for most search-related development scenarios. Common uses would be for a "Catalog Status" monitoring application or a Control Panel-style application.

The following table describes the methods of ISearchCatalogManager used for managing catalog status.


| Method | Description | 
|--------|-------------|
| <a href="/windows/desktop/api/Searchapi/nf-searchapi-isearchcatalogmanager-urlbeingindexed"><strong>URLBeingIndexed</strong></a> | Gets the URL that is currently being indexed. This method would be useful if you were trying to identify whether the indexer was "stuck" on an item. | 
| <a href="/windows/desktop/api/Searchapi/nf-searchapi-isearchcatalogmanager-numberofitems"><strong>NumberOfItems</strong></a> | Gets the number of items in the catalog. | 
| <a href="/windows/desktop/api/Searchapi/nf-searchapi-isearchcatalogmanager-numberofitemstoindex"><strong>NumberOfItemsToIndex</strong></a> | Retrieves the following information about items to be indexed:<ul><li>plIncrementalCount - the number of items to be indexed in the next incremental index</li><li>plNotificationQueue - the number of items in the notification queue. This information would be useful to a notification application that needed to check whether the indexer is receiving the notifications that the application is sending.</li><li>plHighPriorityQueue - the number of items in the high-priority queue. Items in the plHighPriorityQueue are indexed first.</li></ul> | 
| <a href="/windows/desktop/api/Searchapi/nf-searchapi-isearchcatalogmanager-getcatalogstatus"><strong>GetCatalogStatus</strong></a> | Gets the status of the catalog and returns an enumeration value that gives the current status. The following are possible catalog states:<ul><li>Idle: No indexing is needed.</li><li>Paused: Indexing is paused (due to low battery or high CPU usage, for example).</li><li>Recovering: Indexing is recovering.</li><li>Full crawl: Indexer is performing a full crawl of the crawl scope.</li><li>Incremental crawl: Indexer is performing an incremental crawl.</li><li>Processing notifications: Indexer is processing notifications.</li><li>Shutting down: Indexer is shutting down.</li></ul> | 
| <a href="/windows/desktop/api/Searchapi/nf-searchapi-isearchcatalogmanager-get_name"><strong>get_Name</strong></a> | Gets the name of the current catalog that is specified in the <a href="/windows/desktop/api/Searchapi/nf-searchapi-isearchmanager-getcatalog"><strong>ISearchManager::GetCatalog</strong></a> method. Currently, the only catalog supported is SystemIndex. | 


## Managing Catalog Properties

There are three catalog properties that you can manage with the Catalog Manager:

- **Diacritic sensitivity.** Diacritics are accent marks added to letters to signify a word's meaning or pronunciation. This property determines whether the catalog is sensitive to diacritics, and is important when you or your users search and index text in multiple languages. For example, with this property set to **FALSE**, the catalog would treat "resume" and "resumé" as if they were the same word.
- **Connection timeouts.** This property represents the amount of time to wait for a connection response from a server or data store, as represented in a [**TIMEOUT\_INFO**](/windows/desktop/api/Searchapi/ns-searchapi-timeout_info) structure. You can use this property to fine tune Windows Search.
- **Data timeouts** This property represents the amount of time to wait for a data transaction between the indexer and a protocol handler or filter, as represented in a [**TIMEOUT\_INFO**](/windows/desktop/api/Searchapi/ns-searchapi-timeout_info) structure. If this time has elapsed, the process from the Filter Daemon is terminated to prevent deadlock and other resource problems.

The last two properties are intended primarily for future use. Each of these properties has `get` and `put` methods.

| Method                                                                                                                                                                                                          | Description                                                                                                                                                                                                                                     |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**get\_DiacriticSensitivity**](/windows/desktop/api/Searchapi/nf-searchapi-isearchcatalogmanager-get_diacriticsensitivity) /<br/> [**put\_DiacriticSensitivity**](/windows/desktop/api/Searchapi/nf-searchapi-isearchcatalogmanager-put_diacriticsensitivity)<br/> | TRUE if the catalog should differentiate words with diacritics. **FALSE** if the catalog should ignore diacritics. Changing this property requires rebuilding the index because the keys of the index may become invalid.                       |
| [**get\_ConnectTimeout**](/windows/desktop/api/Searchapi/nf-searchapi-isearchcatalogmanager-get_connecttimeout) /<br/> [**put\_ConnectTimeout**](/windows/desktop/api/Searchapi/nf-searchapi-isearchcatalogmanager-put_connecttimeout)<br/>                         | The time, in seconds, that the indexer should wait for a connection response from a server or data store. Setting this too high can cause delays if many sites are unresponsive. Setting it too low can result in some sites not being crawled. |
| [**get\_DataTimeout**](/windows/desktop/api/Searchapi/nf-searchapi-isearchcatalogmanager-get_datatimeout) /<br/> [**put\_DataTimeout**](/windows/desktop/api/Searchapi/nf-searchapi-isearchcatalogmanager-put_datatimeout)<br/>                                     | The time, in seconds, that the indexer should wait for a data transaction.                                                                                                                                                                      |

## Running in Elevated Mode

Any method calls that update the SystemIndex require your application to be run elevated. Otherwise, your application will fail with an Access Denied error.

## Related topics


[Managing the Index](-search-3x-wds-mngidx-overview.md)

[Interfaces for Managing the Index](interfaces-for-managing-the-index.md)

[Using the Search Manager](-search-3x-wds-mngidx-searchmanager.md)

[Using the Crawl Scope Manager](-search-3x-wds-extidx-csm.md)
