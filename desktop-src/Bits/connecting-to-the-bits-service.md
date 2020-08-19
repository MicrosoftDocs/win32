---
title: Connecting to the BITS Service
description: To connect to the BITS service, create an instance of the BackgroundCopyManager object as shown in the following example.
ms.assetid: 2fa88277-c7a1-4f1c-a63c-e2d27a163249
ms.topic: article
ms.date: 11/29/2018
---

# Connecting to the BITS Service

To connect to the BITS system service, create an instance of the BackgroundCopyManager object as shown in the following example. The BITS system service is the Windows system service running on the client computer that implements the background transfer capability.


```C++
#define WIN32_LEAN_AND_MEAN // Exclude rarely-used stuff from Windows headers
#include <windows.h>
#include <bits.h>

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
                        (void**) &g_pbcm);
  if (SUCCEEDED(hr))
  {
    //Use g_pbcm to create, enumerate, or retrieve jobs from the queue.
  }
}
```



To test for a specific version of BITS, use a symbolic class identifier for the BackgroundCopyManager based on the version you want to check. For example, to test for BITS 10.2, use CLSID\_BackgroundCopyManager10\_2.

The following example shows how to use one of the symbolic class identifiers.


```C++
  hr = CoCreateInstance(CLSID_BackgroundCopyManager5_0, NULL,
                        CLSCTX_LOCAL_SERVER,
                        IID_IBackgroundCopyManager,
                        (void**) &g_pbcm);
  if (SUCCEEDED(hr))
  {
    //BITS 5.0 is installed.
  }
```



Use the methods of the [**IBackgroundCopyManager**](/windows/desktop/api/Bits/nn-bits-ibackgroundcopymanager) interface to [create transfer jobs](creating-a-job.md), [enumerate jobs](enumerating-jobs-in-the-transfer-queue.md) in the queue, and [retrieve jobs](/windows/desktop/api/Bits/nf-bits-ibackgroundcopymanager-getjob).



BITS requires that the client's interface proxies use either the IDENTIFY or IMPERSONATE level of impersonation. If the application does not call [**CoInitializeSecurity**](/windows/win32/api/combaseapi/nf-combaseapi-coinitializesecurity), COM uses IDENTIFY by default. BITS fails with E\_ACCESSDENIED if the correct impersonation level is not set. If you provide a library that exercises the BITS interfaces, and an application that calls your library sets the impersonation level below IDENTIFY, then you will need to call [**CoSetProxyBlanket**](/windows/win32/api/combaseapi/nf-combaseapi-cosetproxyblanket) to set the correct impersonation level for each BITS interface that you call.

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

[Calling into BITS from .NET and C#](/windows/desktop/Bits/bits-dot-net) for BITS
</dt> </dl>

 

 