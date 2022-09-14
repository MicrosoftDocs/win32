---
title: Using IDirectorySearch and IDirectoryObject for Range Retrieval
description: The IDirectoryObject or IDirectorySearch interfaces can be used to retrieve a range of property values. To do this, specify the attribute and range for one of the attributes requested in the query.
ms.assetid: 4d9d2a98-51d5-4326-b43e-a2ac3bc54a75
ms.tgt_platform: multiple
keywords:
- IDirectorySearch ADSI , Using for ranging to retrieve members of a group
- IDirectoryObject ADSI , Using for ranging to retrieve members of a group
- Range Retrieval ADSI , Using IDirectorySearch and IDirectoryObject
ms.topic: article
ms.date: 05/31/2018
---

# Using IDirectorySearch and IDirectoryObject for Range Retrieval

The [**IDirectoryObject**](/windows/desktop/api/Iads/nn-iads-idirectoryobject) or [**IDirectorySearch**](/windows/desktop/api/Iads/nn-iads-idirectorysearch) interfaces can be used to retrieve a range of property values. To do this, specify the attribute and range for one of the attributes requested in the query.

## Range Retrieval with IDirectoryObject

The [**IDirectoryObject**](/windows/desktop/api/Iads/nn-iads-idirectoryobject) interface can be used for range retrieval by specifying the attribute and range for one of the attributes in the *pAttributesName* array when calling the [**IDirectoryObject::GetObjectAttributes**](/windows/desktop/api/Iads/nf-iads-idirectoryobject-getobjectattributes) method.


```C++
PADS_ATTR_INFO pAttrInfo;
DWORD dwRetrieved;
LPWSTR pszAttrs[2];
 
pszAttrs[0] = L"Name";
pszAttrs[1] = L"member;range=0-100";

hr = pdo->GetObjectAttributes(pszAttrs, 2, &pAttrInfo, &dwRetrieved);
```



For more information and a code example that shows how to use the [**IDirectoryObject**](/windows/desktop/api/Iads/nn-iads-idirectoryobject) interface for range retrieval, see [Example Code for Ranging with IDirectoryObject](example-code-for-ranging-with-idirectoryobject.md).

## Range Retrieval with IDirectorySearch

The [**IDirectorySearch**](/windows/desktop/api/Iads/nn-iads-idirectorysearch) interface can be used for range retrieval by specifying the attribute and range for one of the retrieved attributes in the *pAttributesName* array when calling the [**IDirectorySearch::ExecuteSearch**](/windows/desktop/api/Iads/nf-iads-idirectorysearch-executesearch) method.


```C++
ADS_SEARCH_HANDLE hSearch;
LPWSTR pszAttrs[2];
 
pszAttrs[0] = L"Name";
pszAttrs[1] = L"member;range=0-100";

hr = pdo->ExecuteSearch(L"(objectClass=user)", pszAttrs, 2, &hSearch);
```



When using the [**IDirectorySearch**](/windows/desktop/api/Iads/nn-iads-idirectorysearch) interface for range retrieval, there is one problem that must be specifically addressed. When the range requested exceeds the number of remaining values, [**IDirectorySearch::GetColumn**](/windows/desktop/api/Iads/nf-iads-idirectorysearch-getcolumn) will return **E\_ADS\_COLUMN\_NOT\_SET**. To retrieve the remaining values, it is necessary to use the range wildcard '\*'. For example, if a group contains 150 members, member values 0-100 can be retrieved normally using ranged retrieval. If range 101-200 is then requested, **IDirectorySearch::GetColumn** will return **E\_ADS\_COLUMN\_NOT\_SET**. This problem can be avoided by using the [**IDirectorySearch::GetNextColumnName**](/windows/desktop/api/Iads/nf-iads-idirectorysearch-getnextcolumnname) method. Normally, **GetNextColumnName** will return the original query string. However, when the range requested exceeds the number of remaining values, **GetNextColumnName** will return a modified version of the query string by replacing the high range value with the range wildcard '\*'. In the example above, the first query would be performed with an attribute string of "member;range=0-100" and **GetNextColumnName** will return "member;range=0-100". In the second query, the attribute string would be "member;range=101-200", but **GetNextColumnName** will return "member;range=101-\*". This case can be determined by comparing the original attribute string to the result of **GetNextColumnName**. If the strings are different, the last block of values should be requested again with the range wildcard.

For more information and a code example that shows how to use the [**IDirectorySearch**](/windows/desktop/api/Iads/nn-iads-idirectorysearch) interface for range retrieval, see [Example Code for Ranging with IDirectorySearch](example-code-for-ranging-with-idirectorysearch.md).

 

 




