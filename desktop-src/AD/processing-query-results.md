---
title: Processing the Search Results
description: After the first call to IDirectorySearch GetFirstRow or IDirectorySearch GetNextRow, either S\_OK, S\_ADS\_NOMORE\_ROWS, or an error result is returned.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 3a84f394-a256-4815-901c-eaaae3d54b75
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- Processing Search Results AD
- Active Directory, Searching, Processing Search Results
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Processing the Search Results

After the first call to [**IDirectorySearch::GetFirstRow**](https://msdn.microsoft.com/library/aa746368) or [**IDirectorySearch::GetNextRow**](https://msdn.microsoft.com/library/aa746370), either **S\_OK**, **S\_ADS\_NOMORE\_ROWS**, or an error result is returned.

If the return value is **S\_ADS\_NOMORE\_ROWS**, no more objects matching the filter were found. If an error result is returned, the query failed. In both cases, you are not required to process the rows in the result because nothing was returned.

If **S\_OK** is returned, a row has been retrieved. You can parse the columns by name using [**IDirectorySearch::GetColumn**](https://msdn.microsoft.com/library/aa746367). The name is the **lDAPDisplayName** of the attribute in the column. The set of all columns was defined by the pAttributeNames parameter of the [**IDirectorySearch::ExecuteSearch**](https://msdn.microsoft.com/library/aa746365) method. If **NULL** was specified, the set of all columns is the union of all properties found for all the objects returned. To read the entire set of columns returned for an object, use the [**IDirectorySearch::GetNextColumnName**](https://msdn.microsoft.com/library/aa746369) to iterate each column, and use the column name returned to call **IDirectorySearch::GetColumn**.

The [**IDirectorySearch::GetColumn**](https://msdn.microsoft.com/library/aa746367) method returns an [**ADS\_SEARCH\_COLUMN**](https://msdn.microsoft.com/library/aa772292) structure that contains the attribute name, the type of the attribute, count of values, and a pointer to an array of [**ADSVALUE**](https://msdn.microsoft.com/library/aa772241) structures that contain the values. You can loop through the **ADSVALUE** structures to read the values for the property returned by the column. You must read the appropriate member of the **ADSVALUE** structure based on the [**ADSTYPE**](https://msdn.microsoft.com/library/aa772240) specified by the **dwADsType** member of the **ADS\_SEARCH\_COLUMN** structure (or the **dwType** member of the **ADSVALUE** structure). For example, if **dwADsType** was **ADSTYPE\_INTEGER**, you would read the **Integer** member of each **ADSVALUE** structure.

For more information and a code example, see [Example Code for Searching for Users](example-code-for-searching-for-users.md).

 

 




