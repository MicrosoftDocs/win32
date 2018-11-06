---
title: Returning Only Attribute Names with IDirectorySearch
description: You can perform a search to determine what type of data is available for a particular object.
ms.assetid: 47e78b79-2063-420b-aa41-f4f0c35f87ea
ms.tgt_platform: multiple
keywords:
- Returning Only Attribute Names with IDirectorySearch ADSI
- ADSI, Searching, IDirectorySearch, Other Search Options, Returning Only Attribute Names
ms.topic: article
ms.date: 05/31/2018
---

# Returning Only Attribute Names with IDirectorySearch

You can perform a search to determine what type of data is available for a particular object. In this case, you are only interested in the attributes names, not the attribute values of the object. The **ADS\_SEARCHPREF\_ATTRIBTYPES\_ONLY** option causes the server to only return the attribute names and not the attribute values. However, the result set includes only those attributes that have values assigned. For example, consider an object with the following attributes:

``` syntax
name = Jeff
sn = Smith
department = Empty
phone = 206-555-0111
```

When the **ADS\_SEARCHPREF\_ATTRIBTYPES\_ONLY** option is set, the result set includes:

``` syntax
name
sn
department
phone
```

The default is for both attribute values and names to be returned.

To retrieve only attribute names, set an **ADS\_SEARCHPREF\_ATTRIBTYPES\_ONLY** search option with an **ADSTYPE\_BOOLEAN** value of **TRUE** in the [**ADS\_SEARCHPREF\_INFO**](/windows/desktop/api/Iads/ns-iads-ads_searchpref_info) array passed to the [**IDirectorySearch::SetSearchPreference**](/windows/desktop/api/Iads/nf-iads-idirectorysearch-setsearchpreference) method.

The following code example shows how to retrieve attribute names only.


```C++
ADS_SEARCHPREF_INFO SearchPref;
SearchPref.dwSearchPref = ADS_SEARCHPREF_ATTRIBTYPES_ONLY;
SearchPref.vValue.dwType = ADSTYPE_BOOLEAN;
SearchPref.vValue.Boolean = TRUE;
```



For more information and a code example that shows how to use the **ADS\_SEARCHPREF\_ATTRIBTYPES\_ONLY** search option, see [Example Code for Searching for Attributes](example-code-for-searching-for-attributes.md).

 

 




