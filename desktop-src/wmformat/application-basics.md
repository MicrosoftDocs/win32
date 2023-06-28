---
title: Application Basics
description: Application Basics
ms.assetid: 5593d27e-e97d-4f03-99ff-aee856abec8e
keywords:
- Windows Media Format SDK,DRM application basics
- digital rights management (DRM),application basics
- DRM (digital rights management),application basics
- digital rights management (DRM),WMDRMStartup function
- DRM (digital rights management),WMDRMStartup function
- WMDRMStartup
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Application Basics

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

There is some extra processing that you must perform for any application that uses the Windows Media DRM Client Extended APIs. This topic describes the requirements for a simple application.

First, you must initialize the Windows Media DRM Client Extended APIs by calling the [**WMDRMStartup**](wmdrmstartup.md) function. The objects of the SDK are COM objects, but you do not need to call **CoIntialize**, because the **WMDRMStatup** function initializes COM for you.

> [!Note]  
> The Windows Media Format SDK uses only a subset of COM, so if you use COM objects other than those in the Windows Media DRM Client Extended API, you must still call **CoInitialize**.

 

All of the objects of the Windows Media DRM Client Extended APIs are created using helper functions and methods. You never need to call **CoCreateInstance** to create an object. The first interface to instantiate for any application that uses the SDK is [**IWMDRMProvider**](iwmdrmprovider.md), which you can use to instantiate all of the other base interfaces. To get an instance of **IWMDRMProvider**, you must call either [**WMDRMCreateProvider**](wmdrmcreateprovider.md) or [**WMDRMCreateProtectedProvider**](wmdrmcreateprotectedprovider.md). The difference between these functions is that **WMDRMCreateProvider** creates an object that can in turn create only objects that do not support methods that require the stub library.

After you have an instance of **IWMDRMProvider**, you can create the other objects that you need by calling [**IWMDRMProvider::CreateObject**](iwmdrmprovider-createobject.md).

When you are ready to exit your application, you must release the DRM subsystem resources by calling the [**WMDRMShutdown**](wmdrmshutdown.md) function. This function also shuts down COM for you.

The following code example demonstrates how to initialize and conclude an application that uses the Windows Media DRM Client Extended APIs.


```C++
#include <wmdrmsdk.h>
// TODO: Include other headers here as needed.

// This example demonstrates the code required in a single, simple
// main function. You will most likely break this code up into appropriate
// functions.
void main(void)
{
    HRESULT hr = S_OK;

    IWMDRMProvider*     pProvider     = NULL;
    // For the sake of example, this code will instantiate the
    //  IWMDRMLicenseQuery interface. The process is the same for the
    //  other base interfaces.
    IWMDRMLicenseQuery* pLicenseQuery = NULL;

    // Initialize the DRM subsystem.
    hr = WMDRMStartup();

    // Create a provider object, that can be used to create the other
    //  objects.
    if (SUCCEEDED(hr))
    {
        hr = WMDRMCreateProvider(&pProvider);
    }

    if(SUCCEEDED(hr))
    {
        hr = pProvider->CreateObject(
            IID_IWMDRMLicenseQuery, 
            (void**)&pLicenseQuery);
    }

    // TODO: Use the methods of IWMDRMLicenseQuery as required.

    // Cleanup and shutdown.
    SAFE_RELEASE(pLicenseQuery);
    SAFE_RELEASE(pProvider);

    hr = WMDRMShutdown();
}
```



## Related topics

<dl> <dt>

[**Getting Started**](drm-getting-started.md)
</dt> </dl>

 

 




