---
title: Paging with IDirectorySearch
description: Paging specifies how many rows that the server returns to the client.
ms.assetid: cf4aa56a-c6f7-47c8-956d-512a5cffbf22
ms.tgt_platform: multiple
keywords:
- Paging with IDirectorySearch ADSI
- ADSI, Searching, IDirectorySearch, Other Search Options, Paging
ms.topic: article
ms.date: 05/31/2018
---

# Paging with IDirectorySearch

Paging specifies how many rows that the server returns to the client. A page can be defined by the number of rows or a time limit. The ADSI COM object retrieves each page of results based on the values listed in the following table. The caller calls [**IDirectorySearch::GetNextRow**](/windows/desktop/api/Iads/nf-iads-idirectorysearch-getnextrow) when it has reached the page end, and the ADSI COM object retrieves the next page.



| Value                                   | Description                                                                                                                                                                                                                                          |
|-----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **ADS\_SEARCHPREF\_PAGESIZE**           | Specifies the maximum number of rows to return in a page.                                                                                                                                                                                            |
| **ADS\_SEARCHPREF\_PAGED\_TIME\_LIMIT** | Specifies the maximum time, in seconds, that the server should spend collecting a page of results before returning the page to the client. If the limit is reached, the server stops the search and returns the rows already retrieved for the page. |



 

If neither of these search preferences is set, the default is no paging. Searches of the Active Directory performed without paging are limited to returning a maximum of the first 1000 records, so you must use a paged search if there is the possibility that the result set will contain more than 1000 items.

A search operation may result in a large number of objects being returned. If the server returns the result in one set, it could decrease the performance of the client and server, as well as affect the network load. Paged searches can be used to prevent this. In a paged search, the client can accept results in smaller packets. The size of a packet is known as the search page size.

Paged searches offer benefits to both the client and the server. The client can be more responsive in presenting the results to users. This is especially relevant to graphical user interface tools that can begin the window display process while the other thread concurrently receives the data.

On the server side, paged searches make the operation scalable. For example, if one hundred clients issue search requests simultaneously and, on the average, each client receives two hundred objects. If no page size is specified, in the worst-case scenario, the server must have sufficient memory to hold 20,000 objects. Conversely, if each client specifies a page size to be, for example, ten objects, the memory requirement on the server is thus reduced by a factor of 20.

In addition, using a paged search, a client can abandon the operation in progress. In contrast, in a non-paged search, the client receives a result set in one packet. This can decrease network performance.

ADSI handles the page size for the client. The client does not have to count the number of objects in progress. ADSI encapsulates the server interaction for the client. From the client perspective, the search returns a complete result set.

It is recommended that paging is used.

To specify a maximum page size, set an **ADS\_SEARCHPREF\_PAGESIZE** search option with an **ADSTYPE\_INTEGER** value set to the maximum number of rows per page in the [**ADS\_SEARCHPREF\_INFO**](/windows/desktop/api/Iads/ns-iads-ads_searchpref_info) array passed to the [**IDirectorySearch::SetSearchPreference**](/windows/desktop/api/Iads/nf-iads-idirectorysearch-setsearchpreference) method.

The following code example shows how to set the maximum page size.


```C++
ADS_SEARCHPREF_INFO SearchPref;
SearchPref.dwSearchPref = ADS_SEARCHPREF_PAGESIZE;
SearchPref.vValue.dwType = ADSTYPE_INTEGER;
SearchPref.vValue.Integer = 1000;
```



To specify a page time, set an **ADS\_SEARCHPREF\_PAGED\_TIME\_LIMIT** search option with an **ADSTYPE\_INTEGER** value set to the maximum number of seconds that the server should spend retrieving a page in the [**ADS\_SEARCHPREF\_INFO**](/windows/desktop/api/Iads/ns-iads-ads_searchpref_info) array passed to the [**IDirectorySearch::SetSearchPreference**](/windows/desktop/api/Iads/nf-iads-idirectorysearch-setsearchpreference) method.

The following code example shows how to specify page time.


```C++
ADS_SEARCHPREF_INFO SearchPref;
SearchPref.dwSearchPref = ADS_SEARCHPREF_PAGED_TIME_LIMIT;
SearchPref.vValue.dwType = ADSTYPE_INTEGER;
SearchPref.vValue.Integer = 60;
```



 

 




