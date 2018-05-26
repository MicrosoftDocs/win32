---
title: Synchronous Searching
description: The Device Finder object enables both synchronous and asynchronous searches. Synchronous searches are completed and return control to the calling application only after all available devices are found.
ms.assetid: 809cfb65-9d08-427b-90d9-b8a836176341
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Synchronous Searching

The Device Finder object enables both synchronous and asynchronous searches. Synchronous searches are completed and return control to the calling application only after all available devices are found. To perform a synchronous search, use one of the synchronous search methods of the [**IUPnPDeviceFinder**](/windows/win32/Upnp/nn-upnp-iupnpdevicefinder?branch=master) interface.

> [!Note]  
> Synchronous searches take at least nine seconds to return. The delay is caused because the initial UDP search message must be sent multiple times. This duplication accounts for the unreliability of the underlying network protocol. Synchronous searches are best for command-line interfaces. They are not recommended for graphical user interfaces.

 

The [**IUPnPDeviceFinder::FindByType**](/windows/win32/Upnp/nf-upnp-iupnpdevicefinder-findbytype?branch=master) method searches by device or service type. This method takes a type URI as an input parameter and returns a collection of Device objects. A Device object represents an individual device.

The following examples demonstrate how to perform a synchronous search for devices in VBScript. Each script uses [**IUPnPDeviceFinder::FindByType**](/windows/win32/Upnp/nf-upnp-iupnpdevicefinder-findbytype?branch=master), called with the type URI (service ID) for the media player device type, *urn:schemas-upnp-org:device:mediaplayer.v1.00.00*. The method returns a collection of Device objects that corresponds to media player devices that were found. For information on extracting individual device objects from a collection, see [Device Collections Returned By Synchronous Searches](device-collections-returned-by-synchronous-searches.md).

## Search for Devices by Type in VBScript


```VB
Dim deviceFinder

Set deviceFinder = CreateObject( "UPnP.UPnPDeviceFinder" )

Dim devices

Set devices = deviceFinder.FindByType( "urn:schemas-upnp-org:device:multidisk-dvd", 0 )
```



## Search for Device by Type in C++

The following example demonstrates a synchronous search for media player devices using C++. The function takes a pointer to the [**IUPnPDeviceFinder**](/windows/win32/Upnp/nn-upnp-iupnpdevicefinder?branch=master) interface as input, and returns the [**IUPnPDevices**](/windows/win32/Upnp/nn-upnp-iupnpdevices?branch=master) interface pointer.

The example first allocates a **BSTR** to represent the device type URI and then passes this to the [**IUPnPDeviceFinder::FindByType**](/windows/win32/Upnp/nf-upnp-iupnpdevicefinder-findbytype?branch=master) method. It also passes the address of a local [**IUPnPDevices**](/windows/win32/Upnp/nn-upnp-iupnpdevices?branch=master) pointer in the buffer in which the method then stores the collection of devices found. If the function call is successful, it returns the pointer to this collection.


```C++
#include <windows.h>
#include <upnp.h>
#include <stdio.h>

#pragma comment(lib, "oleaut32.lib")

IUPnPDevices *FindMediaPlayerDevices(IUPnPDeviceFinder *pDeviceFinder)
{
    HRESULT         hr = S_OK;
    IUPnPDevices    * pFoundDevices = NULL;
    BSTR            bstrTypeURI = NULL;

    bstrTypeURI = 
        SysAllocString(L"urn:schemas-upnp-org:device:multidisk-dvd");

    if (bstrTypeURI)
    {
        hr = pDeviceFinder->FindByType(bstrTypeURI, 
                                       0,
                                       &amp;pFoundDevices);

        if (SUCCEEDED(hr))
        {
            wprintf(L"FindMediaPlayerDevices(): "
                    L"Search returned successfully\n");
        }
        else
        {
            fwprintf(stderr, L"FindMediaPlayerDevices(): "
                     L"FindByType search failed - returned "
                     L"HRESULT 0x%x\n",
                     hr);
            pFoundDevices = NULL;
        }
        SysFreeString(bstrTypeURI);
    }
    else
    {
        fwprintf(stderr, L"FindMediaPlayerDevices(): "
                 L"Could not allocate BSTR for type URI\n");
    }

    return pFoundDevices;
}
```



 

 




