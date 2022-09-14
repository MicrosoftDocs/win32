---
description: The Crawl Scope Manager (CSM) enables you define scope rules that include or exclude URLs from the Windows Search crawl scope.
ms.assetid: 132a55f9-680d-438e-b983-f5ce4cf66a41
title: Managing Scope Rules
ms.topic: article
ms.date: 05/31/2018
---

# Managing Scope Rules

The Crawl Scope Manager (CSM) enables you define scope rules that include or exclude URLs from the Windows Search crawl scope.

The CSM lets you do the following:

-   Add new scope rules to the working rule set
-   Remove existing scope rules
-   Enumerate default scope rules
-   Discover whether a particular URL is included or excluded from the crawl scope or has a parent or child scope rule

 

This topic includes the following subjects:

-   [About Scope Rules](#about-scope-rules)
-   [Before You Begin](#before-you-begin)
-   [Adding Scope Rules](#adding-scope-rules)
    -   [Notes on User Rules](#notes-on-user-rules)
-   [Removing Scope Rules](#removing-scope-rules)
-   [Reverting to Default Rules](#reverting-to-default-rules)
-   [Enumerating Scope Rules](#enumerating-scope-rules)
-   [Tracing Scope Rules](#tracing-scope-rules)
-   [Related topics](#related-topics)

## About Scope Rules

A scope rule is a rule that includes or excludes URLs within a search root from being crawled and indexed. Inclusion rules cause the indexer to include that URL in the scrawl scope, and exclusion rules cause the indexer exclude that URL (and its children) from the crawl scope.

For example, suppose you've installed a new application whose data files are located in the folder WorkteamA\\ProjectFiles on a local computer. Suppose you want everything within the ProjectFiles folder indexed except for items in the subfolder Prototypes. In this situation, you would need an inclusion rule for myPH:///C:\\WorkteamA\\ProjectFiles\\ and an exclusion rule for myPH:///C:\\WorkteamA\\ProjectFiles\\Prototypes\\.

There are three types of rules, with the following order of precedence:

1.  Group Policy rules are set by administrators and can override all other rules.
2.  User rules are set by users modifying the scope in the Windows Search options user interface. Users or other applications can remove all user rules and revert to default rules.
3.  Default rules are typically set by an application to define a default scope. For example, default rules might be set when a new protocol handler or container is added to the system.

Together, these types of rules comprise the *working rule set* from which the Crawl Scope Manager (CSM) generates the full list of URLs to crawl. While default rules can be overridden by group policy rules and by user rules, they are maintained in their own default rule set, which you can revert to at any time. The indexer crawls the URLs from the working rule set and adds items, properties, and content to the catalog.

> [!Note]  
> Users with access to Control Panel can modify the rules through that interface. Therefore, applications offering scope management should always get the rules directly from the CSM by using the enumeration methods instead of relying on a saved copy of user rules.

 

Exclusion rules can define pattern URLs with the wildcard character '\*'; for example: file:///C:\\ProjectA\\\*\\. An exclusion rule using this pattern prevents the indexer from crawling any folders under the ProjectA directory. For a more complicated example, suppose there is an inclusion rule for file:///C:\\ProjectA\\ and an exclusion pattern rule for file:///C:\\ProjectA\\\*\\data\\\*. In this case, the indexer would crawl items in:

-   C:\\ProjectA\\
-   C:\\ProjectA\\**version1**\\testfiles\\
-   C:\\ProjectA\\**version1\\temp**\\data\\

But the indexer would not crawl items in:

-   C:\\ProjectA\\**version1**\\data\\

 

## Before You Begin

Before you use any of the Crawl Scope Manager interfaces, you must perform the following prerequisite steps:

1.  Create the **CSearchManager** object and obtain its **ISearchManager** interface.
2.  Call **ISearchManager::GetCatalog** for "SystemIndex" to obtain an instance of the **ISearchCatalogManager** interface.
3.  Call **ISearchCatalogManager::GetCrawlScopeManager** to obtain an instance of the **ISearchCrawlScopeManager** interface.

After making any changes to the Crawl Scope Manager, you must call the [**ISearchCrawlScopeManager::SaveAll**](/windows/desktop/api/Searchapi/nf-searchapi-isearchcrawlscopemanager-saveall) method. This method takes no parameters and returns S\_OK on success.

 

## Adding Scope Rules

The working rules set for the CSM includes user and default rules, as well as any rules forced by group policy. User rules are set up by users in a user interface, and default rules can be set by any of the following:

-   Group policies implemented by a system administrator (These do not use the [**ISearchCrawlScopeManager**](/windows/desktop/api/Searchapi/nn-searchapi-isearchcrawlscopemanager) interface.)
-   The installation or update of an application like Windows Search or a protocol handler
-   A setup application for the addition of a new data store or container

The [**ISearchCrawlScopeManager**](/windows/desktop/api/Searchapi/nn-searchapi-isearchcrawlscopemanager) provides two methods for adding new scope rules, as described in the following table. Paths for inclusion rules for the file system must end with a backslash '\\' (for example, file:///C:\\files\\), and paths for exclusion rules must end with an asterisk (for example, file:///c:\\files\\\*). Only exclusion rules can contain pattern URLs. Furthermore, we recommend including users' security identifiers (SIDs) in paths, for better security. Per-user paths are more secure as queries would then run in a per-user process, ensuring that one user cannot see items indexed from another user's inbox, for example.

The following table describes the methods of the ISearchCrawlScopeManager interface used for adding new scope rules.



| Method                                                                              | Description                                                                                                                                                                                                                  |
|-------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AddUserScopeRule**](/windows/desktop/api/Searchapi/nf-searchapi-isearchcrawlscopemanager-adduserscoperule)       | Adds a rule for a URL, as specified by the user. These rules override default rules. Use this method if you have implemented a user interface that lets users manage their own scope rules and URLs.                         |
| [**AddDefaultScopeRule**](/windows/desktop/api/Searchapi/nf-searchapi-isearchcrawlscopemanager-adddefaultscoperule) | Adds a rule for a URL, as specified by another application like a protocol handler. Use this method when you have implemented a new protocol handler or added a new data store. These rules can be overridden by user rules. |



 

Each method takes a URL to an indexable location and flags that determine whether the URL should be included or excluded. The *fFollowFlags* parameter is reserved for future use. When you add a new scope rule and the Crawl Scope Manager determines that the rule already exists (based on the URL or the pattern provided), the working rule set is updated so that (1) the old rule is replaced by the new rule and (2) any user rules that contradict it are removed.

**Tip:** While the file:// root is included by default in the crawl scope, Program Files is not indexed by default. Therefore, applications with data saved to their Program Files directory need to add their location as a default rule.

### Notes on User Rules

If a new user rule is the same as an existing default rule, the new user rule overrides the default rule in the working rule set. If the new user rule is the same as an existing user rule, the old user rule is replaced.

Setting the flag *fOverrideChildren* has the following results in the working rule set:

-   **TRUE** results in the removal of all child rules from the working rule set (both user rules and default rules).
-   FALSE results in re-adding to the working rules set all the default rules that are children of the new user rule. If a child default rule is an inclusion and the new user rule is an exclusion, the default rule is changed to an inclusion user rule.

 

## Removing Scope Rules

You can use the [**ISearchCrawlScopeManager**](/windows/desktop/api/Searchapi/nn-searchapi-isearchcrawlscopemanager) interface to remove a scope rule from the working rule set. This interface provides the following two methods for removing scope rules.



| Method                                                                                    | Description                                                                                                                                                                                           |
|-------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**RemoveScopeRule**](/windows/desktop/api/Searchapi/nf-searchapi-isearchcrawlscopemanager-removescoperule)               | Removes a user rule for a specified URL from the working rule set. If the user rule is a duplicate of or overrides a default rule, the default rule remains in the working rule set.                  |
| [**RemoveDefaultScopeRule**](/windows/desktop/api/Searchapi/nf-searchapi-isearchcrawlscopemanager-removedefaultscoperule) | Removes a default rule for a specified URL from both the working rule set and the default rule set. After calling this method, you cannot revert to this default rule by using RevertToDefaultScopes. |



 

Each method takes a URL and a flag indicating whether the rule to be removed is an inclusion or exclusion rule. These methods returns an error if a rule with that URL and inclusion/exclusion flag is not found.

**Tip:** If you want to remove a scope from the crawl scope entirely, use the [**RemoveRoot**](/windows/desktop/api/Searchapi/nf-searchapi-isearchcrawlscopemanager-removeroot) method, which removes the search root and all associated scope rules. Doing this while uninstalling, for example, is considered best practice.

It is also possible to remove all user-set overrides of a search root and revert to the original search root and default scope rules. For more information, refer to the next section.

> [!Note]  
> On Windows Vista, if users are removed through User Profiles in Control Panel, CSM removes all rules and roots that include their SID and removes their indexed items from the catalog. On Windows XP, you must remove the users' roots and rules manually.

 

 

## Reverting to Default Rules

Reverting to default rules removes all user rules for a URL or root and restores all default rules to the working rule set. It does not, however, remove rules set by group policy. The [**RevertToDefaultScopes**](/windows/desktop/api/Searchapi/nf-searchapi-isearchcrawlscopemanager-reverttodefaultscopes) method takes no parameters and returns an error code if it is unable to revert to default rules.

 

## Enumerating Scope Rules

The CSM enumerates scope rules by using a standard COM-style enumerator interface, [**IEnumSearchScopeRules**](/windows/desktop/api/Searchapi/nn-searchapi-ienumsearchscoperules) . You can use this interface to enumerate scope rules for several purposes. For example, you might want to display the entire working rule set in a user interface, or discover whether a rule or the child of a rule is already in the crawl scope.

 

## Tracing Scope Rules

The CSM also enables you to determine whether a specified URL is included in the crawl scope and whether it has a parent or child scope rule. You can also find out why a URL is included or excluded from the crawl scope. These methods are not intended to be used with pattern URLs.

The following table describes the methods of [**ISearchCrawlScopeManager**](/windows/desktop/api/Searchapi/nn-searchapi-isearchcrawlscopemanager) used for adding new scope rules.



| Method                                                                                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|---------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetParentScopeVersionId**](/windows/desktop/api/Searchapi/nf-searchapi-isearchcrawlscopemanager-getparentscopeversionid) | Gets the version ID of the parent inclusion URL. You can use this method to see if the parent scope has changed since the last time you checked it.<br/> Example: If a mail application uses provider-managed notifications, it might get the parent scope version before it closes and check the version again when it opens. Then the application can determine whether it needs to push a new set of notifications to the indexer.<br/> |
| [**HasChildScopeRule**](/windows/desktop/api/Searchapi/nf-searchapi-isearchcrawlscopemanager-haschildscoperule)             | Returns **TRUE** if the specified URL has a child rule (a rule applying to a child at any level within its URL hierarchy). <br/> Example: If the URL is file:///C:\\Folder\\, this method returns **TRUE** if the CSM has a scope rule specifically for file:///C:\\Folder\\Subfolder\\.<br/>                                                                                                                                              |
| [**HasParentScopeRule**](/windows/desktop/api/Searchapi/nf-searchapi-isearchcrawlscopemanager-hasparentscoperule)           | Returns **TRUE** if the specified URL has a parent rule (a rule applying to a parent at any level in the URL hierarchy).<br/> Example: If the URL is file:///C:\\Folder\\Subfolder, this method returns **TRUE** if the CSM has a scope rule specifically for file:///C:\\Folder\\.<br/>                                                                                                                                                   |
| [**IncludedInCrawlScope**](/windows/desktop/api/Searchapi/nf-searchapi-isearchcrawlscopemanager-includedincrawlscope)       | Returns **TRUE** if the specified URL is included in the crawl scope.                                                                                                                                                                                                                                                                                                                                                                                  |
| [**IncludedInCrawlScopeEx**](/windows/desktop/api/Searchapi/nf-searchapi-isearchcrawlscopemanager-includedincrawlscopeex)   | Returns a value from the [**CLUSION\_REASON**](/windows/win32/api/searchapi/ne-searchapi-clusion_reason) enumeration explaining why the URL is included in or excluded from the crawl scope, and retrieves the value **TRUE** if the URL is included in the crawl scope. This method can help you identify conflicts in your working rule set.                                                                                                                                       |



 

 

> [!Note]  
> The [**IncludedInCrawlScope**](/windows/desktop/api/Searchapi/nf-searchapi-isearchcrawlscopemanager-includedincrawlscope) and [**IncludedInCrawlScopeEx**](/windows/desktop/api/Searchapi/nf-searchapi-isearchcrawlscopemanager-includedincrawlscopeex) methods determine whether the URL will be crawled based solely on the rules in the CSM. There can be other reasons that a URL is not crawled, such as the FANCI bit being set (that is, a user has disallowed fast indexing in the folder's Property dialog box.)

 

If you believe that a file path should be excluded, but it is listed as included, be sure that exclusion rules end with "&lt;path&gt;\\\*". If you believe that a file or file path should be included but it is not, be sure to check the FANCI bit setting for the file or path. You can do this by right-clicking the file or file path and selecting **Properties**, then be sure the **For fast searching, allow Indexing Service to index this folder** checkbox is selected. If the file or file path is not marked for indexing here, it will not be indexed even if it is in an inclusion rule.

## Related topics

<dl> <dt>

**Reference**
</dt> <dt>

[**ISearchCrawlScopeManager**](/windows/desktop/api/Searchapi/nn-searchapi-isearchcrawlscopemanager)
</dt> <dt>

[**ISearchCrawlScopeManager2**](/windows/desktop/api/Searchapi/nn-searchapi-isearchcrawlscopemanager2)
</dt> <dt>

[**ISearchScopeRule**](/windows/desktop/api/Searchapi/nn-searchapi-isearchscoperule)
</dt> <dt>

[**IEnumSearchScopeRules**](/windows/desktop/api/Searchapi/nn-searchapi-ienumsearchscoperules)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Managing Search Roots](-search-3x-wds-extidx-csm-searchroots.md)
</dt> </dl>

 

 




