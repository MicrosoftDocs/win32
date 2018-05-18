---
title: Querying All Data Collector Sets
description: To retrieve all previously committed data collector sets on a computer or from a specified namespace, call the IDataCollectorSetCollection GetDataCollectorSets method.
ms.assetid: '263ded8e-356e-43bf-8020-b0d9d373faea'
---

# Querying All Data Collector Sets

To retrieve all previously committed data collector sets on a computer or from a specified namespace, call the [**IDataCollectorSetCollection::GetDataCollectorSets**](idatacollectorsetcollection-getdatacollectorsets.md) method.

For details on retrieving a specific data collector set on a computer, see [Querying a Data Collector Set](querying-a-data-collector-set.md).

You can retrieve data collector sets from the local computer or from a remote computer. There can be a delay when retrieving the data collector sets from a remote computer, so you should not query remote sets from a UI thread.

The following example shows how to retrieve all data collector sets from the local computer. This example uses an enumeration to iterate through the collection; however, you could also use the [**Count**](idatacollectorsetcollection-count.md) and [**Item**](idatacollectorsetcollection-item.md) properties to iterate through the collection.


```C++
#include <windows.h>
#include <stdio.h>
#include <comutil.h>
#include <pla.h>

#pragma comment(lib, "comsupp.lib")

void main(void)
{
    HRESULT hr = S_OK;
    IDataCollectorSetCollection* pdcSets = NULL;
    IDataCollectorSet* pdcSet = NULL;
    IEnumVARIANT* penum = NULL;
    IUnknown* punk = NULL;
    BSTR bstrName = NULL;
    VARIANT var;
    _bstr_t bstrFilter = L"";   // Retrieve all data collector sets. Use one of the 
                                // following strings to retrieve the sets from a specific
                                // namespace: L"Service\\*" L"System\\*" L"Legacy\\*" 
                                // L"Session\\*" L"AutoSession\\*". 

    hr = CoInitializeEx(NULL, COINIT_APARTMENTTHREADED);

    hr = CoCreateInstance(__uuidof(DataCollectorSetCollection), 
                          NULL, 
                          CLSCTX_SERVER,
                          __uuidof(IDataCollectorSetCollection),
                          (void**) &amp;pdcSets);

    if (FAILED(hr))
    {
        wprintf(L"CoCreateInstance(__uuidof(DataCollectorSetCollection) failed with 0x%x.\n", hr);
        goto cleanup;
    }

    // Retrieve all data collector sets from the local computer. To 
    // retrieve data collector sets on a remote computer, specify the domain
    // name of the remote computer in the first parameter. The retrieved 
    // data collector sets overwrite the contents of this instance.
    hr = pdcSets->GetDataCollectorSets(NULL, bstrFilter);
    if (FAILED(hr))
    {
        wprintf(L"pdcSets->GetDataCollectorSets failed with 0x%x.\n", hr);
        goto cleanup;
    }

    // Get the enumeration.
    hr = pdcSets->get__NewEnum(&amp;punk);
    hr = punk->QueryInterface(__uuidof(IEnumVARIANT), (void**)&amp;penum);
    punk->Release();

    VariantInit(&amp;var);

    wprintf(L"List of data collector sets in the specified namespace:\n\n");

    // Iterate through the enumeration.
    while (S_OK == (hr = penum->Next(1, &amp;var, NULL)))
    {
        var.punkVal->QueryInterface(__uuidof(IDataCollectorSet), (void**)&amp;pdcSet);

        hr = pdcSet->get_Name(&amp;bstrName);
        wprintf(L"%s\n", bstrName);
        SysFreeString(bstrName);

        pdcSet->Release();
        pdcSet = NULL;
        VariantClear(&amp;var);
    }

    penum->Release();

cleanup:

    if (pdcSets)
        pdcSets->Release();

    CoUninitialize();
}
```



 

 




