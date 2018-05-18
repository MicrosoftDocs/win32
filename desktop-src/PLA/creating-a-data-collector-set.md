---
title: Creating a Data Collector Set
description: A data collector set contains one or more data collectors. The properties of the set determine when the set runs (if the set is run on a schedule), where the logs are collected, and how the logs are managed.
ms.assetid: 'eb0ef2c5-55a2-4aaf-85fe-705bbc94d4fc'
---

# Creating a Data Collector Set

A data collector set contains one or more data collectors. The properties of the set determine when the set runs (if the set is run on a schedule), where the logs are collected, and how the logs are managed.

The set contains default property values that are used if you do not specify a value.

As an alternative to setting the properties of the data collector set, you could use XML to specify the property values for the data collector set. For details, see [Creating a Data Collector Set from XML](creating-a-data-collector-set-from-xml.md).

The following example shows how to create a data collector set and how to set some its properties.


```C++
HRESULT CreateDCS(IDataCollectorSet* & pdcs)
{
    HRESULT hr = S_OK;

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

    hr = pdcs->put_Description(_bstr_t(L"Creating a data collector set"));
    if (FAILED(hr))
    {
        wprintf(L"put_Description failed, 0x%x\n", hr);
        goto cleanup;
    }

    hr = pdcs->put_DisplayName(_bstr_t(L"DCS Test"));
    if (FAILED(hr))
    {
        wprintf(L"put_DisplayName failed, 0x%x\n", hr);
        goto cleanup;
    }

    // Limit the data collector set to run for one minute. 
    hr = pdcs->put_Duration(60);
    if (FAILED(hr))
    {
        wprintf(L"put_Duration failed, 0x%x\n", hr);
        goto cleanup;
    }

    // You should specify the subdirectory under RootPath where you want the data 
    // written. If you do not specify the subdirectory, the data is written in 
    // the RootPath directory.
    hr = pdcs->put_Subdirectory(_bstr_t(L"MyLogs"));
    if (FAILED(hr))
    {
        wprintf(L"put_Subdirectory failed, 0x%x\n", hr);
        goto cleanup;
    }

    // Use a serial number to format the subdirectory name. Using a serial number 
    // creates a new subdirectory name each time the set runs. If you do not specify a 
    // format for the subdirectory name, the contents of the subdirectory may be 
    // overwritten the next time the set runs.
    hr = pdcs->put_SubdirectoryFormat(plaSerialNumber);
    if (FAILED(hr))
    {
        wprintf(L"put_SubdirectoryFormat failed, 0x%x\n", hr);
        goto cleanup;
    }

    // To specify a Task Scheduler task to run when the data collector set completes 
    // (or the log is segmented), call the put_Task method. 

    // To limit the size of the log file that each collector can create before PLA 
    // writes to a new log file for that collector, call the put_Segment method.

    // To specify how the data from the collectors is managed (for example, how 
    // long to retain the logs), use the DataManager property.
    // 
    // To collect data on a schedule, use the Schedules property
    // to specify one or more scheduled times at which the collectors run.

cleanup:

    return hr;
}
```



After specifying the property values for the data collector set, you need to [add one or more data collectors to the set](adding-a-data-collector-to-a-data-collector-set.md) and call the [**IDataCollectorSet::Commit**](idatacollectorset-commit.md) method to save the set. Before calling **Commit**, you can optionally [specify a schedule for running the set](running-a-data-collector-set.md) and [specify how to manage the collected data](managing-the-data-of-a-data-collector-set.md).

 

 




