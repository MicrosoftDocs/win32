---
description: The following example shows how to consume event data using the TdhGetProperty function.
ms.assetid: 16b36718-087f-4be9-9ca2-fc083358017b
title: Using TdhGetProperty to Consume Event Data
ms.topic: article
ms.date: 05/31/2018
---

# Using TdhGetProperty to Consume Event Data

The following example shows how to consume event data using the [**TdhGetProperty**](/windows/desktop/api/Tdh/nf-tdh-tdhgetproperty) function.


```C++
//Turns the DEFINE_GUID for EventTraceGuid into a const.
#define INITGUID

#include <windows.h>
#include <stdio.h>
#include <strsafe.h>
#include <wbemidl.h>
#include <wmistr.h>
#include <evntrace.h>
#include <tdh.h>
#include <in6addr.h>

#pragma comment(lib, "tdh.lib")
#pragma comment(lib, "ws2_32.lib")  // For ntohs function

#define LOGFILE_PATH L"C:\\Code\\etw\\V2EventTraceController\\mylogfile.etl"

#define MAX_NAME 256

// Used to determine the data size of property values that contain a
// Pointer value. The value will be 4 or 8.
USHORT g_PointerSize = 0;

// Used to calculate CPU usage

ULONG g_TimerResolution = 0;

// Used to determine if the session is a private session or kernel session.
// You need to know this when accessing some members of the EVENT_TRACE.Header
// member (for example, KernelTime or UserTime).

BOOL g_bUserMode = FALSE;

// Handle to the trace file that you opened.

TRACEHANDLE g_hTrace = 0;  


// Prototypes

void WINAPI ProcessEvent(PEVENT_RECORD pEvent);
DWORD GetEventInformation(PEVENT_RECORD pEvent, PTRACE_EVENT_INFO & pInfo);
DWORD PrintProperties(PEVENT_RECORD pEvent, PTRACE_EVENT_INFO pInfo, USHORT i, LPWSTR pStructureName, USHORT StructIndex);
DWORD FormatAndPrintData(PEVENT_RECORD pEvent, USHORT InType, USHORT OutType, PBYTE pData, DWORD DataSize, PEVENT_MAP_INFO pMapInfo); 
void PrintMapString(PEVENT_MAP_INFO pMapInfo, PBYTE pData);
DWORD GetArraySize(PEVENT_RECORD pEvent, PTRACE_EVENT_INFO pInfo, USHORT i, PUSHORT ArraySize);
DWORD GetMapInfo(PEVENT_RECORD pEvent, LPWSTR pMapName, DWORD DecodingSource, PEVENT_MAP_INFO & pMapInfo);
void RemoveTrailingSpace(PEVENT_MAP_INFO pMapInfo);

typedef LPTSTR (NTAPI *PIPV6ADDRTOSTRING)(
  const IN6_ADDR *Addr,
  LPTSTR S
);


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

    g_bUserMode = pHeader->LogFileMode & EVENT_TRACE_PRIVATE_LOGGER_MODE;

    if (pHeader->TimerResolution > 0)
    {
        g_TimerResolution = pHeader->TimerResolution / 10000;
    }

    wprintf(L"Number of events lost:  %lu\n", pHeader->EventsLost);

    // Use pHeader to access all fields prior to LoggerName.
    // Adjust pHeader based on the pointer size to access
    // all fields after LogFileName. This is required only if
    // you are consuming events on an architecture that is 
    // different from architecture used to write the events.

    if (pHeader->PointerSize != sizeof(PVOID))
    {
        pHeader = (PTRACE_LOGFILE_HEADER)((PUCHAR)pHeader +
            2 * (pHeader->PointerSize - sizeof(PVOID)));
    }

    wprintf(L"Number of buffers lost: %lu\n\n", pHeader->BuffersLost);

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


// Callback that receives the events. 

VOID WINAPI ProcessEvent(PEVENT_RECORD pEvent)
{
    DWORD status = ERROR_SUCCESS;
    PTRACE_EVENT_INFO pInfo = NULL;
    LPWSTR pwsEventGuid = NULL;
    ULONGLONG TimeStamp = 0;
    ULONGLONG Nanoseconds = 0;
    SYSTEMTIME st;
    SYSTEMTIME stLocal;
    FILETIME ft;


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
        // Process the event. The pEvent->UserData member is a pointer to 
        // the event specific data, if it exists.

        status = GetEventInformation(pEvent, pInfo);

        if (ERROR_SUCCESS != status)
        {
            wprintf(L"GetEventInformation failed with %lu\n", status);
            goto cleanup;
        }

        // Determine whether the event is defined by a MOF class, in an
        // instrumentation manifest, or a WPP template; to use TDH to decode
        // the event, it must be defined by one of these three sources.

        if (DecodingSourceWbem == pInfo->DecodingSource)  // MOF class
        {
            HRESULT hr = StringFromCLSID(pInfo->EventGuid, &pwsEventGuid);

            if (FAILED(hr))
            {
                wprintf(L"StringFromCLSID failed with 0x%x\n", hr);
                status = hr;
                goto cleanup;
            }

            wprintf(L"\nEvent GUID: %s\n", pwsEventGuid);
            CoTaskMemFree(pwsEventGuid);
            pwsEventGuid = NULL;

            wprintf(L"Event version: %d\n", pEvent->EventHeader.EventDescriptor.Version);
            wprintf(L"Event type: %d\n", pEvent->EventHeader.EventDescriptor.Opcode);
        }
        else if (DecodingSourceXMLFile == pInfo->DecodingSource) // Instrumentation manifest
        {
            wprintf(L"Event ID: %d\n", pInfo->EventDescriptor.Id);
        }
        else // Not handling the WPP case
        {
            goto cleanup;
        }

        // Print the time stamp for when the event occurred.

        ft.dwHighDateTime = pEvent->EventHeader.TimeStamp.HighPart;
        ft.dwLowDateTime = pEvent->EventHeader.TimeStamp.LowPart;

        FileTimeToSystemTime(&ft, &st);
        SystemTimeToTzSpecificLocalTime(NULL, &st, &stLocal);

        TimeStamp = pEvent->EventHeader.TimeStamp.QuadPart;
        Nanoseconds = (TimeStamp % 10000000) * 100;

        wprintf(L"%02d/%02d/%02d %02d:%02d:%02d.%I64u\n", 
            stLocal.wMonth, stLocal.wDay, stLocal.wYear, stLocal.wHour, stLocal.wMinute, stLocal.wSecond, Nanoseconds);

        // If the event contains event-specific data use TDH to extract
        // the event data. For this example, to extract the data, the event 
        // must be defined by a MOF class or an instrumentation manifest.

        // Need to get the PointerSize for each event to cover the case where you are
        // consuming events from multiple log files that could have been generated on 
        // different architectures. Otherwise, you could have accessed the pointer
        // size when you opened the trace above (see pHeader->PointerSize).

        if (EVENT_HEADER_FLAG_32_BIT_HEADER == (pEvent->EventHeader.Flags & EVENT_HEADER_FLAG_32_BIT_HEADER))
        {
            g_PointerSize = 4;
        }
        else
        {
            g_PointerSize = 8;
        }

        // Print the event data for all the top-level properties. Metadata for all the 
        // top-level properties come before structure member properties in the 
        // property information array. If the EVENT_HEADER_FLAG_STRING_ONLY flag is set,
        // the event data is a null-terminated string, so just print it.

        if (EVENT_HEADER_FLAG_STRING_ONLY == (pEvent->EventHeader.Flags & EVENT_HEADER_FLAG_STRING_ONLY))
        {
            wprintf(L"%s\n", (LPWSTR)pEvent->UserData);
        }
        else
        {
            for (USHORT i = 0; i < pInfo->TopLevelPropertyCount; i++)
            {
                status = PrintProperties(pEvent, pInfo, i, NULL, 0);
                if (ERROR_SUCCESS != status)
                {
                    wprintf(L"Printing top level properties failed.\n");
                    goto cleanup;
                }
            }
        }
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


// Print the property.

DWORD PrintProperties(PEVENT_RECORD pEvent, PTRACE_EVENT_INFO pInfo, USHORT i, LPWSTR pStructureName, USHORT StructIndex)
{
    DWORD status = ERROR_SUCCESS;
    DWORD LastMember = 0;  // Last member of a structure
    USHORT ArraySize = 0;
    PEVENT_MAP_INFO pMapInfo = NULL;
    PROPERTY_DATA_DESCRIPTOR DataDescriptors[2];
    ULONG DescriptorsCount = 0;
    DWORD PropertySize = 0;
    PBYTE pData = NULL;

    // Get the size of the array if the property is an array.

    status = GetArraySize(pEvent, pInfo, i, &ArraySize);

    for (USHORT k = 0; k < ArraySize; k++)
    {
        wprintf(L"%*s%s: ", (pStructureName) ? 4 : 0, L"", (LPWSTR)((PBYTE)(pInfo) + pInfo->EventPropertyInfoArray[i].NameOffset));

        // If the property is a structure, print the members of the structure.

        if ((pInfo->EventPropertyInfoArray[i].Flags & PropertyStruct) == PropertyStruct)
        {
            wprintf(L"\n");

            LastMember = pInfo->EventPropertyInfoArray[i].structType.StructStartIndex + 
                pInfo->EventPropertyInfoArray[i].structType.NumOfStructMembers;

            for (USHORT j = pInfo->EventPropertyInfoArray[i].structType.StructStartIndex; j < LastMember; j++)
            {
                status = PrintProperties(pEvent, pInfo, j, (LPWSTR)((PBYTE)(pInfo) + pInfo->EventPropertyInfoArray[i].NameOffset), k);
                if (ERROR_SUCCESS != status)
                {
                    wprintf(L"Printing the members of the structure failed.\n");
                    goto cleanup;
                }
            }
        }
        else
        {
            ZeroMemory(&DataDescriptors, sizeof(DataDescriptors));

            // To retrieve a member of a structure, you need to specify an array of descriptors. 
            // The first descriptor in the array identifies the name of the structure and the second 
            // descriptor defines the member of the structure whose data you want to retrieve. 

            if (pStructureName)
            {
                DataDescriptors[0].PropertyName = (ULONGLONG)pStructureName;
                DataDescriptors[0].ArrayIndex = StructIndex;
                DataDescriptors[1].PropertyName = (ULONGLONG)((PBYTE)(pInfo) + pInfo->EventPropertyInfoArray[i].NameOffset);
                DataDescriptors[1].ArrayIndex = k;
                DescriptorsCount = 2;
            }
            else
            {
                DataDescriptors[0].PropertyName = (ULONGLONG)((PBYTE)(pInfo) + pInfo->EventPropertyInfoArray[i].NameOffset);
                DataDescriptors[0].ArrayIndex = k;
                DescriptorsCount = 1;
            }

            // The TDH API does not support IPv6 addresses. If the output type is TDH_OUTTYPE_IPV6,
            // you will not be able to consume the rest of the event. If you try to consume the
            // remainder of the event, you will get ERROR_EVT_INVALID_EVENT_DATA.

            if (TDH_INTYPE_BINARY == pInfo->EventPropertyInfoArray[i].nonStructType.InType &&
                TDH_OUTTYPE_IPV6 == pInfo->EventPropertyInfoArray[i].nonStructType.OutType)
            {
                wprintf(L"The event contains an IPv6 address. Skipping event.\n");
                status = ERROR_EVT_INVALID_EVENT_DATA;
                break;
            }
            else
            {
                status = TdhGetPropertySize(pEvent, 0, NULL, DescriptorsCount, &DataDescriptors[0], &PropertySize);

                if (ERROR_SUCCESS != status)
                {
                    wprintf(L"TdhGetPropertySize failed with %lu\n", status);
                    goto cleanup;
                }

                pData = (PBYTE)malloc(PropertySize);

                if (NULL == pData)
                {
                    wprintf(L"Failed to allocate memory for property data\n");
                    status = ERROR_OUTOFMEMORY;
                    goto cleanup;
                }

                status = TdhGetProperty(pEvent, 0, NULL, DescriptorsCount, &DataDescriptors[0], PropertySize, pData);

                // Get the name/value mapping if the property specifies a value map.

                status = GetMapInfo(pEvent, 
                    (PWCHAR)((PBYTE)(pInfo) + pInfo->EventPropertyInfoArray[i].nonStructType.MapNameOffset),
                    pInfo->DecodingSource,
                    pMapInfo);

                if (ERROR_SUCCESS != status)
                {
                    wprintf(L"GetMapInfo failed\n");
                    goto cleanup;
                }

                status = FormatAndPrintData(pEvent, 
                    pInfo->EventPropertyInfoArray[i].nonStructType.InType,
                    pInfo->EventPropertyInfoArray[i].nonStructType.OutType,
                    pData, 
                    PropertySize,
                    pMapInfo 
                    );

                if (ERROR_SUCCESS != status)
                {
                    wprintf(L"GetMapInfo failed\n");
                    goto cleanup;
                }

                if (pData)
                {
                    free(pData);
                    pData = NULL;
                }

                if (pMapInfo)
                {
                    free(pMapInfo);
                    pMapInfo = NULL;
                }
            }
        }
    }

cleanup:

    if (pData)
    {
        free(pData);
        pData = NULL;
    }

    if (pMapInfo)
    {
        free(pMapInfo);
        pMapInfo = NULL;
    }

    return status;
}


DWORD FormatAndPrintData(PEVENT_RECORD pEvent, USHORT InType, USHORT OutType, PBYTE pData, DWORD DataSize, PEVENT_MAP_INFO pMapInfo)
{
    UNREFERENCED_PARAMETER(pEvent);
    
    DWORD status = ERROR_SUCCESS;

    switch (InType)
    {
        case TDH_INTYPE_UNICODESTRING:
        case TDH_INTYPE_COUNTEDSTRING:
        case TDH_INTYPE_REVERSEDCOUNTEDSTRING:
        case TDH_INTYPE_NONNULLTERMINATEDSTRING:
        {
            size_t StringLength = 0;

            if (TDH_INTYPE_COUNTEDSTRING == InType)
            {
                StringLength = *(PUSHORT)pData;
            }
            else if (TDH_INTYPE_REVERSEDCOUNTEDSTRING == InType)
            {
                StringLength = MAKEWORD(HIBYTE((PUSHORT)pData), LOBYTE((PUSHORT)pData));
            }
            else if (TDH_INTYPE_NONNULLTERMINATEDSTRING == InType)
            {
                StringLength = DataSize;
            }
            else
            {
                StringLength = wcslen((LPWSTR)pData);
            }

            wprintf(L"%.*s\n", StringLength, (LPWSTR)pData);
            break;
        }

        case TDH_INTYPE_ANSISTRING:
        case TDH_INTYPE_COUNTEDANSISTRING:
        case TDH_INTYPE_REVERSEDCOUNTEDANSISTRING:
        case TDH_INTYPE_NONNULLTERMINATEDANSISTRING:
        {
            size_t StringLength = 0;

            if (TDH_INTYPE_COUNTEDANSISTRING == InType)
            {
                StringLength = *(PUSHORT)pData;
            }
            else if (TDH_INTYPE_REVERSEDCOUNTEDANSISTRING == InType)
            {
                StringLength = MAKEWORD(HIBYTE((PUSHORT)pData), LOBYTE((PUSHORT)pData));
            }
            else if (TDH_INTYPE_NONNULLTERMINATEDANSISTRING == InType)
            {
                StringLength = DataSize;
            }
            else
            {
                StringLength = strlen((LPSTR)pData);
            }

            wprintf(L"%.*S\n", StringLength, (LPSTR)pData);
            break;
        }

        case TDH_INTYPE_INT8:
        {
            wprintf(L"%hd\n", *(PCHAR)pData);
            break;
        }

        case TDH_INTYPE_UINT8:
        {
            if (TDH_OUTTYPE_HEXINT8 == OutType)
            {
                wprintf(L"0x%x\n", *(PBYTE)pData);
            }
            else
            {
                wprintf(L"%hu\n", *(PBYTE)pData);
            }

            break;
        }

        case TDH_INTYPE_INT16:
        {
            wprintf(L"%hd\n", *(PSHORT)pData);
            break;
        }

        case TDH_INTYPE_UINT16:
        {
            if (TDH_OUTTYPE_HEXINT16 == OutType)
            {
                wprintf(L"0x%x\n", *(PUSHORT)pData);
            }
            else if (TDH_OUTTYPE_PORT == OutType)
            {
                wprintf(L"%hu\n", ntohs(*(PUSHORT)pData));
            }
            else
            {
                wprintf(L"%hu\n", *(PUSHORT)pData);
            }

            break;
        }

        case TDH_INTYPE_INT32:
        {
            if (TDH_OUTTYPE_HRESULT == OutType)
            {
                wprintf(L"0x%x\n", *(PLONG)pData);
            }
            else
            {
                wprintf(L"%d\n", *(PLONG)pData);
            }

            break;
        }

        case TDH_INTYPE_UINT32:
        {
            if (TDH_OUTTYPE_HRESULT == OutType ||
                TDH_OUTTYPE_WIN32ERROR == OutType ||
                TDH_OUTTYPE_NTSTATUS == OutType ||
                TDH_OUTTYPE_HEXINT32 == OutType)
            {
                wprintf(L"0x%x\n", *(PULONG)pData);
            }
            else if (TDH_OUTTYPE_IPV4 == OutType)
            {
                wprintf(L"%d.%d.%d.%d\n", (*(PLONG)pData >>  0) & 0xff,
                                          (*(PLONG)pData >>  8) & 0xff,
                                          (*(PLONG)pData >>  16) & 0xff,
                                          (*(PLONG)pData >>  24) & 0xff);
            }
            else
            {
                if (pMapInfo)
                {
                    PrintMapString(pMapInfo, pData);
                }
                else
                {
                    wprintf(L"%lu\n", *(PULONG)pData);
                }
            }

            break;
        }

        case TDH_INTYPE_INT64:
        {
            wprintf(L"%I64d\n", *(PLONGLONG)pData);

            break;
        }

        case TDH_INTYPE_UINT64:
        {
            if (TDH_OUTTYPE_HEXINT64 == OutType)
            {
                wprintf(L"0x%x\n", *(PULONGLONG)pData);
            }
            else
            {
                wprintf(L"%I64u\n", *(PULONGLONG)pData);
            }

            break;
        }

        case TDH_INTYPE_FLOAT:
        {
            wprintf(L"%f\n", *(PFLOAT)pData);

            break;
        }

        case TDH_INTYPE_DOUBLE:
        {
            wprintf(L"%I64f\n", *(DOUBLE*)pData);

            break;
        }

        case TDH_INTYPE_BOOLEAN:
        {
            wprintf(L"%s\n", (0 == (PBOOL)pData) ? L"false" : L"true");

            break;
        }

        case TDH_INTYPE_BINARY:
        {
            if (TDH_OUTTYPE_IPV6 == OutType)
            {
                WCHAR IPv6AddressAsString[46];
                PIPV6ADDRTOSTRING fnRtlIpv6AddressToString;

                fnRtlIpv6AddressToString = (PIPV6ADDRTOSTRING)GetProcAddress(
                    GetModuleHandle(L"ntdll"), "RtlIpv6AddressToStringW");

                if (NULL == fnRtlIpv6AddressToString)
                {
                    wprintf(L"GetProcAddress failed with %lu.\n", status = GetLastError());
                    goto cleanup;
                }

                fnRtlIpv6AddressToString((IN6_ADDR*)pData, IPv6AddressAsString);

                wprintf(L"%s\n", IPv6AddressAsString);
            }
            else
            {
                for (DWORD i = 0; i < DataSize; i++)
                {
                    wprintf(L"%.2x", pData[i]);
                }

                wprintf(L"\n");
            }

            break;
        }

        case TDH_INTYPE_GUID:
        {
            WCHAR szGuid[50];
            
            StringFromGUID2(*(GUID*)pData, szGuid, sizeof(szGuid)-1);
            wprintf(L"%s\n", szGuid);
                
            break;
        }

        case TDH_INTYPE_POINTER:
        case TDH_INTYPE_SIZET:
        {
            if (4 == g_PointerSize)
            {
                wprintf(L"0x%x\n", *(PULONG)pData);
            }
            else
            {
                wprintf(L"0x%x\n", *(PULONGLONG)pData);
            }

            break;
        }

        case TDH_INTYPE_FILETIME:
        {
            break;
        }

        case TDH_INTYPE_SYSTEMTIME:
        {
            break;
        }

        case TDH_INTYPE_SID:
        {
            WCHAR UserName[MAX_NAME];
            WCHAR DomainName[MAX_NAME];
            DWORD cchUserSize = MAX_NAME;
            DWORD cchDomainSize = MAX_NAME;
            SID_NAME_USE eNameUse;

            if (!LookupAccountSid(NULL, (PSID)pData, UserName, &cchUserSize, DomainName, &cchDomainSize, &eNameUse))
            {
                if (ERROR_NONE_MAPPED == status)
                {
                    wprintf(L"Unable to locate account for the specified SID\n");
                    status = ERROR_SUCCESS;
                }
                else
                {
                    wprintf(L"LookupAccountSid failed with %lu\n", status = GetLastError());
                }

                goto cleanup;
            }
            else
            {
                wprintf(L"%s\\%s\n", DomainName, UserName);
            }

            break;
        }

        case TDH_INTYPE_HEXINT32:
        {
            wprintf(L"0x%x\n", (PULONG)pData);
            break;
        }

        case TDH_INTYPE_HEXINT64:
        {
            wprintf(L"0x%x\n", (PULONGLONG)pData);
            break;
        }

        case TDH_INTYPE_UNICODECHAR:
        {
            wprintf(L"%c\n", *(PWCHAR)pData);
            break;
        }

        case TDH_INTYPE_ANSICHAR:
        {
            wprintf(L"%C\n", *(PCHAR)pData);
            break;
        }

        case TDH_INTYPE_WBEMSID:
        {
            WCHAR UserName[MAX_NAME];
            WCHAR DomainName[MAX_NAME];
            DWORD cchUserSize = MAX_NAME;
            DWORD cchDomainSize = MAX_NAME;
            SID_NAME_USE eNameUse;

            if ((PULONG)pData > 0)
            {
                // A WBEM SID is actually a TOKEN_USER structure followed 
                // by the SID. The size of the TOKEN_USER structure differs 
                // depending on whether the events were generated on a 32-bit 
                // or 64-bit architecture. Also the structure is aligned
                // on an 8-byte boundary, so its size is 8 bytes on a
                // 32-bit computer and 16 bytes on a 64-bit computer.
                // Doubling the pointer size handles both cases.

                pData += g_PointerSize * 2;

                if (!LookupAccountSid(NULL, (PSID)pData, UserName, &cchUserSize, DomainName, &cchDomainSize, &eNameUse))
                {
                    if (ERROR_NONE_MAPPED == status)
                    {
                        wprintf(L"Unable to locate account for the specified SID\n");
                        status = ERROR_SUCCESS;
                    }
                    else
                    {
                        wprintf(L"LookupAccountSid failed with %lu\n", status = GetLastError());
                    }

                    goto cleanup;
                }
                else
                {
                    wprintf(L"%s\\%s\n", DomainName, UserName);
                }
            }

            break;
        }

    default:
        status = ERROR_NOT_FOUND;
    }

cleanup:

    return status;
}


void PrintMapString(PEVENT_MAP_INFO pMapInfo, PBYTE pData)
{
    BOOL MatchFound = FALSE;

    if ((pMapInfo->Flag & EVENTMAP_INFO_FLAG_MANIFEST_VALUEMAP) == EVENTMAP_INFO_FLAG_MANIFEST_VALUEMAP ||
        ((pMapInfo->Flag & EVENTMAP_INFO_FLAG_WBEM_VALUEMAP) == EVENTMAP_INFO_FLAG_WBEM_VALUEMAP &&
        (pMapInfo->Flag & (~EVENTMAP_INFO_FLAG_WBEM_VALUEMAP)) != EVENTMAP_INFO_FLAG_WBEM_FLAG))
    {
        if ((pMapInfo->Flag & EVENTMAP_INFO_FLAG_WBEM_NO_MAP) == EVENTMAP_INFO_FLAG_WBEM_NO_MAP)
        {
            wprintf(L"%s\n", (LPWSTR)((PBYTE)pMapInfo + pMapInfo->MapEntryArray[*(PULONG)pData].OutputOffset));
        }
        else
        {
            for (DWORD i = 0; i < pMapInfo->EntryCount; i++)
            {
                if (pMapInfo->MapEntryArray[i].Value == *(PULONG)pData)
                {
                    wprintf(L"%s\n", (LPWSTR)((PBYTE)pMapInfo + pMapInfo->MapEntryArray[i].OutputOffset));
                    MatchFound = TRUE;
                    break;
                }
            }

            if (FALSE == MatchFound)
            {
                wprintf(L"%lu\n", *(PULONG)pData);
            }
        }
    }
    else if ((pMapInfo->Flag & EVENTMAP_INFO_FLAG_MANIFEST_BITMAP) == EVENTMAP_INFO_FLAG_MANIFEST_BITMAP ||
        (pMapInfo->Flag & EVENTMAP_INFO_FLAG_WBEM_BITMAP) == EVENTMAP_INFO_FLAG_WBEM_BITMAP ||
        ((pMapInfo->Flag & EVENTMAP_INFO_FLAG_WBEM_VALUEMAP) == EVENTMAP_INFO_FLAG_WBEM_VALUEMAP &&
        (pMapInfo->Flag & (~EVENTMAP_INFO_FLAG_WBEM_VALUEMAP)) == EVENTMAP_INFO_FLAG_WBEM_FLAG))
    {
        if ((pMapInfo->Flag & EVENTMAP_INFO_FLAG_WBEM_NO_MAP) == EVENTMAP_INFO_FLAG_WBEM_NO_MAP)
        {
            DWORD BitPosition = 0;

            for (DWORD i = 0; i < pMapInfo->EntryCount; i++)
            {
                if ((*(PULONG)pData & (BitPosition = (1 << i))) == BitPosition)
                {
                    wprintf(L"%s%s", 
                        (MatchFound) ? L" | " : L"", 
                        (LPWSTR)((PBYTE)pMapInfo + pMapInfo->MapEntryArray[i].OutputOffset));

                    MatchFound = TRUE;
                }
            }

        }
        else
        {
            for (DWORD i = 0; i < pMapInfo->EntryCount; i++)
            {
                if ((pMapInfo->MapEntryArray[i].Value & *(PULONG)pData) == pMapInfo->MapEntryArray[i].Value)
                {
                    wprintf(L"%s%s", 
                        (MatchFound) ? L" | " : L"", 
                        (LPWSTR)((PBYTE)pMapInfo + pMapInfo->MapEntryArray[i].OutputOffset));

                    MatchFound = TRUE;
                }
            }
        }

        if (MatchFound)
        {
            wprintf(L"\n");
        }
        else
        {
            wprintf(L"%lu\n", *(PULONG)pData);
        }
    }
}


// Get the size of the array. For MOF-based events, the size is specified in the declaration or using 
// the MAX qualifier. For manifest-based events, the property can specify the size of the array
// using the count attribute. The count attribue can specify the size directly or specify the name 
// of another property in the event data that contains the size.

DWORD GetArraySize(PEVENT_RECORD pEvent, PTRACE_EVENT_INFO pInfo, USHORT i, PUSHORT ArraySize)
{
    DWORD status = ERROR_SUCCESS;
    PROPERTY_DATA_DESCRIPTOR DataDescriptor;
    DWORD PropertySize = 0;

    if ((pInfo->EventPropertyInfoArray[i].Flags & PropertyParamCount) == PropertyParamCount)
    {
        DWORD Count = 0;  // Expects the count to be defined by a UINT16 or UINT32
        DWORD j = pInfo->EventPropertyInfoArray[i].countPropertyIndex;
        ZeroMemory(&DataDescriptor, sizeof(PROPERTY_DATA_DESCRIPTOR));
        DataDescriptor.PropertyName = (ULONGLONG)((PBYTE)(pInfo) + pInfo->EventPropertyInfoArray[j].NameOffset);
        DataDescriptor.ArrayIndex = ULONG_MAX;
        status = TdhGetPropertySize(pEvent, 0, NULL, 1, &DataDescriptor, &PropertySize);
        status = TdhGetProperty(pEvent, 0, NULL, 1, &DataDescriptor, PropertySize, (PBYTE)&Count);
        *ArraySize = (USHORT)Count;
    }
    else
    {
        *ArraySize = pInfo->EventPropertyInfoArray[i].count;
    }

    return status;
}


// Both MOF-based events and manifest-based events can specify name/value maps. The
// map values can be integer values or bit values. If the property specifies a value
// map, get the map.

DWORD GetMapInfo(PEVENT_RECORD pEvent, LPWSTR pMapName, DWORD DecodingSource, PEVENT_MAP_INFO & pMapInfo)
{
    DWORD status = ERROR_SUCCESS;
    DWORD MapSize = 0;

    // Retrieve the required buffer size for the map info.

    status = TdhGetEventMapInformation(pEvent, pMapName, pMapInfo, &MapSize);

    if (ERROR_INSUFFICIENT_BUFFER == status)
    {
        pMapInfo = (PEVENT_MAP_INFO) malloc(MapSize);
        if (pMapInfo == NULL)
        {
            wprintf(L"Failed to allocate memory for map info (size=%lu).\n", MapSize);
            status = ERROR_OUTOFMEMORY;
            goto cleanup;
        }

        // Retrieve the map info.

        status = TdhGetEventMapInformation(pEvent, pMapName, pMapInfo, &MapSize);
    }

    if (ERROR_SUCCESS == status)
    {
        if (DecodingSourceXMLFile == DecodingSource)
        {
            RemoveTrailingSpace(pMapInfo);
        }
    }
    else
    {
        if  (ERROR_NOT_FOUND == status)
        {
            status = ERROR_SUCCESS; // This case is okay.
        }
        else
        {
            wprintf(L"TdhGetEventMapInformation failed with 0x%x.\n", status);
        }
    }

cleanup:

    return status;
}


// The mapped string values defined in a manifest will contain a trailing space
// in the EVENT_MAP_ENTRY structure. Replace the trailing space with a null-
// terminating character, so that the bit mapped strings are correctly formatted.

void RemoveTrailingSpace(PEVENT_MAP_INFO pMapInfo)
{
    SIZE_T ByteLength = 0;

    for (DWORD i = 0; i < pMapInfo->EntryCount; i++)
    {
        ByteLength = (wcslen((LPWSTR)((PBYTE)pMapInfo + pMapInfo->MapEntryArray[i].OutputOffset)) - 1) * 2;
        *((LPWSTR)((PBYTE)pMapInfo + (pMapInfo->MapEntryArray[i].OutputOffset + ByteLength))) = L'\0';
    }
}


// Get the metadata for the event.

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
```



 

 



