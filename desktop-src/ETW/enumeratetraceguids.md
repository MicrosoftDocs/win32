---
Description: The EnumerateTraceGuids function retrieves information about registered event trace providers that are running on the computer.
ms.assetid: 9a9e2f53-9916-4a9c-a08e-c8affd5fc4c9
title: EnumerateTraceGuids function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- EnumerateTraceGuids
api_type: 
- DllExport
api_location: 
- Advapi32.dll
- API-MS-Win-eventing-Legacy-l1-1-0.dll
- advapi32legacy.dll
---

# EnumerateTraceGuids function

The **EnumerateTraceGuids** function retrieves information about registered event trace providers that are running on the computer.

> [!Note]  
> This function has been superseded by [**EnumerateTraceGuidsEx**](enumeratetraceguidsex.md).

 

## Syntax


```C++
ULONG EnumerateTraceGuids(
  _Inout_ PTRACE_GUID_PROPERTIES *GuidPropertiesArray,
  _In_    ULONG                  PropertyArrayCount,
  _Out_   PULONG                 GuidCount
);
```



## Parameters

<dl> <dt>

*GuidPropertiesArray* \[in, out\]
</dt> <dd>

An array of pointers to [**TRACE\_GUID\_PROPERTIES**](trace-guid-properties.md) structures.

</dd> <dt>

*PropertyArrayCount* \[in\]
</dt> <dd>

Number of elements in the *GuidPropertiesArray* array.

</dd> <dt>

*GuidCount* \[out\]
</dt> <dd>

Actual number of event tracing providers registered on the computer.

</dd> </dl>

## Return value

If the function succeeds, the return value is ERROR\_SUCCESS.

If the function fails, the return value is one of the [system error codes](https://msdn.microsoft.com/en-us/library/ms681381(v=VS.85).aspx). The following table includes some common errors and their causes.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Return code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><dl> <dt><strong>ERROR_INVALID_PARAMETER</strong></dt> </dl></td>
<td>One of the following is true:<br/>
<ul>
<li><em>PropertyArrayCount</em> is zero</li>
<li><em>GuidPropertiesArray</em> is <strong>NULL</strong></li>
</ul></td>
</tr>
<tr class="even">
<td><dl> <dt><strong>ERROR_MORE_DATA</strong></dt> </dl></td>
<td>The property array is too small to receive information for all registered providers (<em>GuidCount</em> is greater than <em>PropertyArrayCount</em>). The function fills the GUID property array with the number of structures specified in <em>PropertyArrayCount</em>.<br/></td>
</tr>
</tbody>
</table>



 

## Remarks

Event trace controllers call this function.

For information on registering event trace providers, see [**RegisterTraceGuids**](registertraceguids.md).

You can use the [**TRACE\_GUID\_PROPERTIES.LoggerId**](trace-guid-properties.md) member to determine which session enabled the provider if **TRACE\_GUID\_PROPERTIES.IsEnable** is **TRUE**.

The list will not include kernel providers.

## Examples

The following example shows you how to call this function.


```C++
#include <windows.h>
#include <stdio.h>
#include <wmistr.h>
#include <evntrace.h>

#define MAX_SESSION_NAME_LEN 1024
#define MAX_LOGFILE_PATH_LEN 1024

BOOL IsPrivateSession(DWORD SessionId);

void wmain(void)
{
    ULONG status = ERROR_SUCCESS;
    PTRACE_GUID_PROPERTIES pProviderProperties = NULL; // Buffer that contains the block of property structures
    PTRACE_GUID_PROPERTIES *pProviders = NULL;         // Array of pointers to property structures in ProviderProperties
    PTRACE_GUID_PROPERTIES *pTemp = NULL;
    ULONG RegisteredProviderCount = 0;                 // Actual number of providers registered on the computer
    ULONG ProviderCount = 0;
    ULONG EnabledProviderCount = 0;
    ULONG BufferSize = 0;
    WCHAR ProviderGuid[50];

    // EnumerateTraceGuids requires a valid pointer. Create a dummy
    // allocation, so that you can get the actual allocation size.

    pProviders = (PTRACE_GUID_PROPERTIES *) malloc(sizeof(PTRACE_GUID_PROPERTIES));

    if (NULL == pProviders)
    {
        wprintf(L"Error allocating memory for dummy pProviders allocation.\n");
        goto cleanup;
    }

    // Pass zero for the array size to get the number of registered providers 
    // for this snapshot. Then allocate memory for the block of structures
    // and the array of pointers.

    status = EnumerateTraceGuids(pProviders, ProviderCount, &amp;RegisteredProviderCount);

    if (ERROR_MORE_DATA == status)
    {
        ProviderCount = RegisteredProviderCount;

        BufferSize = sizeof(TRACE_GUID_PROPERTIES) * RegisteredProviderCount;

        pProviderProperties = (PTRACE_GUID_PROPERTIES) malloc(BufferSize);

        if (NULL == pProviderProperties)
        {
            wprintf(L"Error allocating memory for properties.\n");
            goto cleanup;
        }

        ZeroMemory(pProviderProperties, BufferSize);

        pTemp = (PTRACE_GUID_PROPERTIES *) realloc(pProviders, RegisteredProviderCount * sizeof(PTRACE_GUID_PROPERTIES));

        if (NULL == pTemp)
        {
            wprintf(L"Error allocating memory for pProviders allocation.\n");
            goto cleanup;
        }

        pProviders = pTemp;
        pTemp = NULL;

        for (USHORT i = 0; i < RegisteredProviderCount; i++)
        {
            pProviders[i] = &amp;pProviderProperties[i];
        }

        status = EnumerateTraceGuids(pProviders, ProviderCount, &amp;RegisteredProviderCount);

        if (ERROR_SUCCESS == status || ERROR_MORE_DATA == status)
        {
            for (USHORT i=0; i < RegisteredProviderCount; i++)
            {
                StringFromGUID2(pProviders[i]->Guid, ProviderGuid, sizeof(ProviderGuid)),

                wprintf(L"Provider: %s\nEnabled: %s\n",
                    ProviderGuid,
                    (pProviders[i]->IsEnable) ? L"TRUE" : L"FALSE");

                if (pProviders[i]->IsEnable)
                {
                    EnabledProviderCount++;

                    wprintf(L"Session ID: %ld\nPrivate Session: %s\n"
                        L"Enable level: %ld\nEnable flags: %ld\n",
                        pProviders[i]->LoggerId,
                        (IsPrivateSession(pProviders[i]->LoggerId)) ? L"TRUE" : L"FALSE",
                        pProviders[i]->EnableLevel,
                        pProviders[i]->EnableFlags);
                }
      
                wprintf(L"\n");
            }

            wprintf(L"\nRegistered provider count is %lu; %lu of which are enabled.\n", 
                RegisteredProviderCount, EnabledProviderCount);
        }
        else
        {
            wprintf(L"Error calling EnumerateTraceGuids, %d.\n", status);
            goto cleanup;
        }
    }
    else
    {
        wprintf(L"Error calling EnumerateTraceGuids to get allocation size, %d.\n", status);
        goto cleanup;
    }

cleanup:

    if (pProviders)
    {
        free(pProviders);
    }

    if (pProviderProperties)
    {
        free(pProviderProperties);
    }
}


BOOL IsPrivateSession(DWORD SessionId)
{
    DWORD status = ERROR_SUCCESS;
    BOOL IsPrivate = FALSE;
    PEVENT_TRACE_PROPERTIES pProperties;
    ULONG BufferSize = 0;

    BufferSize = sizeof(EVENT_TRACE_PROPERTIES) +
        (MAX_SESSION_NAME_LEN*sizeof(WCHAR)) +
        (MAX_LOGFILE_PATH_LEN*sizeof(WCHAR));

    pProperties = (PEVENT_TRACE_PROPERTIES) malloc(BufferSize);

    if (pProperties)
    {
        ZeroMemory(pProperties, BufferSize);

        pProperties->Wnode.BufferSize = BufferSize;
        pProperties->LoggerNameOffset = sizeof(EVENT_TRACE_PROPERTIES);
        pProperties->LogFileNameOffset = sizeof(EVENT_TRACE_PROPERTIES) + (MAX_SESSION_NAME_LEN*sizeof(WCHAR));
    }
    else
    {
        wprintf(L"Error allocating memory for properties.\n");
        goto cleanup;
    }

    status = ControlTrace((TRACEHANDLE)SessionId, NULL, pProperties, EVENT_TRACE_CONTROL_QUERY);

    if (ERROR_SUCCESS == status)
    {
        if ((EVENT_TRACE_PRIVATE_LOGGER_MODE & pProperties->LogFileMode)== EVENT_TRACE_PRIVATE_LOGGER_MODE)
        {
            IsPrivate = TRUE;
        }
    }
    else if (ERROR_WMI_INSTANCE_NOT_FOUND == status)
    {
        wprintf(L"The session is no longer running\n");
    }
    else
    {
        wprintf(L"ControlTrace(QUERY) failed with %lu\n", status);
    }

cleanup:

    if (pProperties)
    {
        free(pProperties);
        pProperties = NULL;
    }

    return IsPrivate;
}
```



## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Evntrace.h</dt> </dl>   |
| Library<br/>                  | <dl> <dt>Advapi32.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Advapi32.dll</dt> </dl> |



## See also

<dl> <dt>

[**EnumerateTraceGuidsEx**](enumeratetraceguidsex.md)
</dt> <dt>

[**QueryAllTraces**](queryalltraces.md)
</dt> <dt>

[**RegisterTraceGuids**](registertraceguids.md)
</dt> <dt>

[**TRACE\_GUID\_PROPERTIES**](trace-guid-properties.md)
</dt> </dl>

 

 




