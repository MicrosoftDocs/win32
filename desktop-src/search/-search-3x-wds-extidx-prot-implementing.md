---
description: Some applications store their items in databases or custom file types.
ms.assetid: 0e2b7b4b-ae87-4092-b924-6191cdf42c9b
title: Understanding Protocol Handlers
ms.topic: article
ms.date: 05/31/2018
---

# Understanding Protocol Handlers

Some applications store their items in databases or custom file types. While Windows Search can index the name and properties of the file, Windows has no knowledge of the content of the file. As a result, such items cannot be indexed or exposed in the Windows Shell. By creating a protocol handler you can make these items available for indexing. You can also index a compound file format such as a .zip file.

This topic is organized as follows:

-   [Indexing Data Stores with Protocol Handlers](#indexing-data-stores-with-protocol-handlers)
    -   [Shell Data Stores](#shell-data-stores)
    -   [Protocol Handlers](#protocol-handlers)
    -   [Filters and Protocol Handlers](#filters-and-protocol-handlers)
-   [Indexing a Compound File Format](#indexing-a-compound-file-format)
-   [Related topics](#related-topics)

## Indexing Data Stores with Protocol Handlers

When users need to search legacy databases, email stores or other data structures that are not supported by Windows Search, you should first determine whether a protocol handler already exists for that data store, perhaps for use with another application such as SharePoint Server. If so, you can install that protocol handler on the system. Windows Search protocol handlers use design specifications similar to SharePoint Server, and they can often be used interchangeably.

For more information about Search Server 2008 deployment with Office SharePoint Server 2007, see [Federated Search \[Search Server 2008\]](/previous-versions/office/bb931109(v=office.14)).

### Shell Data Stores

Before a third-party developer of new file formats and data stores can get those formats and stores to appear in query results in Windows Explorer, the developer must implement a Shell data source. A Shell data source is a component that is used to extend the Shell namespace and expose items in a data store. A data store is a repository of data. A data store can be exposed to the Shell programming model as a container that uses a Shell data source. The items in a data store can be indexed by the Windows Search system using a protocol handler. The protocol handler implements the protocol for accessing a content source in its native format. The [**ISearchProtocol**](/windows/desktop/api/Searchapi/nn-searchapi-isearchprotocol) and [**ISearchProtocol2**](/windows/desktop/api/Searchapi/nn-searchapi-isearchprotocol2) interfaces are used to implement a custom protocol handler to expand the data sources that can be indexed.

If you want the query results to appear in Windows Explorer, you must implement a Shell data source before you can create a protocol handler to extend the index. However, if all queries will be programmatic (through OLE DB for example) and interpreted by the application's code rather than the Shell, a Shell namespace while still preferred is not strictly required.

> [!Note]  
> A Shell data source is sometimes known as a Shell namespace extension. A handler is sometimes known as a Shell extension or a Shell extension handler.

 

If you want users to view their search results from within Windows Explorer, then you must create a protocol handler and one or more of the following add-ins:

-   Shortcut menu handler
-   Icon handler
-   Some other type of file handler

For a list of handlers identified by the developer scenario you are trying to achieve, see "Overview of Handlers" in [Windows Search as a Development Platform](-search-3x-wds-development-ovr.md). For information on creating handlers, see [Registering Shell Extensions](../shell/reg-shell-exts.md), [Context Menu](/previous-versions/windows/desktop/legacy/cc144169(v=vs.85)), and [File Type Handlers](../shell/fa-file-extensions.md).

### Protocol Handlers

If the data store is also a container (such as a file system folder), you must implement a filter to enumerate the URLs in the container. If the data store contains data or file types other than one of the 200 file types supported by Windows Search, you must implement a filter to access and index the contents of items in the store. Windows Search uses protocol handler and [**IFilter**](/windows/win32/api/filter/nn-filter-ifilter) technology similar to that used by SharePoint Server. If you already have filters for a specific store and file type installed on the system being indexed, Windows Search may be able to use the existing interfaces to index this data.

For an overview of the indexing process, see [The Indexing Process](-search-indexing-process-overview.md). For conceptual information on filter handlers, see [Developing Filter Handlers](-search-ifilter-conceptual.md).

### Filters and Protocol Handlers

Protocol handlers give the Windows Search indexer access to data stores, enabling the indexer to crawl the nodes of a data store and extract relevant information to index. Windows Search, for example, ships with protocol handlers for file system stores and for some versions of both Microsoft Outlook data stores. When indexing Outlook email, the protocol handler crawls all messages in a set of Outlook folders and extracts information from each message and attachment. This information is passed to the indexer for inclusion in the Windows Search catalog.

For overviews of the Catalog Manager and Crawl Scope Manager (CSM), see [Using the Catalog Manager](-search-3x-wds-mngidx-catalog-manager.md) and [Using the Crawl Scope Manager](-search-3x-wds-extidx-csm.md).

## Indexing a Compound File Format

A compound file format can be indexed so that individual items in the file can can be returned as individual results. A compound file format such as a compressed file with a .zip file name extension is essentially a data store and can be treated as such for indexing purposes. The following example displays a .zip file in the file system namespace (FILE://c:/test/test.zip) in which there are both subfolders and individual items.

``` syntax
Test.zip 

    |-folder1 

    |    |-folder2 

    |           |- FileX.txt 

    |- FileY.doc
```

The FILE protocol handler discovers when FILE://c:/test/test.zip changes by monitoring file system change logs, and it will invoke an [**IFilter**](/windows/win32/api/filter/nn-filter-ifilter) registered for .zip files on that file when the file changes, but it has no knowledge of the internal structure of the .zip file itself.

You must inform the indexer that the compound file format is a data store. It is necessary to do so for individual items to be indexed and retrieved as unique entities. After you have implemented a Shell data source and performed the following steps, you will have a protocol handler that can process and expose the data from a compound file format (a .zip file) as individual items.

**To inform the indexer that a compound file is a data store:**

1.  Create a protocol handler (using [**ISearchProtocol**](/windows/desktop/api/Searchapi/nn-searchapi-isearchprotocol) or [**ISearchProtocol2**](/windows/desktop/api/Searchapi/nn-searchapi-isearchprotocol2)) for .zip files that has the ability bind to the source file. For more information, see [Installing and Registering Protocol Handlers](-search-3x-wds-ph-install-registration.md).

    For example, you could use an escaped path to the .zip file as the root folder name and then use a hierarchy syntax like any other file format.

    ``` syntax
    .zip:///escapedPathTo.zipFile/.zipfolder/.../.zipfile
    ```

    Using the above sample data for c:\\test\\test.zip, the unique URLs would be as follows. With these URLs the protocol handler has the information necessary to bind to the .zip file and enumerate the child URLs including the inner files so that they can be bound to and indexed by the .doc and .txt filters.

    ``` syntax
      

    .zip:///FILE:%2f%2f%2fc:%2ftest%2ftest.zip/ 

    .zip:///FILE:%2f%2f%2fc:%2ftest%2ftest.zip/FileY.Doc 

    .zip:///FILE:%2f%2f%2fc:%2ftest%2ftest.zip/folder1 

    .zip:///FILE:%2f%2f%2fc:%2ftest%2ftest.zip/folder1/folder2 

    .zip:///FILE:%2f%2f%2fc:%2ftest%2ftest.zip/folder1/folder2/FileX.txt
    ```

2.  Ensure that your protocol handler meets the following two conditions:
    -   The root URLs for a .zip file should emit PKEY\_Search\_IsClosedDirectory ([System.Search.IsClosedDirectory](../properties/props-system-search-iscloseddirectory.md)) on the URLs that are the root .zip file URLs. For example, .zip:///FILE:%2f%2f%2fc:%2ftest%2ftest.zip/ should emit IsClosedDirectory = **TRUE**. This tells the indexer that if the date on this URL has not changed, it does not need to process any of the child URLs.
    -   Every child URL for that URL should emit PKEY\_Search\_IsFullyContained ([System.Search.IsFullyContained](../properties/props-system-search-isfullycontained.md)) on the child URLs of the root .zip URL. Normally at the end of an incremental crawl, the indexer treats all unvisited URLs as items that should be deleted. But the root .zip file should not process root URLs because nothing has changed. Emitting this property as **TRUE** tells the indexer that if this URL has not been processed at the end of an incremental crawl, it should not be deleted. It will only be deleted if the root item has changed and it is not visited.

Windows Search requires a start page for a protocol in order to know what URLs to crawl incrementally and which URLs should be ignored when they are found. But we can't start with a URL for each .zip file, because we don't know where each .zip file is. Hence, the .zip protocol handler's start page URL must be able to enumerate everything at the root of the escaped paths of all of the .zip files. Those .zip files are not necessarily in the FILE: namespace and could be a MAPI type URL that points to a .zip file as an attachment, for example.

**To register a root as a start page:**

1.  Register a root such as .zip:/// as a start page so that all .zip files start there, in effect. When processing the root .zip: URL, your protocol handler should generate the list of child URLs to emit by querying Windows Search for all of the URLs with System.FileExtension = ".zip".
2.  Escape those URLs to remove the slashes and return them as child URLs. An example query to retrieve the types you want might look as follows.

    ``` syntax
    SELECT system.itemurl, System.DateModified FROM SystemIndex 
    WHERE System.FileExtension='.zip' OR System.MimeType='mimetypefor.zip'
    ```

3.  When Windows Search periodically does an incremental crawl on your .zip:/// root URL, you must reflect back the list of URLs that Windows Search is already maintaining that are .zip URLs. If a deletion is discovered in the native store where the .zip file is stored, it does not appear in your enumeration, and that branch of the tree in the .zip is removed.
4.  To bind to the .zip data for another protocol handler, you should ideally go through the [IShellFolder](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ishellfolder) for that URL to bind to the storage of the object, and not assume it is always a file. Doing so affords you the flexibility to work with attachments in mail stores, for example.
5.  When emitting child URLs for each .zip file, you should use PKEY\_Search\_UrlToIndexWithModificationTime ([System.Search.UrlToIndexWithModificationTime](../properties/props-system-search-urltoindexwithmodificationtime.md)) to pass PKEY\_DateModified ([System.DateModified](../properties/props-system-datemodified.md)) of the actual .zip file so that the indexer crawls the .zip file only if it has changed.

To have your .zip URLs indexed immediately after they are created or modified, and not have to wait for an incremental crawl to discover their new state, you could conceivably monitor the file system yourself for .zip file changes. However, such an approach would not work for other data stores such as MAPI.

**To have your .zip urls indexed when they are created or modified:**

1.  Create a filter (and implementation of the [**IFilter**](/windows/win32/api/filter/nn-filter-ifilter) interface) for the .zip file type. For more information, see [Developing Property Handlers for Windows Search](-search-3x-wds-extidx-propertyhandlers.md).
2.  Whenever your [**IFilter**](/windows/win32/api/filter/nn-filter-ifilter) implementation is called, it is because that URL has been discovered or changed. Then, generate an event for the .zip URL appropriate for the source URL, through the [**IGatherNotifyInline**](/previous-versions/windows/desktop/legacy/bb231470(v=vs.85)) interface. Doing so gives you the ability to immediately tell the indexer that there is new data to be indexed without having to wait for the incremental crawl.

## Related topics

<dl> <dt>

[Developing Protocol Handlers](-search-3x-wds-phaddins.md)
</dt> <dt>

[Installing and Registering Protocol Handlers](-search-3x-wds-ph-install-registration.md)
</dt> <dt>

[Notifying the Index of Changes](-search-3x-wds-notifyingofchanges.md)
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

 

 
