---
title: Scheduling a Report Job
description: FSRM uses the Task Scheduler to schedule reports to run.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7994bf40-cc9d-4519-a0d4-d48d7ec10fda
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- File Server Resource Manager examples File Server Resource Manager , scheduling a report job
- reports File Server Resource Manager
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Scheduling a Report Job

FSRM uses the [Task Scheduler](https://msdn.microsoft.com/library/windows/desktop/aa383614) to schedule reports to run. To schedule a report job, use the [Task Scheduler](https://msdn.microsoft.com/library/windows/desktop/aa383614) v2.0 interfaces to define the scheduled task, however, the task definition must be v1.0 compatible. (Use the Task Scheduler API to define the task but not to register the task — FSRM will register the task.)

After defining the task, access the [**ITaskDefinition::XmlText**](https://msdn.microsoft.com/library/windows/desktop/aa381327) property to get the XML. Pass the XML string to the [**IFsrmReportScheduler::CreateScheduleTask**](/previous-versions/windows/desktop/api/FsrmReports/nf-fsrmreports-ifsrmreportscheduler-createscheduletask) method, which creates the Task Scheduler task.

The following XML shows the definition of a valid Task Scheduler task that runs every Friday at 5:00 AM. The XML is passed to the example shown later. The version attribute on the Task element indicates that the task is v1.0 compatible. Also, note that the **UserId** element must specify SYSTEM and the /Task argument switch must specify the same name that is specified for the [**IFsrmReportJob::Task**](/previous-versions/windows/desktop/api/FsrmReports/nf-fsrmreports-ifsrmreportjob-get_task) property.


```XML
<?xml version="1.0" encoding="UTF-8"?>
<Task version="1.1" xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task">
 <RegistrationInfo>
  <Author>SYSTEM</Author>
 </RegistrationInfo>
 <Triggers>
  <CalendarTrigger>
   <StartBoundary>2007-09-07T05:00:00</StartBoundary>
   <Enabled>true</Enabled>
   <ScheduleByWeek>
    <DaysOfWeek>
     <Friday />
    </DaysOfWeek>
    <WeeksInterval>1</WeeksInterval>
   </ScheduleByWeek>
  </CalendarTrigger>
 </Triggers>
 <Principals>
  <Principal id="Author">
   <UserId>SYSTEM</UserId>
   <RunLevel>HighestAvailable</RunLevel>
  </Principal>
 </Principals>
 <Settings>
  <Enabled>true</Enabled>
 </Settings>
 <Actions Context="Author">
  <Exec>
   <Command>C:\Windows\system32\storrept.exe</Command>
   <Arguments>reports generate /scheduled /Task:"Test Report"</Arguments>
  </Exec>
 </Actions>
</Task>
```



The following example shows how to schedule a report job using the XML in the previous example. The specified report job is defined in [Defining a Report Job](defining-a-report-job.md).


```C++
#ifndef UNICODE
#define UNICODE
#endif

#include <windows.h>
#include <stdio.h>
#include <comutil.h>
#include <FsrmReports.h>    // Report objects
#include <fsrmtlb.h>    // Contains CLSIDs.

#pragma comment(lib, "comsupp.lib")


void wmain(void)
{
    HRESULT hr = S_OK;
    IFsrmReportScheduler* pScheduler = NULL;
    SAFEARRAY* psaRoots = NULL;
    VARIANT vRoots;
    _bstr_t bstrTaskXml;  // Set in your Task Scheduler code (not shown)
    long index = 0;

    hr = CoInitializeEx(NULL, COINIT_APARTMENTTHREADED);
    if (FAILED(hr))
    {
        wprintf(L"CoInitializeEx() failed, 0x%x.\n", hr);
        return;
    }

    // Get the scheduler object.
    hr = CoCreateInstance(CLSID_FsrmReportScheduler, 
        NULL,
        CLSCTX_LOCAL_SERVER,
        __uuidof(IFsrmReportScheduler),
        reinterpret_cast<void**> (&amp;pScheduler));

    if (FAILED(hr))
    {
        wprintf(L"CoCreateInstance(FsrmReportScheduler) failed, 0x%x.\n", hr);
        if (E_ACCESSDENIED == hr)
            wprintf(L"Access denied. You must run the client with an elevated token.\n");

        goto cleanup;
    }

    // Specify the directories to scan for the reports. These should be
    // the same directories that you specified when you created the
    // report job.
    psaRoots = SafeArrayCreateVector(VT_VARIANT, 0, 1);
    if (psaRoots)
    {
        _variant_t vRoot = L"c:\\foo";
        hr = SafeArrayPutElement(psaRoots, &amp;index, &amp;vRoot);

        VariantInit(&amp;vRoots);
        V_VT(&amp;vRoots) = VT_ARRAY | VT_VARIANT;
        vRoots.parray = psaRoots;
    }
    else
    {
        wprintf(L"Failed to create roots safearray.\n");
        goto cleanup;
    }

    // Create the schedule. The name of the task (first parameter)
    // must be the same name that you specified for the Task property
    // of the report job.
    hr = pScheduler->CreateScheduleTask(_bstr_t(L"Test Report"), &amp;vRoots, bstrTaskXml));
    if (FAILED(hr))
    {
        wprintf(L"pScheduler->CreateScheduleTask failed, 0x%x.\n", hr);
        goto cleanup;
    }

cleanup:

    if (pScheduler)
        pScheduler->Release();

    if (psaRoots)
        SafeArrayDestroy(psaRoots);

    VariantClear(&amp;vRoots);

    CoUninitialize();
}
```



 

 




