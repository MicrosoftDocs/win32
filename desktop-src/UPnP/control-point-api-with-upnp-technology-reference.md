---
title: Control Point API Reference
description: The following interfaces are part of the Control Point API with UPnP technology. The Control Point API supports Microsoft Visual Basic Scripting Edition (VBScript), Microsoft Visual Basic, and C++.
ms.assetid: 6f73bf8c-0423-430f-a654-58d076712aae
ms.topic: article
ms.date: 05/31/2018
---

# Control Point API Reference

The following interfaces are part of the Control Point API with UPnP technology. The Control Point API supports Microsoft Visual Basic Scripting Edition (VBScript), Microsoft Visual Basic, and C++.



| Interface                                                                                      | Description                                                                                                                                                                                                                    |
|------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IUPnPAddressFamilyControl**](/windows/desktop/api/Upnp/nn-upnp-iupnpaddressfamilycontrol)                                 | Enables an application to access the address family flag of the Device Finder object.                                                                                                                                          |
| [**IUPnPDescriptionDocument**](/windows/desktop/api/Upnp/nn-upnp-iupnpdescriptiondocument)                                   | Enables an application to load a device description. This interface is safe for scripting.                                                                                                                                     |
| [**IUPnPDescriptionDocumentCallback**](/windows/desktop/api/Upnp/nn-upnp-iupnpdescriptiondocumentcallback)                   | Enables an application to receive the results of an asynchronous load operation.                                                                                                                                               |
| [**IUPnPDevice**](/windows/desktop/api/Upnp/nn-upnp-iupnpdevice)                                                             | Enables an application to retrieve information about a specific device.                                                                                                                                                        |
| [**IUPnPDeviceDocumentAccess**](/windows/desktop/api/Upnp/nn-upnp-iupnpdevicedocumentaccess)                                 | Enables an application to obtain the URL of a device description document.                                                                                                                                                     |
| [**IUPnPDeviceDocumentAccessEx**](/windows/desktop/api/Upnp/nn-upnp-iupnpdevicedocumentaccessex)                             | Provides a method to obtain the entire XML device description document for a specific device.                                                                                                                                  |
| [**IUPnPDeviceFinder**](/windows/desktop/api/Upnp/nn-upnp-iupnpdevicefinder)                                                 | Enables an application to find a device.                                                                                                                                                                                       |
| [**IUPnPDeviceFinderAddCallbackWithInterface**](/windows/desktop/api/Upnp/nn-upnp-iupnpdevicefinderaddcallbackwithinterface) | Enables an application to receive asynchronous search results from the UPnP framework along with the GUID of the network adapter through which the device advertisement came.                                                  |
| [**IUPnPDeviceFinderCallback**](/windows/desktop/api/Upnp/nn-upnp-iupnpdevicefindercallback)                                 | Enables an application to receive asynchronous search results from the UPnP framework.                                                                                                                                         |
| [**IUPnPDevices**](/windows/desktop/api/Upnp/nn-upnp-iupnpdevices)                                                           | Enumerates a collection of devices.                                                                                                                                                                                            |
| [**IUPnPHttpHeaderControl**](/windows/desktop/api/Upnp/nn-upnp-iupnphttpheadercontrol)                                       | Enables an application to set "User Agent" HTTP headers from class instances that implement the [**IUPnPDeviceFinder**](/windows/desktop/api/Upnp/nn-upnp-iupnpdevicefinder) or the [**IUPnPDescriptionDocument**](/windows/desktop/api/Upnp/nn-upnp-iupnpdescriptiondocument) interfaces. |
| [**IUPnPService**](/windows/desktop/api/Upnp/nn-upnp-iupnpservice)                                                           | Enables an application to retrieve state information and invoke actions for a service.                                                                                                                                         |
| [**IUPnPServiceAsync**](/windows/desktop/api/Upnp/nn-upnp-iupnpserviceasync)                                                 | Asynchronously query state variables and invoke actions on an instance of a service.                                                                                                                                           |
| [**IUPnPServiceCallback**](/windows/desktop/api/Upnp/nn-upnp-iupnpservicecallback)                                           | Enables an application to receive notification from the UPnP framework when events occur.                                                                                                                                      |
| [**IUPnPServices**](/windows/desktop/api/Upnp/nn-upnp-iupnpservices)                                                         | Enumerates a collection of services.                                                                                                                                                                                           |



 

 

 




