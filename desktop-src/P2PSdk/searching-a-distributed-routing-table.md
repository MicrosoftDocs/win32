---
description: Before an application can search the Distributed Routing Table (DRT), a search query must be created.
ms.assetid: b3403a64-128c-461e-9384-8e62c03322e1
title: Searching a Distributed Routing Table
ms.topic: article
ms.date: 05/31/2018
---

# Searching a Distributed Routing Table

Before an application can search the Distributed Routing Table (DRT), a search query must be created. The desired key value is specified by the application when the [**DrtStartSearch**](/windows/desktop/api/drt/nf-drt-drtstartsearch) function is called. The behavior of the search is determined by information specified by the application in the [**DRT\_SEARCH\_INFO**](/windows/desktop/api/drt/ns-drt-drt_search_info) structure.

Typically, an application event is signaled when the search discovers results and another at the conclusion of the search. However, if **fIterative** is set in [**DRT\_SEARCH\_INFO**](/windows/desktop/api/drt/ns-drt-drt_search_info), an application event can be signaled when contact is made with each node along the way.

After an event is signaled, the application then calls the [**DrtGetSearchResult**](/windows/desktop/api/drt/nf-drt-drtgetsearchresult) function for the results. If the returned code is **S\_OK**, the results are pointed to in the [**DRT\_SEARCH\_RESULT**](/windows/desktop/api/drt/ns-drt-drt_search_result) structure returned by the API. The returned results fall into the range of values specified in [**DRT\_SEARCH\_INFO**](/windows/desktop/api/drt/ns-drt-drt_search_info). In the event that the search finds no matches, only the **DRT\_E\_NO\_MORE** value will be returned at the conclusion of result returns.

The following information details how the members contained in [**DRT\_SEARCH\_INFO**](/windows/desktop/api/drt/ns-drt-drt_search_info) allow an application to specifically dictate the search behavior of the DRT infrastructure:

## fAllowCurrentInstanceMatch

By default, DRT search results include only matches found outside of the local node. Setting **fAllowCurrentInstanceMatch** specifies that the search results also include matches found in the local DRT instance.

## cMaxEndpoints

The quantity and range of the results returned by the search are specified by the application with the **cMaxEndpoints** (quantity) and the **pMinimumKey** and **pMaximumKey** (range) values, and referenced by [**DRT\_SEARCH\_INFO**](/windows/desktop/api/drt/ns-drt-drt_search_info).

When **cMaxEndpoints = 1**, the DRT infrastructure searches for a key, returning one match within the range specified by the **pMinimumKey** and **pMaximumKey** values in [**DRT\_SEARCH\_INFO**](/windows/desktop/api/drt/ns-drt-drt_search_info). This match can be either an exact match or the nearest match within range. If a match is not found, **DRT\_E\_NO\_MORE** is returned.

If **cMaxEndpoints > 1**, the DRT infrastructure will return matches within the range up to the value of **cMaxEndpoints**. The returned matches can contain an exact match or the nearest match results within range. Additionally, if **pMinimumKey** and **pMaximumKey** are set to the same value, a search is carried out only for that value, returning **DRT\_E\_NO\_MORE** if it is not found.

## fAnyMatchInRange

The **fAnyMatchInRange** member indicates whether the search will stop after the first match is located within the specified range, or if the search will continue for the closest match to the key specified in the [**DrtStartSearch**](/windows/desktop/api/drt/nf-drt-drtstartsearch) API. When **fAnyMatchInRange** is set, the search is carried out with **cMaxEndpoints = 1** regardless of the specified value of **cMaxEndpoints** in [**DRT\_SEARCH\_INFO**](/windows/desktop/api/drt/ns-drt-drt_search_info).

## fIterative

The **fIterative** member specifies if each node contacted by the DRT infrastructure during the search will have the key/endpoint data associated with it made available to the application via [**DRT\_SEARCH\_RESULT**](/windows/desktop/api/drt/ns-drt-drt_search_result). By setting **fIterative** to **TRUE**, the value of **cMaxEndpoints = 1** will be forced. When **fIterative** is set to **TRUE** within a search query for the DRT, the application is called back after contact with each node or "hop." Each hop result contains a key indicating which node the DRT will search next. A hop result is returned via [**DrtGetSearchResult**](/windows/desktop/api/drt/nf-drt-drtgetsearchresult) as a **DRT\_MATCH\_INTERMEDIATE** result.

## pMinimumKey and pMaximumKey

The **pMinimumKey** and **pMaximumKey** members can be used to search for keys falling within a range. If the **fAnyMatchInRange** member is set to **FALSE**, the DRT will return the closest key(s) to the search target (specified using the pKey argument passed in the [**DrtStartSearch**](/windows/desktop/api/drt/nf-drt-drtstartsearch) function) falling within the range. Note that the *pKey* argument passed to **DrtStartSearch** must fall within the range defined by **pMinimumKey** and **pMaximumKey**. To search for a precise key, set **pMinimumKey**, **pMaximumKey** and *pKey* to the same value.

## Related topics

<dl> <dt>

[Registering and Deregistering Keys](registering-and-deregistering-keys.md)
</dt> <dt>

[About Distributed Routing Tables](about-distributed-routing-tables.md)
</dt> <dt>

[Distributed Routing Table API Reference](distributed-routing-table-api-reference.md)
</dt> </dl>

 

 



