---
title: Obtaining Service Objects
description: Device objects expose a property called Services that returns a collection of Service objects that contains one service object for each service exported by the device.
ms.assetid: 8ef12b6e-cb9b-4406-95be-002117b8fc3f
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Obtaining Service Objects

Device objects expose a property called [**Services**](/windows/desktop/api/Upnp/) that returns a collection of Service objects that contains one service object for each service exported by the device. Applications are able to traverse this collection sequentially, or request a particular service by using its service ID.

## VBScript Example

The following example is VBScript code that extracts Service objects for two of the services exported by a device.


```VB
' Get the service objects
services = device.Services
    
Set appService = services( "urn:upnp-org:serviceId:DVDVideo" )
Set xportService = services( "urn:upnp-org:serviceId:AVTransport" )
```



The first line extracts the services collection from the Device object by querying the [**Services**](/windows/desktop/api/Upnp/) property. The next two lines obtain the two desired Service objects from the collection by specifying their service IDs. The services collection can also be traversed sequentially by using a **for each … next** loop.

## C++ Example

The following example shows the C++ code required to obtain Service objects from a device. First, the sample code queries the [**IUPnPDevice::Services**](/windows/desktop/api/Upnp/) property on the interface that was passed to the function. This returns a service collection using the [**IUPnPServices**](/windows/desktop/api/Upnp/nn-upnp-iupnpservices) interface. To obtain individual Service objects, use the [**Item**](/windows/desktop/api/Upnp/) method, and specify the requested service IDs. To traverse the collection sequentially, use the [**IEnumVARIANT::Reset**](https://msdn.microsoft.com/windows/desktop/0c3f0cd7-6bad-4cb7-8b84-d8a212dbadbd), [**IEnumVARIANT::Next**](https://msdn.microsoft.com/windows/desktop/691c1624-8d01-41e0-890e-a4782eba1f59), and [**IEnumVARIANT::Skip**](https://msdn.microsoft.com/windows/desktop/5fe6951f-1e21-4a3d-8694-96efb15e6d11) methods. This example is similar to the example used to traverse the [**IUPnPDevices**](/windows/desktop/api/Upnp/nn-upnp-iupnpdevices) collection.


```C++
#include <windows.h>
#include <upnp.h>

#pragma comment(lib, "oleaut32.lib")


HRESULT ExtractServices(IUPnPDevice * pDevice)
{
    // Create a BSTR to hold the service name
    BSTR bstrServiceName = SysAllocString(L"urn:upnp-org:servicId:DVDVideo");
    if (NULL == bstrServiceName)
    {
        return E_OUTOFMEMORY;
    }
    // Get the list of services available on the device
    IUPnPServices * pServices = NULL;
    HRESULT hr = pDevice->get_Services(&amp;pServices);
    if (SUCCEEDED(hr))
    {
        // Retrieve the service we are interested in
        IUPnPService * pAppService = NULL;
        hr = pServices->get_Item(bstrServiceName, &amp;pAppService);
        if (SUCCEEDED(hr))
        {
            // Do something interesting with the service object
            pAppService->Release();
        }
        pServices->Release();
    }
    SysFreeString(bstrServiceName);
    return hr;
}
```



 

 




