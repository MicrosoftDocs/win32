---
description: The following example shows how to use the trace data helper functions to retrieve metadata for each event.
ms.assetid: 599e0405-b125-4742-b134-964e25413f59
title: Retrieving Event Metadata
ms.topic: article
ms.date: 05/31/2018
---

# Retrieving Event Metadata

The following example shows how to use the trace data helper functions to retrieve metadata for each event. Also see the examples included with the [**TdhQueryProviderFieldInformation**](/windows/desktop/api/Tdh/nf-tdh-tdhqueryproviderfieldinformation) and [**TdhEnumerateProviderFieldInformation**](/windows/desktop/api/Tdh/nf-tdh-tdhenumerateproviderfieldinformation) functions.


```C++
//Turns the DEFINE_GUID for EventTraceGuid into a const.
#define INITGUID

#include <windows.h>
#include <stdio.h>
#include <comdef.h>
#include <guiddef.h>
#include <wbemidl.h>
#include <wmistr.h>
#include <evntrace.h>
#include <tdh.h>

#pragma comment(lib, "tdh.lib")

#define LOGFILE_PATH L"<FULLPATHTOTHELOGFILE.etl>"

static const GUID GUID_NULL = 
{ 0x00000000, 0x0000, 0x0000, { 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 } };

// Strings that represent the source of the event metadata.

WCHAR* pSource[] = {L"XML instrumentation manifest", L"WMI MOF class", L"WPP TMF file"};

// Handle to the trace file that you opened.

TRACEHANDLE g_hTrace = 0;  


// Prototypes

void WINAPI ProcessEvent(PEVENT_RECORD pEvent);
DWORD GetEventInformation(PEVENT_RECORD pEvent, PTRACE_EVENT_INFO & pInfo);
DWORD PrintPropertyMetadata(TRACE_EVENT_INFO* pInfo, DWORD i, USHORT indent);


void wmain(void)
{
    ULONG status = ERROR_SUCCESS;
    EVENT_TRACE_LOGFILE trace;
    TRACE_LOGFILE_HEADER* pHeader = &trace.LogfileHeader;

    // Identify the log file from which you want to consume events
    // and the callbacks used to process the events and buffers.

    ZeroMemory(&trace, sizeof(EVENT_TRACE_LOGFILE));
    trace.LogFileName = (LPWSTR) LOGFILE_PATH;
    trace.EventRecordCallback = (PEVENT_RECORD_CALLBACK) (ProcessEvent);
    trace.ProcessTraceMode = PROCESS_TRACE_MODE_EVENT_RECORD;

    g_hTrace = OpenTrace(&trace);
    if (INVALID_PROCESSTRACE_HANDLE == g_hTrace)
    {
        wprintf(L"OpenTrace failed with %lu\n", GetLastError());
        goto cleanup;
    }

    status = ProcessTrace(&g_hTrace, 1, 0, 0);
    if (status != ERROR_SUCCESS && status != ERROR_CANCELLED)
    {
        wprintf(L"ProcessTrace failed with %lu\n", status);
        goto cleanup;
    }

cleanup:

    if (INVALID_PROCESSTRACE_HANDLE != g_hTrace)
    {
        status = CloseTrace(g_hTrace);
    }
}


VOID WINAPI ProcessEvent(PEVENT_RECORD pEvent)
{
    DWORD status = ERROR_SUCCESS;
    HRESULT hr = S_OK;
    PTRACE_EVENT_INFO pInfo = NULL;
    LPWSTR pStringGuid = NULL;


    // Skips the event if it is the event trace header. Log files contain this event
    // but real-time sessions do not. The event contains the same information as 
    // the EVENT_TRACE_LOGFILE.LogfileHeader member that you can access when you open 
    // the trace. 

    if (IsEqualGUID(pEvent->EventHeader.ProviderId, EventTraceGuid) &&
        pEvent->EventHeader.EventDescriptor.Opcode == EVENT_TRACE_TYPE_INFO)
    {
        ; // Skip this event.
    }
    else
    {
        // Process the event. This example does not process the event data but
        // instead prints the metadata that describes each event.

        status = GetEventInformation(pEvent, pInfo);

        if (ERROR_SUCCESS != status)
        {
            wprintf(L"GetEventInformation failed with %lu\n", status);
            goto cleanup;
        }

        wprintf(L"Decoding source: %s\n", pSource[pInfo->DecodingSource]);

        if (DecodingSourceWPP == pInfo->DecodingSource)
        {
            // This example is not rendering WPP metadata.
            goto cleanup;
        }

        if (pInfo->ProviderNameOffset > 0)
        {
            wprintf(L"Provider name: %s\n", (LPWSTR)((PBYTE)(pInfo) + pInfo->ProviderNameOffset));
        }

        hr = StringFromCLSID(pInfo->ProviderGuid, &pStringGuid);
        if (FAILED(hr))
        {
            wprintf(L"StringFromCLSID(ProviderGuid) failed with 0x%x\n", hr);
            status = hr;
            goto cleanup;
        }

        wprintf(L"\nProvider GUID: %s\n", pStringGuid);
        CoTaskMemFree(pStringGuid);
        pStringGuid = NULL;

        if (!IsEqualGUID(pInfo->EventGuid, GUID_NULL))
        {
            hr = StringFromCLSID(pInfo->EventGuid, &pStringGuid);
            if (FAILED(hr))
            {
                wprintf(L"StringFromCLSID(EventGuid) failed with 0x%x\n", hr);
                status = hr;
                goto cleanup;
            }

            wprintf(L"\nEvent GUID: %s\n", pStringGuid);
            CoTaskMemFree(pStringGuid);
            pStringGuid = NULL;
        }


        if (DecodingSourceXMLFile == pInfo->DecodingSource)
        {
            wprintf(L"Event ID: %hu\n", pInfo->EventDescriptor.Id);
        }

        wprintf(L"Version: %d\n", pInfo->EventDescriptor.Version);

        if (pInfo->ChannelNameOffset > 0)
        {
            wprintf(L"Channel name: %s\n", (LPWSTR)((PBYTE)(pInfo) + pInfo->ChannelNameOffset));
        }

        if (pInfo->LevelNameOffset > 0)
        {
            wprintf(L"Level name: %s\n", (LPWSTR)((PBYTE)(pInfo) + pInfo->LevelNameOffset));
        }
        else
        {
            wprintf(L"Level: %hu\n", pInfo->EventDescriptor.Level);
        }

        if (DecodingSourceXMLFile == pInfo->DecodingSource)
        {
            if (pInfo->OpcodeNameOffset > 0)
            {
                wprintf(L"Opcode name: %s\n", (LPWSTR)((PBYTE)(pInfo) + pInfo->OpcodeNameOffset));
            }
        }
        else
        {
            wprintf(L"Type: %hu\n", pInfo->EventDescriptor.Opcode);
        }

        if (DecodingSourceXMLFile == pInfo->DecodingSource)
        {
            if (pInfo->TaskNameOffset > 0)
            {
                wprintf(L"Task name: %s\n", (LPWSTR)((PBYTE)(pInfo) + pInfo->TaskNameOffset));
            }
        }
        else
        {
            wprintf(L"Task: %hu\n", pInfo->EventDescriptor.Task);
        }

        wprintf(L"Keyword mask: 0x%x\n", pInfo->EventDescriptor.Keyword);
        if (pInfo->KeywordsNameOffset)
        {
            LPWSTR pKeyword = (LPWSTR)((PBYTE)(pInfo) + pInfo->KeywordsNameOffset);

            for (; *pKeyword != 0; pKeyword += (wcslen(pKeyword) + 1))
                wprintf(L"  Keyword name: %s\n", pKeyword);
        }

        if (pInfo->EventMessageOffset > 0)
        {
            wprintf(L"Event message: %s\n", (LPWSTR)((PBYTE)(pInfo) + pInfo->EventMessageOffset));
        }

        if (pInfo->ActivityIDNameOffset > 0)
        {
            wprintf(L"Activity ID name: %s\n", (LPWSTR)((PBYTE)(pInfo) + pInfo->ActivityIDNameOffset));
        }

        if (pInfo->RelatedActivityIDNameOffset > 0)
        {
            wprintf(L"Related activity ID name: %s\n", (LPWSTR)((PBYTE)(pInfo) + pInfo->RelatedActivityIDNameOffset));
        }

        wprintf(L"Number of top-level properties: %lu\n", pInfo->TopLevelPropertyCount);

        wprintf(L"Total number of properties: %lu\n", pInfo->PropertyCount);

        // Print the metadata for all the top-level properties. Metadata for all the 
        // top-level properties come before structure member properties in the 
        // property information array.

        if (pInfo->TopLevelPropertyCount > 0)
        {
            wprintf(L"\nThe following are the user data properties defined for this event:\n");

            for (USHORT i = 0; i < pInfo->TopLevelPropertyCount; i++)
            {
                status = PrintPropertyMetadata(pInfo, i, 0);
                if (ERROR_SUCCESS != status)
                {
                    wprintf(L"Printing metadata for top-level properties failed.\n");
                    goto cleanup;
                }
            }
        }
        else
        {
            wprintf(L"\nThe event does not define any user data properties.\n");
        }

        wprintf(L"\n");
    }

cleanup:

    if (pInfo)
    {
        free(pInfo);
    }

    if (ERROR_SUCCESS != status)
    {
        CloseTrace(g_hTrace);
    }
}



DWORD GetEventInformation(PEVENT_RECORD pEvent, PTRACE_EVENT_INFO & pInfo)
{
    DWORD status = ERROR_SUCCESS;
    DWORD BufferSize = 0;

    // Retrieve the required buffer size for the event metadata.

    status = TdhGetEventInformation(pEvent, 0, NULL, pInfo, &BufferSize);

    if (ERROR_INSUFFICIENT_BUFFER == status)
    {
        pInfo = (TRACE_EVENT_INFO*) malloc(BufferSize);
        if (pInfo == NULL)
        {
            wprintf(L"Failed to allocate memory for event info (size=%lu).\n", BufferSize);
            status = ERROR_OUTOFMEMORY;
            goto cleanup;
        }

        // Retrieve the event metadata.

        status = TdhGetEventInformation(pEvent, 0, NULL, pInfo, &BufferSize);
    }

    if (ERROR_SUCCESS != status)
    {
        wprintf(L"TdhGetEventInformation failed with 0x%x.\n", status);
    }

cleanup:

    return status;
}


// Print the metadata for each property.

DWORD PrintPropertyMetadata(TRACE_EVENT_INFO* pinfo, DWORD i, USHORT indent)
{
    DWORD status = ERROR_SUCCESS;
    DWORD j = 0;
    DWORD lastMember = 0;  // Last member of a structure

    // Print property name.

    wprintf(L"%*s%s", indent, L"", (LPWSTR)((PBYTE)(pinfo) + pinfo->EventPropertyInfoArray[i].NameOffset));


    // If the property is an array, the property can define the array size or it can
    // point to another property whose value defines the array size. The PropertyParamCount
    // flag tells you where the array size is defined.

    if ((pinfo->EventPropertyInfoArray[i].Flags & PropertyParamCount) == PropertyParamCount)
    {
        j = pinfo->EventPropertyInfoArray[i].countPropertyIndex;
        wprintf(L" (array size is defined by %s)", (LPWSTR)((PBYTE)(pinfo) + pinfo->EventPropertyInfoArray[j].NameOffset));
    }
    else
    {
        if (pinfo->EventPropertyInfoArray[i].count > 1)
            wprintf(L" (array size is %lu)", pinfo->EventPropertyInfoArray[i].count);
    }


    // If the property is a buffer, the property can define the buffer size or it can
    // point to another property whose value defines the buffer size. The PropertyParamLength
    // flag tells you where the buffer size is defined.

    if ((pinfo->EventPropertyInfoArray[i].Flags & PropertyParamLength) == PropertyParamLength)
    {
        j = pinfo->EventPropertyInfoArray[i].lengthPropertyIndex;
        wprintf(L" (size is defined by %s)", (LPWSTR)((PBYTE)(pinfo) + pinfo->EventPropertyInfoArray[j].NameOffset));
    }
    else
    {
        // Variable length properties such as structures and some strings do not have
        // length definitions.

        if (pinfo->EventPropertyInfoArray[i].length > 0)
            wprintf(L" (size is %lu bytes)", pinfo->EventPropertyInfoArray[i].length);
        else
            wprintf(L" (size  is unknown)");
    }

    wprintf(L"\n");


    // If the property is a structure, print the members of the structure.

    if ((pinfo->EventPropertyInfoArray[i].Flags & PropertyStruct) == PropertyStruct)
    {
        wprintf(L"%*s(The property is a structure and has the following %hu members:)\n", 4, L"",
            pinfo->EventPropertyInfoArray[i].structType.NumOfStructMembers);

        lastMember = pinfo->EventPropertyInfoArray[i].structType.StructStartIndex + 
            pinfo->EventPropertyInfoArray[i].structType.NumOfStructMembers;

        for (j = pinfo->EventPropertyInfoArray[i].structType.StructStartIndex; j < lastMember; j++)
        {
            PrintPropertyMetadata(pinfo, j, 4);
        }
    }
    else
    {
        // You can use InType to determine the data type of the member and OutType
        // to determine the output format of the data.

        if (pinfo->EventPropertyInfoArray[i].nonStructType.MapNameOffset)
        {
            // You can pass the name to the TdhGetEventMapInformation function to 
            // retrieve metadata about the value map.

            wprintf(L"%*s(Map attribute name is %s)\n", indent, L"", 
                (PWCHAR)((PBYTE)(pinfo) + pinfo->EventPropertyInfoArray[i].nonStructType.MapNameOffset));
        }
    }

    return status;
}
```



 

 



