---
title: Example Code for Searching for Attributes
description: The following code example shows how to use the ADS\_SEARCHPREF\_ATTRIBTYPES\_ONLY search preference to retrieve only the names of attributes to which values have been assigned.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: '0e166f06-6030-4615-a46d-a282961d3b55'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
keywords: ["ADSI, Example Code C/C++ , Searching for Attributes", "Example Code for Searching for Attributes", "ADSI, Searching, IDirectorySearch, Other Search Options, Returning Only Attribute Names, Example Code"]
---

# Example Code for Searching for Attributes

The following code example shows how to use the **ADS\_SEARCHPREF\_ATTRIBTYPES\_ONLY** search preference to retrieve only the names of attributes to which values have been assigned. The example initializes an [**ADS\_SEARCHPREF\_INFO**](ads-searchpref-info.md) structure and sets the search preference by calling the [**SetSearchPreference**](idirectorysearch-setsearchpreference.md) method of the [**IDirectorySearch**](idirectorysearch.md) interface. The example then calls the [**ExecuteSearch**](idirectorysearch-executesearch.md) method to perform the search.


```C++
// Setting the search preference.
// m_pSearch is a valid pointer to an IDirectorySearch interface.
ADS_SEARCHPREF_INFO prefInfo[1];
LPWSTR pszColumn = NULL;

// Set the search preference to indicate attribute names only.
prefInfo[0].dwSearchPref = ADS_SEARCHPREF_ATTRIBTYPES_ONLY;
prefInfo[0].vValue.dwType = ADSTYPE_BOOLEAN;
prefInfo[0].vValue.Integer = TRUE;
hr = m_pSearch->SetSearchPreference(prefInfo, 1);

// Execute the search.
hr = m_pSearch->ExecuteSearch(
                L"(|(objectCategory=domainDNS)(objectCategory=organizationalUnit))", 
                NULL, -1, &amp;hSearch );

if(FAILED(hr))
{
   return;
}

// Retrieve the column name.
hr = m_pSearch->GetNextRow(hSearch);

if(FAILED(hr))
{
   return;
}
    
while( m_pSearch->GetNextColumnName( hSearch, &amp;pszColumn ) != S_ADS_NOMORE_COLUMNS )
{
   wprintf(L"%S ", pszColumn );
   FreeADsMem( pszColumn );
}
```



 

 




