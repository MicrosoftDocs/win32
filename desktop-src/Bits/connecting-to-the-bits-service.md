---
title: Connecting to the BITS Service
description: To connect to the BITS service, create an instance of the BackgroundCopyManager object as shown in the following example.
ms.assetid: 2fa88277-c7a1-4f1c-a63c-e2d27a163249
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Connecting to the BITS Service

To connect to the BITS service, create an instance of the BackgroundCopyManager object as shown in the following example.


```C++
#define UNICODE
#define _WIN32_WINNT  0x0500
#include <windows.h>
#include "bits.h"

//Global variable that several of the code examples in this document reference.
IBackgroundCopyManager* g_pbcm = NULL;  
HRESULT hr;

//Specify the appropriate COM threading model for your application.
hr = CoInitializeEx(NULL, COINIT_APARTMENTTHREADED);
if (SUCCEEDED(hr))
{
  hr = CoCreateInstance(__uuidof(BackgroundCopyManager), NULL,
                        CLSCTX_LOCAL_SERVER,
                        __uuidof(IBackgroundCopyManager),
                        (void**) &amp;g_pbcm);
  if (SUCCEEDED(hr))
  {
    //Use g_pbcm to create, enumerate, or retrieve jobs from the queue.
  }
}
```



To test for a specific version of BITS, use one of the following symbolic class identifiers:

-   For BITS 3.0, use CLSID\_BackgroundCopyManager3\_0.
-   For BITS 2.5, use CLSID\_BackgroundCopyManager2\_5.
-   For BITS 2.0, use CLSID\_BackgroundCopyManager2\_0.
-   For BITS 1.5, use CLSID\_BackgroundCopyManager1\_5.
-   For BITS 1.0, use CLSID\_BackgroundCopyManager.

The following example shows how to use one of the symbolic class identifiers.


```C++
  hr = CoCreateInstance(CLSID_BackgroundCopyManager2_0, NULL,
                        CLSCTX_LOCAL_SERVER,
                        IID_IBackgroundCopyManager,
                        (void**) &amp;g_pbcm);
  if (SUCCEEDED(hr))
  {
    //BITS 2.0 is installed.
  }
```



Use the methods of the [**IBackgroundCopyManager**](/windows/desktop/api/Bits/nn-bits-ibackgroundcopymanager) interface to [create transfer jobs](creating-a-job.md), [enumerate jobs](enumerating-jobs-in-the-transfer-queue.md) in the queue, and [retrieve jobs](/windows/desktop/api/Bits/nf-bits-ibackgroundcopymanager-getjob).

To retrieve a pointer to the [**IBitsPeerCacheAdministration**](/windows/desktop/api/Bits3_0/nn-bits3_0-ibitspeercacheadministration) interface, call the **IBackgroundCopyManager::QueryInterface** method. The following example shows how to get the **IBitsPeerCacheAdministration** interface.


```C++
  HRESULT hr = S_OK;
  IBackgroundCopyManager* pbcm = NULL;
  IBitsPeerCacheAdministration* pCacheAdmin = NULL;

  hr = pbcm>QueryInterface(__uuidof(IBitsPeerCacheAdministration), (void**)&amp;pCacheAdmin);
  pbcm->Release();
  if (FAILED(hr))
  {
    wprintf(L"pbcm->QueryInterface failed with 0x%x.\n", hr);
    goto cleanup;
  }
```



BITS requires that the client's interface proxies use either the IDENTIFY or IMPERSONATE level of impersonation. If the application does not call [**CoInitializeSecurity**](https://www.bing.com/search?q=**CoInitializeSecurity**), COM uses IDENTIFY by default. BITS fails with E\_ACCESSDENIED if the correct impersonation level is not set. If you provide a library that exercises the BITS interfaces, and an application that calls your library sets the impersonation level below IDENTIFY, then you will need to call [**CoSetProxyBlanket**](https://www.bing.com/search?q=**CoSetProxyBlanket**) to set the correct impersonation level for each BITS interface that you call.

Before your application exits, release your copy of the [**IBackgroundCopyManager**](/windows/desktop/api/Bits/nn-bits-ibackgroundcopymanager) interface pointer, as shown in the following example.


```C++
if (g_pbcm)
{
  g_pbcm->Release();
  g_pbcm = NULL;
}
CoUninitialize();
```



## Related topics

<dl> <dt>

[SharpBITS.NET](http://sharpbits.codeplex.com/)
</dt> </dl>

 

 




