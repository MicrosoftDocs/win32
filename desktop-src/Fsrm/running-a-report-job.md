---
title: Running a Report Job
description: You can run reports on demand or on a schedule.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8087542d-5873-414b-8903-544c2e57cba1
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- File Server Resource Manager examples File Server Resource Manager , running a report job
- reports File Server Resource Manager
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Running a Report Job

You can run reports on demand or on a schedule. The report job must be saved before you can run the reports in the job.

The following example shows how to run a report on demand. The *RunReportJob* function is defined in the [Defining a Report Job](defining-a-report-job.md) example. For an example that shows how to run a report on a schedule, see [Scheduling a Report Job](scheduling-a-report-job.md).


```C++
// Run the reports in the job.
HRESULT RunReportJob(IFsrmReportJob* pJob)
{
    HRESULT hr = S_OK;
    VARIANT_BOOL Completed = VARIANT_FALSE;
    BSTR bstrLastError = NULL;
    BSTR bstrStoredIn = NULL;

    // Run the report in the interactive (on-demand) context. The context determines the
    // location where the reports are written. To deterine where the reports
    // were written, access the LastGeneratedInDirectory property.
    hr = pJob->Run(FsrmReportGenerationContext_InteractiveReport);
    if (FAILED(hr))
    {
        wprintf(L"pJob->Run failed, 0x%x.\n", hr);
        goto cleanup;
    }

    // The Run method is asynchronous. To determine the status of the
    // report generation, poll the RunningStatus property. When the status changes
    // to NotRunning, access the LastError property to deterimine if the job
    // finished successfully. 
    
    // Alternatively, you can call the WaitForCompletion method to wait for the 
    // reports to complete. Then, access the LastError property to deterimine if the job
    // finished successfully.

    // Wait indefinetly (-1) for the reports to complete.
    hr = pJob->WaitForCompletion(-1, &amp;Completed);
    if (FAILED(hr))
    {
        wprintf(L"pJob->WaitForCompletion failed, 0x%x.\n", hr);
        goto cleanup;
    }

    // If you do not wait for indefinetly, you should check Completed to determine
    // if the report finished within the specified time.
    if (VARIANT_FALSE == Completed)
    {
        wprintf(L"The reports did not finish within the specified interval.\n");
    }
    else
    {
        // Check if the reports completed successfully. The reports succeeded
        // if the LastError string is empty, otherwise, the string contains
        // the error message.
        hr = pJob->get_LastError(&amp;bstrLastError);
        if (FAILED(hr))
        {
            wprintf(L"pJob->get_LastError failed, 0x%x.\n", hr);
            goto cleanup;
        }

        if (!SysStringLen(bstrLastError))
        {
            wprintf(L"The reports completed successfully.\n");

            hr = pJob->get_LastGeneratedInDirectory(&amp;bstrStoredIn);
            if (FAILED(hr))
            {
                wprintf(L"pJob->get_LastGeneratedInDirectory failed, 0x%x.\n", hr);
                goto cleanup;
            }

            wprintf(L"The reports are located at %s.\n", bstrStoredIn);
            SysFreeString(bstrStoredIn);
        }
        else
        {
            wprintf(L"The reports failed.\n%s\n", bstrLastError);
        }
    }

cleanup:

    if (bstrLastError)
        SysFreeString(bstrLastError);

    return hr;
}
```



 

 




