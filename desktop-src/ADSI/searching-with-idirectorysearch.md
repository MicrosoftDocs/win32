---
title: Searching with the IDirectorySearch Interface
description: The IDirectorySearch interface provides a high-level and low-overhead interface for querying data of a directory or a global catalog.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 'da415cb2-f320-4be4-b5bd-053cd6a6b2fd'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
keywords: ["Searching with the IDirectorySearch Interface ADSI", "Queries ADSI , Query Interfaces, IDirectorySearch", "ADSI ADSI , Example Code C/C++ , Searching a Directory with IDirectorySearch", "IDirectorySearch ADSI , Using to Search a Directory"]
---

# Searching with the IDirectorySearch Interface

The [**IDirectorySearch**](idirectorysearch.md) interface provides a high-level and low-overhead interface for querying data of a directory or a global catalog. The **IDirectorySearch** COM interface can be used only with a vtable, and thus, is not available to Automation-based development environments.

**To perform a search**

1.  Bind to an object in the directory.
2.  Call [**QueryInterface**](_com_iunknown_queryinterface) to get the [**IDirectorySearch**](idirectorysearch.md) pointer.
3.  Run the search using the [**IDirectorySearch**](idirectorysearch.md) pointer. Call the [**IDirectorySearch::ExecuteSearch**](idirectorysearch-executesearch.md) method, and pass a search filter, the requested attribute names, and other parameters.

For more information about the search filter syntax, see [Search Filter Syntax](search-filter-syntax.md).

Query execution is provider-specific. With some providers, the actual query execution does not occur until [**IDirectorySearch::GetFirstRow**](idirectorysearch-getfirstrow.md) or [**IDirectorySearch::GetNextRow**](idirectorysearch-getnextrow.md) is called. The [**IDirectorySearch**](idirectorysearch.md) interface works with search filters directly. Neither the SQL dialect nor the LDAP dialect are required.

The [**IDirectorySearch**](idirectorysearch.md) interface provides methods to enumerate the result set, row by row. The [**IDirectorySearch::GetFirstRow**](idirectorysearch-getfirstrow.md) method retrieves the first row and [**IDirectorySearch::GetNextRow**](idirectorysearch-getnextrow.md) moves you to the next row from the current row. When you have reached the last row, calling these methods returns the S\_ADS\_NOMORE\_ROWS error code. Conversely, [**IDirectorySearch::GetPreviousRow**](idirectorysearch-getpreviousrow.md) moves you back one row at a time. An S\_ADS\_NOMORE\_ROWS return value indicates that you have reached the first row of the result set. These methods operate on the result set, resident in memory, on the client. Thus, when paged and asynchronous searches are performed and the \_CACHE\_RESULTS option is turned off, backward scrolling can have unexpected consequences.

When you have located the appropriate row, call [**IDirectorySearch::GetColumn**](idirectorysearch-getcolumn.md) to obtain data items, column by column. For each call, you pass the name of the column of interest. The data item returned is a pointer to an [**ADS\_SEARCH\_COLUMN**](ads-search-column.md) structure. **GetColumn** allocates this structure for you, but you must free it using [**FreeColumn**](idirectorysearch-freecolumn.md). Call [**CloseSearchHandle**](idirectorysearch-closesearchhandle.md) to complete the search operation.

**To perform a directory search**

1.  Bind to an LDAP provider. It may be a domain controller or a global catalog provider.
2.  Retrieve the [**IDirectorySearch**](idirectorysearch.md) COM Interface with a call to [**QueryInterface**](_com_iunknown_queryinterface); this operation may have been done in Step 1 during the initial binding.

    Optionally, call [**SetSearchPreference**](idirectorysearch-setsearchpreference.md) to select options for handling the results of your search.

3.  Call [**ExecuteSearch**](idirectorysearch-executesearch.md). Depending on the options set in [**SetSearchPreference**](idirectorysearch-setsearchpreference.md) this may, or may not, begin query execution.
4.  Call [**GetNextRow**](idirectorysearch-getnextrow.md) to move the row index (internal to [**IDirectorySearch**](idirectorysearch.md)) to the first row.
5.  Read the data from the row using [**GetColumn**](idirectorysearch-getcolumn.md), then call [**FreeColumn**](idirectorysearch-freecolumn.md) to release the memory allocated by **GetColumn**.
6.  Repeat Step 5 until all data is retrieved from the search result, or until [**GetNextRow**](idirectorysearch-getnextrow.md) returns S\_ADS\_NOMORE\_ROWS.
7.  Call [**AbandonSearch**](idirectorysearch-abandonsearch.md) and [**CloseSearchHandle**](idirectorysearch-closesearchhandle.md) when complete.

The following code example shows this scenario. To start binding to ADSI, call the [**ADsOpenObject**](adsopenobject.md) function.


```C++
HRESULT hr = S_OK; // COM result variable
ADS_SEARCH_COLUMN col;  // COL for iterations
LPWSTR szUsername = NULL; // user name
LPWSTR szPassword = NULL; // password
 
// Interface Pointers.
IDirectorySearch     *pDSSearch    =NULL;
 
// Initialize COM.
CoInitialize(0);

// Add code to securely retrieve the user name and password or
// leave both as NULL to use the default security context.
 
// Open a connection with server.
hr = ADsOpenObject(L"LDAP://coho.salmon.Fabrikam.com", 
szUsername,
szPassword,
ADS_SECURE_AUTHENTICATION,
IID_IDirectorySearch,
(void **)&amp;pDSSearch);
```



This provides a pointer to the [**IDirectorySearch**](idirectorysearch.md) interface.

Now that there is a COM interface for an IDirectoryInterface instance, call [**IDirectorySearch::SetSearchPreference**](idirectorysearch-setsearchpreference.md).

Build an array of attribute names to prepare to call the [**IDirectorySearch::ExecuteSearch**](idirectorysearch-executesearch.md) function. The attribute names are defined within the schema of Active Directory. For more information about the schema definition, see [ADSI Schema Model](adsi-schema-model.md). The attribute names listed are returned, if supported by the object, as the result set of the search.


```C++
LPWSTR pszAttr[] = { L"description", L"Name", L"distinguishedname" };
ADS_SEARCH_HANDLE hSearch;
DWORD dwCount = 0;
DWORD dwAttrNameSize = sizeof(pszAttr)/sizeof(LPWSTR);
```



Now, call the [**ExecuteSearch**](idirectorysearch-executesearch.md) function. The search does not run until you call the [**GetNextRow**](idirectorysearch-getnextrow.md) method.


```C++
// Search for all objects with the 'cn' property that start with c.
hr = pDSSearch->ExecuteSearch(L"(cn=c*)",pszAttr ,dwAttrNameSize,&amp;hSearch );
```



Call [**GetNextRow**](idirectorysearch-getnextrow.md) to iterate rows in the result. Each row is then queried for the "description" attribute. If the attribute is found, it is displayed.


```C++
LPWSTR pszColumn;
    while( pDSSearch->GetNextRow( hSearch) != S_ADS_NOMORE_ROWS )
    {
        // Get the property.
        hr = pDSSearch->GetColumn( hSearch, L"description", &amp;col );
 
        // If this object supports this attribute, display it.
        if ( SUCCEEDED(hr) )
        { 
           if (col.dwADsType == ADSTYPE_CASE_IGNORE_STRING)
              wprintf(L"The description property:%s\r\n", col.pADsValues->CaseIgnoreString); 
           pDSSearch->FreeColumn( &amp;col );
        }
        else
            puts("description property NOT available");
        puts("------------------------------------------------");
        dwCount++;
    }
    pDSSearch->CloseSearchHandle(hSearch);
    pDSSearch->Release();
```



To end the search, call the [**AbandonSearch**](idirectorysearch-abandonsearch.md) method.

Be aware that if a page size is not set, [**GetNextRow**](idirectorysearch-getnextrow.md) blocks until the entire result set is returned to the client. If page size is set, then **GetNextRow** blocks until the first page (page size = number of rows in a page) is returned. If page size is set and the query is to be sorted and you are not searching on at least one indexed attribute, then the page size value is ignored, and the server calculates the entire result set prior to returning the data. This has the effect of **GetNextRow** blocking until the query completes.

> [!Note]  
> To change this query from a directory search to a global catalog search, the [**ADsOpenObject**](adsopenobject.md) call is changed.

 


```C++
// Open a connection with the server.
hr = ADsOpenObject(L"GC://coho.salmon.Fabrikam.com", 
szUsername, 
szPassword, 
ADS_SECURE_AUTHENTICATION,
IID_IDirectorySearch,
(void **)&amp;pDSSearch);
```



 

 




