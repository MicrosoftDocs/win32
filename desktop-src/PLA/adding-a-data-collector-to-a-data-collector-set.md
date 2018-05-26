---
title: Adding a Data Collector to a Data Collector Set
description: To collect data, the data collector set must contain one or more data collectors.
ms.assetid: 0495cab6-d9d7-496f-8150-e36ff75210da
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Adding a Data Collector to a Data Collector Set

To collect data, the data collector set must contain one or more data collectors. If you use the data collector set to collect event traces, the set can contain only one trace data collector (and the set cannot contain any other data collector types).

The following example shows how to create an alert data collector and add it to the data collector set in [Creating a Data Collector Set](creating-a-data-collector-set.md).


```C++
HRESULT AddDataCollector(IDataCollectorSet* pdcs)
{
    HRESULT hr = S_OK;
    IDataCollectorCollection* pCollectors = NULL;
    IDataCollector* pdc = NULL;
    IPerformanceCounterDataCollector* pdcPerfCounter = NULL;
    SAFEARRAY* psaCounters = NULL;
    BSTR bstr = NULL;
    long index = 0;

    // Retrieve the collection of data collectors from the data
    // collector set.
    hr = pdcs->get_DataCollectors(&amp;pCollectors);
    if (FAILED(hr))
    {
        wprintf(L"pdcs->get_DataCollectors failed, 0x%x\n", hr);
        goto cleanup;
    }

    // Create an performance counter data collector. The method returns an IDataCollector
    // interface that contains the base properties for all data collectors.
    // Query IDataCollector for the IPerformanceCounterDataCollector interface.
    hr = pCollectors->CreateDataCollector(plaPerformanceCounter, &amp;pdc);
    hr = pdc->QueryInterface(IID_IPerformanceCounterDataCollector, (void**)&amp;pdcPerfCounter);
    pdc->Release();

    // TODO: Set one or more of the perf counter properties; you must specify one or 
    // or more counters. You can also change the sample interval (the rate at which
    // PLA samples the counter).

    // Create an array of performance counters that you want to sample. This example
    // adds a single counter.
    psaCounters = SafeArrayCreateVector(VT_BSTR, 0, 1);
    if (psaCounters)
    {
        bstr = SysAllocString(L"\\Processor(0)\\% Processor Time");
        hr = SafeArrayPutElement(psaCounters, &amp;index, bstr);
        SysFreeString(bstr);

        hr = pdcPerfCounter->put_PerformanceCounters(psaCounters);
        if (FAILED(hr))
        {
            wprintf(L"pdcPerfCounter->put_PerformanceCounters failed, 0x%x\n", hr);
            goto cleanup;
        }

        hr = SafeArrayDestroy(psaCounters);
        psaCounters = NULL;
    }
    else
    {
        wprintf(L"Failed to create perf counters safearray\n");
        goto cleanup;
    }

    // Change the sample interval to every 5 seconds.
    hr = pdcPerfCounter->put_SampleInterval(5);
    if (FAILED(hr))
    {
        wprintf(L"pdcPerfCounter->put_SampleInterval failed, 0x%x\n", hr);
        goto cleanup;
    }


    // TODO: Set one or more of the IDataCollector properties.

    hr = pdcPerfCounter->put_Name(_bstr_t(L"Test Counters"));
    if (FAILED(hr))
    {
        wprintf(L"pdcPerfCounter->put_Name failed, 0x%x\n", hr);
        goto cleanup;
    }

    hr = pdcPerfCounter->put_FileName(_bstr_t(L"TestCounters"));
    if (FAILED(hr))
    {
        wprintf(L"pdcPerfCounter->put_FileName failed, 0x%x\n", hr);
        goto cleanup;
    }

    hr = pdcPerfCounter->put_FileNameFormat(plaYearMonthDayHour);
    if (FAILED(hr))
    {
        wprintf(L"pdcPerfCounter->put_FileNameFormat failed, 0x%x\n", hr);
        goto cleanup;
    }

    // Add the perf counter data collector to the collection of data collectors in the set.
    hr = pCollectors->Add(pdcPerfCounter);
    if (FAILED(hr))
    {
        wprintf(L"pCollectors->Add failed, 0x%x\n", hr);
        goto cleanup;
    }

cleanup:

    if (pdcPerfCounter)
        pdcPerfCounter->Release();

    if (psaCounters)
        SafeArrayDestroy(psaCounters);

    if (pCollectors)
        pCollectors->Release();

    return hr;
}
```



 

 




