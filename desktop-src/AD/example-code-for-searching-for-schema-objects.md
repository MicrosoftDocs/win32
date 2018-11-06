---
title: Example Code for Searching for Schema Objects
description: This topic includes a code example used to search for schema objects.
ms.assetid: 539e0127-1355-4606-97bd-49dfafb25f8d
ms.tgt_platform: multiple
keywords:
- Example Code for Searching for Schema Objects AD
ms.topic: article
ms.date: 05/31/2018
---

# Example Code for Searching for Schema Objects

This topic includes a code example used to search for schema objects.

The following C++ code example shows how to search for schema objects that have bits set in the **systemFlags** attribute.


```C++
#include <stdio.h>
#include <atlbase.h>
#include <activeds.h>
#include <ntldap.h>

/***************************************************************************

    PrintAttributesByType()

    Searches for and prints all attributeSchema objects that contain all of 
    the specified attribute type flags.

    Parameters:

    pSchemaNC - IDirectorySearch pointer to schema naming context.

    dwAttributeType - Bit flags to search for in systemFlags. These are 
        values such as ADS_SYSTEMFLAG_ATTR_IS_CONSTRUCTED.

    bIsExactMatch - TRUE to find attributes that have systemFlags exactly 
        matching dwAttributeType. FALSE to find attributes that have the 
        dwAttributeType bit set, and possibly others.

***************************************************************************/

HRESULT PrintAttributesByType(IDirectorySearch *pSchemaNC,
        DWORD dwAttributeType,
        BOOL bIsExactMatch)
{
    HRESULT hr;

    // Attributes are one-level deep in the Schema container, so only search one level.
    ADS_SEARCHPREF_INFO SearchPrefs[2];
    SearchPrefs[0].dwSearchPref = ADS_SEARCHPREF_SEARCH_SCOPE;
    SearchPrefs[0].vValue.dwType = ADSTYPE_INTEGER;
    SearchPrefs[0].vValue.Integer = ADS_SCOPE_ONELEVEL;
 
    // Use paging if there are more properties than can be returned by one page.
    SearchPrefs[1].dwSearchPref = ADS_SEARCHPREF_PAGESIZE;
    SearchPrefs[1].vValue.dwType = ADSTYPE_INTEGER;
    SearchPrefs[1].vValue.Integer = 1000;

    // Set the search preferences.
    hr = pSchemaNC->SetSearchPreference(SearchPrefs, sizeof(SearchPrefs)/sizeof(ADS_SEARCHPREF_INFO));
    if(FAILED(hr))
    {
        return hr;
    }
 
    // Handle that is used for searching.
    ADS_SEARCH_HANDLE hSearch;
 
    LPWSTR rgpwszAttributes[] = {L"cn"};
    DWORD dwAttributes = sizeof(rgpwszAttributes)/sizeof(LPWSTR);

    // Create the search filter.
    WCHAR wszAttributeType[30]; // Plenty large enough to handle the biggest 32-bit number.
    swprintf_s(wszAttributeType, L"%d", dwAttributeType);

    CComBSTR sbstrSearchFilter;
    if (bIsExactMatch)
    {
        sbstrSearchFilter = "(&(objectCategory=attributeSchema)(systemFlags=";
        sbstrSearchFilter += wszAttributeType;
        sbstrSearchFilter += "))";
    }
    else
    {
        sbstrSearchFilter = "(&(objectCategory=attributeSchema)(systemFlags:";
        sbstrSearchFilter += LDAP_MATCHING_RULE_BIT_AND;
        sbstrSearchFilter += ":=";
        sbstrSearchFilter += wszAttributeType;
        sbstrSearchFilter += "))";
    }
 
    // Execute the search.
    hr = pSchemaNC->ExecuteSearch(sbstrSearchFilter,
                                  rgpwszAttributes,
                                  dwAttributes,
                                  &hSearch);
    if(SUCCEEDED(hr))
    {
        // Get the first row of results.
        hr = pSchemaNC->GetFirstRow(hSearch);

        while(S_OK == hr)
        {
            ADS_SEARCH_COLUMN col;

            // Print each column.
            for(DWORD i = 0; i < dwAttributes; i++)
            {
                hr = pSchemaNC->GetColumn(hSearch, rgpwszAttributes[i], &col);
                if(SUCCEEDED(hr))
                {
                    // Print the data for the column and free the column.
                    if (col.dwADsType == ADSTYPE_CASE_IGNORE_STRING)
                    {
                        wprintf(L"%s:", rgpwszAttributes[i]); 

                        // Print each attribute value.
                        for(DWORD x = 0; x < col.dwNumValues; x++)
                        {
                            wprintf(L"\t%s\n", col.pADsValues[x].CaseIgnoreString); 
                        }
                    }
                    else
                    {
                        wprintf(L"<%s property is not a string>", rgpwszAttributes[0]);
                    }
                    
                    // Free the column.
                    pSchemaNC->FreeColumn(&col);
                }
            }

            // Get the next set of results.
            hr = pSchemaNC->GetNextRow(hSearch);
        }

        // Close the search handle to cleanup.
        pSchemaNC->CloseSearchHandle(hSearch);
    } 

    return hr;
}
```



The following C and C++ code example shows how to search for schema objects replicated to the global catalog.


```C++
#include <stdio.h>
#include <atlbase.h>
#include <activeds.h>
#include <ntldap.h>

/***************************************************************************

    PrintGCAttributes()

    Searches for and prints all attributeSchema objects replicated 
    to the global catalog.

    Parameters:
    
    pSchemaNC - IDirectorySearch pointer to schema naming context.
    
***************************************************************************/

HRESULT PrintGCAttributes(IDirectorySearch *pSchemaNC)
{
    HRESULT hr;

    // Attributes are one-level deep in the Schema container, so only search one level.
    ADS_SEARCHPREF_INFO SearchPrefs[2];
    SearchPrefs[0].dwSearchPref = ADS_SEARCHPREF_SEARCH_SCOPE;
    SearchPrefs[0].vValue.dwType = ADSTYPE_INTEGER;
    SearchPrefs[0].vValue.Integer = ADS_SCOPE_ONELEVEL;
 
    // Use paging if there are more properties than can be returned by one page.
    SearchPrefs[1].dwSearchPref = ADS_SEARCHPREF_PAGESIZE;
    SearchPrefs[1].vValue.dwType = ADSTYPE_INTEGER;
    SearchPrefs[1].vValue.Integer = 1000;

    // Set the search preferences.
    hr = pSchemaNC->SetSearchPreference(SearchPrefs, sizeof(SearchPrefs)/sizeof(ADS_SEARCHPREF_INFO));
    if(FAILED(hr))
    {
        return hr;
    }
 
    // Handle used for search.
    ADS_SEARCH_HANDLE hSearch;
 
    LPWSTR rgpwszAttributes[] = {L"cn"};
    DWORD dwAttributes = sizeof(rgpwszAttributes)/sizeof(LPWSTR);

    // Create the search filter.
    LPWSTR pwszSearchFilter = L"(&(objectCategory=attributeSchema)(isMemberOfPartialAttributeSet=TRUE))";
 
    // Execute the search.
    hr = pSchemaNC->ExecuteSearch(pwszSearchFilter,
                                  rgpwszAttributes,
                                  dwAttributes,
                                  &hSearch);
    if(SUCCEEDED(hr))
    {
        // Get the first row of results.
        hr = pSchemaNC->GetFirstRow(hSearch);

        while(S_OK == hr)
        {
            ADS_SEARCH_COLUMN col;

            // Print each column.
            for(DWORD i = 0; i < dwAttributes; i++)
            {
                hr = pSchemaNC->GetColumn(hSearch, rgpwszAttributes[i], &col);
                if(SUCCEEDED(hr))
                {
                    // Print the data for the column and free the column.
                    if (col.dwADsType == ADSTYPE_CASE_IGNORE_STRING)
                    {
                        wprintf(L"%s:", rgpwszAttributes[i]); 

                        // Print each attribute value.
                        for(DWORD x = 0; x < col.dwNumValues; x++)
                        {
                            wprintf(L"\t%s\n", col.pADsValues[x].CaseIgnoreString); 
                        }
                    }
                    else
                    {
                        wprintf(L"<%s property is not a string>", rgpwszAttributes[0]);
                    }
                    
                    // Free the column.
                    pSchemaNC->FreeColumn(&col);
                }
            }

            // Get the next set of results.
            hr = pSchemaNC->GetNextRow(hSearch);
        }

        // Close the search handle to cleanup.
        pSchemaNC->CloseSearchHandle(hSearch);
    } 

    return hr;
}
```



The following C and C++ code example shows how to search for indexed schema objects.


```C++
#include <stdio.h>
#include <atlbase.h>
#include <activeds.h>
#include <ntldap.h>

/***************************************************************************

    PrintIndexedAttributes()

    Searches for, and prints, all indexed attributeSchema objects.

    Parameters:

    pSchemaNC - IDirectorySearch pointer to schema naming context.

***************************************************************************/

HRESULT PrintIndexedAttributes(IDirectorySearch *pSchemaNC)
{
    HRESULT hr;

    // Attributes are one-level deep in the Schema container, so only search one level.
    ADS_SEARCHPREF_INFO SearchPrefs[2];
    SearchPrefs[0].dwSearchPref = ADS_SEARCHPREF_SEARCH_SCOPE;
    SearchPrefs[0].vValue.dwType = ADSTYPE_INTEGER;
    SearchPrefs[0].vValue.Integer = ADS_SCOPE_ONELEVEL;
 
    // Use paging in the case that there are more properties than can be returned by one page.
    SearchPrefs[1].dwSearchPref = ADS_SEARCHPREF_PAGESIZE;
    SearchPrefs[1].vValue.dwType = ADSTYPE_INTEGER;
    SearchPrefs[1].vValue.Integer = 1000;

    // Set the search preferences.
    hr = pSchemaNC->SetSearchPreference(SearchPrefs, sizeof(SearchPrefs)/sizeof(ADS_SEARCHPREF_INFO));
    if(FAILED(hr))
    {
        return hr;
    }
 
    // Handle used for search.
    ADS_SEARCH_HANDLE hSearch;
 
    LPWSTR rgpwszAttributes[] = {L"cn"};
    DWORD dwAttributes = sizeof(rgpwszAttributes)/sizeof(LPWSTR);

    /*
    Create the search filter. Indexed attributes have the least significant bit 
    of the searchFlags attribute set to 1.
    */
    CComBSTR sbstrSearchFilter;    
    sbstrSearchFilter = "(&(objectCategory=attributeSchema)(searchFlags:";
    sbstrSearchFilter += LDAP_MATCHING_RULE_BIT_AND;
    sbstrSearchFilter += ":=1))";
 
    // Execute the search.
    hr = pSchemaNC->ExecuteSearch(sbstrSearchFilter,
                                  rgpwszAttributes,
                                  dwAttributes,
                                  &hSearch);
    if(SUCCEEDED(hr))
    {
        // Get the first row of results.
        hr = pSchemaNC->GetFirstRow(hSearch);

        while(S_OK == hr)
        {
            ADS_SEARCH_COLUMN col;

            // Print each column.
            for(DWORD i = 0; i < dwAttributes; i++)
            {
                hr = pSchemaNC->GetColumn(hSearch, rgpwszAttributes[i], &col);
                if(SUCCEEDED(hr))
                {
                    // Print the data for the column and free the column.
                    if (col.dwADsType == ADSTYPE_CASE_IGNORE_STRING)
                    {
                        wprintf(L"%s:", rgpwszAttributes[i]); 

                        // Print each attribute value.
                        for(DWORD x = 0; x < col.dwNumValues; x++)
                        {
                            wprintf(L"\t%s\n", col.pADsValues[x].CaseIgnoreString); 
                        }
                    }
                    else
                    {
                        wprintf(L"<%s property is not a string>", rgpwszAttributes[0]);
                    }
                    
                    // Free the column.
                    pSchemaNC->FreeColumn(&col);
                }
            }

            // Get the next set of results.
            hr = pSchemaNC->GetNextRow(hSearch);
        }

        // Close the search handle to cleanup.
        pSchemaNC->CloseSearchHandle(hSearch);
    } 

    return hr;
}
```



 

 




