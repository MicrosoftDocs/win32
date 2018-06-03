---
title: Running a Data Collector Set
ms.assetid: d6b63af3-2303-41e3-9496-221aa7fed4de
description: 
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Running a Data Collector Set

To run a data collector set, you can perform one of the following actions:

-   Call the [**IDataCollectorSet::Start**](/previous-versions/windows/desktop/api/Pla/nf-pla-idatacollectorset-start) method.
-   Schedule the data collector set to run.
-   Specify that an alert trigger a data collector set to run.

Before you can run a new data collector set, you must first call the [**IDataCollectorSet::Commit**](/previous-versions/windows/desktop/api/Pla/nf-pla-idatacollectorset-commit) method.

The following example shows how to schedule a data collector set to run. You can specify one or more schedules on which to run the data collector set. This example builds on the example in [Creating a Data Collector Set](creating-a-data-collector-set.md).


```C++
HRESULT ScheduleDCS(IDataCollectorSet* pdcs)
{
    HRESULT hr = S_OK;
    IScheduleCollection* pSchedules = NULL;
    ISchedule* pSchedule = NULL;
    SYSTEMTIME st;
    double date;
    VARIANT var;

    VariantInit(&amp;var);
    V_VT(&amp;var) = VT_DATE;

    // Get the collection of schedules from the data collector set. 
    hr = pdcs->get_Schedules(&amp;pSchedules);
    if (FAILED(hr))
    {
        wprintf(L"get_Schedules failed, 0x%x\n", hr);
        goto cleanup;
    }

    // Get an instance of the Schedule object.
    hr = pSchedules->CreateSchedule(&amp;pSchedule);
    if (FAILED(hr))
    {
        wprintf(L"CreateSchedule failed, 0x%x\n", hr);
        goto cleanup;
    }

    // Specify one or more days on which the set runs.
    // This example runs only one time.
    hr = pSchedule->put_Days(plaRunOnce);
    if (FAILED(hr))
    {
        wprintf(L"put_Days failed, 0x%x\n", hr);
        goto cleanup;
    }

    // Specify the date on which the schedule begins.
    ZeroMemory(&amp;st, sizeof(SYSTEMTIME));
    st.wDay = 27;
    st.wMonth = 5;
    st.wYear = 2009;
    SystemTimeToVariantTime(&amp;st, &amp;date);
    V_DATE(&amp;var) = date;

    hr = pSchedule->put_StartDate(var);
    if (FAILED(hr))
    {
        wprintf(L"put_StartDate failed, 0x%x\n", hr);
        goto cleanup;
    }

    // You do not have to specify an end date because the 
    // job is schedule to run only once.

    // Specify the time of day that the set runs.
    ZeroMemory(&amp;st, sizeof(SYSTEMTIME));
    st.wHour = 10;
    st.wMinute = 30;
    SystemTimeToVariantTime(&amp;st, &amp;date);
    V_DATE(&amp;var) = date;

    hr = pSchedule->put_StartTime(var);
    if (FAILED(hr))
    {
        wprintf(L"put_StartTime failed, 0x%x\n", hr);
        goto cleanup;
    }

    VariantClear(&amp;var);

    // Add the schedule to the schedule collection.
    hr = pSchedules->Add(pSchedule);
    if (FAILED(hr))
    {
        wprintf(L"pSchedules->Add failed, 0x%x\n", hr);
        goto cleanup;
    }

cleanup:

    if (pSchedule)
        pSchedule->Release();

    if (pSchedules)
        pSchedules->Release();

    return hr;
}
```



 

 




