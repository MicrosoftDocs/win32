---
title: Processing the Search Results
description: After the first call to IDirectorySearch GetFirstRow or IDirectorySearch GetNextRow, either S\_OK, S\_ADS\_NOMORE\_ROWS, or an error result is returned.
ms.assetid: 3a84f394-a256-4815-901c-eaaae3d54b75
ms.tgt_platform: multiple
keywords:
- Processing Search Results AD
- Active Directory, Searching, Processing Search Results
ms.topic: article
ms.date: 05/31/2018
---

# Processing the Search Results

After the first call to [**IDirectorySearch::GetFirstRow**](/windows/desktop/api/iads/nf-iads-idirectorysearch-getfirstrow) or [**IDirectorySearch::GetNextRow**](/windows/desktop/api/iads/nf-iads-idirectorysearch-getnextrow), either **S\_OK**, **S\_ADS\_NOMORE\_ROWS**, or an error result is returned.

If the return value is **S\_ADS\_NOMORE\_ROWS**, no more objects matching the filter were found. If an error result is returned, the query failed. In both cases, you are not required to process the rows in the result because nothing was returned.

If **S\_OK** is returned, a row has been retrieved. You can parse the columns by name using [**IDirectorySearch::GetColumn**](/windows/desktop/api/iads/nf-iads-idirectorysearch-getcolumn). The name is the **lDAPDisplayName** of the attribute in the column. The set of all columns was defined by the pAttributeNames parameter of the [**IDirectorySearch::ExecuteSearch**](/windows/desktop/api/iads/nf-iads-idirectorysearch-executesearch) method. If **NULL** was specified, the set of all columns is the union of all properties found for all the objects returned. To read the entire set of columns returned for an object, use the [**IDirectorySearch::GetNextColumnName**](/windows/desktop/api/iads/nf-iads-idirectorysearch-getnextcolumnname) to iterate each column, and use the column name returned to call **IDirectorySearch::GetColumn**.

The [**IDirectorySearch::GetColumn**](/windows/desktop/api/iads/nf-iads-idirectorysearch-getcolumn) method returns an [**ADS\_SEARCH\_COLUMN**](/windows/desktop/api/iads/ns-iads-ads_search_column) structure that contains the attribute name, the type of the attribute, count of values, and a pointer to an array of [**ADSVALUE**](/windows/desktop/api/iads/ns-iads-adsvalue) structures that contain the values. You can loop through the **ADSVALUE** structures to read the values for the property returned by the column. You must read the appropriate member of the **ADSVALUE** structure based on the [**ADSTYPE**](/windows/win32/api/iads/ne-iads-adstypeenum) specified by the **dwADsType** member of the **ADS\_SEARCH\_COLUMN** structure (or the **dwType** member of the **ADSVALUE** structure). For example, if **dwADsType** was **ADSTYPE\_INTEGER**, you would read the **Integer** member of each **ADSVALUE** structure.

For more information and a code example, see [Example Code for Searching for Users](example-code-for-searching-for-users.md).

 

 