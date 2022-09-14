---
title: Performing an Attribute Scope Query
description: The attribute scope query is a search preference that enables a search of an object's distinguished name valued attributes to be performed.
ms.assetid: 026fbe17-5df7-4007-9d74-5c0abbe793b1
ms.tgt_platform: multiple
keywords:
- Performing an Attribute Scope Query ADSI
- ADSI, Searching, IDirectorySearch, Other Search Options, Attribute Scope Query
ms.topic: article
ms.date: 05/31/2018
---

# Performing an Attribute Scope Query

The attribute scope query is a search preference that enables a search of an object's distinguished name valued attributes to be performed. The attribute to search can be either single or multi-valued, but must be of the **ADS\_DN\_STRING** type. When the search is performed, ADSI will enumerate the distinguished name values of the attribute and perform the search on the objects represented by the distinguished names. For example, if an attribute scoped search is performed of the [**member**](/windows/desktop/ADSchema/a-member) attribute of a group object, ADSI will enumerate the distinguished names in the **member** attribute and search each of the members of the group for the specified search criteria.

If an attribute scoped query is performed on an attribute that is not of type **ADS\_DN\_STRING**, the search will fail. The attribute scoped query also requires that the **ADS\_SEARCHPREF\_SEARCH\_SCOPE** preference be set to **ADS\_SCOPE\_BASE**. The **ADS\_SEARCHPREF\_SEARCH\_SCOPE** preference will automatically be set to **ADS\_SCOPE\_BASE**, but if the **ADS\_SEARCHPREF\_SEARCH\_SCOPE** preference is set to any other value, [**IDirectorySearch::SetSearchPreference**](/windows/desktop/api/Iads/nf-iads-idirectorysearch-setsearchpreference) will fail with **E\_ADS\_BAD\_PARAMETER**.

The results of an attribute-scope query may span multiple servers and a server may not return all the data requested for the all the rows returned. If this occurs, when the last row is retrieved by calling [**IDirectorySearch::GetNextRow**](/windows/desktop/api/Iads/nf-iads-idirectorysearch-getnextrow) or [**IDirectorySearch::GetFirstRow**](/windows/desktop/api/Iads/nf-iads-idirectorysearch-getfirstrow), ADSI will return **S\_ADS\_ERRORSOCCURRED** instead of **S\_ADS\_NOMORE\_ROWS**.

To specify an attribute scope query, set an **ADS\_SEARCHPREF\_ATTRIBUTE\_QUERY** search option with an **ADSTYPE\_CASE\_IGNORE\_STRING** value set to the lDAPDisplayName of the attribute to search in the [**ADS\_SEARCHPREF\_INFO**](/windows/desktop/api/Iads/ns-iads-ads_searchpref_info) array passed to the [**IDirectorySearch::SetSearchPreference**](/windows/desktop/api/Iads/nf-iads-idirectorysearch-setsearchpreference) method. This operation is shown in the following code example.


```C++
ADS_SEARCHPREF_INFO SearchPref;
SearchPref.dwSearchPref = ADS_SEARCHPREF_ATTRIBUTE_QUERY;
SearchPref.vValue.dwType = ADSTYPE_CASE_IGNORE_STRING;
SearchPref.vValue.Boolean = L"member";
```



The following code example shows how to use the **ADS\_SEARCHPREF\_ATTRIBUTE\_QUERY** search option.


```C++
/***************************************************************************

    SearchGroupMembers()

    Searches the members of a group that are of type user and prints each 
    user's cn and distinguishedName values to the console.

    Parameters:

    pwszGroupDN - Contains the distinguished name of the group whose 
    members will be searched.

***************************************************************************/

HRESULT SearchGroupMembers(LPCWSTR pwszGroupDN)
{
    HRESULT hr;
    CComPtr<IDirectorySearch> spSearch;
    CComBSTR sbstrADsPath;
 
    // Bind to the group and get the IDirectorySearch interface.
    sbstrADsPath = "LDAP://";
    sbstrADsPath += pwszGroupDN;
    hr = ADsOpenObject(sbstrADsPath,
        NULL,
        NULL,
        ADS_SECURE_AUTHENTICATION,
        IID_IDirectorySearch,
        (void**)&spSearch);
    if(FAILED(hr))
    {
        return hr;
    }
 
    ADS_SEARCHPREF_INFO SearchPrefs[1];

    // Set the ADS_SEARCHPREF_ATTRIBUTE_QUERY search preference.
    SearchPrefs[0].dwSearchPref = ADS_SEARCHPREF_ATTRIBUTE_QUERY;
    SearchPrefs[0].vValue.dwType = ADSTYPE_CASE_IGNORE_STRING;
    SearchPrefs[0].vValue.CaseIgnoreString = L"member";

    // Set the search preferences.
    hr = spSearch->SetSearchPreference(SearchPrefs, sizeof(SearchPrefs)/sizeof(ADS_SEARCHPREF_INFO));
    if(FAILED(hr))
    {
        return hr;
    }

    ADS_SEARCH_HANDLE hSearch;
    
    // Create the search filter.
    LPWSTR pwszSearchFilter = L"(&(objectClass=user))";
 
    // Set attributes to return.
    LPWSTR rgpwszAttributes[] = {L"cn", L"distinguishedName"};
    DWORD dwNumAttributes = sizeof(rgpwszAttributes)/sizeof(LPWSTR);
 
    // Execute the search.
    hr = spSearch->ExecuteSearch(pwszSearchFilter,
        rgpwszAttributes,
        dwNumAttributes,
        &hSearch);
    if(FAILED(hr))
    {
        return hr;
    }

    // Get the first result row.
    hr = spSearch->GetFirstRow(hSearch);
    while(S_OK == hr)
    {
        ADS_SEARCH_COLUMN col;

        // Enumerate the retrieved attributes.
        for(DWORD i = 0; i < dwNumAttributes; i++)
        {
            hr = spSearch->GetColumn(hSearch, rgpwszAttributes[i], &col);
            if(SUCCEEDED(hr))
            {
                switch(col.dwADsType)
                {
                case ADSTYPE_DN_STRING:
                    wprintf(L"%s: %s\n\n", rgpwszAttributes[i], col.pADsValues[0].DNString);
                    break;

                case ADSTYPE_CASE_IGNORE_STRING:
                    wprintf(L"%s: %s\n\n", rgpwszAttributes[i], col.pADsValues[0].CaseExactString);
                    break;

                default:
                    break;
                }
                
                // Free the column.
                spSearch->FreeColumn(&col);
            }
        }
        
        // Get the next row.
        hr = spSearch->GetNextRow(hSearch);
    }

    // Close the search handle to cleanup.
    hr = spSearch->CloseSearchHandle(hSearch);

    return hr;
}
```



When this search is executed and the results are enumerated, it would return the **name**, **telephone number**, and **office number** of all of the user objects contained in the group's **member** attribute list.

Error handling: The results of an attribute-scope query may span multiple servers and a server may not return all the data requested for the all the rows returned. If this occurs, when the last row is retrieved by calling [**GetNextRow**](/windows/desktop/api/Iads/nf-iads-idirectorysearch-getnextrow) or [**GetFirstRow**](/windows/desktop/api/Iads/nf-iads-idirectorysearch-getfirstrow), ADSI will return **S\_ADS\_ERRORSOCCURRED**, instead of **S\_ADS\_NOMORE\_ROWS**.

 

 