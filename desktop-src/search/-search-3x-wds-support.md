---
description: Notifications Process in Windows Search
ms.assetid: 378e346b-2067-484f-85e9-76673a35550b
title: Notifications Process in Windows Search
ms.topic: article
ms.date: 05/31/2018
---

# Notifications Process in Windows Search

This topic is organized as follows:

-   [Overview of the Notifications Process](#overview-of-the-notifications-process)
-   [Crawls](#crawls)
-   [Indexer-Managed Notifications](#indexer-managed-notifications)
-   [Provider-Managed Notifications](#provider-managed-notifications)
-   [Notifications on Rowsets](#notifications-on-rowsets)
-   [Related topics](#related-topics)

## Overview of the Notifications Process

There are three approaches by which data from your data store can be indexed:

-   Crawls
-   Indexer-managed notifications
-   Provider-managed notifications

The merits of each approach are described in the following sections.

## Crawls

Notification-enabled sources do an incremental crawl on start-up and then rely on notifications or an explicit command to crawl again. This happens automatically on Windows Vista and later. On operating systems prior to Windows Vista, you must set up a scheduled event in the [Task Scheduler](../taskschd/task-scheduler-start-page.md) that calls into your code to initiate a crawl over your start page(s). You do not need to implement any form of notifications. As a background process, the indexer traverses its crawl scope, looking for changes and updating the catalog. This option is recommended for almost all situations.

## Indexer-Managed Notifications

With indexer-managed notifications, you implement a notification strategy that notifies the indexer when data in the data store has changed, and the indexer manages tracking the notifications and indexing the data. In this situation, your component (which we'll call a notifications provider) monitors the data store, collects information about changes to the store, and then periodically notifies the indexer with a list of items that need indexing. The indexer is responsible for recovering and resolving notifications in case of failure. This option, which you can think of as the "send it and forget it" strategy, reduces the frequency of indexer crawls.

## Provider-Managed Notifications

With provider-managed notifications, you implement a notification strategy that is similar to the second approach, except that your notifications provider must track notifications and is responsible for recovering and resolving notifications in case of failure. In this situation, your notifications provider monitors the data store, collects and maintains information about changes to the store, periodically notifies the indexer with a list of items that need indexing, receives status updates from the indexer, and re-sends notifications in case of failure.

> [!Note]  
> This option is **not recommended unless** you expect incremental crawls of your data store to hinder performance significantly, and you require granular control over or insight into the indexing status.

 

## Notifications on Rowsets

In Windows 7 and later, indexing eventing enables providers to receive notifications about their rowsets. Providers that use indexing eventing can maintain their rowsets in a manner that resembles the behavior of actual file system locations. Libraries and searches are the primary examples of non-file-system locations in Windows 7. Indexer eventing is to library views as notifications are to file-folder views. The [**IRowsetEvents**](/windows/desktop/api/Searchapi/nn-searchapi-irowsetevents) interface must be implemented in order to receive notifications of events. The data layer is the primary client of indexer eventing, and decides what to do with events in the Items View UI. For more information, see [Indexing Prioritization and Rowset Events in Windows 7](indexing-prioritization-and-rowset-events.md).

In contrast, in Windows Vista, query based views have no associated eventing, except for the Shell cache for file property edits. When you perform a search, the results that are returned are static. Hence, if another document is added to your system that matches your search term, your view is not updated to include the new addition. This behavior is standard for static web-based results. However, static results are less acceptable when you are trying to provide a query-based view over a storage location. Users expect that content from the indexer is current. For more information, see [Notifying the Index of Changes](-search-3x-wds-notifyingofchanges.md). For reference documentation, see [Notifications Interfaces](-search-notifications-interfaces-entry-page.md).

## Related topics

<dl> <dt>

[Indexing, Querying and Notifications in Windows Search](-search-3x-wds-included-in-index.md)
</dt> <dt>

[What is Included in the Index](-search-indexing-process-overview.md)
</dt> <dt>

[Indexing Process in Windows Search](-search-indexing-process-overview.md)
</dt> <dt>

[Querying Process in Windows Search](querying-process--windows-search-.md)
</dt> <dt>

[URL Formatting Requirements](url-formatting-requirements.md)
</dt> </dl>

 

 
