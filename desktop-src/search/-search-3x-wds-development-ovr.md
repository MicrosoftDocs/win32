---
description: To index the contents and properties of new file formats and data stores, Microsoft Windows Search must be extended with add-ins.
ms.assetid: 04ddcd97-c358-44d2-9092-a035436c50c9
title: Windows Search as a Development Platform
ms.topic: article
ms.date: 05/31/2018
---

# Windows Search as a Development Platform

To index the contents and properties of new file formats and data stores, Microsoft Windows Search must be extended with add-ins.

Before a third-party developer of new file formats and data stores can get those formats and stores to appear in query results in Windows Explorer, the developer must do the following three things:

-   Implement a Shell data source to extend the Shell namespace.
-   Expose items in a data store (if they are adding a new data store, because it would need to be indexed).
-   Develop a protocol handler so that Windows Search can access the data for indexing.

This topic is organized as follows:

-   [Getting Started](#getting-started)
-   [Overview of Search Development Scenarios](#overview-of-search-development-scenarios)
    -   [Adding a New Data Store](#adding-a-new-data-store)
    -   [Adding a New File Format](#adding-a-new-file-format)
    -   [Consuming Windows Search Results](#consuming-windows-search-results)
-   [Overview of Handlers](#overview-of-handlers)
-   [Add-in Installer Guidelines](#add-in-installer-guidelines)
-   [Note to Implementers](#note-to-implementers)
-   [Additional Resources](#additional-resources)
-   [Related topics](#related-topics)

## Getting Started

Before you start creating a Windows Search application, remember that the preferred way to do it is through a Shell data source. A Shell data source extends the Shell namespace and exposes the items in a data store. The items in the data store can then be indexed by the Windows Search system by using a protocol handler. This indirect approach for accessing Windows Search by implementing a Shell data source is preferred because it provides access to full Shell functionality. Doing it this way ensures a reasonable user experience.

If you want the query results to appear in Windows Explorer, you must implement a Shell data source before you can create a protocol handler to extend the index. However, if all queries will be programmatic (through OLE DB for example) and interpreted by the application's code rather than the Shell, a Shell namespace is still preferred but not required.

A protocol handler is required for Windows to obtain knowledge of file contents, such as items in databases or custom file types. While Windows Search can index the name and properties of the file, Windows has no knowledge of the content of the file. As a result, such items cannot be indexed or exposed in the Windows Shell. By implementing a custom protocol handler, you can expose these items. For a list of handlers identified by the developer scenario you are trying to achieve, see [Overview of Handlers](#overview-of-handlers).

## Overview of Search Development Scenarios

The most common development scenarios in Windows Search are:

-   [Adding a new data store](#adding-a-new-data-store)
-   [Adding a new file format](#adding-a-new-file-format)
-   [Consuming Windows Search results](#consuming-windows-search-results)

### Adding a New Data Store

You need a Shell data store for Windows Search only if you are adding a new data store to be indexed. A data store is a repository of data that can be exposed to the Shell programming model as a container by using a Shell data source. The items in a data store can then be indexed by the Windows Search system using a protocol handler. The protocol handler implements the protocol for accessing a content source in its native format. The [**ISearchProtocol**](/windows/win32/api/Searchapi/nn-searchapi-isearchprotocol) and [**ISearchProtocol2**](/windows/win32/api/Searchapi/nn-searchapi-isearchprotocol2) interfaces are used to implement a custom protocol handler to expand the data sources that can be indexed. For information about creating a Shell data source, see [Implementing the Basic Folder Object Interfaces](/previous-versions/windows/desktop/legacy/cc144093(v=vs.85)).

### Adding a New File Format

If you add a new custom file format, you need to develop either a filter handler or a property handler, but not both. A filter is an implementation of the [**IFilter**](/windows/win32/api/filter/nn-filter-ifilter) interface. It opens files of a particular file type, and filters properties and chunks of text for the indexer. Filters are associated with file types, as denoted by file name extensions, MIME types, or class identifiers (CLSIDs). Although one filter can handle multiple file types, each file type works with only one filter.

A property handler translates data stored in a file into a structured schema that is recognized by and can be accessed by Windows Explorer, Windows Search, and other applications. These systems can then interact with the property handler to write and read properties to and from a file. The translated data includes details view, infotips, details pane, property pages, and so forth. Each property handler is associated with a particular file type, identified by the file name extension. You need a property handler to do the following:

-   Show non-indexed item properties in the UI.
-   Support writing properties.

### Consuming Windows Search Results

The following sections describe several ways of consuming Windows Search results:

-   [Querying data](#querying-data)
-   [Querying remote data stores (Federated Search)](#querying-remote-data-stores-federated-search)
-   [Indexing files and items](#indexing-files-and-items)
-   [Indexing a data store](#indexing-a-data-store)
-   [Managing the indexing process](#managing-the-indexing-process)
-   [Integrating the Windows Property System with Windows Search applications](#integrating-the-windows-property-system-with-windows-search-applications)

### Querying Data

Developers writing applications on top of the combined Windows Search and Windows property system can access files and items regardless of application or file type. There are two ways for applications to access the indexer data:

-   Applications communicate directly with OLE DB by sending Windows Search Structured Query Language (SQL) queries to the Windows Search OLE DB provider to retrieve results. Queries can be constructed manually or by using the [**ISearchQueryHelper**](/windows/win32/api/Searchapi/nn-searchapi-isearchqueryhelper) interface to generate the SQL from search keywords, and Advanced Query Syntax (AQS).
-   Applications work through the Shell layer. The advantage of the Shell layer is that it also supports other sources like grep. However, the disadvantage is that not all indexer features are available.

Another option is using the search-ms:// and search:// protocols, which execute URL-based searches rendered through Windows Explorer. This option enables the lightest-weight development but does not return results or user selections from the results view to the calling application. Also, like other protocols, third-party search applications can take over the search-ms:// and search:// protocols if the applications conform to the required feature set. For more information on querying, see [Querying Process in Windows Search](querying-process--windows-search-.md) and [Querying the Index Programmatically](-search-3x-wds-qryidx-overview.md).

### Querying Remote Data Stores (Federated Search)

In Windows 7 and later, federated search offers a new search provider that queries remote data stores through web servers, through the [OpenSearch](https://github.com/dewitt/opensearch) protocol, and enumerates the results as RSS or Atom XML feeds. Search Connectors are namespace junctions that simulate folder behavior by using a search provider. For more information about search federation to remote data stores in Windows 7, see [Federated Search in Windows](-search-federated-search-overview.md).

### Indexing Files and Items

The content that is indexed is based on the file and data types supported through add-ins included with Windows Search and the default inclusion and exclusion rules for folders in the file system. For example, the filters included in Window Search support over 200 common types of data, including Microsoft Office documents, Microsoft Outlook email (in conjunction with the MAPI protocol handler), plain-text files, HTML, and many more. For a full list of file types natively supported, see [What Is Included in the Index](-search-3x-wds-included-in-index.md).

The index can be extended with property handlers and filters to expose the content and properties of new file formats to the index and Windows Explorer. Filters are an implementation of the [**IFilter**](/windows/win32/api/filter/nn-filter-ifilter) interface. There are two kinds of filters: one that interacts with individual items such as files and one that interacts with containers such as folders. Filters are multi-purpose in that they support chunking data, text content, some properties, and multiple languages.

In contrast, property handlers have a more specific purpose: to expose the properties of specific file types that are identified by file name extensions. A property handler for a file type can enable get and set properties, and can enumerate the properties associated with that file type. Unlike filters, property handlers do not support chucking data or text content, and property handlers have no way of indicating what language a text property is in unless they support writing properties.

### Indexing a Data Store

The index can be extended with protocol handlers to provide access to proprietary data stores. For example, files and items contained in non-file-system data stores (such as databases and email stores) require a protocol handler to map from a URL to a stream. Protocol handlers can also optionally determine the correct filters to use for extracting information from a stream. Filters enumerate the data store URLs. The items are then individually indexed using the proper filter and/or property handler. For more information, see [Extending the Index](-search-3x-wds-extidx-overview.md).

### Managing the Indexing Process

Application developers can control the scope and frequency of Windows Search indexing by using various management interfaces. These interfaces include functionality to add and remove the directories that the indexer scans for changes, manually notify the index of changes to data, check the status of the indexer, and force re-indexing of some or all data. For more information, see [Managing the Index](-search-3x-wds-mngidx-overview.md).

### Integrating the Windows Property System with Windows Search Applications

The Windows Property System is an extensible read/write system of data definitions that provides a uniform way of expressing metadata about Shell items. The Windows Property system in Windows Vista and later enables you to store and retrieve metadata for Shell items. A Shell item is any single piece of content, such as a file, folder, email or contact. A property is an individual piece of metadata associated with a Shell item. Property values are expressed as a [**PROPVARIANT**](/windows/win32/api/propidlbase/ns-propidlbase-propvariant) structure.

An extensive list of common properties is included for a number of common item types such as photos, music, documents, messages, contacts, and files. Developers can also introduce their own properties to the platform if no existing property meets their needs. For more information on integrating applications with the Windows property system, see [Developing Property Handlers](-search-3x-wds-extidx-propertyhandlers.md).

## Overview of Handlers

A handler is a Component Object Model (COM) object that provides functionality for a Shell item. Most Shell data sources offer an extensible system for binding handlers to items. For example, the file system folder uses the association system to look up the handlers for a particular file type. A specific handler is required for every file type. One filter handler is required for the Adobe Acrobat .pdf file type, for example, another filter handler is required for the .doc file format, and so forth.

Different handlers have some commonality. In Windows Vista and later, all handlers must use one of the following interfaces to initialize the handler: [**IInitializeWithStream**](/windows/win32/api/propsys/nn-propsys-iinitializewithstream), [**IInitializeWithItem**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-iinitializewithitem), or [**IItinitializeWithFile**](/windows/win32/api/propsys/nn-propsys-iinitializewithfile).

The following table lists high-level developer tasks, the type of handler needed for each task, and provides a link to conceptual information about how to perform each task.



| Task                                                                                                                                                            | Handler                          | Conceptual information                                                                                                                                                                                 |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Accessing the properties of a file for indexing                                                                                                                 | Property handler                 | [Developing Property Handlers](-search-3x-wds-extidx-propertyhandlers.md)<br/> [System-Defined Properties for Custom File Formats](-shell-systemdefinedpropertiesforfileformats.md)<br/> |
| Adding clipboard formats for the data object ([**IDataObject**](/windows/win32/api/objidl/nn-objidl-idataobject)) of an item (Data objects are used in drag-and-drop and copy/paste scenarios.) | Data object handler              | [Creating Data Handlers](/previous-versions/windows/desktop/legacy/cc144163(v=vs.85))                                                                                                                                                          |
| Adding verbs for an item that are commonly displayed in a shortcut menu                                                                                         | Shortcut menu handler            | [Creating Context Menu Handlers](../shell/context-menu-handlers.md)<br/> [Customizing a Shortcut Menu Using Dynamic Verbs](../shell/shortcut-menu-using-dynamic-verbs.md)<br/>                         |
| Associating a file type with a specific icon                                                                                                                    | Icon handler                     | [Creating Icon Handlers](../shell/how-to-create-icon-handlers.md)                                                                                                                                                          |
| Creating property sheets with UI pictures and controls that permit custom interaction with a file type                                                          | Property sheet handler           | [Property Sheet Handlers](/previous-versions/windows/desktop/legacy/cc144106(v=vs.85))                                                                                                                                                    |
| Enabling an item type to support drag-and-drop and copy/paste scenarios                                                                                         | Drop handler                     | [Transferring Shell Objects with Drag-and-Drop and the Clipboard](/previous-versions/windows/desktop/legacy/bb776905(v=vs.85))                                                                                                                      |
| Extracting chunks of text and document properties for indexing                                                                                                  | Filter handler                   | [Developing Filter Handlers](-search-ifilter-conceptual.md)                                                                                                                                           |
| Indexing a new file type                                                                                                                                        | Filter handler, property handler | [Developing Filter Handlers](-search-ifilter-conceptual.md)<br/> [Developing Property Handlers](-search-3x-wds-extidx-propertyhandlers.md)<br/>                                          |
| Indexing the contents of a data store                                                                                                                           | Protocol handler                 | [Developing Protocol Handlers](-search-3x-wds-phaddins.md)                                                                                                                                            |
| Previewing a simplified view of the Shell item in the Windows Explorer preview pane                                                                             | Preview handler                  | [Preview Handlers](../shell/preview-handlers.md)                                                                                                                                                             |
| Supplying pop-up text when a mouse hovers over a UI object                                                                                                      | Infotip handler                  | [Creating Shell Extension Handlers](../shell/handlers.md) (Infotip Customization)                                                                                                                            |
| Supplying a static image to represent a Shell item                                                                                                              | Thumbnail handler                | [Thumbnail Handlers](/previous-versions/windows/desktop/legacy/cc144118(v=vs.85))                                                                                                                                                        |



 

The following table lists handlers and the interfaces for implementing each type of handler.



| Handler                | Interfaces                                                                                                                                                                                                                                                                                                                                                                |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Drop handler           | [**IDropTarget**](/windows/win32/api/oleidl/nn-oleidl-idroptarget), [**IDropTargetHelper**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-idroptargethelper), [**IPersistFile**](/windows/win32/api/objidl/nn-objidl-ipersistfile), [**IShellExtInit**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ishellextinit)                                                                                                                                                                                                      |
| Data object handler    | [**IDataObject**](/windows/win32/api/objidl/nn-objidl-idataobject), [**IPersistFile**](/windows/win32/api/objidl/nn-objidl-ipersistfile)                                                                                                                                                                                                                                                                                                  |
| Filter handler         | [**IFilter**](/windows/win32/api/filter/nn-filter-ifilter)<br/>                                                                                                                                                                                                                                                                                                                             |
| Icon handler           | [**IExtractIcon**](/windows/win32/api/shlobj_core/nn-shlobj_core-iextracticona)<br/> Optional: [**IPersist**](/windows/win32/api/objidl/nn-objidl-ipersist), [**IPersistFile**](/windows/win32/api/objidl/nn-objidl-ipersistfile)<br/>                                                                                                                                                                                                                                 |
| Infotip handler        | [**IQueryInfo**](/windows/win32/api/shlobj_core/nn-shlobj_core-iqueryinfo)                                                                                                                                                                                                                                                                                                                                        |
| Preview handler        | [**IPreviewHandler**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ipreviewhandler)                                                                                                                                                                                                                                                                                                                              |
| Property handler       | [**IPropertyStore**](/windows/win32/api/propsys/nn-propsys-ipropertystore)                                                                                                                                                                                                                                                                                                                           |
| Protocol handler       | [**IFilter**](/windows/win32/api/filter/nn-filter-ifilter), [**ISearchProtocol**](/windows/win32/api/Searchapi/nn-searchapi-isearchprotocol), [**IUrlAccessor**](/windows/win32/api/Searchapi/nn-searchapi-iurlaccessor)<br/> Optional: [**ISearchProtocol2**](/windows/win32/api/Searchapi/nn-searchapi-isearchprotocol2), [**IUrlAccessor2**](/windows/win32/api/Searchapi/nn-searchapi-iurlaccessor2), [**IUrlAccessor3**](/windows/win32/api/Searchapi/nn-searchapi-iurlaccessor3), [**IUrlAccessor4**](/windows/win32/api/Searchapi/nn-searchapi-iurlaccessor4)<br/> |
| Property sheet handler | [**IShellExtInit**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ishellextinit), [**IShellPropSheetExt**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ishellpropsheetext)                                                                                                                                                                                                                                                                              |
| Shortcut menu handler  | [**IContextMenu**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-icontextmenu), [**IExplorerCommand**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-iexplorercommand), [**IShellExtInit**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ishellextinit)                                                                                                                                                                                                                                          |
| Thumbnail handler      | [**IThumbnailProvider**](/windows/win32/api/thumbcache/nn-thumbcache-ithumbnailprovider)                                                                                                                                                                                                                                                                                                                        |



 

> [!Note]  
> A property handler is sometimes kown as a metadata handler. A Shell data source is sometimes known as a Shell namespace extension. A file type handler is sometimes known as a Shell extension handler or a Shell extension.

 

For more information about creating handlers, see [Creating Shell Extension Handlers](../shell/handlers.md). For more information about properties, see [Windows Property System](../properties/windows-properties-system.md).

## Add-in Installer Guidelines

Use the following guidelines when creating an Add-in installer:

-   The installer must use either the EXE or MSI installer.
-   Release notes must be provided.
-   An **Add/Remove Programs** entry must be created for each add-in installed.
-   The installer must take over all registry settings for the particular file type or store that the current add-in understands.
-   If a previous add-in is being overwritten, the installer should notify the user.
-   If a newer add-in has overwritten a previous add-in, the user should be able to restore the previous add-in's functionality and make it the default add-in again for that file type or store.

## Note to Implementers

Before creating a filter or property handler, developers should consider the following:

-   These handlers are in-process extensions that are loaded into processes that you do not control, such as the filter daemon process, Windows Explorer (grep search), and third-party hosts like Windows Mail).
-   You must write secure code that is robust enough to handle arbitrarily corrupt forms of your file format that were created to attack the system.
-   Your add-in must not leak resources that will produce problems for the host processes.
-   Your add-in must not crash as this will also crash the host processes and slow down the filtering process.
-   Because these handlers are run in a background system process, they must perform quickly with a minimum of CPU and I/O consumed in order to meet the performance requirements of the system.

Thus, these add-ins should be written by developers with expertise in creating system-level code.

## Additional Resources

-   For information about creating a Shell data source, see [Implementing the Basic Folder Object Interfaces](/previous-versions/windows/desktop/legacy/cc144093(v=vs.85)).
-   For data sources that need to use the Shell Default System Folder View Object (DefView), see [Implementing a Folder View](../lwef/nse-folderview.md), [**SHCreateShellFolderView**](/windows/win32/api/shlobj_core/nf-shlobj_core-shcreateshellfolderview) function, and [**SFV\_CREATE**](/windows/win32/api/shlobj_core/ns-shlobj_core-sfv_create) structure. Data sources that use the Shell Default System Folder View Object (DefView) must implement the following set of interfaces: [**IShellFolder**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ishellfolder), [**IShellFolder2**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ishellfolder2), [**IPersistFolder**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ipersistfolder), [**IPersistFolder2**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ipersistfolder2), and (optionally) [**IPersistFolder3**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ipersistfolder3). If your **IShellFolder** implementation does not use **SHCreateShellFolderView** to create the DefView, the Shell view object may need [**IFolderView**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ifolderview).
-   [**ISearchFolderItemFactory**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-isearchfolderitemfactory) is the primary interface for consumers of the Shell data source known as DBFolder. For more information about DBFolder, see the description of the STR\_PARSE\_WITH\_PROPERTIES constant in [**Bind Context String Keys**](../shell/str-constants.md). See also [Association Arrays](/previous-versions/windows/desktop/legacy/ee872122(v=vs.85)) and [**IPropertySystem::GetPropertyDescriptionListFromString**](/windows/win32/api/propsys/nf-propsys-ipropertysystem-getpropertydescriptionlistfromstring).
-   For information on OLE DB, see [OLE DB Programming Overview](https://msdn.microsoft.com/library/5d8sd9we(VS.71).aspx). For information on the .NET Framework Data Provider for OLE DB, see the [System.Data.OleDb Namespace](/dotnet/api/system.data.oledb?view=dotnet-plat-ext-3.1) documentation.
-   For community-supported message boards on Search technologies, see [Windows: Search Forums](https://social.msdn.microsoft.com/Forums/windowsdesktopsearchdevelopment/threads) on MSDN.
-   For related code samples, see [Windows Search Code Samples](-search-samples-ovw.md).

## Related topics

<dl> <dt>

[Windows Search Overview](-search-3x-wds-overview.md)
</dt> <dt>

[Languages Supported by Windows Search](-search-3x-wds-language-support.md)
</dt> <dt>

[Using Managed Code with Shell Data and Windows Search](-search-3x-wds-managed-code.md)
</dt> <dt>

[Windows Search Developer's Guide](-search-developers-guide-entry-page.md)
</dt> </dl>

 

 
