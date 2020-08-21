---
title: Developing Protocol Handler Add-ins
description: You can extend Microsoft Windows Desktop Search (WDS) to include new data stores by implementing a custom protocol handler.
ms.assetid: 2447d95f-5832-453c-8857-3b4f4c158177
ms.topic: article
ms.date: 05/31/2018
---

# Developing Protocol Handler Add-ins

> [!NOTE]
> Windows Desktop Search 2.x is an obsolete technology that was originally available as an add-in for Windows XP and Windows Server 2003. On later releases, use [Windows Search](../search/-search-3x-wds-overview.md) instead.

You can extend Microsoft Windows Desktop Search (WDS) to include new data stores by implementing a custom protocol handler.

## Indexing Data Stores with Protocol Handlers

A data store is a content source (a database system, a directory, a file system) where data is stored and can be crawled by the WDS Indexer. The store can be hierarchical (like a database) or link-based (like a website). A protocol handler enables indexing applications like WDS to systematically crawl the nodes of a data store to extract relevant information to include in the index. Each protocol handler is used to index a specific type of data store. WDS ships with protocol handlers for file system stores and for both Microsoft Outlook and Microsoft Outlook Express data stores (email stores, .PST files, and so on). When indexing Outlook email, for example, the protocol handler crawls all messages in all folders extracting information from each message and attachment. This information is passed to the Indexer to include in the WDS catalog.

Often users need to search other data stores such as legacy databases, email stores or data structures not supported by WDS. You can extend WDS to crawl a new data store by using or implementing a protocol handler specifically for that data store. First, you should first determine if a protocol handler already exists for your data store, perhaps for use with another application like SharePoint Services. If so, you can install that protocol handler on the system. If, however, another protocol handler does not exist, then you need to implement one. WDS protocol handlers use the same design specifications as SharePoint Services, and they can often be used interchangeably.

Furthermore, if the data store contains data or file types other than one of the 200 file types supported by WDS, you also need to implement a filter to access and index the contents of items in the store. WDS 2.x uses the protocol handler and [**IFilter**](/windows/desktop/api/filter/nn-filter-ifilter)technology used by SharePoint Services. If you already have filters for a specific store and file type installed on the system being indexed, WDS uses the existing interfaces to index this data.

 

## Roadmap to Adding New Data Stores

To extend WDS to crawl new data stores, you can create a protocol handler and one or more of the following add-ins: context menu handler, icon handler and a SearchProtocolOptions add-in.

1.  Create and register a multithreaded protocol handler for the data store:
    -   **ISearchProtocol** - This interface accesses a protocol and maps a URL to an IUrlAccessor.
    -   **IUrlAccessor** - This is the main interface used for accessing items from the content source and binding the content to appropriate filter.
    -   **IProtocolHandlerSite** - This interface is used to request and load additional filters.
    -   **IFilter** - This interface returns the URL of each item in a folder as value properties for processing.

    > [!Note]
    >
    > The minimum add-in functionality needed to return search results from a non-hierarchical data store is an implementation of ISearchProtocol and IUrlAccessor interfaces.

     

2.  Implement the ISearchProtocolOptions interface to include customized protocol handler options, like predefined start page(s):
    -   **ISearchProtocolOptions** - This interface defines default URLs for the protocol handler to process, determines what the requirements are for a protocol handler, and determines whether the requirements have been met on a given system.
3.  Extend Shell to include user interface elements, like context menus and file-specific icons, by implementing the following interfaces:
    -   **IShellFolder** - This interface, which is used to manage folders, is required to provide the IContextMenu and IExtractIcon interfaces for a URL in a new store.
    -   **IPersistFolder** - This interface is required to instruct a Shell folder object to initialize itself.
    -   **IPersist** - This interface supplies the class identifier (CLSID) of an object that can be stored persistently in the system.
    -   **IContextMenu** - This interface defines the right-click context menu for an item pointed to by URL.
    -   **IExtractIcon** - This interface defines the icon to display for an item pointed to by URL.
4.  Implement a mechanism to notify the Indexer of changes to your data store:
    -   **ISearchItemsChangedSink** - This interface enables your protocol handler to notify the Index of changes to your data store. This improves performance by ensuring the Indexer doesn't crawl the entire store on incremental indexes.

## Related topics

<dl> <dt>

**Reference**
</dt> <dt>

[Implementing a Protocol Handler for WDS](-search-2x-wds-phimplementing.md)
</dt> <dt>

[Adding Icons, Previews, and Context Menus with Shell Extensions](-search-2x-wds-ph-ui-extensions.md)
</dt> <dt>

[Notifying the Index of Changes](-search-2x-wds-notifyingofchanges.md)
</dt> <dt>

[Installing and Registering Protocol Handlers](-search-2x-wds-ph-install-registration.md)
</dt> </dl>

 

 