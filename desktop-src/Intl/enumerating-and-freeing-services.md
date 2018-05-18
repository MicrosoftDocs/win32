---
Description: Enumerating and Freeing Services
ms.assetid: '526e51c7-9ff2-4590-b092-172f4942ce8e'
title: Enumerating and Freeing Services
---

# Enumerating and Freeing Services

The ELS application calls the [**MappingGetServices**](mappinggetservices.md) function to determine the services that are available on the operating system. The function can be used either to enumerate all available ELS services, or to filter the services based on application-provided search criteria. When services are no longer needed, the application calls [**MappingFreeServices**](mappingfreeservices.md).

## Get All Supported Services

This code example illustrates the use of [**MappingGetServices**](mappinggetservices.md) and [**MappingFreeServices**](mappingfreeservices.md) to enumerate and then free all available services on the operating system. To do this, the application passes **NULL** for the *pOptions* parameter of **MappingGetServices**.


```C++
#include <windows.h>
#include <stdio.h>
#include <elscore.h>

int __cdecl main()
{
    PMAPPING_SERVICE_INFO   prgServices = NULL;
    DWORD                   dwServicesCount = 0;
    HRESULT                 Result;
    DWORD                   i;

    // Get all installed ELS services.
    Result = MappingGetServices(NULL, &amp;prgServices, &amp;dwServicesCount);

    if (SUCCEEDED(Result))
    {
        for (i = 0; i < dwServicesCount; ++i)
        {
            // Do something with each service.
            // ... prgServices[i] ...
            printf_s("Service: %ws, category: %ws\n",
                prgServices[i].pszDescription, prgServices[i].pszCategory);
        }
        MappingFreeServices(prgServices);
    }
    return 0;
}
```



## Get Specific Services

The next example illustrates the use of [**MappingGetServices**](mappinggetservices.md) and [**MappingFreeServices**](mappingfreeservices.md) to enumerate and then free all services of category "Language Detection". For more information about this service category, see [**Microsoft Language Detection**](microsoft-language-detection.md).


```C++
#include <windows.h>
#include <stdio.h>
#include <elscore.h>

int __cdecl main()
{
    MAPPING_ENUM_OPTIONS    EnumOptions;
    PMAPPING_SERVICE_INFO   prgServices = NULL;
    DWORD                   dwServicesCount = 0;
    HRESULT                 Result;
    DWORD                   i;

    ZeroMemory(&amp;EnumOptions, sizeof (MAPPING_ENUM_OPTIONS));
    EnumOptions.Size = sizeof (MAPPING_ENUM_OPTIONS);

    // Use the Language Auto-Detection category to enumerate
    // all language detection services.
    EnumOptions.pszCategory = L"Language Detection";

    // Execute the enumeration:
    Result = MappingGetServices(&amp;EnumOptions, &amp;prgServices, &amp;dwServicesCount);

    if (SUCCEEDED(Result))
    {
        for (i = 0; i < dwServicesCount; ++i)
        {
            // Do something with each service.
            // ... prgServices[i] ...
            printf_s("Service: %ws, category: %ws\n",
                prgServices[i].pszDescription, prgServices[i].pszCategory);
        }
        MappingFreeServices(prgServices);
    }
    return 0;
}
```



## Related topics

<dl> <dt>

[Using Extended Linguistic Services](using-extended-linguistic-services.md)
</dt> <dt>

[**MappingFreeServices**](mappingfreeservices.md)
</dt> <dt>

[**MappingGetServices**](mappinggetservices.md)
</dt> </dl>

 

 



