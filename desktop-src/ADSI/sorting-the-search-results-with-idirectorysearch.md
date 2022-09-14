---
title: Sorting the Search Results with IDirectorySearch
description: By default, the results of a search are returned in no guaranteed order. The ADS\_SEARCHPREF\_SORT\_ON preference instructs the server to sort the result set on a specified attribute value before it is returned to the client.
ms.assetid: 1e44a572-7927-4fd5-a3eb-6dad0760d6e5
ms.tgt_platform: multiple
keywords:
- Sorting the Search Results with IDirectorySearch
- ADSI, Searching, IDirectorySearch, Other Search Options, Sorting Search Results
ms.topic: article
ms.date: 05/31/2018
---

# Sorting the Search Results with IDirectorySearch

By default, the results of a search are returned in no guaranteed order. The **ADS\_SEARCHPREF\_SORT\_ON** preference instructs the server to sort the result set on a specified attribute value before it is returned to the client.

It is recommended that indexed attributes be used for sorting. Otherwise, the server must retrieve the complete result set and sort it before sending any results to the client. This also applies to paged searches. Be aware that performance of a sorted search will be increased if the filter includes an indexed attribute and that attribute is specified as the sort key; in this case, Active Directory can satisfy the sort while processing the filter. For example, an efficient sort query for a set of users could have a filter that included (sn>smith) and a sort key of sn.

Server-side sorting with the **ADS\_SEARCHPREF\_SORT\_ON** search option will reduce the performance of the server. If you will be performing many searches, consider sorting the results manually on the client side to reduce the workload on the server.

By default, result sorting is disabled. To enable result sorting, set an **ADS\_SEARCHPREF\_SORT\_ON** search option with an **ADSTYPE\_PROV\_SPECIFIC** that points to an [**ADS\_SORTKEY**](/windows/desktop/api/Iads/ns-iads-ads_sortkey) structure in the [**ADS\_SEARCHPREF\_INFO**](/windows/desktop/api/Iads/ns-iads-ads_searchpref_info) array passed to the [**IDirectorySearch::SetSearchPreference**](/windows/desktop/api/Iads/nf-iads-idirectorysearch-setsearchpreference) method. The **ADS\_SORTKEY** structure is used to specify the attribute to sort on and the order of the sort.

The following code example shows how to enable result sorting.


```C++
ADS_SORTKEY SortKey;
SortKey.pszAttrType = L"cn";
SortKey.pszReserved = NULL;
SortKey.fReverseorder = FALSE;

ADS_SEARCHPREF_INFO SearchPref;
SearchPref.dwSearchPref = ADS_SEARCHPREF_SORT_ON;
SearchPref.vValue.dwType = ADSTYPE_PROV_SPECIFIC;
SearchPref.vValue.ProviderSpecific.dwLength = sizeof(SortKey);
SearchPref.vValue.ProviderSpecific.lpValue = (LPBYTE)&SortKey;
```



Active Directory does not support sorting on constructed attributes, so it is not possible to specify a constructed attribute for sorting. The [**distinguishedName**](/windows/desktop/ADSchema/a-distinguishedname) attribute also cannot be used for sorting. Active Directory also does not allow sorting on more than one attribute, so the **ADS\_SEARCHPREF\_SORT\_ON** search option can only contain one [**ADS\_SORTKEY**](/windows/desktop/api/Iads/ns-iads-ads_sortkey) structure.

 

 