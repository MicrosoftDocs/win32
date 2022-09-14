---
title: How to Search Using VLV
description: Active Directory supports virtual list view (VLV) searches. This style of search is specifically designed for large result sets and enables an application to display a subset of thousands of entries without actually having to retrieve every entry.
ms.assetid: fea04190-0846-4b62-99f4-7d8fb35fd510
ms.tgt_platform: multiple
keywords:
- How to Search Using VLV
ms.topic: article
ms.date: 05/31/2018
---

# How to Search Using VLV

Active Directory supports virtual list view (VLV) searches. This style of search is specifically designed for large result sets and enables an application to display a subset of thousands of entries without actually having to retrieve every entry.

There are two distinct ways that a VLV search can be used. The first is to retrieve the attributes for particular entries based on a numeric offset. This method is useful when retrieving search results in response to a scrolling operation.

The second way to use VLV searches is to search for part or all of a textual attribute and only display the results of the search. An example usage of this is an address book. If the user types an "s", then the application can use a VLV search to search for entries that have a common-name that begins with "s". If the user then adds an "m" to the "s", the application can use another VLV search to search for entries that have a common-name that begins with "sm".

To perform a VLV search, instruct ADSI to use the VLV control. To do this, call the [**IDirectorySearch::SetSearchPreference**](/windows/desktop/api/Iads/nf-iads-idirectorysearch-setsearchpreference) method with an **ADS\_SEARCHPREF\_VLV** search option with an **ADSTYPE\_PROV\_SPECIFIC** value. The **ADSTYPE\_PROV\_SPECIFIC** value is a pointer to an [**ADS\_VLV**](/windows/desktop/api/Iads/ns-iads-ads_vlv) structure that contains data about the search. The [**GetVLVItemCount**](example-code-for-using-a-vlv-search.md) example function shows how to set both of these search preferences.

All VLV searches must use server-side result sorting, which is performed by setting the **ADS\_SEARCHPREF\_SORT\_ON** search preference. For more information about the **ADS\_SEARCHPREF\_SORT\_ON** search preference, see [Sorting the Search Results with IDirectorySearch](sorting-the-search-results-with-idirectorysearch.md).

When a VLV search is performed, a certain amount of metadata about the search is returned in a column that is retrieved by calling [**IDirectorySearch::GetColumn**](/windows/desktop/api/Iads/nf-iads-idirectorysearch-getcolumn) with the **ADS\_VLV\_RESPONSE** identifier. This data is contained in an [**ADS\_VLV**](/windows/desktop/api/Iads/ns-iads-ads_vlv) structure. Of particular importance are the **dwContentCount** and **lpContextID** members. The **dwContentCount** member will contain the number of results that meet the VLV search criteria. This value can be used as an estimate of the total number of items that would be returned for a search of that type. The **lpContextID** member contains a server-defined value that can be passed to the next search to identify the search. Using the **lpContextID** can enhance the search performance. Be aware that the **lpContextID** is a server-defined value and its length is contained in the **dwContextIDLength** member. This buffer is freed when the [**IDirectorySearch::FreeColumn**](/windows/desktop/api/Iads/nf-iads-idirectorysearch-freecolumn) method is called, so the caller must allocate a buffer of the appropriate size and copy and save the contents of the buffer between searches.

For more information about the LDAP VLV control, see [Searching with the LDAP VLV Control](/previous-versions/windows/desktop/ldap/searching-with-the-ldap-vlv-control).

For more information, see:

-   Obtaining the Number of Items
-   Searching by Offset
-   Searching by String
-   [Example Code for Using a VLV Search](example-code-for-using-a-vlv-search.md)

## Obtaining the Number of Items

**To obtain an estimate of the number of items that will be returned for a particular search, perform the following steps.**

1.  Fill an [**ADS\_VLV**](/windows/desktop/api/Iads/ns-iads-ads_vlv) structure with all zero or **NULL** values.
2.  Fill an [**ADS\_SEARCHPREF\_INFO**](/windows/desktop/api/Iads/ns-iads-ads_searchpref_info) with the following values.

    -   Set the **dwSearchPref** member to **ADS\_SEARCHPREF\_VLV**.
    -   Set the **vValue.dwType** member to **ADSTYPE\_PROV\_SPECIFIC**.
    -   Set the **vValue.ProviderSpecific.dwLength** member to the size of the [**ADS\_VLV**](/windows/desktop/api/Iads/ns-iads-ads_vlv) structure.
    -   Set the **vValue.ProviderSpecific.lpValue** member to the address of the [**ADS\_VLV**](/windows/desktop/api/Iads/ns-iads-ads_vlv) structure from Step 1.

3.  Fill an [**ADS\_SORTKEY**](/windows/desktop/api/Iads/ns-iads-ads_sortkey) structure as shown in [Sorting the Search Results with IDirectorySearch](sorting-the-search-results-with-idirectorysearch.md) to sort on the desired attribute.
4.  Fill another [**ADS\_SEARCHPREF\_INFO**](/windows/desktop/api/Iads/ns-iads-ads_searchpref_info) to add the [**ADS\_SORTKEY**](/windows/desktop/api/Iads/ns-iads-ads_sortkey) structure to the search preferences as shown in [Sorting the Search Results with IDirectorySearch](sorting-the-search-results-with-idirectorysearch.md).
5.  Add any other desired search preferences and call [**IDirectorySearch::SetSearchPreference**](/windows/desktop/api/Iads/nf-iads-idirectorysearch-setsearchpreference) to set the search preferences.
6.  Perform the search with [**IDirectorySearch::ExecuteSearch**](/windows/desktop/api/Iads/nf-iads-idirectorysearch-executesearch).
7.  Get the first row of results by calling [**IDirectorySearch::GetFirstRow**](/windows/desktop/api/Iads/nf-iads-idirectorysearch-getfirstrow).
8.  Call [**IDirectorySearch::GetColumn**](/windows/desktop/api/Iads/nf-iads-idirectorysearch-getcolumn) with **ADS\_VLV\_RESPONSE** to obtain the VLV search metadata.
9.  Cast the **pADsValues->ProviderSpecific.lpValue** of the [**ADS\_SEARCH\_COLUMN**](/windows/desktop/api/Iads/ns-iads-ads_search_column) structure to an [**ADS\_VLV**](/windows/desktop/api/Iads/ns-iads-ads_vlv) structure pointer. The **dwContentCount** member of this **ADS\_VLV** structure contains the approximate number of items that would be returned by a search of that type.
10. If other VLV searches of the same type will be performed, make a copy of the **lpContextID** data and preserve it for the next VLV search.

The [**GetVLVItemCount**](example-code-for-using-a-vlv-search.md) example function shows how to do this.

## Searching by Offset

One thing that makes VLV searches so quick is that it is possible to search for a specific result by a numerical offset. For example, if a search would result in 10,000 items being returned, a VLV search makes it possible to obtain the information for approximately the 4072nd item without having to retrieve all of the items before the item in question.

Offsets are specified as a ratio between the offset and the content count. Ratios are useful because the server may not have an accurate estimate of the number of entries that exist in the list or the list size may be changing during the time the user is browsing it. Because you must indicate the beginning and end of the list, you can use an estimated value for the content count in the first search request, along with an offset value. The server uses this data to compute the corresponding offsets within the list, based on its idea of content count, which is sent in its response to the client through the **dwContentCount** member of the [**ADS\_VLV**](/windows/desktop/api/Iads/ns-iads-ads_vlv) structure. For example, if you estimate the list size to be 3000, and you want the offset to be list entry 1500, you would set **dwContentCount** to 3000 and **dwOffset** to 1500. If the server estimates the actual list size to be 4500, it will recalculate the offset to 2250, and return the new estimates in **dwContentCount** and **dwOffset**.

> [!Note]
>
> All of the numeric values in a VLV search are approximations and should not be used for absolute values. For example, if you issue a VLV search for the 50th item in a ration of 100, you are not guaranteed to get the exact middle item.
>
> **To search for a particular item by offset, perform the following steps.**
>
> 1.  Fill an [**ADS\_VLV**](/windows/desktop/api/Iads/ns-iads-ads_vlv) structure with the following values. Additional members of the structure should be set to zero or **NULL**.
>
>     -   Set the **dwContentCount** member to the maximum value of the ratio of items to retrieve.
>     -   Set the **dwOffset** member to the ratio, relative to **dwContentCount**, of the item or items to retrieve.
>     -   Set the **lpContextID** member to the address of the copy of the context ID buffer and the **dwContextIDLength** to the length, in bytes, of the context ID buffer. If no context ID has been saved, both of the these members should be zero or **NULL**.
>
> 2.  Set the search preferences as shown in Steps 2 through 5 of the Obtaining the Number of Items procedure.
> 3.  Perform the search with [**IDirectorySearch::ExecuteSearch**](/windows/desktop/api/Iads/nf-iads-idirectorysearch-executesearch).
> 4.  Get the first row of results by calling [**IDirectorySearch::GetFirstRow**](/windows/desktop/api/Iads/nf-iads-idirectorysearch-getfirstrow).
> 5.  Call [**IDirectorySearch::GetColumn**](/windows/desktop/api/Iads/nf-iads-idirectorysearch-getcolumn) with the name of the attribute to retrieve to get the actual data for the requested item.
> 6.  Call [**IDirectorySearch::GetColumn**](/windows/desktop/api/Iads/nf-iads-idirectorysearch-getcolumn) with **ADS\_VLV\_RESPONSE** to obtain the VLV search metadata.
> 7.  Cast the **pADsValues->ProviderSpecific.lpValue** of the [**ADS\_SEARCH\_COLUMN**](/windows/desktop/api/Iads/ns-iads-ads_search_column) structure to an [**ADS\_VLV**](/windows/desktop/api/Iads/ns-iads-ads_vlv) structure pointer.
> 8.  Make a copy of the **lpContextID** data and preserve it for the next VLV search.

 

The [**GetVLVItemText**](example-code-for-using-a-vlv-search.md) example function shows how to do this.

It is also possible to retrieve more than one row of data with a single search call. This is done in Step 1 by setting the **dwBeforeCount** and **dwAfterCount** members of the [**ADS\_VLV**](/windows/desktop/api/Iads/ns-iads-ads_vlv) structure appropriately. The **dwBeforeCount** member contains the number of items that appear in the list prior to the item in question and the **dwAfterCount** member contains the number of items that appear in the list after to the item in question. Both of these counts exclude the item itself, so setting **dwBeforeCount** to 10 and **dwAfterCount** to 10 will result in a total of 21 items returned. This option enables caching the search results on the client side.

## Searching by String

It is also possible to use a VLV search to find items that have a string attribute whose value matches all or part of a string without having to retrieve all items. The string matching is performed against the attribute specified in the [**ADS\_SORTKEY**](/windows/desktop/api/Iads/ns-iads-ads_sortkey) structure of the **ADS\_SEARCHPREF\_SORT\_ON** search preference.

**To search for a particular item by string, perform the following steps.**

1.  Fill an [**ADS\_VLV**](/windows/desktop/api/Iads/ns-iads-ads_vlv) structure with the following values. Additional members of the structure should be set to zero or **NULL**.

    -   Set the **pszTarget** member to a pointer to a NULL-terminated string that contains the string to search for.
    -   Set the **lpContextID** member to the address of the copy of the context ID buffer and the **dwContextIDLength** to the length, in bytes, of the context ID buffer. If no context ID has been saved, both of the these members should be zero or **NULL**.

2.  Set the search preferences as shown in Steps 2 through 5 of the Obtaining the Number of Items procedure.
3.  Perform the search with [**IDirectorySearch::ExecuteSearch**](/windows/desktop/api/Iads/nf-iads-idirectorysearch-executesearch).
4.  Get the first row of results by calling [**IDirectorySearch::GetFirstRow**](/windows/desktop/api/Iads/nf-iads-idirectorysearch-getfirstrow).
5.  Call [**IDirectorySearch::GetColumn**](/windows/desktop/api/Iads/nf-iads-idirectorysearch-getcolumn) with the name of the attribute to retrieve to get the actual data for the requested item.
6.  Call [**IDirectorySearch::GetColumn**](/windows/desktop/api/Iads/nf-iads-idirectorysearch-getcolumn) with **ADS\_VLV\_RESPONSE** to obtain the VLV search metadata.
7.  Cast the **pADsValues->ProviderSpecific.lpValue** of the [**ADS\_SEARCH\_COLUMN**](/windows/desktop/api/Iads/ns-iads-ads_search_column) structure to an [**ADS\_VLV**](/windows/desktop/api/Iads/ns-iads-ads_vlv) structure pointer.
8.  Make a copy of the **lpContextID** data and preserve it for the next VLV search. If required, the **dwOffset** member contains the one-based index of the first item whose string attribute begins with the value specified in **pszTarget**.

The [**GetVLVItemsByString**](example-code-for-using-a-vlv-search.md) example function shows how to do this.

Similarly to searching by index, it is also possible to retrieve more than one row of data with a single search call. This is accomplished in the same manner by setting the **dwBeforeCount** and **dwAfterCount** members of the [**ADS\_VLV**](/windows/desktop/api/Iads/ns-iads-ads_vlv) structure appropriately.

 

 