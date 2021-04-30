---
description: The following example shows you how to use events to calculate the CPU usage for a set of instructions. This example assumes the provider wraps the instruction set with a start event type and an end event type.
ms.assetid: 7bc15ed3-d299-40dd-9838-520f896921e3
title: Using Events to Calculate CPU Usage
ms.topic: article
ms.date: 05/31/2018
---

# Using Events to Calculate CPU Usage

The following example shows you how to use events to calculate the CPU usage for a set of instructions. This example assumes the provider wraps the instruction set with a start event type and an end event type.


```C++
//Turns the DEFINE_GUID for EventTraceGuid into a const.
#define INITGUID

#include <windows.h>
#include <stdio.h>
#include <wbemidl.h>
#include <wmistr.h>
#include <evntrace.h>


#define LOGFILE_PATH L"<FULLPATHTOLOGFILE.etl>"

//Remember to use your own GUID. Event class GUID used in the provider.

// {12BF20F2-0B1C-47e8-90B3-13C81C7AFD9A}
static const GUID CpuUsageEvent = 
{ 0x12bf20f2, 0xb1c, 0x47e8, { 0x90, 0xb3, 0x13, 0xc8, 0x1c, 0x7a, 0xfd, 0x9a } };

// Used to calculate CPU usage
ULONG g_TimerResolution = 0;

// Used to determine if the session is a private session or kernel session.
// You need to know this when accessing some members of the EVENT_TRACE.Header
// member (for example, KernelTime or UserTime).
BOOL g_bUserMode = FALSE;

//Start time value for the start event.
ULONG g_StartKernelTime = 0;
ULONG g_StartUserTime = 0;
ULONG64 g_StartProcessTime = 0;

void WINAPI ProcessEvent(PEVENT_TRACE pEvent);


void wmain(void)
{
    ULONG status = ERROR_SUCCESS;
    EVENT_TRACE_LOGFILE trace;
    TRACE_LOGFILE_HEADER* pHeader = &trace.LogfileHeader;
    TRACEHANDLE hTrace = 0;  

    // Identify the log file from which you want to consume events
    // and the callbacks used to process the events and buffers.

    ZeroMemory(&trace, sizeof(EVENT_TRACE_LOGFILE));
    trace.LogFileName = (LPWSTR) LOGFILE_PATH;
    trace.EventCallback = (PEVENT_CALLBACK) (ProcessEvent);

    hTrace = OpenTrace(&trace);
    if ((TRACEHANDLE)INVALID_HANDLE_VALUE == hTrace)
    {
        wprintf(L"OpenTrace failed with %lu\n", GetLastError());
        goto cleanup;
    }

    g_bUserMode = pHeader->LogFileMode & EVENT_TRACE_PRIVATE_LOGGER_MODE;

    if (pHeader->TimerResolution > 0)
    {
        g_TimerResolution = pHeader->TimerResolution / 10000;
    }

    status = ProcessTrace(&hTrace, 1, 0, 0);
    if (status != ERROR_SUCCESS && status != ERROR_CANCELLED)
    {
        wprintf(L"ProcessTrace failed with %lu\n", status);
        goto cleanup;
    }

cleanup:

    if ((TRACEHANDLE)INVALID_HANDLE_VALUE != hTrace)
    {
        status = CloseTrace(hTrace);
    }
}


VOID WINAPI ProcessEvent(PEVENT_TRACE pEvent)
{
    ULONG64 CPUProcessUnits = 0;
    ULONG CPUUnits = 0;
    double CPUTime = 0;


    // Skips the event if it is the event trace header. Log files contain this event
    // but real-time sessions do not. The event contains the same information as 
    // the EVENT_TRACE_LOGFILE.LogfileHeader member that you can access when you open 
    // the trace. 

    if (IsEqualGUID(pEvent->Header.Guid, EventTraceGuid) &&
        pEvent->Header.Class.Type == EVENT_TRACE_TYPE_INFO)
    {
        ; // Skip this event.
    }
    else
    {
        if (IsEqualGUID(CpuUsageEvent, pEvent->Header.Guid))
        {
            // This example assumes that the start and end events are paired.
            // If this is the start event type, retrieve the start time values from the 
            // event; otherwise, retrieve the end time values from the event.

            if (pEvent->Header.Class.Type == EVENT_TRACE_TYPE_START)
            {
                // If the session is a private session, use the ProcessorTime
                // value to calculate the CPU time; otherwise, use the 
                // KernelTime and UserTime values.

                if (g_bUserMode) // Private session
                {
                    g_StartProcessTime = pEvent->Header.ProcessorTime;
                }
                else  // Kernel session
                {
                    g_StartKernelTime = pEvent->Header.KernelTime;
                    g_StartUserTime = pEvent->Header.UserTime;
                }
            }
            else if (pEvent->Header.Class.Type == EVENT_TRACE_TYPE_END)
            {
                if (g_bUserMode) // Private session
                {
                    // Calculate CPU time units used.

                    CPUProcessUnits = pEvent->Header.ProcessorTime - g_StartProcessTime;
                    wprintf(L"CPU time units used, %Lu.\n", CPUProcessUnits);

                    // Processor time is in CPU ticks. Convert ticks to seconds.
                    // 1000000000 = nanoseconds in one second.

                    CPUTime = (double)(CPUProcessUnits) / 1000000000;
                    wprintf(L"Process CPU usage in seconds, %Lf.\n", CPUTime);
                }
                else  // Kernel session
                {
                    // Calculate the kernel mode CPU time units used for the set of instructions.

                    CPUUnits = pEvent->Header.KernelTime - g_StartKernelTime;
                    wprintf(L"CPU time units used (kernel), %d.\n", CPUUnits);

                    // Calculate the kernel mode CPU time in seconds for the set of instructions.
                    // 100 = 100 nanoseconds, 1000000000 = nanoseconds in one second

                    CPUTime = (double)(g_TimerResolution * CPUUnits * 100) / 1000000000;
                    wprintf(L"Kernel mode CPU usage in seconds, %Lf.\n", CPUTime);

                    // Calculate user mode CPU time units used for the set of instructions.

                    CPUUnits = pEvent->Header.UserTime - g_StartUserTime;
                    wprintf(L"\nCPU time units used (user), %d.\n", CPUUnits);

                    // Calculate the user mode CPU time in seconds for the set of instructions.
                    // 100 = 100 nanoseconds, 1000000000 = nanoseconds in one second

                    CPUTime = (double)(g_TimerResolution * CPUUnits * 100) / 1000000000;
                    wprintf(L"User mode CPU usage in seconds, %Lf.\n", CPUTime);
                }
            }
        }
    }
}
```



 

 



