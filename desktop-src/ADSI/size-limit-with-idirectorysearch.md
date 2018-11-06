---
title: Size Limit with IDirectorySearch
description: The client can focus on a small number of objects returned from the server and ignore the rest of the result set.
ms.assetid: 55393177-f49b-4163-8e33-2ec24a64b99a
ms.tgt_platform: multiple
keywords:
- Size Limit with IDirectorySearch ADSI
- ADSI, Searching, IDirectorySearch, Other Search Options, Size Limit
ms.topic: article
ms.date: 05/31/2018
---

# Size Limit with IDirectorySearch

To reduce the memory requirement or for other purposes, the client can focus on a small number of objects returned from the server and ignore the rest of the result set that are not of interest. To accomplish this, the client specifies the search size limit and other appropriate search criteria. For example, if the directory stores the test scores of a school district, you can query the top ten students with the highest test scores by specifying a size limit of ten (10) and a descending sort order.

The default for size limit is no limit. To set a size limit, set an **ADS\_SEARCHPREF\_SIZE\_LIMIT** search option with an **ADSTYPE\_INTEGER** value that contains the maximum size in the [**ADS\_SEARCHPREF\_INFO**](/windows/desktop/api/Iads/ns-iads-ads_searchpref_info) array passed to the [**IDirectorySearch::SetSearchPreference**](/windows/desktop/api/Iads/nf-iads-idirectorysearch-setsearchpreference) method.

The following code example shows how to set the size limit. A size limit value of zero indicates no size limit.


```C++
ADS_SEARCHPREF_INFO SearchPref;
SearchPref.dwSearchPref = ADS_SEARCHPREF_SIZE_LIMIT;
SearchPref.vValue.dwType = ADSTYPE_INTEGER;
SearchPref.vValue.Integer = 1000;
```



For Active Directory, the size limit specifies the maximum number of objects to be returned by the search. Also for Active Directory, the maximum number of objects returned by a search is 1000 objects.

 

 




