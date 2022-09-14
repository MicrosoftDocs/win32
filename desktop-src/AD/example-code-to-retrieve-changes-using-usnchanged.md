---
title: Example Code to Retrieve Changes Using USNChanged
description: The following code example uses the uSNChanged attribute of an object in Active Directory Domain Services to retrieve changes since a previous query.
ms.assetid: 519fd20f-9eb4-4702-9338-8cda899604bd
ms.tgt_platform: multiple
keywords:
- Active Directory examples Active Directory , retrieving changes using USNChanged
ms.topic: article
ms.date: 05/31/2018
---

# Example Code to Retrieve Changes Using USNChanged

The following code example uses the **uSNChanged** attribute of an object in Active Directory Domain Services to retrieve changes since a previous query. The code example can perform either a full synchronization or an incremental update. For a full synchronization, the sample application connects to the rootDSE of a domain controller and reads the following parameters that it stores to be used in the next incremental synchronization:

-   The DNS name of the DC. Incremental synchronizations must be performed on the same DC as the previous synchronization.
-   The **invocationID** GUID of the DC. The code example uses this value to detect that the DC has been restored from a backup, in which case, the sample must perform a full synchronization.
-   The **highestCommittedUSN**. This value becomes the lower bound for the **uSNChanged** filter on the next incremental synchronization.

The code example uses the [**IDirectorySearch**](/windows/desktop/api/iads/nn-iads-idirectorysearch) interface, specifying the distinguished name of the base of the search, a search scope, and a filter. There are no restrictions on the search base or scope. In addition to specifying the objects of interest, the filter must also specify a **uSNChanged** comparison, such as "uSNChanged >= \<lower bound USN\>". For a full synchronization, "&lt;lower bound USN&gt;" is zero. For an incremental synchronization, it is the 1 plus the **highestCommittedUSN** value from the previous search.

Be aware that this sample application is intended only to show how to use **uSNChanged** to retrieve changes from the Active Directory server. It prints the changes and does not actually synchronize the data in a secondary storage. Consequently, it does not show how to handle issues like moved objects or "no parent" conditions. It does show how to retrieve deleted objects, but it does not show how an application uses the **objectGUID** of the deleted objects to determine the corresponding object to delete in the storage.

Also, the sample caches the DC name, **invocationID**, and **highestCommittedUSN** in the registry. In a real synchronization application, you must store the parameters in the same storage that are kept consistent with the Active Directory server. This ensures that the parameters and object data remain synchronized if your database is ever restored from a backup.


```C++
#include <windows.h>
#include <stdio.h>
#include <activeds.h>
#include <ntdsapi.h>
#include <atlbase.h>

#pragma comment(lib, "activeds")
#pragma comment(lib, "adsiid")

typedef struct _MYUSERDATA
{
    WCHAR objectGUID[40];
    WCHAR distinguishedName[MAX_PATH];
    WCHAR phoneNumber[32];
} MYUSERDATA, *PMYUSERDATA;

#define ARRAYSIZE(__buf__) (sizeof(__buf__)/sizeof(__buf__[0]))

// Forward declaration
VOID BuildGUIDString(WCHAR *szGUID, LPBYTE pGUID); VOID WriteObjectDataToStorage(PMYUSERDATA pUserData, BOOL bUpdate); VOID DeleteObjectDataFromStorage(PMYUSERDATA pUserData);

//********************************************************************
// DoUSNSyncSearch
//********************************************************************
HRESULT DoUSNSyncSearch(
    LPWSTR pszSearchBaseDN,      // Distinguished name of search base
    ULONG ulScope,               // Scope of the search
    LPWSTR *pAttributeNames,     // Attributes to retrieve
    DWORD dwAttributes,          // Number of attributes
    LPWSTR pszPrevInvocationID,  // GUID string for DC's invocationID
    LPWSTR pszPrevHighUSN,       // Highest USN from previous sync
    LPWSTR pszDC)                // Name of DC to bind to
{
    LPWSTR pszServerPath = NULL;
    LPWSTR pszDSPath = NULL;
    IADs *pRootDSE = NULL;
    IADs *pDCService = NULL;
    IADs *pDeletedObj = NULL;
    IDirectorySearch *pSearch = NULL;
    ADS_SEARCH_HANDLE hSearch = NULL;
    ADS_SEARCHPREF_INFO arSearchPrefs[3];
    WCHAR szSearchFilter[256];    // Search filter
    ADS_SEARCH_COLUMN col;
    MYUSERDATA userdata;
    void HUGEP *pArray;
    WCHAR szGUID[40];
    INT64 iLowerBoundUSN;
    HRESULT hr = E_FAIL;
    DWORD dwCount = 0;
    VARIANT var;
    BOOL bUpdate = TRUE;

    // Validate input parameters.
    if (!pszPrevInvocationID || !pszPrevHighUSN || !pszDC)
    {
        wprintf(L"Invalid parameter.\n");
        return E_INVALIDARG;
    }

    VariantInit(&var);

    // Allocate the server path string buffer.
    pszServerPath = new WCHAR[7 + wcslen(pszDC) + 1 + 1];
    if(!pszServerPath)
    {
        wprintf(L"failed to allocate memory");
        hr = E_OUTOFMEMORY;
        goto cleanup;
    }

    // If there exists a DC name from the previous USN synchronization,
    // include it in the binding string.
    if (pszDC[0])
    {
        wcscpy_s(pszServerPath, L"LDAP://");
        wcscat_s(pszServerPath, pszDC);
        wcscat_s(pszServerPath, L"/");
    }
    else
    {
        wcscpy_s(pszServerPath, L"LDAP://");
    }

    // Allocate the DS path string buffer.
    pszDSPath = new WCHAR[wcslen(pszServerPath) + 7 + 1];
    if(!pszDSPath)
    {
        wprintf(L"failed to allocate memory");
        hr = E_OUTOFMEMORY;
        goto cleanup;
    }

    // Bind to the root DSE.
    wcscpy_s(pszDSPath, pszServerPath);
    wcscat_s(pszDSPath, L"rootDSE");
    hr = ADsOpenObject(pszDSPath,
                    NULL,
                    NULL,
                    ADS_SECURE_AUTHENTICATION,
                    IID_IADs,
                    (void**)&pRootDSE);
    if (FAILED(hr))
    {
        wprintf(L"failed to bind to root: 0x%x\n", hr);
        goto cleanup;
    }

    // Get the name of the DC connected to.
    hr = pRootDSE->Get(CComBSTR("DnsHostName"), &var);
    if (FAILED(hr))
    {
        wprintf(L"failed to get DnsHostName: 0x%x\n", hr);
        goto cleanup;
    }

    // Compare it to the DC name from the previous USN sync operation.
    // If not the same, perform a full synchronization.
    if (_wcsicmp(pszDC, var.bstrVal) != 0)
    {
        bUpdate = FALSE;
        // This prevents a full sync being performed
        // EVERY time
        wcscpy_s( pszDC, var.bstrVal );

        // Reallocate the string buffer.
        delete[] pszServerPath;
        pszServerPath = new WCHAR[7 + wcslen(var.bstrVal) + 1 + 1];
        if(!pszServerPath)
        {
            wprintf(L"failed to allocate memory");
            hr = E_OUTOFMEMORY;
            goto cleanup;
        }

        // Use the DC name in the bind string prefix.
        wcscpy_s(pszServerPath, L"LDAP://");
        wcscat_s(pszServerPath, var.bstrVal);
        wcscat_s(pszServerPath, L"/");
    }

    // Bind to the DC service object to get the invocationID.
    // The dsServiceName property of root DSE contains the distinguished
    // name of this DC service object.
    VariantClear(&var);
    hr = pRootDSE->Get(CComBSTR("dsServiceName"), &var);
    if (FAILED(hr))
    {
        wprintf(L"failed to get \"dsServiceName\"\n");
        goto cleanup;
    }

    // Reallocate the DS path buffer.
    delete[] pszDSPath;
    pszDSPath = new WCHAR[wcslen(pszServerPath) + wcslen(var.bstrVal) + 1];
    if(!pszDSPath)
    {
        wprintf(L"failed to allocate memory");
        hr = E_OUTOFMEMORY;
        goto cleanup;
    }

    wcscpy_s(pszDSPath, pszServerPath);
    wcscat_s(pszDSPath, var.bstrVal);
    hr = ADsOpenObject(pszDSPath,
                    NULL,
                    NULL,
                    ADS_SECURE_AUTHENTICATION,
                    IID_IADs,
                    (void**)&pDCService);
    VariantClear(&var);
    if (FAILED(hr))
    {
        wprintf(L"failed to bind to the DC service object: 0x%x\n", hr);
        goto cleanup;
    }

    // Get the invocationID GUID from the service object.
    hr = pDCService->Get(CComBSTR("invocationID"), &var);
    if (FAILED(hr))
    {
        wprintf(L"failed to get \"invocationID\"\n");
        goto cleanup;
    }

    hr = SafeArrayAccessData((SAFEARRAY*)(var.pparray), (void HUGEP* FAR*)&pArray);
    if (FAILED(hr))
    {
        wprintf(L"failed to get hugep: 0x%x\n", hr);
        goto cleanup;
    }

    BuildGUIDString(szGUID, (LPBYTE)pArray);
    VariantClear(&var);

    // Compare the invocationID GUID to the GUID string from the previous
    // synchronization. If not the same, this is a different DC or the DC
    // was restored from backup; perform a full synchronization.
    if (_wcsicmp(szGUID, pszPrevInvocationID)!=0)
    {
        bUpdate = FALSE;
        wcscpy_s(pszPrevInvocationID, szGUID);  // Save the invocationID GUID.
    }

    // If previous high USN is an empty string, handle this as a full synchronization.
    bUpdate = (pszPrevHighUSN[0] != '\0');

    // Set the lower bound USN to zero if this is a full synchronization.
    // Otherwise, set it to the previous high USN plus one.
    if (bUpdate == FALSE)
    {
        iLowerBoundUSN = 0;
    }
    else
    {
        iLowerBoundUSN = _wtoi64(pszPrevHighUSN) + 1; // Convert the string to an integer.
    }

    // Get and save the current high USN.
    hr = pRootDSE->Get(CComBSTR("highestCommittedUSN"), &var);
    if (FAILED(hr))
    {
        wprintf(L"failed to get \"highestCommittedUSN\"\n");
        goto cleanup;
    }

    wcscpy_s(pszPrevHighUSN, var.bstrVal);
    wprintf(L"current highestCommittedUSN: %s\n", pszPrevHighUSN);
    VariantClear(&var);

    // Reallocate the DS path buffer.
    delete[] pszDSPath;
    pszDSPath = new WCHAR[wcslen(pszServerPath) + wcslen(pszSearchBaseDN) + 1];
    if(!pszDSPath)
    {
        wprintf(L"failed to allocate memory");
        hr = E_OUTOFMEMORY;
        goto cleanup;
    }

    // Get an IDirectorySearch pointer to the base of the search.
    wcscpy_s(pszDSPath, pszServerPath);
    wcscat_s(pszDSPath, pszSearchBaseDN);
    hr = ADsOpenObject(pszDSPath,
                    NULL,
                    NULL,
                    ADS_SECURE_AUTHENTICATION,
                    IID_IDirectorySearch,
                    (void**)&pSearch);
    if (FAILED(hr))
    {
        wprintf(L"failed to get IDirectorySearch: 0x%x\n", hr);
        goto cleanup;
    }

    // Set up the scope and page size search preferences.
    arSearchPrefs [0].dwSearchPref = ADS_SEARCHPREF_SEARCH_SCOPE;
    arSearchPrefs [0].vValue.dwType = ADSTYPE_INTEGER;
    arSearchPrefs [0].vValue.Integer = ulScope;

    arSearchPrefs [1].dwSearchPref = ADS_SEARCHPREF_PAGESIZE;
    arSearchPrefs [1].vValue.dwType = ADSTYPE_INTEGER;
    arSearchPrefs [1].vValue.Integer = 100;

    hr = pSearch->SetSearchPreference(arSearchPrefs, 2);
    if (FAILED(hr))
    {
        wprintf(L"failed to set search prefs: 0x%x\n", hr);
        goto cleanup;
    }

    // The search filter specifies the objects to monitor
    // and the USNChanged value to exceed.
    swprintf_s(szSearchFilter,

L"(&(objectClass=user)(objectCategory=person)(uSNChanged>=%I64d))",
            iLowerBoundUSN );

    // Search for the objects indicated by the search filter.
    hr = pSearch->ExecuteSearch(szSearchFilter,
                        pAttributeNames, dwAttributes, &hSearch );
    if (FAILED(hr))
    {
        wprintf(L"failed to set execute search: 0x%x\n", hr);
        goto cleanup;
    }

    // Loop through the rows of the search result. Each row is an object
    // with USNChanged greater than or equal to the specified value.
    hr = pSearch->GetNextRow(hSearch);
    while ( SUCCEEDED(hr) && hr != S_ADS_NOMORE_ROWS )
    {
        ZeroMemory(&userdata, sizeof(MYUSERDATA));

        // Get the distinguishedName.
        hr = pSearch->GetColumn(hSearch, L"distinguishedName", &col);
        if ( SUCCEEDED(hr) )
        {
            if (col.dwADsType == ADSTYPE_DN_STRING && col.pADsValues)
            {
                wcscpy_s(userdata.distinguishedName,
col.pADsValues->DNString);
            }

            pSearch->FreeColumn( &col );
        }

        // Get the telephone number.
        hr = pSearch->GetColumn( hSearch, L"telephoneNumber", &col );
        if ( SUCCEEDED(hr) )
        {
            if (col.dwADsType == ADSTYPE_CASE_IGNORE_STRING &&
col.pADsValues)
            {
                wcscpy_s(userdata.phoneNumber, col.pADsValues->CaseIgnoreString);
            }

            pSearch->FreeColumn( &col );
        }

        // Get the objectGUID.
        hr = pSearch->GetColumn( hSearch, L"objectGUID", &col );
        if ( SUCCEEDED(hr) )
        {
            if ((col.dwADsType == ADSTYPE_OCTET_STRING) && col.pADsValues &&
                (col.pADsValues->OctetString.lpValue))
            {
                BuildGUIDString(szGUID, (LPBYTE) col.pADsValues->OctetString.lpValue);
                wcscpy_s(userdata.objectGUID, szGUID);
            }

            pSearch->FreeColumn( &col );
        }

        // Write the data from Active Directory to the secondary storage.
        WriteObjectDataToStorage(&userdata, bUpdate);
        dwCount++;
        hr = pSearch->GetNextRow( hSearch);
    }

    wprintf(L"dwCount: %d\n", dwCount);

    // If this is a full synchronization, the operation is complete.
    if (!bUpdate)
    {
        goto cleanup;
    }

    // If it is an update, search for deleted objects.

    // Release the search handle and pointer to reuse them.
    wprintf(L"Searching for deleted objects\n");
    if (hSearch)
    {
        pSearch->CloseSearchHandle(hSearch);
        hSearch = NULL;
    }
    if (pSearch)
    {
        pSearch->Release();
        pSearch = NULL;
    }

    // Bind to the Deleted Objects container.
    hr = pRootDSE->Get(CComBSTR("defaultNamingContext"), &var);
    if (FAILED(hr))
    {
        wprintf(L"failed to get \"defaultNamingContext\"\n");
        goto cleanup;
    }

    LPWSTR pwszFilter = L"%s<WKGUID=%s,%s>";

    // Reallocate the DS path buffer.
    delete[] pszDSPath;
    pszDSPath = new WCHAR[  wcslen(pwszFilter) +
                            wcslen(pszServerPath) +
                            wcslen(GUID_DELETED_OBJECTS_CONTAINER_W) +
                            wcslen(var.bstrVal) +
                            1];
    if(!pszDSPath)
    {
        wprintf(L"failed to allocate memory");
        hr = E_OUTOFMEMORY;
        goto cleanup;
    }

    swprintf_s(   pszDSPath, pwszFilter,
                pszServerPath,
                GUID_DELETED_OBJECTS_CONTAINER_W,
                var.bstrVal);
    VariantClear(&var);

    hr = ADsOpenObject(pszDSPath,
                    NULL,
                    NULL,
                    ADS_SECURE_AUTHENTICATION | ADS_FAST_BIND,
                    IID_IDirectorySearch,
                    (void**)&pSearch);
    if (FAILED(hr))
    {
        wprintf(L"failed to get IDirectorySearch: 0x%x\n", hr);
        goto cleanup;
    }

    // Specify the scope, pagesize, and tombstone search preferences.
    arSearchPrefs[0].dwSearchPref = ADS_SEARCHPREF_SEARCH_SCOPE;
    arSearchPrefs[0].vValue.dwType = ADSTYPE_INTEGER;
    arSearchPrefs[0].vValue.Integer = ADS_SCOPE_SUBTREE;

    arSearchPrefs[1].dwSearchPref = ADS_SEARCHPREF_PAGESIZE;
    arSearchPrefs[1].vValue.dwType = ADSTYPE_INTEGER;
    arSearchPrefs[1].vValue.Integer = 100;

    arSearchPrefs[2].dwSearchPref = ADS_SEARCHPREF_TOMBSTONE;
    arSearchPrefs[2].vValue.dwType = ADSTYPE_BOOLEAN;
    arSearchPrefs[2].vValue.Boolean = TRUE;

    hr = pSearch->SetSearchPreference(arSearchPrefs, 3);
    if (FAILED(hr))
    {
        wprintf(L"failed to set search prefs: 0x%x\n", hr);
        goto cleanup;
    }

    // Set up the search filter.
    swprintf_s(szSearchFilter,
            L"(&(isDeleted=TRUE)(uSNChanged>=%I64d))",
            iLowerBoundUSN );

    // Execute the search.
    hr = pSearch->ExecuteSearch(szSearchFilter,
                        pAttributeNames, dwAttributes, &hSearch );
    if (FAILED(hr))
    {
        wprintf(L"failed to set execute search: 0x%x\n", hr);
        goto cleanup;
    }
    wprintf(L"Started search for deleted objects.\n");

    // Loop through the rows of the search result.
    // Each row is an object deleted since the previous call.
    dwCount = 0;
    hr = pSearch->GetNextRow(hSearch);
    while ( SUCCEEDED(hr) && hr != S_ADS_NOMORE_ROWS )
    {
        ZeroMemory(&userdata, sizeof(MYUSERDATA) );

        // Get the distinguishedName.
        hr = pSearch->GetColumn(hSearch, L"distinguishedName", &col);
        if ( SUCCEEDED(hr) )
        {
            if (col.dwADsType == ADSTYPE_DN_STRING && col.pADsValues)
            {
                wcscpy_s(userdata.distinguishedName,
col.pADsValues->DNString);
            }

            pSearch->FreeColumn( &col );
        }

        // Get the objectGUID number.
        hr = pSearch->GetColumn( hSearch, L"objectGUID", &col );
        if ( SUCCEEDED(hr) )
        {
            if ((col.dwADsType == ADSTYPE_OCTET_STRING) && col.pADsValues &&
                (col.pADsValues->OctetString.lpValue))
            {
                BuildGUIDString(szGUID, (LPBYTE) col.pADsValues->OctetString.lpValue);
                wcscpy_s(userdata.objectGUID, szGUID);
            }

            pSearch->FreeColumn( &col );
        }

        // If the objectGUID of a deleted object matches an objectGUID in
        // the secondary storage, delete the object from storage.
        DeleteObjectDataFromStorage(&userdata);
        dwCount++;
        hr = pSearch->GetNextRow(hSearch);
    }

    wprintf(L"deleted dwCount: %d\n", dwCount);

cleanup:

    if (pszServerPath)
      {
        delete[] pszServerPath;
            pszServerPath = NULL;
      }
    if (pszDSPath)
      {
        delete[] pszDSPath;
            pszDSPath = NULL;
      }
    if (pRootDSE)
      {
        pRootDSE->Release();
            pRootDSE = NULL;
      }
    if (pDCService)
      {
        pDCService->Release();
            pDCService = NULL;
      }
    if (pDeletedObj)
      {
        pDeletedObj->Release();
            pDeletedObj = NULL;
      }
    if (hSearch)
      {
        pSearch->CloseSearchHandle(hSearch);
            hSearch = NULL;
      }
    if (pSearch)
      {
        pSearch->Release();
            pSearch = NULL;
      }
    VariantClear(&var);

    return hr;
}

//********************************************************************
// DeleteObjectDataFromStorage routine
//********************************************************************
VOID DeleteObjectDataFromStorage(PMYUSERDATA pUserData) {
    wprintf(L"DELETED OBJECT:\n");
    wprintf(L"   objectGUID: %s\n", pUserData->objectGUID);
    wprintf(L"   distinguishedName: %s\n", pUserData->distinguishedName);
    wprintf(L"---------------------------------------------\n");

    return;
}

//********************************************************************
// WriteObjectDataToStorage routine
//********************************************************************
VOID WriteObjectDataToStorage(PMYUSERDATA pUserData, BOOL bUpdate) {
    if (bUpdate)
    {
        wprintf(L"UPDATE:\n");
    }
    else
    {
        wprintf(L"INITIAL DATA:\n");
    }

    wprintf(L"   objectGUID: %s\n", pUserData->objectGUID);
    wprintf(L"   distinguishedName: %s\n", pUserData->distinguishedName);
    wprintf(L"   phoneNumber: %s\n", pUserData->phoneNumber);
    wprintf(L"---------------------------------------------\n");

    return;
}

//********************************************************************
// WriteSyncParamsToStorage routine
// This example caches the parameters in the registry. In a real // synchronization application, store the parameters in the same // storage that you are keeping consistent with Active Directory.
// This ensures that the parameters and object data remain synchronized // if the storage is ever restored from a backup.
//********************************************************************
DWORD WriteSyncParamsToStorage(
    LPWSTR pszPrevInvocationID, // Receives invocation ID
    LPWSTR pszPrevHighUSN,      // Receives previous high USN
    LPWSTR pszDCName)           // Receives name of DC to bind to
{
    HKEY hReg = NULL;
    DWORD dwStat = NO_ERROR;

    // Create a registry key under
    // HKEY_CURRENT_USER\SOFTWARE\Vendor\Product.
    dwStat = RegCreateKeyExW(HKEY_CURRENT_USER,
        L"Software\\Microsoft\\Windows 2000 AD-Synchro-USN",
        0,
        NULL,
        REG_OPTION_NON_VOLATILE,
        KEY_WRITE,
        NULL,
        &hReg,
        NULL);
    if (NO_ERROR == dwStat)
    {
        // Cache the invocationID as a value under the registry key.
        dwStat = RegSetValueExW(hReg,
            L"InvocationID",
            0,
            REG_SZ,
            (LPBYTE)pszPrevInvocationID,
            (lstrlenW(pszPrevInvocationID) + 1) * sizeof(WCHAR));

        // Cache the previous high USN as a value under the registry key.
        dwStat = RegSetValueExW(hReg,
            L"PreviousHighUSN",
            0,
            REG_SZ,
            (LPBYTE)pszPrevHighUSN,
            (lstrlenW(pszPrevHighUSN) + 1) * sizeof(WCHAR));

        // Cache the DC name as a value under the registry key.
        dwStat = RegSetValueExW(hReg,
            L"DC name",
            0,
            REG_SZ,
            (LPBYTE)pszDCName,
            (lstrlenW(pszDCName) + 1) * sizeof(WCHAR));

        RegCloseKey(hReg);
    }

    return dwStat;
}

//********************************************************************
// GetSyncParamsFromStorage routine
// This example reads the parameters from the registry. In a real // synchronization application, store the parameters in the // same storage that you are keeping consistent with Active Directory.
//********************************************************************
DWORD GetSyncParamsFromStorage(
    LPWSTR pszPrevInvocationID, // Receives invocation ID
    DWORD dwPrevInvocationSize, // size of the buffer, in WCHARS
    LPWSTR pszPreviousHighUSN,  // Receives previous high USN
    DWORD dwPrevHighUSNSize,    // size of the buffer, in WCHARS
    LPWSTR pszDCName,           // Receives name of DC to bind to
    DWORD dwDCNameSize)         // size of the buffer, in WCHARS
{
    HKEY hReg = NULL;
    DWORD dwStat;

    // Open the registry key.
    dwStat = RegOpenKeyExW(
                HKEY_CURRENT_USER,
                L"Software\\Microsoft\\Windows 2000 AD-Synchro-USN",
                0,
                KEY_QUERY_VALUE,
                &hReg);
    if (NO_ERROR == dwStat)
    {
        // Get the previous invocationID from the registry.
        dwPrevInvocationSize = dwPrevInvocationSize * sizeof(WCHAR);
        dwStat = RegQueryValueExW(hReg,
            L"InvocationID",
            NULL,
            NULL,
            (LPBYTE)pszPrevInvocationID,
            &dwPrevInvocationSize);
        if (dwStat != NO_ERROR)
        {
            wprintf(L"RegQueryValueEx failed to get invocationID: 0x%x\n", dwStat);
        }

        // Get the previous high USN from the registry.
        dwPrevHighUSNSize = dwPrevHighUSNSize * sizeof(WCHAR);
        dwStat = RegQueryValueExW(hReg,
            L"PreviousHighUSN",
            NULL,
            NULL,
            (LPBYTE)pszPreviousHighUSN,
            &dwPrevHighUSNSize);
        if (dwStat != NO_ERROR)
        {
            wprintf(L"RegQueryValueEx failed to get previous high USN:
0x%x\n", dwStat);
        }

        // Get the DC name from the registry.
        dwDCNameSize = dwDCNameSize * sizeof(WCHAR);
        dwStat = RegQueryValueExW(hReg,
            L"DC name",
            NULL,
            NULL,
            (LPBYTE)pszDCName,
            &dwDCNameSize);
        if (dwStat != NO_ERROR)
        {
            wprintf(L"RegQueryValueEx failed to get DC name: 0x%x\n", dwStat);
        }

        RegCloseKey(hReg);
    }

    return dwStat;
}

//********************************************************************
// BuildGUIDString
// Routine that makes the GUID a string in directory service bind form.
//********************************************************************
VOID BuildGUIDString(WCHAR *szGUID, LPBYTE pGUID) {
    DWORD i;
    DWORD dwlen = sizeof(GUID);
    WCHAR buf[4];

    wcscpy_s(szGUID, L"");
    for(i = 0; i < dwlen; i++)
    {
        swprintf_s(buf, L"%02x", pGUID[i]);
        wcscat_s(szGUID, buf);
    }
}

//********************************************************************
// Main
//********************************************************************
int main(int argc, char* argv[])
{
    DWORD dwStat;
    HRESULT hr;

    // Attributes to retrieve
    LPWSTR szAttribs[] =
    {
        {L"telephoneNumber"},
        {L"distinguishedName"},
        {L"uSNChanged"},
        {L"objectGUID"},
        {L"isDeleted"}
    };
    LPWSTR *pszAttribs=szAttribs;
    DWORD dwAttribs = sizeof(szAttribs)/sizeof(LPWSTR);

    // DC properties to cache for next synchronization.
    WCHAR szPrevInvocationID[40];
    WCHAR szPrevHighUSN[40];
    WCHAR szDCName[MAX_PATH];

    CoInitialize(NULL);

    if (argc > 1)
    {
        // Perform a full synchronization.
        // Initialize synchronization parameters to empty strings.
        wprintf(L"Performing a full read.\n");
        szPrevInvocationID[0] = '\0';
        szPrevHighUSN[0] = '\0';
        szDCName[0] = '\0';
    }
    else
    {
        // Perform a synchronization update.
        // Initialize synchronization parameters from storage.
        wprintf(L"Retrieving changes only.\n");
        dwStat = GetSyncParamsFromStorage(
            szPrevInvocationID,
            ARRAYSIZE(szPrevInvocationID),
            szPrevHighUSN,
            ARRAYSIZE(szPrevHighUSN),
            szDCName,
            ARRAYSIZE(szDCName));
        if (dwStat != NO_ERROR)
        {
            wprintf(L"Could not get synchronization parameters: %u\n", dwStat);
            goto cleanup;
        }
    }

    // Perform the search and update the synchronization parameters.
    hr = DoUSNSyncSearch(L"OU=UK,DC=xapac,DC=xnet,DC=intra",
                        ADS_SCOPE_SUBTREE,
                        pszAttribs, dwAttribs,
                        szPrevInvocationID, szPrevHighUSN, szDCName);
    if (FAILED(hr))
    {
        wprintf(L"DoUSNSyncSearch failed: 0x%x\n", hr);
        goto cleanup;
    }

    // Cache the synchronization parameters in storage for the next synchronization.
    wprintf(L"Caching the synchronization parameters.\n");
    dwStat = WriteSyncParamsToStorage(
                szPrevInvocationID, szPrevHighUSN, szDCName);
    if (dwStat != NO_ERROR)
    {
        wprintf(L"Error caching the synchronization parameters: %u\n", dwStat);
        goto cleanup;
    }

cleanup:

    CoUninitialize();

    return 1;
}
```



 

 