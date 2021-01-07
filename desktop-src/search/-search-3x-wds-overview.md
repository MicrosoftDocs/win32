---
description: Windows Search is a desktop search platform that has instant search capabilities for most common file types and data types, and third-party developers can extend these capabilities to new file types and data types.
ms.assetid: 6da601c6-3742-40ad-99f2-8817f7f642b3
title: Windows Search Overview
ms.topic: article
ms.date: 05/31/2018
---

# Windows Search Overview

Windows Search is a desktop search platform that has instant search capabilities for most common file types and data types, and third-party developers can extend these capabilities to new file types and data types.

This topic is organized as follows:

-   [Introduction](#introduction)
    -   [Windows Search Service](#windows-search-service)
    -   [Development Platform](#development-platform)
    -   [User Interface](#user-interface)
-   [Technical Prerequisites](#technical-prerequisites)
    -   [SDK Download and Contents](#sdk-download-and-contents)
-   [Windows Search SDK Documentation](#windows-search-sdk-documentation)
-   [History of Windows Search](#history-of-windows-search)
-   [Additional Resources](#additional-resources)
-   [Related topics](#related-topics)

## Introduction

Windows Search is a standard component of Windows 7 and Windows Vista, and is enabled by default. Windows Search replaces Windows Desktop Search (WDS), which was available as an add-in for Windows XP and Windows Server 2003.

Windows Search is composed of three components:

-   [Windows Search Service](#windows-search-service) (WSS)
-   [Development platform](#development-platform)
-   [User interface](#user-interface)

### Windows Search Service

The WSS organizes the extracted features of a collection of documents. The Windows Search Protocol enables a client to communicate with a server that is hosting a WSS, both to issue queries and to enable an administrator to manage the indexing server. When processing files, WSS analyzes a set of documents, extracts useful information, and then organizes the extracted information so that properties of those documents can be efficiently returned in response to queries.

A collection of documents that can be queried comprises a catalog, which is the highest-level unit of organization in Windows Search. A catalog represents a set of indexed documents that can be queried. A catalog consists of a properties table with the text or value and corresponding location (locale) stored in columns of the table. Each row of the table corresponds to a separate document in the scope of the catalog, and each column of the table corresponds to a property. A catalog may contain an inverted index (for quick word matching) and a property cache (for quick retrieval of property values).

The indexer process is implemented as a Windows service running in the LocalSystem account and is always running for all users (even if no user is logged in), which permits Windows Search to accomplish the following:

-   Maintain one index that is shared among all users.
-   Maintain security restrictions on content access.
-   Process remote queries from client computers on the network.

The Search service is designed to protect the user experience and system performance when indexing. The following conditions cause the service to throttle back or pause indexing:

-   High CPU usage by non-search-related processes.
-   High system I/O rate including file reads and writes, page file and file cache I/O, and mapped file I/O.
-   Low memory availability.
-   Low battery life.
-   Low disk space on the drive that stores the index.

### Development Platform

The preferred way to access the Search APIs and create Windows Search applications is through a Shell data source. A Shell data source is a component that is used to extend the Shell namespace and expose items in a data store. A data store is a repository of data. A data store can be exposed to the Shell programming model as a container that uses a Shell data source. The items in a data store can be indexed by the Windows Search system using a protocol handler.

For example, [ISearchFolderItemFactory](/windows/win32/api/shobjidl_core/nn-shobjidl_core-isearchfolderitemfactory) is a component that can create instances of the search folder data source, which is a sort of "virtual" data source provided by the Shell that can execute queries over other data sources in the Shell namespace and enumerate results. It can do so either by using the indexer or by manually enumerating and inspecting items in the specified scopes. This interface permits you to set up the parameters of the search by using methods that create and modify search folders. If methods of this interface are not called, default values are used instead.

Accessing the Windows Search capability indirectly through the Shell data model is preferred because it provides access to full Shell functionality at the level of the Shell data model. For example, you can set the scope of a search to a library (which is a feature available in Windows 7 and later) to use the library folders as the scope of the query. Windows Search then aggregates the search results from those locations if they are in different indexes (if the folders are on different computers). The Shell data layer also creates a more complete view of items' properties, synthesizing some property values. It also provides access to search features for data stores that are not indexed by Windows Search. For example, you can search a Universal Serial Bus (USB) storage devices, portable device that uses the MTP protocol, or an File Transfer Protocol (FTP) server through the Shell data sources that provides access to those storage systems. Doing so ensures a better user experience.

Windows Search has a cache of property values that is used in the implementation of the Windows Search Service (WSS). These property values can be programmatically queried by using the Windows Search OLE DB provider, or through [ISearchFolderItemFactory](/windows/win32/api/shobjidl_core/nn-shobjidl_core-isearchfolderitemfactory), which represents items in search results and query-based views. Windows Search then collects and stores properties emitted by filter handlers or property handlers when an item such as a Word document is indexed. This store is discarded and rebuilt when the index is rebuilt.

Third-party developers can create applications that consume the data in the index through programmatic queries, and can extend the data in the index for custom file and item types to be indexed by Windows Search. If you want to show query results in Windows Explorer, you must implement a Shell data source before you can create a protocol handler to extend the index. However, if all queries are programmatic (through OLE DB for example) and interpreted by the application's code rather than the Shell, a Shell namespace is still preferred but not required.

A protocol handler is required for Windows to obtain information about file contents, such as items in databases or custom file types. While Windows Search can index the name and properties of the file, Windows has no information about the content of the file. As a result, such items cannot be indexed or exposed in the Windows Shell. By implementing a custom protocol handler, you can expose these items. For a list of handlers identified by the developer scenario you are trying to achieve, see "Overview of Handlers" in [Windows Search as a Development Platform](-search-3x-wds-development-ovr.md).

> [!Note]  
> A Shell data source is sometimes known as a Shell namespace extension. A handler is sometimes known as a Shell extension or a Shell extension handler.

 

### User Interface

In Windows Vista and later, Windows Search is integrated into all Windows Explorer windows for instant access to search. This enables users to quickly search for files and items by file name, properties, and full-text contents. Results can also be filtered further to refine the search. Here are some more features of Windows Search:

-   An instant search box in every window enables instant filtering of all items currently in view. Instant search boxes appear in the Start menu to search for programs or files, and in the upper-right corner of all Windows Explorer windows to filter the results shown. Instant search is also integrated into some other Windows features, such as Windows Media Player, to find related files.
-   Documents can be tagged with keywords to group them by custom criteria that are defined by the user. Tags are metadata items that are assigned by the user or applications to make it easier to find files based on keywords that may not be in the item name or contents. For example, a set of pictures might be tagged as "Arizona Vacation 2009" to quickly retrieve later by searching for any of the included words.
-   Enhanced column headers in Windows Explorer views enable sorting and grouping documents in different ways. For example, files can be sorted according to name, date modified, type, size, and tags. Documents can also be grouped according to any of these properties and each group can be filtered (hidden or displayed) as desired.
-   Documents can be stacked according to name, date modified, type, size, and tags. Stacks include all documents that have the specified property and are located within any subfolder of the selected folder.
-   Searches can be saved (to be retrieved later) by clicking the **Save Search** button in the search pane in Windows Explorer. The results will be dynamically repopulated based on the original criteria when the saved search is opened. For instructions, see [Save Your Search Results](https://windows.microsoft.com/windows-vista/Save-your-search-results).
-   Preview handlers and thumbnail handlers enable users to preview documents in Windows Explorer without having to open the application that created them.

## Technical Prerequisites

Before you start reading the Windows Search SDK documentation, you should have a fundamental understanding of the following concepts:

-   How to implement a Shell data source.
-   How to implement a handler.
-   How to work in native code.

A Shell data source is a component that is used to extend the Shell namespace and expose items in a data store. In the past, the Shell data source was referred to as the Shell namespace extension. A handler is a Component Object Model (COM) object that provides functionality for a Shell item. For a list of handlers identified by the developer scenario you are trying to achieve, see "Overview of Handlers" in [Windows Search as a Development Platform](-search-3x-wds-development-ovr.md).

For more information about the Windows Search SDK interoperability assembly for working with COM objects that are exposed by Windows Search and other programs that use managed code, see [Using Managed Code with Shell Data and Windows Search](-search-3x-wds-managed-code.md). However, note that filters, property handlers, and protocol handlers must be written in native code. This is due to potential common language runtime (CLR) versioning issues with the process that multiple add-ins run in. Developers who are new to C++ can get started with the [Visual C++ Developer Center](https://msdn.microsoft.com/vstudio//default.aspx) and [Windows Development Getting Started](../desktop-programming.md).

### SDK Download and Contents

In addition to meeting the listed technical prerequirements, you must also download the [Windows SDK](https://msdn.microsoft.com/windowsvista/bb980924.aspx) to get the Windows Search libraries. The [Windows Search SDK Samples](https://www.microsoft.com/downloads/details.aspx?FamilyID=645300AE-5E7A-4CE7-95F0-49793F8F76E8) contain useful code samples and an interoperability assembly for developing with managed code. For more information on using the code samples, see [Windows Search Code Samples](-search-3x-wds-sampleentry.md).

## Windows Search SDK Documentation

The contents of the Windows Search SDK documentation are as follows:

-   [Windows Search as a Development Platform](-search-3x-wds-development-ovr.md)

    Outlines the main development scenarios in Windows Search. Provides a list of handlers identified by the development scenario you are trying to achieve, add-in installer guidelines, and implementation notes.

-   [Windows Search Developer's Guide](-search-developers-guide-entry-page.md)

    Provides explanations for [Managing the Index](-search-3x-wds-mngidx-overview.md), [Querying the Index Programmatically](-search-3x-wds-qryidx-overview.md), [Extending the Index](-search-3x-wds-extidx-overview.md), and [Extending Language Resources](extending-language-resources-in-windows-search.md).

-   [Windows Search Reference](-search-reference-entry-page.md)

    Documents the following categories of Windows Search interfaces: [Protocol Handlers](-search-protocol-handlers-interfaces-entry-page.md), [Querying](-search-querying-interfaces-entry-page.md), [Crawl Scope](-search-crawl-scope-interfaces-entry-page.md), [Data Add-ins](-search-data-addins-interfaces-entry-page.md), [Index Management](-search-index-mgt-interfaces-entry-page.md), and [Notifications](-search-notifications-interfaces-entry-page.md). The reference documentation also includes [Constants and Enumerations](-search-constants-and-enumerations-entry-page.md), [Structures](-search-structures-entry-page.md), [Property Mappings](-search-3x-wds-propertymappings.md), and the [Saved Search File Format](-search-savedsearchfileformat.md).

-   [Windows Search Code Samples](-search-samples-ovw.md)

    Describes the Search API code samples that are available.

-   [Federated Search in Windows](-search-federated-search-overview.md)

    Describes Windows 7 support for search federation to remote data stores using OpenSearch technologies that enable users to access and interact with their remote data from within Windows Explorer.

-   [Related Search Technologies](-search-3x-wds-sampleentry.md)

    Lists technologies related to Windows Search: Enterprise Search, SharePoint Enterprise Search, and legacy applications such as Windows Desktop Search 2.x and Platform SDK: Indexing Service.

-   [Windows Search Glossary](search-glossary.md)

    Defines essential terms used in Windows Search and Shell technologies.

## History of Windows Search

Windows Search replaces Windows Desktop Search (WDS), which was available as an add-in for Windows XP and Windows Server 2003. WDS replaced the legacy Indexing Service from previous versions of Windows with enhancements to performance, usability, and extensibility. The new development platform supports requirements that produce a more secure and stable system. While the new querying platform is not compatible with Microsoft Windows Desktop Search (WDS) 2.x, filters and protocol handlers written for previous versions of WDS can be updated to work with Windows Search. Windows Search also supports a new property system. For information on filters, property handlers, and protocol handlers, see [Extending the Index](-search-3x-wds-extidx-overview.md).

Windows Search is built into Windows Vista and later, and is available as a redistributable update to WDS 2.x, to support the following operating systems:

-   32-bit versions of Windows XP with Service Pack 2 (SP2).
-   All x64-based versions of Windows XP.
-   Windows Server 2003 with Service Pack 1 (SP1) and later.
-   All x64-based versions of Windows Server 2003.

Systems running these operating systems must have Windows Search installed in order to run applications written for Windows Search. For more information, see [KB article 917013: Description of Windows Desktop Search 3.01 and the Multilingual User Interface Pack for Windows Desktop Search 3.01](https://support.microsoft.com/kb/917013).

## Additional Resources

-   For information about creating a Shell data source, see [Implementing the Basic Folder Object Interfaces](/previous-versions//bb776815(v=vs.85)).
-   For more information about [ISearchFolderItemFactory](/windows/win32/api/shobjidl_core/nn-shobjidl_core-isearchfolderitemfactory) and the DB folder data source, see the description of the STR\_PARSE\_WITH\_PROPERTIES constant in [Bind Context String Keys](../shell/str-constants.md). See also [Association Arrays](/previous-versions/windows/desktop/legacy/ee872122(v=vs.85)) and [IPropertySystem::GetPropertyDescriptionListFromString](/windows/win32/api/propsys/nf-propsys-ipropertysystem-getpropertydescriptionlistfromstring).
-   For information on OLE DB, see [OLE DB Programming Overview](/cpp/data/oledb/ole-db-programming-overview?view=vs-2019). For information on the .NET Framework Data Provider for OLE DB, see the [System.Data.OleDb Namespace](/dotnet/api/system.data.oledb?view=dotnet-plat-ext-3.1&preserve-view=true) documentation.
-   For an overview of file type handlers (also known as Shell extension handlers and Search handlers), see [Windows Search as a Development Platform](-search-3x-wds-development-ovr.md).
-   For community-supported message boards about Search technologies, see [MSDN Forum: Windows Desktop Search Development](https://social.msdn.microsoft.com/Forums/windowsdesktopsearchdevelopment/threads).
-   For related code samples, see [Windows Search Code Samples](-search-samples-ovw.md).

## Related topics

<dl> <dt>

[Windows Search as a Development Platform](-search-3x-wds-development-ovr.md)
</dt> <dt>

[Languages Supported by Windows Search](-search-3x-wds-language-support.md)
</dt> <dt>

[Using Managed Code with Shell Data and Windows Search](-search-3x-wds-managed-code.md)
</dt> </dl>

 

 
