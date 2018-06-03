---
title: Querying a Data Collector Set
description: To retrieve a previously committed data collector set, call the IDataCollectorSet Query method.
ms.assetid: 200c3f29-b109-4896-ad2a-40838cd2c444
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Querying a Data Collector Set

To retrieve a previously committed data collector set, call the [**IDataCollectorSet::Query**](/previous-versions/windows/desktop/api/Pla/nf-pla-idatacollectorset-query) method.

You can retrieve a data collector set from the local computer or from a remote computer. There can be a delay when retrieving the data collector set from a remote computer, so you should not query a remote set from a UI thread.

The following example shows how to retrieve a specific data collector set from the local computer. (For details on retrieving all data collector sets on a computer or from a specified namespace, see [Querying All Data Collector Sets](querying-all-data-collector-sets.md).)


```C++
#include <windows.h>
#include <stdio.h>
#include <comutil.h>
#include <pla.h>

#pragma comment(lib, "comsupp.lib")

LPWSTR statusStrings[] = {L"Stopped", L"Running", L"Compiling", 
                          L"Pending", L"Undefined"};

void main(void)
{
    HRESULT hr = S_OK;
    IDataCollectorSet* pdcs = NULL;
    _bstr_t bstrDCSName = L"<data collector set name goes here>";
    DataCollectorSetStatus status;

    hr = CoInitializeEx(NULL, COINIT_APARTMENTTHREADED);

    // Get an instance of the DataCollectorSet object.
    hr = CoCreateInstance(__uuidof(DataCollectorSet), 
                          NULL, 
                          CLSCTX_SERVER,
                          __uuidof(IDataCollectorSet),
                          (void**) &amp;pdcs);

    if (FAILED(hr))
    {
        wprintf(L"CoCreateInstance(__uuidof(DataCollectorSet) failed with 0x%x.\n", hr);
        goto cleanup;
    }

    // Retrieve the specified data collector set from the local computer. To 
    // retrieve a data collector set on a remote computer, specify the domain
    // name of the remote computer in the second parameter. The retrieved 
    // data collector set overwrites the contents of this instance.
    hr = pdcs->Query(bstrDCSName, NULL);
    if (FAILED(hr))
    {
        if (PLA_E_DCS_NOT_FOUND == hr)
            wprintf(L"Did not find the %s data collector set.\n", bstrDCSName);
        else if (HRESULT_FROM_WIN32(ERROR_INVALID_NAME) == hr)
            wprintf(L"The name is not valid.\n");
        else
            wprintf(L"pdcs->Query failed, 0x%x\n", hr);

        goto cleanup;
    }

    // TODO: Do something with the data collector set.

    hr = pdcs->get_Status(&amp;status);
    wprintf(L"Status: %s\n", statusStrings[status]);

cleanup:

    if (pdcs)
        pdcs->Release();

    CoUninitialize();
}
```



 

 




