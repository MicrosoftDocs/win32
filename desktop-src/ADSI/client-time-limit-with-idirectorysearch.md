---
title: Client Time Limit with IDirectorySearch
description: A client can impose a time limit for a server to return the result set. When the server fails to respond to a query within the specified time period, the client can abandon the search and try it again later.
ms.assetid: fe8a8b08-b34d-4aa5-a925-bcda6e72d437
ms.tgt_platform: multiple
keywords:
- Client Time Limit with IDirectorySearch
- ADSI, Searching, IDirectorySearch, Other Search Options, Client Time Limit
ms.topic: article
ms.date: 05/31/2018
---

# Client Time Limit with IDirectorySearch

A client can impose a time limit for a server to return the result set. When the server fails to respond to a query within the specified time period, the client can abandon the search and try it again later.

The client time limit preference is useful when a client requests an asynchronous search. In an asynchronous search, the client makes a request and then proceeds with other tasks while waiting for the server to return the results. It is possible that the server can go offline without notifying the client. In this case, the client will have no notification of whether the server is still processing the query, or if it no longer live. The client time limit preference gives the client some control of situations like this.

The default for the client time limit is no limit. To set a client time limit, set an **ADS\_SEARCHPREF\_TIMEOUT** search option with an **ADSTYPE\_INTEGER** value that contains the client time limit, in seconds, in the [**ADS\_SEARCHPREF\_INFO**](/windows/desktop/api/Iads/ns-iads-ads_searchpref_info) array passed to the [**IDirectorySearch::SetSearchPreference**](/windows/desktop/api/Iads/nf-iads-idirectorysearch-setsearchpreference) method. A client time limit of zero indicates no time limit.

The following code example shows how to set the client time limit.


```C++
ADS_SEARCHPREF_INFO SearchPref;
SearchPref.dwSearchPref = ADS_SEARCHPREF_TIMEOUT;
SearchPref.vValue.dwType = ADSTYPE_INTEGER;
SearchPref.vValue.Integer = 10;
```



 

 




