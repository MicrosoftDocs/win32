---
title: Searching Binary Data
description: Even though the ADSI search feature only supports searching for string data, it is possible to search for binary data.
ms.assetid: 52b75ae0-dbf1-4310-8b6b-a176de9f1b7d
ms.tgt_platform: multiple
keywords:
- Searching Binary Data ADSI
- Binary Data ADSI
- Binary Data ADSI , Searching Binary Data
- ADSI ADSI , Example Code C/C++ , Searching for Binary Data
ms.topic: article
ms.date: 05/31/2018
---

# Searching Binary Data

Even though the ADSI search feature only supports searching for string data, it is possible to search for binary data. To do this, use the [**ADsEncodeBinaryData**](/windows/desktop/api/Adshlp/nf-adshlp-adsencodebinarydata) function to convert the binary data into a string that can be used with the search methods. Searching for binary data is particularly useful when searching for a GUID or a SID because these data types are stored as binary data.

When using the [**ADsEncodeBinaryData**](/windows/desktop/api/Adshlp/nf-adshlp-adsencodebinarydata) function, the memory allocated must be freed using the [**FreeADsMem**](/windows/desktop/api/Adshlp/nf-adshlp-freeadsmem) function.

The following C++ code example shows how to build a query string to search for an object that has a particular **objectGUID** value.


```C++
LPWSTR pwszGuid = NULL;
LPWSTR pwszFormat = L"(objectGUID=%s)";
LPWSTR pwszSearch = NULL;
hr = ADsEncodeBinaryData((LPBYTE)pguid, sizeof(GUID), &pwszGuid);
if(FAILED(hr))
{
    goto cleanup;
}

pwszSearch = new WCHAR[lstrlenW(pwszFormat) + lstrlenW(pwszGuid) + 1];
if(NULL == pwszSearch)
{
    goto cleanup;
}
    
swprintf_s(pwszSearch, pwszFormat, pwszGuid);

// Use pwszSearch to perform a query for the object.

cleanup:    
if(pwszGuid)
{
    FreeADsMem(pwszGuid);
}
if(pwszSearch)
{
    delete pwszSearch;
}

```



 

 




