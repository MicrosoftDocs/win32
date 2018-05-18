---
title: Control Point API Reference
description: The following interfaces are part of the Control Point API with UPnP technology. The Control Point API supports Microsoft Visual Basic Scripting Edition (VBScript), Microsoft Visual Basic, and C++.
ms.assetid: '6f73bf8c-0423-430f-a654-58d076712aae'
---

# Control Point API Reference

The following interfaces are part of the Control Point API with UPnP technology. The Control Point API supports Microsoft Visual Basic Scripting Edition (VBScript), Microsoft Visual Basic, and C++.



| Interface                                                                                      | Description                                                                                                                                                                                                                    |
|------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IUPnPAddressFamilyControl**](iupnpaddressfamilycontrol.md)                                 | Enables an application to access the address family flag of the Device Finder object.                                                                                                                                          |
| [**IUPnPDescriptionDocument**](iupnpdescriptiondocument.md)                                   | Enables an application to load a device description. This interface is safe for scripting.                                                                                                                                     |
| [**IUPnPDescriptionDocumentCallback**](iupnpdescriptiondocumentcallback.md)                   | Enables an application to receive the results of an asynchronous load operation.                                                                                                                                               |
| [**IUPnPDevice**](iupnpdevice.md)                                                             | Enables an application to retrieve information about a specific device.                                                                                                                                                        |
| [**IUPnPDeviceDocumentAccess**](iupnpdevicedocumentaccess.md)                                 | Enables an application to obtain the URL of a device description document.                                                                                                                                                     |
| [**IUPnPDeviceDocumentAccessEx**](iupnpdevicedocumentaccessex.md)                             | Provides a method to obtain the entire XML device description document for a specific device.                                                                                                                                  |
| [**IUPnPDeviceFinder**](iupnpdevicefinder.md)                                                 | Enables an application to find a device.                                                                                                                                                                                       |
| [**IUPnPDeviceFinderAddCallbackWithInterface**](iupnpdevicefinderaddcallbackwithinterface.md) | Enables an application to receive asynchronous search results from the UPnP framework along with the GUID of the network adapter through which the device advertisement came.                                                  |
| [**IUPnPDeviceFinderCallback**](iupnpdevicefindercallback.md)                                 | Enables an application to receive asynchronous search results from the UPnP framework.                                                                                                                                         |
| [**IUPnPDevices**](iupnpdevices.md)                                                           | Enumerates a collection of devices.                                                                                                                                                                                            |
| [**IUPnPHttpHeaderControl**](iupnphttpheadercontrol.md)                                       | Enables an application to set "User Agent" HTTP headers from class instances that implement the [**IUPnPDeviceFinder**](iupnpdevicefinder.md) or the [**IUPnPDescriptionDocument**](iupnpdescriptiondocument.md) interfaces. |
| [**IUPnPService**](iupnpservice.md)                                                           | Enables an application to retrieve state information and invoke actions for a service.                                                                                                                                         |
| [**IUPnPServiceAsync**](iupnpserviceasync.md)                                                 | Asynchronously query state variables and invoke actions on an instance of a service.                                                                                                                                           |
| [**IUPnPServiceCallback**](iupnpservicecallback.md)                                           | Enables an application to receive notification from the UPnP framework when events occur.                                                                                                                                      |
| [**IUPnPServices**](iupnpservices.md)                                                         | Enumerates a collection of services.                                                                                                                                                                                           |



 

 

 




