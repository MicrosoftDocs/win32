---
title: Defining a Report Job
description: A report job contains one or more reports to run.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a91c4fe7-ec8c-4d2b-b565-559e16668c87
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- File Server Resource Manager examples File Server Resource Manager , defining a report job
- reports File Server Resource Manager
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Defining a Report Job

A report job contains one or more reports to run. The job specifies the directories to scan for the reports and the report formats.

The following example shows how to create and configure a report job. The code for adding a report to the job and running the report job are shown in [Adding a Report to a Job](adding-a-report-to-a-job.md) and [Running a Report Job](running-a-report-job.md), respectively.


```C++
#ifndef UNICODE
#define UNICODE
#endif

#include <windows.h>
#include <stdio.h>
#include <comutil.h>
#include <FsrmReports.h>    // Report objects
#include <fsrmtlb.h>    // Contains CLSIDs.

IFsrmReportJob* ConfigureReportJob(IFsrmReportManager* prm);
HRESULT AddReportToJob(IFsrmReportJob* pJob);
HRESULT RunReportJob(IFsrmReportJob* pJob);


// Creates a report job. Adds a report to the job. Runs the report.

void wmain(void)
{
    HRESULT hr = S_OK;
    IFsrmReportManager* prm = NULL;
    IFsrmReportJob* pJob = NULL;

    hr = CoInitializeEx(NULL, COINIT_APARTMENTTHREADED);
    if (FAILED(hr))
    {
        wprintf(L"CoInitializeEx() failed, 0x%x.\n", hr);
        return;
    }

    // Get the report manager.
    hr = CoCreateInstance(CLSID_FsrmReportManager, 
        NULL,
        CLSCTX_LOCAL_SERVER,
        __uuidof(IFsrmReportManager),
        reinterpret_cast<void**> (&amp;prm));

    if (FAILED(hr))
    {
        wprintf(L"CoCreateInstance(FsrmReportManager) failed, 0x%x.\n", hr);
        if (E_ACCESSDENIED == hr)
            wprintf(L"Access denied. You must run the client with an elevated token.\n");

        goto cleanup;
    }

    pJob = ConfigureReportJob(prm);
    
    if (pJob)
    {
        hr = AddReportToJob(pJob);
        if (FAILED(hr))
        {
            wprintf(L"Failed to add report to report job.\n");
            goto cleanup;
        }

        hr = RunReportJob(pJob);
        if (FAILED(hr))
        {
            wprintf(L"Report job failed.\n");
            goto cleanup;
        }
    }

cleanup:

    if (prm)
        prm->Release();

    if (pJob)
        pJob->Release();


    CoUninitialize();
}



// Configure the report job. Specify the name of the job, the 
// directories that you want scanned for the reports, and the 
// formats of the reports.
IFsrmReportJob* ConfigureReportJob(IFsrmReportManager* prm)
{
    HRESULT hr = S_OK;
    IFsrmReportJob* pJob = NULL;
    SAFEARRAY* psaRoots = NULL;    // Directories to scan
    SAFEARRAY* psaFormats = NULL;  // Report formats 
    _variant_t var = NULL;
    long index = 0;

    // Create a report job.
    hr = prm->CreateReportJob(&amp;pJob);
    if (FAILED(hr))
    {
        wprintf(L"prm->CreateReportJob failed, 0x%x.\n", hr);
        goto cleanup;
    }

    // Name the job. If you schedule the job to run at certain time,
    // also use the name for the name of the Task Scheduler job.
    hr = pJob->put_Task(_bstr_t(L"Test Report"));
    if (FAILED(hr))
    {
        wprintf(L"pJob->put_Task failed, 0x%x.\n", hr);
        goto cleanup;
    }

    // Specify the directories that you want to scan for the report.
    // All descendant subdirectories of the specified directories are
    // included in the scan.
    psaRoots = SafeArrayCreateVector(VT_VARIANT, 0, 1);
    if (psaRoots)
    {
        var = L"c:\\folder";
        hr = SafeArrayPutElement(psaRoots, &amp;index, &amp;var);

        hr = pJob->put_NamespaceRoots(psaRoots);
        if (FAILED(hr))
        {
            wprintf(L"pJob->put_NamespaceRoots failed, 0x%x.\n", hr);
            goto cleanup;
        }

        SafeArrayDestroy(psaRoots);
        psaRoots = NULL;
    }
    else
    {
        wprintf(L"Failed to create roots safearray.\n");
        hr = E_FAIL;
        goto cleanup;
    }

    // Specify the report formats, for example, XML or plain text.
    psaFormats = SafeArrayCreateVector(VT_VARIANT, 0, 2);
    if (psaFormats)
    {
        var = (long) FsrmReportFormat_Txt;
        hr = SafeArrayPutElement(psaFormats, &amp;index, &amp;var);

        var = (long) FsrmReportFormat_Xml;
        index = 1;
        hr = SafeArrayPutElement(psaFormats, &amp;index, &amp;var);

        hr = pJob->put_Formats(psaFormats);
        if (FAILED(hr))
        {
            wprintf(L"pJob->put_Formats failed, 0x%x.\n", hr);
            goto cleanup;
        }

        SafeArrayDestroy(psaFormats);
        psaFormats = NULL;
    }
    else
    {
        wprintf(L"Failed to create formats safearray.\n");
        hr = E_FAIL;
        goto cleanup;
    }


cleanup:

    if (FAILED(hr))
        if (pJob)
        {
            pJob->Release();
            pJob = NULL;
        }

    if (psaRoots)
        SafeArrayDestroy(psaRoots);

    if (psaFormats)
        SafeArrayDestroy(psaFormats);

    return pJob;
}
```



 

 




