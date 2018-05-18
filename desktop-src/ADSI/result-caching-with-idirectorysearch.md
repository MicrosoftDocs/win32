---
title: Result Caching with IDirectorySearch
description: The ADS\_SEARCHPREF\_CACHE\_RESULTS preference caches the result set on the client.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 'bb286879-7d84-4085-88e1-600c848b8af8'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
keywords: ["Result Caching with IDirectorySearch ADSI", "ADSI, Searching, IDirectorySearch, Other Search Options, Result Caching"]
---

# Result Caching with IDirectorySearch

The **ADS\_SEARCHPREF\_CACHE\_RESULTS** preference caches the result set on the client. Result caching enables an application to retain a retrieved result set and go through the retrieved rows again. It also enables cursor support where the [**IDirectorySearch::GetNextRow**](idirectorysearch-getnextrow.md) and [**IDirectorySearch::GetPreviousRow**](idirectorysearch-getpreviousrow.md) methods can be used to move up and down the result set.

By default, result caching is disabled. Result caching should be enabled if any one of the following is true:

-   If the same result set must be enumerated multiple times without performing the search again on the server.
-   If performing the search is resource-intensive on the server (slow connection, large result set, or complex query).
-   If cursor support is required.

Turn off caching if your application must reduce memory requirements for caching a large result set at the client.

Result caching increases the memory requirements on the client, so result caching should be disabled if this is a concern.

To enable result caching, set an **ADS\_SEARCHPREF\_CACHE\_RESULTS** search option with an **ADSTYPE\_BOOLEAN** value of **TRUE** in the [**ADS\_SEARCHPREF\_INFO**](ads-searchpref-info.md) array passed to the [**IDirectorySearch::SetSearchPreference**](idirectorysearch-setsearchpreference.md) method.

The following code example shows how to enable result caching.


```C++
ADS_SEARCHPREF_INFO SearchPref;
SearchPref.dwSearchPref = ADS_SEARCHPREF_CACHE_RESULTS;
SearchPref.vValue.dwType = ADSTYPE_BOOLEAN;
SearchPref.vValue.Boolean = TRUE;
```



 

 




