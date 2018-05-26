---
title: Device Registration Object
description: Device Registration Object
ms.assetid: 6a23b314-deec-47aa-b12e-cb8f4ff71fb6
keywords:
- Windows Media Format SDK,device registration objects
- Advanced Systems Format (ASF),device registration objects
- ASF (Advanced Systems Format),device registration objects
- objects,device registration objects
- device registration objects
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Device Registration Object

The device registration object manages the device registration database. This database stores information about network devices, such as set-top video players, that are connected to the client computer. The primary purpose of the device registration database is to manage devices that use the Windows Media DRM 10 for Network Devices protocol to receive secured data streams.

If your application supports Windows Media DRM 10 for Network Devices, you must use the interfaces of this object to register network devices, and to validate those devices. You can also use the device registration database to store information about network devices that do not use Windows Media DRM 10 for Network Devices, although not all of the information in the database will apply to such devices.

The device registration object is created by the [**WMCreateDeviceRegistration**](/windows/win32/Wmsdkidl/nf-wmsdkidl-wmcreatedeviceregistration?branch=master) function, which sets a pointer to an **IWMDeviceRegistration** interface. The other methods of the device registration object can be obtained by calling the **QueryInterface** method.

The following interfaces are supported by the device registration object.



| Interface                                              | Description                               |
|--------------------------------------------------------|-------------------------------------------|
| [**IWMDeviceRegistration**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmdeviceregistration?branch=master) | Manages the device registration database. |
| [**IWMDRMMessageParser**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmdrmmessageparser?branch=master)     | Parses messages sent by devices.          |
| [**IWMProximityDetection**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmproximitydetection?branch=master) | Manages device validation.                |



 

The following callback interface must be implemented by the application in order to use the methods of the **IWMProximityDetection** interface.



| Interface                                      | Description                                                                |
|------------------------------------------------|----------------------------------------------------------------------------|
| [**IWMStatusCallback**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmstatuscallback?branch=master) | Receives status messages from processes that execute in a separate thread. |



 

## Related topics

<dl> <dt>

[**Objects**](objects.md)
</dt> </dl>

 

 




