---
title: Example Code for Ranging with IDirectorySearch
description: The following code example uses ranging to retrieve the members of a group using the IDirectorySearch interface.
ms.assetid: 13aba22f-c649-4dda-804f-01ba493cd6d7
ms.tgt_platform: multiple
keywords:
- Example Code for Ranging with IDirectorySearch ADSI
- Range Retrieval ADSI , Example code, Using IDirectorySearch
ms.topic: article
ms.date: 05/31/2018
---

# Example Code for Ranging with IDirectorySearch

The following code example uses ranging to retrieve the members of a group using the [**IDirectorySearch**](/windows/desktop/api/Iads/nn-iads-idirectorysearch) interface.


```C++
HRESULT EnumGroupWithIDirectorySearch(LPCWSTR pwszGroupDN, 
                                      LPCWSTR pwszUsername, 
                                      LPCWSTR pwszPassword)
{
    if(NULL == pwszGroupDN)
    {
        return E_POINTER;
    }
    
    HRESULT hr;
    IDirectorySearch *pSearch;

    hr = ADsOpenObject( pwszGroupDN,
                        pwszUsername,
                        pwszPassword,
                        ADS_SECURE_AUTHENTICATION,
                        IID_IDirectorySearch, 
                        (void**)&pSearch);

    if(SUCCEEDED(hr))
    {
        const DWORD dwStep = 1000;
        DWORD dwLowRange;
        DWORD dwHighRange;
        BOOL fLastQuery;
        BOOL fExit;

        // Only search for properties of this object.
        ADS_SEARCHPREF_INFO rgSearchPrefs[1];
        rgSearchPrefs[0].dwSearchPref = ADS_SEARCHPREF_SEARCH_SCOPE;
        rgSearchPrefs[0].vValue.dwType = ADSTYPE_INTEGER;
        rgSearchPrefs[0].vValue.Integer = ADS_SCOPE_BASE;

        // Set the search preference.
        hr = pSearch->SetSearchPreference(rgSearchPrefs, 1);
        if (FAILED(hr))
        {
            return hr;
        }

        dwLowRange = 0;
        dwHighRange = dwLowRange + (dwStep - 1);

        // Set the search filter.
        LPWSTR pszSearch = L"(CN=*)";

        fLastQuery = FALSE;
        fExit = FALSE;

        do
        {
            WCHAR wszName[] = L"name";
            WCHAR wszAttribute[MAX_PATH];
            ADS_SEARCH_HANDLE hSearch;

            if(fLastQuery)
            {
                // Perform this query with the "range=<lowRange>-*" range.
                swprintf_s(wszAttribute, L"member;range=%d-*", dwLowRange);
            }
            else
            {
                // Perform this query with the "range=<lowRange>-<highRange>" range.
                swprintf_s(wszAttribute, L"member;range=%d-%d", dwLowRange, dwHighRange);
            }
  
            OutputDebugStringW(L"Query:");
            OutputDebugStringW(wszAttribute);
            OutputDebugStringW(L"\n");

            LPWSTR rgAttributes[2] = {wszName, wszAttribute};

            // Execute the query.
            hr = pSearch->ExecuteSearch(pszSearch, rgAttributes, 2, &hSearch);
            if(SUCCEEDED(hr))
            {
                // Enumerate the rows.
                while(SUCCEEDED(hr = pSearch->GetNextRow(hSearch)))
                {
                    if(S_OK == hr)
                    {
                        LPWSTR pwszColumnName;
                        hr = pSearch->GetNextColumnName(hSearch, &pwszColumnName);
                        if(SUCCEEDED(hr))
                        {
                            /*
                            If the column name retrieved from the server is 
                            different than the query string, this indicates that 
                            last range requested was beyond the range of 
                            property values. Perform one last query with the 
                            "range=<lowRange>-*" range.
                            */
                            if(0 != lstrcmpiW(pwszColumnName, wszAttribute))
                            {
                                if(fLastQuery)
                                {
                                    /*
                                    The request failed to retrieve the attribute in
                                    two of two attempts. This will occur if the group has
                                    no members. Exit the loop to avoid an infinite loop
                                    condition.
                                    */
                                    fExit = TRUE;
                                }

                                fLastQuery = TRUE;

                                FreeADsMem(pwszColumnName);

                                break;
                            }
                            else
                            {
                                ADS_SEARCH_COLUMN col;
                                
                                // Get the column.
                                hr = pSearch->GetColumn(hSearch, pwszColumnName, &col);
                                if(SUCCEEDED(hr))
                                {
                                    DWORD i;

                                    // Enumerate the retrieved property values.
                                    for(i = 0; i < col.dwNumValues; i++)
                                    {
                                        wprintf(L"%s\n", col.pADsValues[i].CaseIgnoreString);
                                    }

                                    // Free the column.
                                    pSearch->FreeColumn(&col);
                                }

                                FreeADsMem(pwszColumnName);

                                if(fLastQuery)
                                {
                                    /*
                                    The last query was just completed, so exit the loop.
                                    */
                                    fExit = TRUE;
                                    break;
                                }
                            }
                        }
                    }
                    else if(S_ADS_NOMORE_ROWS == hr)
                    {
                        /*
                        Call ADsGetLastError to verify that the search is waiting 
                        for a response to a previous query.
                        */
                        DWORD dwError = ERROR_SUCCESS;
                        WCHAR szError[512];
                        WCHAR szProvider[512];
                            
                        ADsGetLastError(&dwError, szError, 512, szProvider, 512);
                        if(ERROR_MORE_DATA != dwError)
                        {
                            break;
                        }
                        /*
                        The search is waiting for a response to a previous 
                        query. Call GetNextRow again.
                        */
                    }
                    else
                    {
                        break;
                    }

                }

                // Close the search handle to cleanup.
                pSearch->CloseSearchHandle(hSearch);

                // If the last query was performed, exit the loop.
                if(!fLastQuery)
                {
                    // Increment the high and low ranges to query for the next block of objects.
                    dwLowRange = dwHighRange + 1;
                    dwHighRange = dwLowRange + (dwStep - 1);
                }
            }
        }while(!fExit);

        pSearch->Release();
    }

    return hr;
}
```



 

 




