---
description: The Crawl Scope Manager (CSM) is a set of interfaces that provides methods to inform the Windows Search engine about containers to crawl and items under those containers to include or exclude in the catalog.
ms.assetid: 7d65d00a-7294-4718-b593-89394b2e416f
title: Using the Crawl Scope Manager
ms.topic: article
ms.date: 05/31/2018
---

# Using the Crawl Scope Manager

The Crawl Scope Manager (CSM) is a set of interfaces that provides methods to inform the Windows Search engine about containers to crawl and items under those containers to include or exclude in the catalog. Developers can use the CSM to define a crawl scope programmatically for a new data store or protocol handler. Administrators can use the CSM to view all users' indexes, search roots, and scope rules.

This section is organized as follows:

-   [What is the Crawl Scope Manager?](#what-is-the-crawl-scope-manager)
-   [Search Roots and Scope Rules](#search-roots-and-scope-rules)
    -   [Search Roots](#search-roots-and-scope-rules)
    -   [Scope Rules](#scope-rules)
-   [Group Policies Supported by the Crawl Scope Manager](#group-policies-supported-by-the-crawl-scope-manager)
-   [Related topics](#related-topics)

## What is the Crawl Scope Manager?

To understand the Crawl Scope Manager, you must understand the following terms:

-   A *crawl scope* is a set of URLs pointing to data stores or containers (email data stores, databases, network file shares, and so on) that the indexer crawls to index items. For a hierarchical data store, the crawl scope can include a parent URL but exclude a child URL and vice versa. Items within the crawl scope are indexed; items outside the crawl scope are ignored.
-   A *search root* is the top-level URL identifying a container or data store that is associated with a particular protocol handler. Search roots can identify locations that are specific to a user, that are on a remote computer, or that match a wildcard pattern. When you add a new data store or protocol handler, you should also add a search root to the crawl scope.
-   A *scope rule* is a rule that includes or excludes URLs within a search root from being crawled and indexed. For example, suppose you want everything within the ProjectFiles folder indexed except for the subfolder Prototypes. You would need an inclusion rule for file:///C:\\WorkteamA\\ProjectFiles\\ and an exclusion rule for file:///C:\\WorkteamA\\ProjectFiles\\Prototypes\\.

The **Crawl Scope Manager (CSM)** is a set of APIs that lets you add, remove, and enumerate search roots and scope rules for the Windows Search indexer. When you want the indexer to begin crawling a new container, you can use the CSM to set the search root(s) and scope rules for paths within the search root(s). For example, if you install a new protocol handler, you can create a search root and add one or more inclusion rules; then the indexer can start a crawl for the initial indexing. The CSM offers the following interfaces to help you do this programmatically.

-   [**IEnumSearchRoots**](/windows/desktop/api/Searchapi/nn-searchapi-ienumsearchroots)
-   [IEnumSearchScopeRules](/windows/win32/api/searchapi/nn-searchapi-ienumsearchscoperules)
-   [**ISearchCrawlScopeManager**](/windows/desktop/api/Searchapi/nn-searchapi-isearchcrawlscopemanager)
-   [ISearchCrawlScopeManager2](/windows/win32/api/searchapi/nn-searchapi-isearchcrawlscopemanager2)
-   [**ISearchRoot**](/windows/desktop/api/Searchapi/nn-searchapi-isearchroot)
-   [**ISearchScopeRule**](/windows/desktop/api/Searchapi/nn-searchapi-isearchscoperule)
-   [ISearchItem](./-search-isearchitem.md)

While you can use the CSM APIs to define a crawl scope programmatically, the CSM was designed to support end users as well. For example, suppose you have developed a protocol handler for a new data store, and you want to let users or administrators manage which paths should be indexed. You can use the Crawl Scope Manager to set one or more search roots (for example, file:///C:\\MyContainer\\), and the Windows Search user interface for setting indexing options will display each search root with a check box. Users can then include or exclude that path or children of that path.

## Search Roots and Scope Rules

Search roots and scope rules together define a working set of URLs that comprise the indexer's crawl scope.

### Search Roots

Setting a search root does not specify which parts of this store should be indexed; it merely signals that a content store exists and is associated with a registered protocol handler. The syntax of a search root includes a protocol, a site or user security identifier, and a path to the location(s) to be crawled.

You should create new search roots when you:

-   Install a protocol handler OR
-   Want to index a new data store

AND

-   that data store is not already in the indexer's crawl scope.

Refer to [Managing Search Roots](-search-3x-wds-extidx-csm-searchroots.md) for instructions on adding, removing, and enumerating search roots.

### Scope Rules

Scope rules include or exclude URLs within a search root from being crawled and indexed. Scope rules can be set by end users, by group policy, or by third-party developers. You should define scope rules programmatically when you define a new search root. Your search roots and scope rules comprise the default crawl scope for your data store and protocol handler.

> [!Note]  
> Users with access to Control Panel can modify the default crawl scope. Therefore, any application that offers scope management should always get the rules directly from the CSM by using the enumeration methods instead of relying on its own saved copy of the user's rules.

 

Refer to [Managing Scope Rules](-search-3x-wds-extidx-csm-scoperules.md) for instructions on adding, removing, reverting, and enumerating scope rules.

## Group Policies Supported by the Crawl Scope Manager

System administrators can define crawl scopes across their organizations by using Group Policies. These group policy rules can also act as default rules, which users can override. For example, you can have one set of directories indexed for one group of users and a different set for another group of users, allowing the users to deselect these defaults. Group policy rules can also act as forced exclusion rules that users cannot override, preventing certain users from indexing certain network shares, for example.

## Related topics

<dl> <dt>

[Managing Search Roots](-search-3x-wds-extidx-csm-searchroots.md)
</dt> <dt>

[Managing Scope Rules](-search-3x-wds-extidx-csm-scoperules.md)
</dt> <dt>

[The Indexing Process](-search-indexing-process-overview.md)
</dt> </dl>

 

 
