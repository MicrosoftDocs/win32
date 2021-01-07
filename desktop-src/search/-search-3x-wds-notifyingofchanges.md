---
description: By using the notification APIs components can notify the indexer that an item has been changed, moved or deleted, and can add search scopes to the Windows Search indexer's queue of URLs that require indexing.
ms.assetid: 817550e2-a256-48d5-9fa6-1ea04f8b8589
title: Notifying the Index of Changes (Windows Search)
ms.topic: article
ms.date: 05/31/2018
---

# Notifying the Index of Changes (Windows Search)

By using the notification APIs components can notify the indexer that an item has been changed, moved or deleted, and can add search scopes to the Windows Search indexer's queue of URLs that require indexing.

Components can notify the Windows Search indexer that data in their store has changed. Typically, you can rely on the indexer's scheduled crawls. However, providing notifications to the indexer can improve performance by ensuring the indexer doesn't crawl the entire store on incremental indexes. For example, this might recommended if you expect your data store to be exceptionally large and/or exceptionally busy, such as an email data store for example.

-   [Implementing Indexer-managed Notifications](#implementing-indexer-managed-notifications)
    -   [Notifications Queue](#notifications-queue)
    -   [ISearchPersistentItemsChangedSink](#isearchpersistentitemschangedsink)
-   [Implementing Provider-managed Notifications](#implementing-provider-managed-notifications)
    -   [Notifications Queue](#notifications-queue)
    -   [ISearchItemsChangedSink](#isearchitemschangedsink)
    -   [ISearchNotifyInlineSite](#isearchnotifyinlinesite)
-   [Additional Resources](#additional-resources)
-   [Related topics](#related-topics)

## Implementing Indexer-managed Notifications

Indexer-managed notifications enable you to control access to your data store while freeing you of maintaining the notifications queue throughout the entire indexing process. Your notifications provider must monitor changes to the data store and create a notifications queue. Periodically, your provider sends a batch of change notifications to the indexer. When the indexer receives your notifications, it returns an acknowledgement and you can remove the item(s) from your queue. If after a period of time you do not receive an acknowledgement, you can re-send the notifications. In case of failure, the indexer rebuilds its internal queue of items to crawl or performs an incremental crawl of the store.

To implement indexer-managed notifications, you need to implement the following:

-   A mechanism for monitoring changes in your data store.
-   A data structure to queue up information (multiple [**SEARCH\_ITEM\_PERSISTENT\_CHANGE**](/windows/desktop/api/Searchapi/ns-searchapi-search_item_persistent_change) structures) about those changes.
-   [**ISearchPersistentItemsChangedSink**](/windows/desktop/api/Searchapi/nn-searchapi-isearchpersistentitemschangedsink) interface to send your notifications to the indexer and to get notification acknowledgements from the indexer.

### Notifications Queue

You need to monitor and queue up every change in your data store to send to the indexer as a notification. How many notifications you queue up and how frequently you send them to the indexer depends on your circumstance. Perhaps you send a batch of notifications for every *n* number of changes or after some *t* time interval, or a combination of the two.

The indexer expects the notifications to come in an array of [**SEARCH\_ITEM\_PERSISTENT\_CHANGE**](/windows/desktop/api/Searchapi/ns-searchapi-search_item_persistent_change) structures, so you may choose to implement your queue similarly.

### ISearchPersistentItemsChangedSink

To access this interface, you first instantiate an [**ISearchManager**](/windows/desktop/api/Searchapi/nn-searchapi-isearchmanager) object to gain access to an [**ISearchCatalogManager**](/windows/desktop/api/Searchapi/nn-searchapi-isearchcatalogmanager) object. From that **ISearchCatalogManager** object, you instantiate an [**ISearchPersistentItemsChangedSink**](/windows/desktop/api/Searchapi/nn-searchapi-isearchpersistentitemschangedsink) object and notify the indexer of the data changes with a call to the **OnItemsChanged** method.

In the call to this method, you include the number of changes being reported and an array of [**SEARCH\_ITEM\_PERSISTENT\_CHANGE**](/windows/desktop/api/Searchapi/ns-searchapi-search_item_persistent_change) structures. You get back an array of HR completion codes indicating whether each URL was accepted for indexing. This is your acknowledgement from the indexer.

## Implementing Provider-managed Notifications

Provider-managed notifications enable you to control access to your data store and to monitor the progress of the indexer as it updates the Windows Search catalog. Your provider must monitor changes to the data store and create a notifications queue. Periodically, your provider sends a batch of change notifications to the indexer. When the indexer receives your notifications, it returns an acknowledgement. If after a period of time you do not receive an acknowledgement, you can re-send the notifications. As the indexer crawls the data store and updates the Windows Search catalog, it notifies your provider of each catalog update and you can remove the item(s) from your queue. Your provider maintains its notification queue throughout this process so that in case of failure, you can resend notifications to the indexer.

To implement provider-managed notifications, you need to implement the following:

-   A mechanism for monitoring changes in your data store.
-   A data structure to queue up information (multiple [**SEARCH\_ITEM\_CHANGE**](/windows/desktop/api/Searchapi/ns-searchapi-search_item_change) structures) about those changes.
-   [**ISearchItemsChangedSink**](/windows/desktop/api/Searchapi/nn-searchapi-isearchitemschangedsink) interface to send your notifications to the indexer and to get notification acknowledgements from the indexer.
-   [**ISearchNotifyInlineSite**](/windows/desktop/api/Searchapi/nn-searchapi-isearchnotifyinlinesite) interface to receive updates about the status of indexing.

### Notifications Queue

You need to monitor and queue up every change in your data store to send to the indexer as a notification. How many notifications you queue up and how frequently you send them to the indexer depends on your circumstance. Perhaps you send a batch of notifications for every *n* number of changes or after some *t* time interval, or a combination of the two.

The indexer expects the notifications to come in an array of [**SEARCH\_ITEM\_CHANGE**](/windows/desktop/api/Searchapi/ns-searchapi-search_item_change) structures, so you may choose to store change information similarly. However, you also need to be able to match the notifications you send with the acknowledgements and updates returned by the indexer. You may also want to be able to detect how long it takes to get acknowledgements, so you can decide if/when to resend notifications.

### ISearchItemsChangedSink

To access this interface, you first instantiate an [**ISearchManager**](/windows/desktop/api/Searchapi/nn-searchapi-isearchmanager) object to gain access to an [**ISearchCatalogManager**](/windows/desktop/api/Searchapi/nn-searchapi-isearchcatalogmanager) object. From that **ISearchCatalogManager** object, you instantiate an [**ISearchItemsChangedSink**](/windows/desktop/api/Searchapi/nn-searchapi-isearchitemschangedsink) object and notify the indexer of the data changes with a call to the **OnItemsChanged** method.

In the call to this method, you include the number of changes being reported and an array of [**SEARCH\_ITEM\_CHANGE**](/windows/desktop/api/Searchapi/ns-searchapi-search_item_change) structures. You get back an array of indexer-assigned DocIds that represent each change as well as an array of HR completion codes indicating whether each URL was accepted for indexing. This is your acknowledgement from the indexer that it has received your notifications and is preparing to index the items.

From that point forward the indexer sends updates using the [**ISearchNotifyInlineSite**](/windows/desktop/api/Searchapi/nn-searchapi-isearchnotifyinlinesite) interface.

### ISearchNotifyInlineSite

In order to get updates about the status of both your items and the catalog, you must register your [**ISearchNotifyInlineSite**](/windows/desktop/api/Searchapi/nn-searchapi-isearchnotifyinlinesite) interface with the indexer so it can send you callbacks. Each update sent using [**ISearchNotifyInlineSite::OnItemIndexedStatusChange**](/windows/desktop/api/Searchapi/nf-searchapi-isearchnotifyinlinesite-onitemindexedstatuschange) identifies the items by DocId, the status of each item ([**SEARCH\_ITEM\_INDEXING\_STATUS**](/windows/desktop/api/Searchapi/ns-searchapi-search_item_indexing_status)) and the indexing phase ([**SEARCH\_INDEXING\_PHASE**](/windows/desktop/api/Searchapi/ne-searchapi-search_indexing_phase)) the items are in.

Not only do you receive updates on the status of each item, as described earlier, you also get important information about the status of the catalog itself. The Windows Search service can be interrupted or restarted by the end user, a third party application, or some other failure. When this happens, you need a way to determine what notifications to repush to the indexer.

The [**ISearchNotifyInlineSite::OnCatalogStatusChange**](/windows/desktop/api/Searchapi/nf-searchapi-isearchnotifyinlinesite-oncatalogstatuschange) method, called by the Windows Search service, informs clients about the status of the catalog using the parameters described in the following table.



| Parameter                 | Description                                                                                                                                           |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| guidCatalogResetSignature | A GUID representing the catalog reset. If this GUID changes, all notifications must be resent.                                                        |
| guidCheckPointSignature   | A GUID representing the last checkpoint restored. If this GUID changes, all notifications accumulated since the last saved checkpoint must be resent. |
| dwLastCheckPointNumber    | A number indicating the last checkpoint saved.                                                                                                        |



 

 

When a catalog checkpoint occurs, the search service updates the *dwLastCheckPointNumber*, and all notifications sent prior to that checkpoint are safe and recoverable in the event of a service failure. Notifications providers need to track only those notifications sent between checkpoints and repush in case of a catalog restore or reset.

If a catalog restore occurs, the search service rolls back the catalog to the last saved checkpoint and updates the *guidCheckPointSignature*. In this situation, notifications providers must repush all notifications accumulated since the most recent saved checkpoint as identified by the *dwLastCheckPointNumber*.

If a catalog reset should occur, the search service resets the entire catalog and updates the *guidCatalogResetSignature*. Notifications provider must repush its entire crawl scope again.

## Additional Resources

-   For an overview of the indexing process, see [The Indexing Process](-search-indexing-process-overview.md).
-   For overviews of the Catalog Manager and Catalog Search Manager (CSM), see [Using the Catalog Manager](-search-3x-wds-mngidx-catalog-manager.md) and [Using the Crawl Scope Manager](-search-3x-wds-extidx-csm.md).
-   For information about creating a Shell data store, see [Implementing the Basic Folder Object Interfaces](/previous-versions/windows/desktop/legacy/cc144093(v=vs.85)).

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[Developing Protocol Handlers](-search-3x-wds-phaddins.md)
</dt> <dt>

[Understanding Protocol Handlers](-search-3x-wds-extidx-prot-implementing.md)
</dt> <dt>

[Adding Icons and Context Menus](-search-3x-wds-ph-ui-extensions.md)
</dt> <dt>

[Code Sample: Shell Extensions for Protocol Handlers](-search-3x-wds-ph-ui-samplecode.md)
</dt> <dt>

[Installing and Registering Protocol Handlers](-search-3x-wds-ph-install-registration.md)
</dt> <dt>

[Creating a Search Connector for a Protocol Handler](-search-3x-wds-ph-search-connector.md)
</dt> <dt>

[Debugging Protocol Handlers](-search-ws-protocolhandlertesting.md)
</dt> </dl>

 

 
