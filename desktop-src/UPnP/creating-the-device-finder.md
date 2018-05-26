---
title: Creating the Device Finder
description: The following examples demonstrate how to create an instance of the Device Finder object in C++, Visual Basic, and VBScript.
ms.assetid: 0084a64d-458e-471c-a6be-aeb6ed0962d0
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Creating the Device Finder

The following examples demonstrate how to create an instance of the Device Finder object in C++, Visual Basic, and VBScript. The script languages use the programmatic ID (ProgID) [**UPnP.UPnPDeviceFinder**](/windows/win32/Upnp/nn-upnp-iupnpdevicefinder?branch=master) to identify the Device Finder class. The C++ code uses the class identifier.

## C++ Example


```C++
HRESULT hr = S_OK;
IUPnPDeviceFinder *pDeviceFinder = NULL;

hr = CoCreateInstance(CLSID_UPnPDeviceFinder, 
                      NULL,
                      CLSCTX_INPROC_SERVER,
                      IID_IUPnPDeviceFinder,
                      (void **) &amp;pDeviceFinder);
```



As this C++ example indicates, the Device Finder object exposes a default interface, [**IUPnPDeviceFinder**](/windows/win32/Upnp/nn-upnp-iupnpdevicefinder?branch=master). The methods of this interface perform searches according to the valid search criteria for a UPnP-based device. This interface is Automation capable, so its methods can be called by scripting code.

## VBScript Example


```VB
Dim deviceFinder

Set deviceFinder = CreateObject( "UPnP.UPnPDeviceFinder" )
```



 

 




