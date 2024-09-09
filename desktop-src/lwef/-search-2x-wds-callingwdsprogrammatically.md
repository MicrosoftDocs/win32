---
title: Calling WDS Programmatically
description: Microsoft Windows Desktop Search (WDS) 2.x can be queried programmatically using the ExecuteQuery and ExecuteSQLQuery methods in the ISearchDesktop interface.
ms.assetid: 38426f63-2039-410e-8c70-ebd9fc269d74
ms.topic: article
ms.date: 05/31/2018
---

# Calling WDS Programmatically

> [!NOTE]
> Windows Desktop Search 2.x is an obsolete technology that was originally available as an add-in for Windows XP and Windows Server 2003. On later releases, use [Windows Search](../search/-search-3x-wds-overview.md) instead.

Microsoft Windows Desktop Search (WDS) 2.x can be queried programmatically using the **ExecuteQuery** and **ExecuteSQLQuery** methods in the [**ISearchDesktop**](/previous-versions//aa965729(v=vs.85)) interface. The **ExecuteQuery** method returns a record set from the index based on the query text, columns, and restrictions passed as parameters. The **ExecuteSQLQuery** method also returns a record set of results but requires the exact Structured Query Language (SQL) command to be passed in. **ExecuteQuery** should be used in most scenarios.

## Regular Queries

Regular queries are those typed into the WDS input box by the user including all [Advanced Query Syntax](-search-2x-wds-aqsreference.md). The query is passed to **ExecuteQuery** along with the WDS 2.x [schema](-search-2x-wds-schematable.md) columns to return, the column and order to sort results, and any clauses to restrict results by.

The method has the form:

`HRESULT ExecuteQuery(LPCWSTR lpcwstrQuery, LPCWSTR lpcwstrColumn, LPCWSTR lpcwstrSort, LPCWSTR lpcwstrRestriction, Recordset **ppiRs);`



| Direction | Variable           | Description                                                                                                                                                                                   |
|-----------|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| In        | lpcwstrQuery       | The query text. This query is the same as a query typed into the search text box in the Windows Desktop Search user interface. <br/> For example: `"from:Zara dinner plans"`<br/> |
| In        | lpcwstrColumn      | The columns to include, separated by commas. <br/> For example: `"DocTitle, Url"`<br/>                                                                                            |
| In        | lpcwstrSort        | The Override Column to sort by followed by ASC for ascending or DESC for descending. <br/> For example: `"LastAuthor DESC"`<br/>                                                  |
| In        | lpcwstrRestriction | Restrictions to append through WHERE clauses in the Windows Desktop Search select. <br/> For example: `"Contains(LastAuthor, 'Bill')"`<br/>                                       |
| Out       | ppiRs              | The resulting record set<br/>                                                                                                                                                           |



 

## SQL Queries

The **ISearchDesktop.ExecuteSQLQuery** method is used to send direct WDS database queries. The syntax for the queries is similar to that used for SharePoint Server, along with the ability to use Monarch-style SQL GROUP BY clauses. The query is executed against the index exactly as it is passed in with no additional processing of Advanced Query Syntax as the ExecuteQuery API does.

<!-- Outdated link

`https://msdn.microsoft.com/library/default.asp?url=/library/spssdk/html/_tahoe_search_sql_syntax.asp`

-->

The method has the form:

`HRESULT ExecuteSQLQuery(LPCWSTR lpcwstrSQL, Recordset **ppiRs);`



| Direction | Variable   | Description                                    |
|-----------|------------|------------------------------------------------|
| In        | lpcwstrSQL | The SQL query to execute against the WDS index |
| Out       | ppiRs      | The resulting record set                       |


<!-- Outdated links

Resources:

-   Support files for the ISearchDesktop interface: https://addins.msn.com/support/WDSSDK.zip
-   ISearchDesktop C# Sample: https://addins.msn.com/support/WDSSample.zip

-->

## Sample C++ Code

> [!Note]
>
> THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR PURPOSE.
>
> Copyright (C) Microsoft. All rights reserved.

 


```
#include <stdio.h>
#include <wchar.h>
#include <windows.h>
#include <msnldl.h>
#include <adoint.h>
#include <adoguids.h>
 
HRESULT TestExecuteQuery(ISearchDesktop *psd)
{
ADORecordset *prs = NULL;
 
    HRESULT hr;
 
    hr = psd->ExecuteQuery( L"ToName:Moishe", 
                            L"DocTitle,DocFormat", 
                            L"PrimaryDate DESC", 
                            L"Contains('text')", 
                            &prs);
    if (SUCCEEDED(hr))
        prs->Release();
    return hr;
}
 
HRESULT TestExecuteSQLQuery(ISearchDesktop *psd)
{
    ADORecordset *prs = NULL;
    HRESULT hr;

    hr = psd->ExecuteSQLQuery(L"select DocTitle from MyIndex..Scope() where contains('text')", &prs);

    if (SUCCEEDED(hr))
      prs->Release();
    return hr;
}
 
extern "C" int __cdecl wmain( int argc, WCHAR * argv[] )
{
    SCODE sc = CoInitialize(0);
    ISearchDesktop *psd = NULL;
    HRESULT         hr;
     
    if (SUCCEEDED(hr = CoCreateInstance(__uuidof(SearchDesktop), NULL, CLSCTX_INPROC_SERVER, 
                                        __uuidof(ISearchDesktop), (void**)&psd)))
          {
             TestExecuteSQLQuery(psd);
             TestExecuteQuery(psd);
             psd->Release();
          }
          CoUninitialize();
}
```



## Related topics

<dl> <dt>

**Reference**
</dt> <dt>

[Advanced Query Syntax](-search-2x-wds-aqsreference.md)
</dt> <dt>

[Perceived Types](-search-2x-wds-perceivedtype.md)
</dt> <dt>

[Calling WDS from Web Pages](-search-2x-wds-browserhelpobject.md)
</dt> </dl>

 

