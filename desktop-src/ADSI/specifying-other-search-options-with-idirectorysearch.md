---
title: Specifying Other Search Options with IDirectorySearch
description: The IDirectorySearch interface provide additional control over how the search is performed through the use of search options.
ms.assetid: 91b7ba90-99b3-4137-8e4e-8d0ccfb0ec13
ms.tgt_platform: multiple
keywords:
- Specifying Other Search Options with IDirectorySearch ADSI
- ADSI, Searching, IDirectorySearch, Other Search Options
ms.topic: article
ms.date: 05/31/2018
---

# Specifying Other Search Options with IDirectorySearch

The [**IDirectorySearch**](/windows/desktop/api/Iads/nn-iads-idirectorysearch) interface provide additional control over how the search is performed through the use of search options. These search options are set by filling in an array of [**ADS\_SEARCHPREF\_INFO**](/windows/desktop/api/Iads/ns-iads-ads_searchpref_info) structures and calling the [**IDirectorySearch::SetSearchPreference**](/windows/desktop/api/Iads/nf-iads-idirectorysearch-setsearchpreference) method. For more information, see the following topics:

-   [Using the SetSearchPreference Method](using-the-setsearchpreference-method.md)
-   [Synchronous and Asynchronous Searches with IDirectorySearch](synchronous-and-asynchronous-searches-with-idirectorysearch.md)
-   [Paging with IDirectorySearch](paging-with-idirectorysearch.md)
-   [Result Caching with IDirectorySearch](result-caching-with-idirectorysearch.md)
-   [Performing an Attribute Scope Query](performing-an-attribute-scoped-query.md)
-   [Sorting the Search Results with IDirectorySearch](sorting-the-search-results-with-idirectorysearch.md)
-   [Referral Chasing with IDirectorySearch](referral-chasing-with-idirectorysearch.md)
-   [Size Limit with IDirectorySearch](size-limit-with-idirectorysearch.md)
-   [Server Time Limit with IDirectorySearch](server-time-limit-with-idirectorysearch.md)
-   [Client Time Limit with IDirectorySearch](client-time-limit-with-idirectorysearch.md)
-   [Returning Only Attribute Names with IDirectorySearch](returning-only-attribute-names-with-idirectorysearch.md)

 

 




