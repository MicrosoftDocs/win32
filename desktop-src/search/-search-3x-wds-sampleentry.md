---
description: This topic describes technologies that are related to Windows Search.
ms.assetid: 76b39ea6-2aaf-40e0-aa56-2165e188244d
title: Related Search Technologies
ms.topic: article
ms.date: 05/31/2018
---

# Related Search Technologies

This topic describes technologies that are related to [Windows Search](-search-3x-wds-overview.md).

This topic is organized as follows:

-   [Enterprise Search](#enterprise-search)
    -   [SharePoint Enterprise Search](#sharepoint-enterprise-search)
-   [Windows Desktop Search 2.x](#windows-desktop-search-2x)
-   [Platform SDK: Indexing Service](#platform-sdk-indexing-service)
-   [Related topics](#related-topics)

## Enterprise Search

For an overview of technical resources for [Enterprise Search from Microsoft](https://www.microsoft.com/enterprisesearch/en/us/default.aspx), see:

-   [Enterprise Search Resource Center](https://developer.microsoft.com/office/docs)
-   [Microsoft Enterprise Search Blog](https://blogs.msdn.com/b/enterprisesearch/rss.aspx)

### SharePoint Enterprise Search

SharePoint Foundation 2010 provides [querying from server-side code](/previous-versions/office/developer/sharepoint-2010/ee536691(v=office.14)) and [querying from client-side code](/previous-versions/office/developer/sharepoint-2010/ee539764(v=office.14)). For more information on querying, searching for new content, and improving relevance with Sharepoint Server 2010 Enterprise Search, see [Enterprise Search Fundamentals](/previous-versions/office/ee554857(v=office.14)).

Windows 7 Search supports search federation to remote data stores by using OpenSearch technologies, which enable users to access and interact with their remote data from within Windows Explorer. SharePoint Search Server 2008 and MOSS 2007 SP2 also support federated search of remote servers using OpenSearch. For information about Search Server 2008 deployment with Office SharePoint Server 2007, see [Federated Search \[Search Server 2008\]](/previous-versions/office/bb931109(v=office.14)). For information on MOSS Faceted Search, in which search results are refinded by category, see [Codeplex](https://www.codeplex.com/FacetedSearch).

Windows Search protocol handlers use design specifications similar to SharePoint Server, and they can often be used interchangeably. Hence, when users need to search legacy databases, email stores or other data structures that are not supported by Windows Search, you should first determine whether a protocol handler already exists for that data store, perhaps for use with another application such as SharePoint Server. If so, you can install that protocol handler on the system.

## Windows Desktop Search 2.x

The use of and development for the 2.x versions of Microsoft Windows Desktop Search (WDS) is strongly discouraged. Instead of using [Windows Desktop Search 2.x](../lwef/-search-2x-wds-overview.md), use [Windows Search](-search-3x-wds-overview.md) and [Windows Search API](-search-reference-entry-page.md).

## Platform SDK: Indexing Service

[Platform SDK: Indexing Service](/previous-versions/windows/desktop/indexsrv/indexsrv-portal) is obsolete as of Windows XP. Instead, use [Windows Search](-search-3x-wds-overview.md) and [Windows Search API](-search-reference-entry-page.md).

## Related topics

<dl> <dt>

[Windows Search Overview](-search-3x-wds-overview.md)
</dt> <dt>

[Windows Search Developer's Guide](-search-developers-guide-entry-page.md)
</dt> <dt>

[Windows Search Reference](-search-reference-entry-page.md)
</dt> <dt>

[Windows Search Code Samples](-search-samples-ovw.md)
</dt> <dt>

[Federated Search in Windows](-search-federated-search-overview.md)
</dt> <dt>

[Windows Search Glossary](search-glossary.md)
</dt> </dl>

 

 
