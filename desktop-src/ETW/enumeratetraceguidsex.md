---
Description: Use this function to retrieve information about trace providers that are registered on the computer.
ms.assetid: 9d70fe21-1750-4d60-a825-2004f7d666c7
title: EnumerateTraceGuidsEx function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# EnumerateTraceGuidsEx function

Use this function to retrieve information about trace providers that are registered on the computer.

## Syntax


```C++
ULONG WINAPI EnumerateTraceGuidsEx(
  _In_  TRACE_QUERY_INFO_CLASS TraceQueryInfoClass,
  _In_  PVOID                  InBuffer,
  _In_  ULONG                  InBufferSize,
  _Out_ PVOID                  OutBuffer,
  _In_  ULONG                  OutBufferSize,
  _Out_ PULONG                 ReturnLength
);
```



## Parameters

<dl> <dt>

*TraceQueryInfoClass* \[in\]
</dt> <dd>

Determines the type of information to include with the list of registered providers. For possible values, see the [**TRACE\_QUERY\_INFO\_CLASS**](etw.trace_query_info_class) enumeration.

</dd> <dt>

*InBuffer* \[in\]
</dt> <dd>

GUID of the provider or provider group whose information you want to retrieve. Specify the GUID only if *TraceQueryInfoClass* is **TraceGuidQueryInfo** or **TraceGroupQueryInfo**.

</dd> <dt>

*InBufferSize* \[in\]
</dt> <dd>

Size, in bytes, of the data *InBuffer*.

</dd> <dt>

*OutBuffer* \[out\]
</dt> <dd>

Application-allocated buffer that contains the enumerated information. The format of the information depends on the value of *TraceQueryInfoClass*. For details, see Remarks.

</dd> <dt>

*OutBufferSize* \[in\]
</dt> <dd>

Size, in bytes, of the *OutBuffer* buffer. If the function succeeds, the *ReturnLength* parameter receives the size of the buffer used. If the buffer is too small, the function returns ERROR\_INSUFFICIENT\_BUFFER and the *ReturnLength* parameter receives the required buffer size. If the buffer size is zero on input, no data is returned in the buffer and the *ReturnLength* parameter receives the required buffer size.

</dd> <dt>

*ReturnLength* \[out\]
</dt> <dd>

Actual size of the data in *OutBuffer*, in bytes.

</dd> </dl>

## Return value

If the function succeeds, the return value is ERROR\_SUCCESS.

If the function fails, the return value is one of the [system error codes](base.system_error_codes). The following table includes some common errors and their causes.



| Return code                                                                                                | Description                                                                                                                                                          |
|------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**ERROR\_INVALID\_PARAMETER**</dt> </dl>   | One of the parameters is not valid. <br/>                                                                                                                      |
| <dl> <dt>**ERROR\_INSUFFICIENT\_BUFFER**</dt> </dl> | The *OutBuffer* buffer is too small to receive information for all registered providers. Reallocate the buffer using the size returned in *ReturnLength*.<br/> |



 

## Remarks

Event trace controllers call this function.

If *TraceQueryInfoClass* is **TraceGuidQueryInfo**, ETW returns the data in a [**TRACE\_GUID\_INFO**](trace-guid-info.md) block that is a header to the information. The info block contains a [**TRACE\_PROVIDER\_INSTANCE\_INFO**](trace-provider-instance-info.md) block for each provider that uses the same GUID. Each instance info block contains a [**TRACE\_ENABLE\_INFO**](trace-enable-info.md) structure for each session that enabled the provider.

For information on registering event trace providers, see [**EventRegister**](/windows/win32/Evntprov/nf-evntprov-eventregister?branch=master) and [**RegisterTraceGuids**](registertraceguids.md).

## Examples

The following example shows you how to call this function.


```C++
#include <windows.h>
#include <stdio.h>
#include <evntcons.h>

DWORD GetProviderInfo(GUID ProviderGuid, PTRACE_GUID_INFO & pInfo);

void wmain(void)
{
    ULONG status = ERROR_SUCCESS;
    GUID *pTemp = NULL;
    GUID *pGuids = NULL;
    DWORD GuidListSize = 0;
    DWORD GuidCount = 0;
    DWORD RequiredListSize = 0;
    WCHAR ProviderGuid[50];
    PTRACE_GUID_INFO pInfo = NULL;
    PTRACE_PROVIDER_INSTANCE_INFO pInstance = NULL;
    PTRACE_ENABLE_INFO pEnable = NULL;


    // Get the required buffer size for the query.

    status = EnumerateTraceGuidsEx(TraceGuidQueryList, NULL, 0, pGuids, GuidListSize, &amp;RequiredListSize);

    // The number of registered providers could change between the 
    // time you called to get the buffer size and the time you called
    // to get the actual data, so call EnumerateTraceGuidsEx in a loop
    // until you no longer get ERROR_INSUFFICIENT_BUFFER.

    while (ERROR_INSUFFICIENT_BUFFER == status)
    {
        pTemp = (GUID *) realloc(pGuids, RequiredListSize);

        if (NULL == pTemp)
        {
            wprintf(L"Error allocating memory for list of provider GUIDs.\n");
            goto cleanup;
        }

        pGuids = pTemp;
        pTemp = NULL;

        GuidListSize = RequiredListSize;

        ZeroMemory(pGuids, GuidListSize);

        status = EnumerateTraceGuidsEx(TraceGuidQueryList, NULL, 0, pGuids, GuidListSize, &amp;RequiredListSize);
    }

    if (ERROR_SUCCESS == status)
    {
        GuidCount = GuidListSize / sizeof(GUID);

        // For each registered provider on the computer, get information
        // about how it was registered. If a session enabled the
        // provider, get information on how the session enabled the provider.

        for (USHORT i = 0; i < GuidCount; i++)
        {
            StringFromGUID2(pGuids[i], ProviderGuid, sizeof(ProviderGuid)),

            wprintf(L"Provider: %s\n", ProviderGuid);

            status = GetProviderInfo(pGuids[i], pInfo);

            if (ERROR_SUCCESS == status)
            {
                pInstance = (PTRACE_PROVIDER_INSTANCE_INFO)((PBYTE)pInfo + sizeof(TRACE_GUID_INFO));

                if (pInfo->InstanceCount > 1)
                {
                    wprintf(L"There are %d providers that use the same GUID.\n", pInfo->InstanceCount);
                }

                for (DWORD j = 0; j < pInfo->InstanceCount; j++)
                {
                    wprintf(L"\tThe PID of the process that registered the provider is %lu.\n", pInstance->Pid);

                    if ((pInstance->Flags & TRACE_PROVIDER_FLAG_PRE_ENABLE) == TRACE_PROVIDER_FLAG_PRE_ENABLE)
                    {
                        wprintf(L"\tThe provider is not registered; however, one or more sessions have enabled the provider.\n");
                    }
                    else
                    {
                        if ((pInstance->Flags & TRACE_PROVIDER_FLAG_LEGACY) == TRACE_PROVIDER_FLAG_LEGACY)
                        {
                            wprintf(L"\tThe provider used RegisterTraceGuids to register itself.\n");
                        }
                        else
                        {
                            wprintf(L"\tThe provider used EventRegister to register itself.\n");
                        }
                    }

                    if (pInstance->EnableCount > 0)
                    {
                        wprintf(L"\tThe provider is enabled to the following sessions.\n");

                        pEnable = (PTRACE_ENABLE_INFO)((PBYTE)pInstance + sizeof(TRACE_PROVIDER_INSTANCE_INFO));

                        for (DWORD k = 0; k < pInstance->EnableCount; k++)
                        {
                            wprintf(L"\t\tSession Id: %hu\n", pEnable->LoggerId);
                            wprintf(L"\t\tLevel used to enable the provider: %hu\n", pEnable->Level);
                            wprintf(L"\t\tMatchAnyKeyword value used to enable the provider: %I64u\n", pEnable->MatchAnyKeyword);
                            wprintf(L"\t\tMatchAllKeyword value used to enable the provider: %I64u\n", pEnable->MatchAllKeyword);

                            if (pEnable->EnableProperty > 0)
                            {
                                wprintf(L"\t\tThe session requested that the following information be included with each event:\n");

                                if ((pEnable->EnableProperty & EVENT_ENABLE_PROPERTY_SID) == EVENT_ENABLE_PROPERTY_SID)
                                {
                                    wprintf(L"\t\t\tThe SID of the user that logged the event\n");
                                }

                                if ((pEnable->EnableProperty & EVENT_ENABLE_PROPERTY_TS_ID) == EVENT_ENABLE_PROPERTY_TS_ID)
                                {
                                    wprintf(L"\t\t\tThe terminal session ID\n");
                                }
                            }

                            pEnable++;

                            wprintf(L"\n");
                        }
                    }

                    pInstance = (PTRACE_PROVIDER_INSTANCE_INFO)((PBYTE)pInstance + pInstance->NextOffset);

                    wprintf(L"\n");
                }

                wprintf(L"\n");
            }
            else
            {
                wprintf(L"Error retrieving provider info (%lu)\n\n", status);
            }
        }

        wprintf(L"\nRegistered provider count is %lu.\n", GuidCount);
    }
    else
    {
        wprintf(L"EnumerateTraceGuidsEx(TraceGuidQueryList) failed with %lu.\n", status);
        goto cleanup;
    }

cleanup:

    if (pGuids)
    {
        free(pGuids);
        pGuids = NULL;
    }

    if (pInfo)
    {
        free(pInfo);
        pInfo = NULL;
    }
}


// Get information about the specified provider.

DWORD GetProviderInfo(GUID ProviderGuid, PTRACE_GUID_INFO & pInfo)
{
    ULONG status = ERROR_SUCCESS;
    PTRACE_GUID_INFO pTemp = NULL;
    DWORD InfoListSize = 0;
    DWORD RequiredListSize = 0;

    status = EnumerateTraceGuidsEx(TraceGuidQueryInfo, &amp;ProviderGuid, sizeof(GUID), pInfo, InfoListSize, &amp;RequiredListSize);

    while (ERROR_INSUFFICIENT_BUFFER == status)
    {
        pTemp = (PTRACE_GUID_INFO) realloc(pInfo, RequiredListSize);

        if (NULL == pTemp)
        {
            wprintf(L"Error allocating memory for provider info.\n");
            goto cleanup;
        }

        pInfo = pTemp;
        pTemp = NULL;

        InfoListSize = RequiredListSize;

        ZeroMemory(pInfo, InfoListSize);

        status = EnumerateTraceGuidsEx(TraceGuidQueryInfo, &amp;ProviderGuid, sizeof(GUID), pInfo, InfoListSize, &amp;RequiredListSize);
    }

    if (ERROR_SUCCESS != status)
    {
        wprintf(L"EnumerateTraceGuidsEx(TraceGuidQueryInfo) failed with %lu.\n", status);
    }

cleanup:

    return status;
}
```



## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps \| UWP apps\]<br/>                                   |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps \| UWP apps\]<br/>                             |
| Header<br/>                   | <dl> <dt>Evntrace.h</dt> </dl>   |
| Library<br/>                  | <dl> <dt>Advapi32.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Advapi32.dll</dt> </dl> |



## See also

<dl> <dt>

[**TRACE\_QUERY\_INFO\_CLASS**](etw.trace_query_info_class)
</dt> </dl>

 

 




