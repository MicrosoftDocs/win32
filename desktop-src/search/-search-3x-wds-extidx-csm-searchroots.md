---
description: The Crawl Scope Manager (CSM) enables you to add and remove search roots for your data stores to and from the Windows Search crawl scope.
ms.assetid: 0f1ff41f-7c4c-4516-bb55-bf09a8f2f3bc
title: Managing Search Roots
ms.topic: article
ms.date: 05/31/2018
---

# Managing Search Roots

The Crawl Scope Manager (CSM) enables you to add and remove search roots for your data stores to and from the Windows Search crawl scope.

This topic includes the following subjects:

-   [About Search Roots](#about-search-roots)
-   [Before You Begin](#before-you-begin)
-   [Windows 7: New Crawl Scope Manager API](#windows-7-new-crawl-scope-manager-api)
-   [Adding Roots to the Crawl Scope](#adding-roots-to-the-crawl-scope)
-   [Removing Roots from the Crawl Scope](#removing-roots-from-the-crawl-scope)
-   [Enumerating Roots in the Crawl Scope](#enumerating-roots-in-the-crawl-scope)
-   [Related topics](#related-topics)

 

## About Search Roots

A search root defines the base of a Shell namespace where specific scopes could be included or excluded, and is usually the highest level container in a protocol that can be enumerated. It does not specify which parts of this store should or should not be indexed; it merely signals that a content store exists and is associated with a registered protocol handler. The syntax for identifying a search root URL includes the protocol, the store or user's security identifier, the path, and optionally a specific item (like a file). The following examples show two forms of the syntax for a search root.


```
<protocol>://<store or SID>\<path>\[item]
or
<protocol>://<store or SID>/<path>/[item]
```



The <protocol> segment must be followed by two (2) forward slashes ('/') unless it is the file: protocol, which requires three slashes (file:///). The <site or SID> segment represents either a content store or a user security identifier if the search root is meant to be specific to the user. The <path> segment is a set of containers, like directories or folders, and can include the wildcard character '\*'. The <item> segment is optional and can also include the wildcard character '\*'. If you do not include an item, be sure to finish your path segment with a slash or the indexer will assume that the last subcontainer is an item.

For example, suppose you have implemented a protocol handler (myPH) to handle files of type \*.myext for a custom application. All of these files will be located in the folder WorkteamA\\ProjectFiles on a local computer. The search root for that might look like this:

-   myPH:///C:\\WorkteamA\\ProjectFiles\\

Suppose you are planning to include all .myext files but nothing else from that container in the index. The search root for that might look like this:

-   myPH:///C:\\WorkteamA\\ProjectFiles\\\*.myext.

Wildcard patterns define URLs by using the wildcard character '\*' and are considered a pattern rather than a URL, but the terminology is often used interchangeably. For example, file:///C:\\ProjectA\\\*\\data\\ would match the following URLs:

-   C:\\ProjectA\\**version1**\\data\\
-   C:\\ProjectA\\**version2**\\data\\

But that pattern would not match this URL:

-   C:\\ProjectA\\**version1\\temp**\\data\\

You should create new search roots for containers that are not already in the crawl scope of the indexer. If path C:\\ParentScope is already included in the crawl scope, you do not need to add a new search root for C:\\ParentScope\\ChildScope unless you know that the child scope was previously excluded.

The user interface for setting Windows Search options displays search roots to users so they can refine the scope rules for their searches. As part of the installation process for your custom protocol handler, container, and/or application, you might define a default crawl scope, with inclusion and exclusion rules. These rules are presented to end users as locations. Users can navigate within the subdirectories of your predefined search root and select the ones they want to include in searches or clear the ones they want to exclude.

 

## Before You Begin

Before you can use any of the Crawl Scope Manager (CSM) interfaces, you must perform the following prerequisite steps:

1.  Create the **CrawlSearchManager** object and obtain its [**ISearchManager**](/windows/desktop/api/Searchapi/nn-searchapi-isearchmanager) interface.
2.  Call [**ISearchManager::GetCatalog**](/windows/desktop/api/Searchapi/nf-searchapi-isearchmanager-getcatalog) for "SystemIndex" to obtain an instance of an [**ISearchCatalogManager**](/windows/desktop/api/Searchapi/nn-searchapi-isearchcatalogmanager) interface.
3.  Call [**ISearchCatalogManager::GetCrawlScopeManager**](/windows/desktop/api/Searchapi/nf-searchapi-isearchcatalogmanager-getcrawlscopemanager) to obtain an instance of [**ISearchCrawlScopeManager**](/windows/desktop/api/Searchapi/nn-searchapi-isearchcrawlscopemanager) interface.

After making any changes to the Crawl Scope Manager (CSM), you must call [**ISearchCrawlScopeManager::SaveAll**](/windows/desktop/api/Searchapi/nf-searchapi-isearchcrawlscopemanager-saveall). This method takes no parameters and returns S\_OK on success.

 

## Windows 7: New Crawl Scope Manager API

In **Windows 7 and later**, [**ISearchCrawlScopeManager2**](/windows/desktop/api/Searchapi/nn-searchapi-isearchcrawlscopemanager2) extends the functionality of the [**ISearchCrawlScopeManager**](/windows/desktop/api/Searchapi/nn-searchapi-isearchcrawlscopemanager) interface. The [**ISearchCrawlScopeManager2::GetVersion**](/windows/desktop/api/Searchapi/nf-searchapi-isearchcrawlscopemanager2-getversion) method gets the Crawl Scope Manager (CSM) version, which informs clients if the state of the CSM has changed. **ISearchCrawlScopeManager2::GetVersion** does not result in a cross-process call. If the function succeeds, then the pointer that is returned remains valid until the client calls **UnmapViewOfFile** on the pointer and **CloseHandle** on the returned handle.

 

## Adding Roots to the Crawl Scope

The [**ISearchCrawlScopeManager**](/windows/desktop/api/Searchapi/nn-searchapi-isearchcrawlscopemanager) tells the search engine about containers to crawl and/or watch, and items under those containers to include or exclude. To add a new search root, instantiate an [**ISearchRoot**](/windows/desktop/api/Searchapi/nn-searchapi-isearchroot) object, set the root attributes, and then call [**ISearchCrawlScopeManager::AddRoot**](/windows/desktop/api/Searchapi/nf-searchapi-isearchcrawlscopemanager-addroot) and pass it a pointer to your **ISearchRoot** object. The search root URL takes the same form as the search root described earlier.

The following table describes the relevant put methods for [**ISearchRoot**](/windows/desktop/api/Searchapi/nn-searchapi-isearchroot); the interface's other put methods are not used currently by Windows Search. We recommend including the users' security identifiers (SIDs) in all roots for better security. Per-user roots are more secure as queries are run in a per-user process, ensuring that one user cannot see items indexed from another user's inbox, for example.



| Method                     | Description                                                                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| put\_ProvidesNotifications | Set to **TRUE** if a protocol handler or other application will notify the search engine about changes to the URLs under the search root. The notification indicates that the URLs need reindexing. |
| put\_RootURL               | Sets the root URL of the current search. The URL takes the search root form described earlier.                                                                                                      |



 

 

By default, the indexer does not crawl a scope when you add a search root. You must also add an include rule for the root. If you want to add a user-specific root for an application, that application should add the appropriate roots for new users when the application starts.

To add the appropriate roots for new users:

1.  Get the user's SID.
2.  Enumerate all roots to check whether one exists for this SID.
3.  Add a new root, using the SID, if necessary.

 

## Removing Roots from the Crawl Scope

You can use [**ISearchCrawlScopeManager**](/windows/desktop/api/Searchapi/nn-searchapi-isearchcrawlscopemanager) to remove a root from the crawl scope when you no longer want that URL indexed. Removing a root also deletes all scope rules for that URL. For example, suppose you want to uninstall a content store and/or its protocol handler from a system. You can uninstall the application, remove all data, and then remove the search root from the crawl scope, and the Crawl Scope Manager will remove the root and all scope rules associated with the root.

To remove an existing search root, call [**ISearchCrawlScopeManager::RemoveRoot**](/windows/desktop/api/Searchapi/nf-searchapi-isearchcrawlscopemanager-removeroot) with the search root you want to remove. The search root URL takes the same form as the search root described earlier. This method returns S\_FALSE if the root is not found and an error code if there was an error removing a root that was found.

Removing a search root also removes the URL from the user interface for Windows Search options, so users may not be able to re-add that container or location using the user interface. It is also possible to remove all user-set overrides of a search root and revert to the original search root and scope rules. For more information, see [Managing Scope Rules](-search-3x-wds-extidx-csm-scoperules.md).

> [!Note]  
> On Windows Vista, if users are removed through User Profiles in Control Panel, CSM removes all rules and roots with their SID and removes their indexed items from the catalog. On Windows XP, you need to remove the users' roots and rules manually.

 

 

## Enumerating Roots in the Crawl Scope

The CSM enumerates search roots using a standard COM-style enumerator interface, [**IEnumSearchRoots**](/windows/desktop/api/Searchapi/nn-searchapi-ienumsearchroots). You can use this interface to enumerate search roots for a number of purposes. For example, you might want to display the entire crawl scope in a user interface, or discover whether a particular root or the child of a root is already in the crawl scope.

 

## Related topics

<dl> <dt>

**Reference**
</dt> <dt>

[**ISearchCrawlScopeManager**](/windows/desktop/api/Searchapi/nn-searchapi-isearchcrawlscopemanager)
</dt> <dt>

[**ISearchRoot**](/windows/desktop/api/Searchapi/nn-searchapi-isearchroot)
</dt> <dt>

[**IEnumSearchRoots**](/windows/desktop/api/Searchapi/nn-searchapi-ienumsearchroots)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Using the Crawl Scope Manager](-search-3x-wds-extidx-csm.md)
</dt> <dt>

[Managing Scope Rules](-search-3x-wds-extidx-csm-scoperules.md)
</dt> </dl>

 

 



