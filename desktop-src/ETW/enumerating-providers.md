---
Description: To retrieve a list of providers that have installed their manifest or MOF classes on the computer, call the TdhEnumerateProviders function.
ms.assetid: 79a29a55-e211-4921-ac78-a21ef8ef238f
title: Enumerating Providers
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Enumerating Providers

To retrieve a list of providers that have installed their manifest or MOF classes on the computer, call the [**TdhEnumerateProviders**](/windows/win32/Tdh/nf-tdh-tdhenumerateproviders?branch=master) function.

The following example shows how to enumerate providers.


```C++
#include <windows.h>
#include <stdio.h>
#include <tdh.h>

#pragma comment(lib, "tdh.lib")

void wmain(void)
{
    DWORD status = ERROR_SUCCESS;
    PROVIDER_ENUMERATION_INFO* penum = NULL;    // Buffer that contains provider information
    PROVIDER_ENUMERATION_INFO* ptemp = NULL; 
    DWORD BufferSize = 0;                       // Size of the penum buffer
    HRESULT hr = S_OK;                          // Return value for StringFromCLSID
    LPWSTR pStringGuid = NULL;
    DWORD RegisteredMOFCount = 0;
    DWORD RegisteredManifestCount = 0;

    // Retrieve the required buffer size.

    status = TdhEnumerateProviders(penum, &amp;BufferSize);
    
    // Allocate the required buffer and call TdhEnumerateProviders. The list of 
    // providers can change between the time you retrieved the required buffer 
    // size and the time you enumerated the providers, so call TdhEnumerateProviders
    // in a loop until the function does not return ERROR_INSUFFICIENT_BUFFER.

    while (ERROR_INSUFFICIENT_BUFFER == status)
    {
        ptemp = (PROVIDER_ENUMERATION_INFO*) realloc(penum, BufferSize);
        if (NULL == ptemp)
        {
            wprintf(L"Allocation failed (size=%lu).\n", BufferSize);
            goto cleanup;
        }

        penum = ptemp;
        ptemp = NULL;

        status = TdhEnumerateProviders(penum, &amp;BufferSize);
    }

    if (ERROR_SUCCESS != status)
    {
        wprintf(L"TdhEnumerateProviders failed with %lu.\n", status);
    }
    else
    {
        // Loop through the list of providers and print the provider's name, GUID, 
        // and the source of the information (MOF class or instrumentation manifest).

        for (DWORD i = 0; i < penum->NumberOfProviders; i++)
        {
            hr = StringFromCLSID(penum->TraceProviderInfoArray[i].ProviderGuid, &amp;pStringGuid);

            if (FAILED(hr))
            {
                wprintf(L"StringFromCLSID failed with 0x%x\n", hr);
                goto cleanup;
            }

            wprintf(L"Provider name: %s\nProvider GUID: %s\nSource: %s\n\n",
                (LPWSTR)((PBYTE)(penum) + penum->TraceProviderInfoArray[i].ProviderNameOffset),
                pStringGuid,
                (penum->TraceProviderInfoArray[i].SchemaSource) ? L"WMI MOF class" : L"XML manifest");

            CoTaskMemFree(pStringGuid);

            (penum->TraceProviderInfoArray[i].SchemaSource) ? RegisteredMOFCount++ : RegisteredManifestCount++;
        }

        wprintf(L"\nThere are %d registered providers; %lu are registered via MOF class and\n%lu are registered via a manifest.\n", 
            penum->NumberOfProviders,
            RegisteredMOFCount,
            RegisteredManifestCount);
    }

cleanup:

    if (penum)
    {
        free(penum);
        penum = NULL;
    }
}
```



 

 



