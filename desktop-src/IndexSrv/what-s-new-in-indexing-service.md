---
title: About the Indexing Service
description: About the Indexing Service
ms.assetid: '4c83a189-11fb-4781-9674-581d51a6d7e3'
---

# About the Indexing Service

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

This topic contains an overview of new features by operating system.

### Windows XP

Indexing Service 3.0 includes the following new features:

-   Media property sets that enable you to query for media properties in queries that use the OLE DB Provide for Indexing Service. The media property sets include properties for audio, video, music, image, and digital rights management. For more information about media properties and property sets, see [Property Sets](property-sets.md).

### Windows 2000

Indexing Service 3.0 includes the following new features:

-   Indexing Service is now a system service that indexes the content and properties of all files defined for the "system" catalog in addition to all virtual Webs defined for the "Web" catalog.
-   When Indexing Service is started, time-intensive disk scans aren't required on NTFS file system volumes. Disk volumes converted to NTFS file system 5.0 format support the use of Update Sequence Number (USN) from the change journal. Indexing Service benefits directly from the sparse file formats and native property sets of the NTFS file system.
-   The Start/Search dialog uses Indexing Service, when available, to perform queries.
-   Programmatic read-only access is available to Indexing Service content and property indexes for resolving queries through the Microsoft OLE DB Provider for Indexing Service:
    -   Script writers can use Microsoft ActiveX Data Objects (ADO) methods and properties along with Indexing Service [**Query**](iixssoquery.md) and [**Utility**](iixssoutil.md) helper objects to create and control queries and display results. Indexing Service also supplies [**AdminIndexServer**](iadminindexserver.md), [**CatAdm**](icatadm.md), and [**ScopeAdm**](iscopeadm.md) administration helper objects to manage the indexing catalogs and performance.
    -   C and C++ programmers can use OLE DB interface methods and properties and Indexing Service OLE DB helper functions to manage the state of the catalog, create and control queries, and display results.
-   Three query languages are now available:
    -   [Indexing Service query language](indexing-service-query-language.md), Dialect 1. The original query language supported in Index Server 2.0 and earlier.
    -   [Indexing Service query language](indexing-service-query-language.md), Dialect 2. A more powerful and extensible query language that is new to Indexing Service 3.0.
    -   [SQL Query Language](sql-query-language.md). The Structured Query Language (SQL) language with extensions tailored to accept query-related terms.
-   Expanded processing is available for query results. The functionality of the [**GroupBy**](iixssoquery-groupby.md) property of the [**Query**](iixssoquery.md) object can now be applied to search results so that you can specify grouping within a column in addition to specifying the columns of the result table.
-   Catalogs for removable media, including CD-ROMs, can be created using the MMC. The catalogs can reside on the removable medium, and when that medium is inserted into a computer running Indexing Service, the catalog is opened in read-only format for queries.

 

 




