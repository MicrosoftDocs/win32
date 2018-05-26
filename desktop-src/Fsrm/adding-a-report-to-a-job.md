---
title: Adding a Report to a Job
description: A report defines the information that you want the scan to return.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2dd5420b-33ab-4831-83b8-a9a4b2201a60
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- File Server Resource Manager examples File Server Resource Manager , adding a report to a job
- reports File Server Resource Manager
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Adding a Report to a Job

A report defines the information that you want the scan to return. For example, you can create a report that lists files over a given size or files that have not been accessed in the last *n* days. For a list of reports that you can request, see the [**FsrmReportType**](/windows/previous-versions/FsrmEnums/ne-fsrmenums-_fsrmreporttype?branch=master) enumeration. A report job can contain only one report of each type.

You can specify a filter value for most of the report types which lets you limit the information provided in the report. To specify a filter value for a report type that is applied to all reports of that type, call the [**IFsrmReportManager::SetDefaultFilter**](/windows/previous-versions/FsrmReports/nf-fsrmreports-ifsrmreportmanager-setdefaultfilter?branch=master) method. To override the global filter value, you can call the [**IFsrmReport::SetFilter**](/windows/previous-versions/FsrmReports/nf-fsrmreports-ifsrmreport-setfilter?branch=master) method.

The following example shows how to create and configure a report for a report job. The **AddReportToJob** function is defined in the [Defining a Report Job](defining-a-report-job.md) example.


```C++
// Create and configures a report that lists files that 
// have not been accessed in the last five days.
HRESULT AddReportToJob(IFsrmReportJob* pJob)
{
    HRESULT hr = S_OK;
    IFsrmReport* pReport = NULL;

    // Add a report that lists the least recently accessed files.
    hr = pJob->CreateReport(FsrmReportType_LeastRecentlyAccessed, &amp;pReport);
    if (FAILED(hr))
    {
        wprintf(L"pJob->CreateReport failed, 0x%x.\n", hr);
        goto cleanup;
    }

    // The name and description are included in the report. The name
    // is used as the subject if the report is being mailed.
    hr = pReport->put_Name(_bstr_t(L"Least Accessed"));
    if (FAILED(hr))
    {
        wprintf(L"pReport->put_Name failed, 0x%x.\n", hr);
        goto cleanup;
    }

    hr = pReport->put_Description(_bstr_t(L"This report list the files "
        L"that have not been accessed within the last five days."));
    if (FAILED(hr))
    {
        wprintf(L"pReport->put_Description failed, 0x%x.\n", hr);
        goto cleanup;
    }

    // Use the filter on the report object to specify the least accessed report.
    hr = pReport->SetFilter(FsrmReportFilter_MinAgeDays, _variant_t(5));
    if (FAILED(hr))
    {
        wprintf(L"pReport->SetFilter failed, 0x%x.\n", hr);
        goto cleanup;
    }

    // Save the report job.
    hr = pJob->Commit();
    if (FAILED(hr))
    {
        wprintf(L"pJob->Commit failed, 0x%x.\n", hr);
        goto cleanup;
    }

cleanup:

    if (pReport)
        pReport->Release();

    return hr;
}
```



 

 




