---
title: Windows Desktop Search 2.x
description: Understand Windows Desktop Search 2.x. For Windows releases later than Windows XP and Windows Server 2003, use Windows Search instead.
ms.assetid: 3d73f850-58b8-4a41-8863-e2914661d4b9
ms.topic: article
ms.date: 05/31/2018
---

# Windows Desktop Search 2.x

> [!NOTE]
> Windows Desktop Search 2.x is an obsolete technology that was originally available as an add-in for Windows XP and Windows Server 2003. On later releases, use [Windows Search](../search/-search-3x-wds-overview.md) instead.

The use of and development for the 2.x versions of Microsoft Windows Desktop Search (WDS) is strongly discouraged in favor of [Windows Search](../search/-search-3x-wds-overview.md).

WDS is an indexing service and platform that provides fast search of files and data across different data sources and locations. WDS helps users and other applications find almost anything on their computers, email messages, calendar appointments, photos, documents, and more. Additionally, WDS can return results from multiple data sources all in a Windows Explorer environment so your users can quickly preview, filter, and act on search results.

WDS indexes data within a given crawl scope, the specified locations within a local computer and shared network that the Indexer should crawl. This crawl scope can be controlled by user-set options, management APIs, and Group Policies, which network administrators can configure to control user access permissions and indexing settings. Group Policies can restrict access to certain network resources as well as define resources to be indexed.

This section contains the following topics:

-   [Overview](#windows-desktop-search-2x)
    -   [About the WDS Indexer](#about-the-wds-indexer)
    -   [About the WDS Catalog](#about-the-wds-catalog)
    -   [About the Search Engine and Results](#about-the-search-engine-and-results)
-   [Developing with WDS](#developing-with-wds)
    -   [Adding Data to the Index with Add-Ins](#adding-data-to-the-index-with-add-ins)
    -   [Querying the Index](#querying-the-index)
-   [Compatibility Requirements](#compatibility-requirements)
    -   [System Requirements](#system-requirements)
-   [Related Topics](#related-topics)

## Overview

### About the WDS Indexer

When first installed, the Indexer crawls most common user-facing files in the My Documents folder, Microsoft Outlook and Microsoft Outlook Express email folders, and locations specified in Group Policy. Users can also specify new files and locations for the Indexer to include (or exclude) in successive crawls. Each included location is identified by URL, and the Indexer will start at that URL and recursively iterate through any subfolders or locations until all items have been indexed. A scope is a set of URLs. The management APIs can be used by custom applications to define their crawl scope, a set of URLs pointing to paths within a protocol such as `file://` for folders on a drive or `mapi:// ` for MAPI email stores like Outlook. WDS uses protocol handlers to access the data stores and filters to parse and index the items text and properties. This data is then stored in the catalog.

### About the WDS Catalog

The WDS catalog is an index of text and properties collected from items in specified email, local drives, network resources and other local data stores. The contents of the catalog are based on options and rules set by WDS, applications built on the WDS platform, user preferences and group policies. There are over 200 properties available for each item indexed, such as creation date, size, and type-specific properties ("From" for email messages). For a list of these properties, see the WDS [Schema Reference](-search-2x-wds-schematable.md).

### About the Search Engine and Results

From the WDS Deskbar or from Windows Explorer, users can search the full-text content and property metadata of indexed items. The same kinds of searches can also be initiated from the command-line, from a webpage, or from a custom application. The WDS Search Engine locates items matching the search criteria and returns them as Microsoft ActiveX Data Objects (ADO) result sets. WDS displays items matching the search criteria and can present a rich preview of the item. You can create applications to intercept the search query, perform the search, and/or display the result set.

## Developing with WDS

There are two primary types of integration with WDS: adding data to the index and querying the contents of the index to retrieve records matching search criteria.

### Adding Data to the Index with Add-Ins

There are basically two types of data sources: file system stores and non-file system stores. A group of files in My Documents is a simple file system store. WDS can search information in the files stored in such a file system if it can locate a filter for the file type. You can enable WDS to index a new proprietary file type if you provide an implementation of the [**IFilter**](/windows/desktop/api/filter/nn-filter-ifilter)interface for that file type.

A non-file system store, like a database, requires a protocol handler to enable WDS to navigate through and index data within the data store. For example, if you have a mail client that stores its list of received email in its own file (such as PST files in Outlook), you can provide a protocol handler to index and search each individual email by providing a protocol handler. If the data store is hierarchical, you will also need to implement an [**IFilter**](/windows/desktop/api/filter/nn-filter-ifilter)interface to enumerate the items in the store. For a better user experience, you can implement a Shell Extension to provide context menus and icons from within the results view.

Currently, WDS contains filters for over 200 types of items (including plaintext items such as HTML, XML, and source code files) and uses the same [**IFilter**](/windows/desktop/api/filter/nn-filter-ifilter)and protocol handler technology as SharePoint Services. If you already have filters installed for proprietary file types, WDS can use the existing filter interfaces to index this data.

### Querying the Index

WDS provides applications with customized result sets of data from the index based on any of the schema values available. Results are returned as ADO record sets. There are four ways to incorporate WDS queries into an application, each offering various levels of customization and robustness.

-   ISearchDesktop Interface - APIs in this interface are used to call WDS programmatically by specifying a query string, a list of columns to return, scope restrictions similar to a Structured Query Language (SQL) WHERE clause, and the name of the column to sort by. These APIs are available for native and managed code.
-   WDS ActiveX Control - This control draws the WDS search interface and manages searching and displaying results. This method is easier than using the APIs but is less flexible. To use this control in a Microsoft Visual Studio application, go to the **Choose Toolbox Items** dialog from the **Tools** menu and add "Windows Desktop Search - Results Viewer" to the **Toolbox** from the **COM Components** tab. Then add the control to the form you want to include it on. The WDS ActiveX control is compatible with WDS 2.x and 3.x on Windows XP only.
-   Command Line Parameters - Applications can call the WDS executable with various parameters to search and display results. This will open a WDS window with the results displayed. This is the easiest way to add search to an application but does not return to the calling application any information about what the user does within the WDS window.
-   WDS Browser Helper Object (BHO) - Similarly, webpages can use the BHO to send queries to WDS or the registered search application. After validating the webpages URL against the WDS domain safe list, WDS will either execute the query and display the results using the standard search interface, or pass the query on to the registered search application.

Users can use [Advanced Query Syntax](-search-2x-wds-aqsreference.md) to query the catalog more powerfully by controlling the scope of searches and combining search parameters with Boolean operators. For example, a user could search for an attachment in an email from John that includes either "project schedule" or "project plan" with a query like the following: `from:John isattachment:true "project schedule" OR "project plan"`.

## Compatibility Requirements

WDS 2.6.5 is available for Windows 2000, Windows Server 2003, and Windows XP only. WDS is a separate download available from Microsoft for free for personal and business use. It must be installed and in use for indexing the user account before applications built for WDS 2.6.5 will work.

### System Requirements

The following are required to use Windows Desktop Search:

-   Windows Internet Explorer or later.
-   To include your email messages in the catalog, you must have either Microsoft Microsoft Outlook 2000 or later, or Microsoft Outlook Express 6.0 or later.
-   Full preview of Microsoft Microsoft Office documents in the results view requires Office XP or later.
-   Minimum Pentium 500 MHz processor (1 GHz recommended).
-   Windows XP, Windows 2000 SP4 or later, or Windows Server 2003 Service Pack 1.
-   Minimum 128 MB of RAM (256 MB recommended).
-   500 MB of free hard disk space recommended. The size of your index depends on how much content you have indexed.
-   1024 x 768 screen resolution recommended.

## Related Topics

1.  Querying the Index

    -   [Calling WDS Programmatically (via ISearchDesktop)](-search-2x-wds-callingwdsprogrammatically.md)
    -   [Calling WDS from Web Pages](-search-2x-wds-browserhelpobject.md)
    -   [Calling WDS from the Command Line](-search-2x-wds-fromcommandline.md)

2.  [Extending the Index (Overview)](-search-2x-wds-extendingtheindex.md)

    -   [Developing IFilter Add-ins](-search-2x-wds-ifilteraddins.md)
    -   [Developing Protocol Handlers](-search-2x-wds-phaddins.md)

3.  General References

    -   [WDS Schema](-search-2x-wds-schematable.md)
    -   [Advanced Query Syntax](-search-2x-wds-aqsreference.md)
    -   [WDS Perceived Types](-search-2x-wds-perceivedtype.md)

 

 