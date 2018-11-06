---
title: Using the SetSearchPreference Method
description: Calling the IDirectorySearch SetSearchPreference method changes the way in which the search results are obtained and presented through the IDirectorySearch interface.
ms.assetid: 37583276-8372-4478-82aa-3e456cc0f8f1
ms.tgt_platform: multiple
keywords:
- SetSearchPreference ADSI ,using the SetSearchPreference method
- ADSI ADSI ,example code C/C++ ,using the SetSearchPreference method
- queries ADSI ,using SetSearchPreference
ms.topic: article
ms.date: 05/31/2018
---

# Using the SetSearchPreference Method

Calling the [**IDirectorySearch::SetSearchPreference**](/windows/desktop/api/Iads/nf-iads-idirectorysearch-setsearchpreference) method changes the way in which the search results are obtained and presented through the [**IDirectorySearch**](/windows/desktop/api/Iads/nn-iads-idirectorysearch) interface.

The SDK documentation defines [**SetSearchPreference**](/windows/desktop/api/Iads/nf-iads-idirectorysearch-setsearchpreference) as follows:


```C++
HRESULT SetSearchPreference(
            //Search preferences to be set.
            PADS_SEARCHPREF_INFO pSearchPrefs,
            //Number of preferences.
            DWORD dwNumPrefs
            );
```



Multiple preferences may be set by passing an array as the first parameter and the array size as the second parameter.


```C++
ADS_SEARCHPREF_INFO arSearchPrefs[2];
 
arSearchPrefs[0].dwSearchPref = ADS_SEARCHPREF_PAGESIZE; 
arSearchPrefs[0].vValue.dwType = ADSTYPE_INTEGER;
arSearchPrefs[0].vValue.Integer = 100;
 
arSearchPrefs[1].dwSearchPref = ADS_SEARCHPREF_SEARCH_SCOPE; 
arSearchPrefs[1].vValue.dwType = ADSTYPE_INTEGER; 
arSearchPrefs[1].vValue.Integer = ADS_SCOPE_SUBTREE; 
 
hr = pDSearch->SetSearchPreference(&arSearchPrefs, 2);
```



This example sets the page size to 100 rows and the scope to the ADS\_SCOPE\_SUBTREE type. The page size setting causes the server to immediately return data to the client, after 100 rows have been calculated. The ADS\_SCOPE\_SUBTREE setting causes the search to encompass all branches in the tree below the point from which the search is being executed.

 

 




