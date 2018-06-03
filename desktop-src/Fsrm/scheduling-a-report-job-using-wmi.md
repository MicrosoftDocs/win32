---
title: Scheduling a Storage Report using WMI
description: Starting with Windows Server 2012 FSRM uses WMI to schedule reports to run.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 558ce579-2cde-4bd5-90f9-4dd6d0cf8207
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- File Server Resource Manager examples File Server Resource Manager , scheduling a report job using WMI
- reports File Server Resource Manager
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Scheduling a Storage Report using WMI

Starting with Windows Server 2012 FSRM uses WMI to schedule reports to run.

The following C++ example shows how to schedule a storage report using WMI.


```C++
#include "main.h"

void __cdecl wmain()
{
    MI_Result          result                 = MI_RESULT_OK;
    MI_Application     application            = MI_APPLICATION_NULL;
    MI_Session         session                = MI_SESSION_NULL;
    MI_Operation       createScheduleResult   = MI_OPERATION_NULL;
    MI_Operation       createReportResult     = MI_OPERATION_NULL;
    MI_Instance       *pSchedule              = NULL;
    MI_Instance       *pStorageReport         = NULL;
    const MI_Instance *pScheduleResult        = NULL;
    const MI_Instance *pStorageReportResult   = NULL;
    MI_Instance       *pScheduledTaskInParams = NULL;
    MI_Boolean         moreResults            = MI_TRUE;

    MI_Value           value;
    ::ZeroMemory(&amp;value, sizeof(MI_Value));

    static const unsigned int aDaysOfTheWeek[] = {0, 6};
    static const MI_Datetime time = {1 /* is a timestamp */, {2012, 1, 1, 1, 0, 0, 0, 1}};
    static PCWSTR pwszNamespace = L"Root\\Microsoft\\Windows\\FSRM";
    static PCWSTR aNamespaces[] = {L"P:\\namespace1", L"P:\\namespace2"};

    // 1 - Large files report
    // 3 - Least recently accessed report
    static const unsigned int aReportTypes[] = {1, 3};

    ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    wprintf(L"\nInitializing ...\n");

    CheckResultAndExit( "MI_Application_Initialize", 
                        MI_Application_Initialize(0, NULL, NULL, &amp;application) );

    assert( application.ft );

    CheckResultAndExit( "MI_Application_NewSession", 
                        MI_Application_NewSession(&amp;application, NULL, NULL, NULL, NULL, NULL, &amp;session) );

    assert( session.ft );

    ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    wprintf(L"\nCreating a scheduled task ...\n");

    CheckResultAndExit( "MI_Application_NewParameterSet for method to create schedule", 
                        MI_Application_NewParameterSet(&amp;application, NULL, &amp;pScheduledTaskInParams) );

    assert( pScheduledTaskInParams );

    // Set the day of the week to trigger the scheduled task
    // 0 - Sunday
    // 6 - Saturday
    // This means schedule will run every weekend
    value.uint32a.data = (MI_Uint32 *) aDaysOfTheWeek;
    value.uint32a.size = ARRAYSIZE(aDaysOfTheWeek);
    CheckResultAndExit( "MI_Instance_AddElement for day of the week for schedule", 
                        MI_Instance_AddElement(pScheduledTaskInParams, L"Weekly", &amp;value, MI_UINT32A, MI_FLAG_ANY) );

    // Set the time of the day to trigger the scheduled task
    // Time stamp used is 1:00:00 AM on 1:1:2012 in UTC.
    // This means schedule will run at 1 AM on the scheduled days in UTC time.
    value.datetime = time;
    CheckResultAndExit( "MI_Instance_AddElement for time of the day for schedule", 
                        MI_Instance_AddElement(pScheduledTaskInParams, L"Time", &amp;value, MI_DATETIME, MI_FLAG_ANY) );

    MI_Session_Invoke(&amp;session, 
                      0, 
                      NULL, 
                      pwszNamespace, 
                      L"MSFT_FSRMScheduledTask", 
                      L"CreateScheduledTask", 
                      NULL, 
                      pScheduledTaskInParams, 
                      NULL, 
                      &amp;createScheduleResult);

    while (moreResults == MI_TRUE)
    {
        // MI_Session_Invoke results should be obtained using 
        // MI_Operation_GetInstance until there are no more results left
        const MI_Char *errorMessage = NULL;
        CheckResultAndExit( "MI_Operation_GetInstance for schedule", 
                            MI_Operation_GetInstance(&amp;createScheduleResult, 
                                                     &amp;pScheduleResult, 
                                                     &amp;moreResults, 
                                                     &amp;result, 
                                                     &amp;errorMessage, 
                                                     NULL) );

        if (result != MI_RESULT_OK)
        {
            fwprintf(stderr, 
                     L"MI_Session_Invoke to create a scheduled task sent back failure with MI Result = %d and error message = \n", 
                     result, 
                     errorMessage);
            goto end;
        }

        assert( pScheduleResult );

        MI_Type type;
        ::ZeroMemory(&amp;type, sizeof(MI_Type));

        // Extract the scheduled task instance from the output using MI_Instance_GetElement
        CheckResultAndExit( "MI_Instance_GetElement", 
                            MI_Instance_GetElement(pScheduleResult, L"ScheduledTask", &amp;value, &amp;type, NULL, NULL) );

        assert( type == MI_INSTANCE );

        pSchedule = value.instance;
        assert( pSchedule );
    }

    ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    wprintf(L"Creating a storage report ...\n");

    CheckResultAndExit( "MI_Application_NewInstance for storage report", 
                        MI_Application_NewInstance(&amp;application, L"MSFT_FSRMStorageReport", NULL, &amp;pStorageReport) );

    assert( pStorageReport );

    // Set name for the storage report
    value.string = L"Storage Report 1";
    CheckResultAndExit( "MI_Instance_AddElement for name", 
                        MI_Instance_AddElement(pStorageReport, L"Name", &amp;value, MI_STRING, MI_FLAG_KEY) );

    // Set namespaces for the storage report
    value.stringa.data = (MI_Char **) aNamespaces;
    value.stringa.size = ARRAYSIZE(aNamespaces);
    CheckResultAndExit( "MI_Instance_AddElement for namespace", 
                        MI_Instance_AddElement(pStorageReport, L"Namespace", &amp;value, MI_STRINGA, MI_FLAG_ANY) );

    // Set report types for the storage report
    value.uint32a.data = (MI_Uint32 *) aReportTypes;
    value.uint32a.size = ARRAYSIZE(aReportTypes);
    CheckResultAndExit( "MI_Instance_AddElement for report type", 
                        MI_Instance_AddElement(pStorageReport, L"ReportType", &amp;value, MI_UINT32A, MI_FLAG_ANY) );

    // Set least accessed minimum bar to 100 days for the least recently accessed report in the storage report
    value.uint32 = 100;
    CheckResultAndExit( "MI_Instance_AddElement for least accessed minimum", 
                        MI_Instance_AddElement(pStorageReport, L"LeastAccessedMinimum", &amp;value, MI_UINT32, MI_FLAG_ANY) );

    // Set file pattern to *.mp3 for the large files report in the storage report
    value.string = L"*.mp3";
    CheckResultAndExit( "MI_Instance_AddElement for large file pattern", 
                        MI_Instance_AddElement(pStorageReport, L"LargeFilePattern", &amp;value, MI_STRING, MI_FLAG_ANY) );

    // Set schedule for the storage report
    value.instance = pSchedule;
    CheckResultAndExit( "MI_Instance_AddElement for schedule", 
                        MI_Instance_AddElement(pStorageReport, L"Schedule", &amp;value, MI_INSTANCE, MI_FLAG_ANY) );

    MI_Session_CreateInstance(&amp;session, 0, 0, pwszNamespace, pStorageReport, NULL, &amp;createReportResult);

    moreResults = MI_TRUE;

    while (moreResults == MI_TRUE)
    {
        const MI_Char *errorMessage;

        // MI_Session_CreateInstance results should be obtained using 
        // MI_Operation_GetInstance until there are no more results left
        MI_Operation_GetInstance(&amp;createReportResult, &amp;pStorageReportResult, &amp;moreResults, &amp;result, &amp;errorMessage, NULL);

        if (result != MI_RESULT_OK)
        {
            fwprintf(stderr, 
                     L"MI_Session_CreateInstance for storage report sent back failure with MI Result = %d and error message = \n", 
                     result, 
                     errorMessage);
            goto end;
        }
    }

end:
    if (createReportResult.ft)
    {
        CheckResult( "MI_Operation_Close for operation result", MI_Operation_Close(&amp;createReportResult) );
        // This frees objects in the operation
    }

    if (createScheduleResult.ft)
    {
        CheckResult( "MI_Operation_Close for operation result", MI_Operation_Close(&amp;createScheduleResult) );
        // This frees objects in the operation including pSchedule
    }

    if (pStorageReport)
    {
        CheckResult( "MI_Instance_Delete for pStorageReport", MI_Instance_Delete(pStorageReport) );
        pStorageReport = NULL;
    }

    if (pScheduledTaskInParams)
    {
        CheckResult( "MI_Instance_Delete for pScheduledTaskInParams", MI_Instance_Delete(pScheduledTaskInParams) );
        pScheduledTaskInParams = NULL;
    }

    if (session.ft)
    {
        CheckResult( "MI_Session_Close", MI_Session_Close(&amp;session, NULL, NULL) );
    }

    if (application.ft)
    {
        CheckResult( "MI_Application_Close", MI_Application_Close(&amp;application) );
    }

    wchar_t chTemp = L'\0';
    ::wprintf(L"\nDone.\nPress \"Enter\" to quit");
    ::wscanf_s(L"%c", &amp;chTemp, 1);
}
```



This is the header named Main.h used by the example above.


```C++
#pragma once

#include <stdio.h>
#include <objbase.h>
#include <assert.h>
#include <tchar.h>
#include <crtdbg.h>

#define MI_CHAR_TYPE 2 // Maps MI_CHAR to wchar_t

#include <mi.h>

inline
bool
CheckResult(
    __in PCSTR pwszOperation, 
    __in MI_Result Result
    )
{
    if (Result != MI_RESULT_OK)
    {
        fwprintf(stderr, L"%s failed with MI Result = %d\n", pwszOperation, Result);
        return false;
    }

    return true;
}

#define CheckResultAndExit(Operation, Result) { if (!CheckResult(Operation, Result)) { goto end; } }
```



## Related topics

<dl> <dt>

**FSRM**
</dt> <dt>

[**MSFT\_FSRMScheduledTask**](msft-fsrmscheduledtask.md)
</dt> <dt>

[**CreateScheduledTask**](msft-fsrmscheduledtask-createscheduledtask.md)
</dt> <dt>

[**MSFT\_FSRMStorageReport**](msft-fsrmstoragereport.md)
</dt> <dt>

**WMI**
</dt> <dt>

[**MI\_Application\_Close**](https://msdn.microsoft.com/library/hh437437)
</dt> <dt>

[**MI\_Application\_Initialize**](https://msdn.microsoft.com/library/hh437439)
</dt> <dt>

[**MI\_Application\_NewInstance**](https://msdn.microsoft.com/library/hh448848)
</dt> <dt>

[**MI\_Application\_NewParameterSet**](https://msdn.microsoft.com/library/hh448852)
</dt> <dt>

[**MI\_Application\_NewSession**](https://msdn.microsoft.com/library/hh448856)
</dt> <dt>

[**MI\_Instance\_AddElement**](https://msdn.microsoft.com/library/hh449170)
</dt> <dt>

[**MI\_Instance\_Delete**](https://msdn.microsoft.com/library/hh449179)
</dt> <dt>

[**MI\_Instance\_GetElement**](https://msdn.microsoft.com/library/hh449186)
</dt> <dt>

[**MI\_Operation\_Close**](https://msdn.microsoft.com/library/hh449271)
</dt> <dt>

[**MI\_Operation\_GetInstance**](https://msdn.microsoft.com/library/hh449277)
</dt> <dt>

[**MI\_Session\_Close**](https://msdn.microsoft.com/library/hh437515)
</dt> <dt>

[**MI\_Session\_CreateInstance**](https://msdn.microsoft.com/library/hh437518)
</dt> <dt>

[**MI\_Session\_Invoke**](https://msdn.microsoft.com/library/hh437537)
</dt> </dl>

 

 




