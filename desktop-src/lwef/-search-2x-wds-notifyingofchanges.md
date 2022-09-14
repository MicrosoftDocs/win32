---
title: Notifying the Index of Changes (Legacy Windows Environment Features)
description: With Microsoft Windows Desktop Search (WDS) 2.6, protocol handlers for a given data store can tell the WDS Indexer when data in their store has changed.
ms.assetid: 700b1707-dd11-4a30-8f00-5c4aae1173ff
ms.topic: article
ms.date: 05/31/2018
---

# Notifying the Index of Changes (Legacy Windows Environment Features)

> [!NOTE]
> Windows Desktop Search 2.x is an obsolete technology that was originally available as an add-in for Windows XP and Windows Server 2003. On later releases, use [Windows Search](../search/-search-3x-wds-overview.md) instead.

With Microsoft Windows Desktop Search (WDS) 2.6, protocol handlers for a given data store can tell the WDS Indexer when data in their store has changed. This improves performance by ensuring the Indexer doesn't crawl the entire store on incremental indexes. Using notification APIs, protocol handlers can notify the Indexer that an item has been moved or deleted, and they can add scopes to the WDS Indexer's crawl queue of URLs requiring indexing. Notification is helpful for applications such as email, where the protocol handler monitors the store and notifies the Indexer that items have changed and require indexing.

## ISearchItemsChangedSink

Protocol handlers notify the Indexer of changes through the [**ISearchItemsChangedSink**](/windows/desktop/api/searchapi/nn-searchapi-isearchitemschangedsink) interface. Information about data changes should be collected in SEARCH\_ITEM\_CHANGE structs and SEARCH\_KIND\_OF\_CHANGE enumeration types and then communicated to the Indexer through the **OnItemsChanged** method of the **ISearchItemsChangedSink** interface.

To access this interface, a custom protocol handlers must first instantiate an [**ISearchManager**](/windows/desktop/api/searchapi/nn-searchapi-isearchmanager) object to gain access to the [**ISearchCatalogManager**](/windows/desktop/api/searchapi/nn-searchapi-isearchcatalogmanager) object. From there, one can instantiate an [**ISearchItemsChangedSink**](/windows/desktop/api/searchapi/nn-searchapi-isearchitemschangedsink) object and notify the Indexer of the data changes.

The OnItemsChanged method lets you collect and communicate data changes to your customer data store to initiate indexing.



| Direction | Variable              | Description                                                              |
|-----------|-----------------------|--------------------------------------------------------------------------|
| In        | dwNumberofChanges     | Total number of changes in the notification.                             |
| In        | DataChangeEntries\[\] | All change notifications in an array of SEARCH\_ITEM\_CHANGE structures. |
| Out       | dwBatchId             | The batch ID that will be passed back with errors.                       |
| Out       | hrCompletionCodes\[\] | Indicates whether each URL was accepted for indexing.                    |



 

The SEARCH\_ITEM\_CHANGE structure identifies the kind of change that occurred as well as the item's current URL and previous URL, if applicable. The structure is defined as follows:



| Property Name | Property Type                  | Description                                                                |
|---------------|--------------------------------|----------------------------------------------------------------------------|
| Change        | SEARCH\_KIND\_OF\_CHANGE       | The type of change that is being notified.                                 |
| URL           | LPWSTR                         | The URL for the object that has changed.                                   |
| OldURL        | LPWSTR                         | If the notification is a move, the old URL is provided and must be unique. |
| Priority      | SEARCH\_NOTIFICATION\_PRIORITY | The priority of the change.                                                |



 

The SEARCH\_KIND\_OF\_CHANGE enumeration is defined as follows:



| Enum Value                           | Value   | Description                                                                                     |
|--------------------------------------|---------|-------------------------------------------------------------------------------------------------|
| SEARCH\_CHANGE\_ADD                  | 0       | The notification is for an additional URL.                                                      |
| SEARCH\_CHANGE\_DELETE               | 1       | The notification is for the deletion of a URL.                                                  |
| SEARCH\_CHANGE\_MODIFY               | 2       | The notification is that a URL has been modified.                                               |
| SEARCH\_CHANGE\_MOVE\_RENAME         | 3       | The notification is for the move and rename of an object to a new URL.                          |
| SEARCH\_CHANGE\_SEMANTICS\_DIRECTORY | 0x10000 | The notification is for a container URL.                                                        |
| SEARCH\_CHANGE\_SEMANTICS\_SHALLOW   | 0x20000 | The notification is for a container URL that should only have its container properties indexed. |
| SEARCH\_CHANGE\_SEMANTICS\_SECURITY  | 0x40000 | The notification is for a URL or container URL that has had its security properties changed.    |



 

The SEARCH\_NOTIFICATION\_PRIORITY enumeration is defined as follows:



| Enum Value               | Value | Description                                                                                                                                                                    |
|--------------------------|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SEARCH\_NORMAL\_PRIORITY | 0     | Only a normal priority should be used when indexing the URL. These notifications are processed before the normal background incremental indexing of a user's files and stores. |



 

 

 
