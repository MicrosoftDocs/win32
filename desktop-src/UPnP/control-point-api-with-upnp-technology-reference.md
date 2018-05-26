---
title: Control Point API Reference
description: The following interfaces are part of the Control Point API with UPnP technology. The Control Point API supports Microsoft Visual Basic Scripting Edition (VBScript), Microsoft Visual Basic, and C++.
ms.assetid: 6f73bf8c-0423-430f-a654-58d076712aae
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Control Point API Reference

The following interfaces are part of the Control Point API with UPnP technology. The Control Point API supports Microsoft Visual Basic Scripting Edition (VBScript), Microsoft Visual Basic, and C++.



| Interface                                                                                      | Description                                                                                                                                                                                                                    |
|------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IUPnPAddressFamilyControl**](/windows/win32/Upnp/nn-upnp-iupnpaddressfamilycontrol?branch=master)                                 | Enables an application to access the address family flag of the Device Finder object.                                                                                                                                          |
| [**IUPnPDescriptionDocument**](/windows/win32/Upnp/nn-upnp-iupnpdescriptiondocument?branch=master)                                   | Enables an application to load a device description. This interface is safe for scripting.                                                                                                                                     |
| [**IUPnPDescriptionDocumentCallback**](/windows/win32/Upnp/nn-upnp-iupnpdescriptiondocumentcallback?branch=master)                   | Enables an application to receive the results of an asynchronous load operation.                                                                                                                                               |
| [**IUPnPDevice**](/windows/win32/Upnp/nn-upnp-iupnpdevice?branch=master)                                                             | Enables an application to retrieve information about a specific device.                                                                                                                                                        |
| [**IUPnPDeviceDocumentAccess**](/windows/win32/Upnp/nn-upnp-iupnpdevicedocumentaccess?branch=master)                                 | Enables an application to obtain the URL of a device description document.                                                                                                                                                     |
| [**IUPnPDeviceDocumentAccessEx**](/windows/win32/Upnp/nn-upnp-iupnpdevicedocumentaccessex?branch=master)                             | Provides a method to obtain the entire XML device description document for a specific device.                                                                                                                                  |
| [**IUPnPDeviceFinder**](/windows/win32/Upnp/nn-upnp-iupnpdevicefinder?branch=master)                                                 | Enables an application to find a device.                                                                                                                                                                                       |
| [**IUPnPDeviceFinderAddCallbackWithInterface**](/windows/win32/Upnp/nn-upnp-iupnpdevicefinderaddcallbackwithinterface?branch=master) | Enables an application to receive asynchronous search results from the UPnP framework along with the GUID of the network adapter through which the device advertisement came.                                                  |
| [**IUPnPDeviceFinderCallback**](/windows/win32/Upnp/nn-upnp-iupnpdevicefindercallback?branch=master)                                 | Enables an application to receive asynchronous search results from the UPnP framework.                                                                                                                                         |
| [**IUPnPDevices**](/windows/win32/Upnp/nn-upnp-iupnpdevices?branch=master)                                                           | Enumerates a collection of devices.                                                                                                                                                                                            |
| [**IUPnPHttpHeaderControl**](/windows/win32/Upnp/nn-upnp-iupnphttpheadercontrol?branch=master)                                       | Enables an application to set "User Agent" HTTP headers from class instances that implement the [**IUPnPDeviceFinder**](/windows/win32/Upnp/nn-upnp-iupnpdevicefinder?branch=master) or the [**IUPnPDescriptionDocument**](/windows/win32/Upnp/nn-upnp-iupnpdescriptiondocument?branch=master) interfaces. |
| [**IUPnPService**](/windows/win32/Upnp/nn-upnp-iupnpservice?branch=master)                                                           | Enables an application to retrieve state information and invoke actions for a service.                                                                                                                                         |
| [**IUPnPServiceAsync**](/windows/win32/Upnp/nn-upnp-iupnpserviceasync?branch=master)                                                 | Asynchronously query state variables and invoke actions on an instance of a service.                                                                                                                                           |
| [**IUPnPServiceCallback**](/windows/win32/Upnp/nn-upnp-iupnpservicecallback?branch=master)                                           | Enables an application to receive notification from the UPnP framework when events occur.                                                                                                                                      |
| [**IUPnPServices**](/windows/win32/Upnp/nn-upnp-iupnpservices?branch=master)                                                         | Enumerates a collection of services.                                                                                                                                                                                           |



 

 

 




