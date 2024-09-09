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
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Device Registration Object

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The device registration object manages the device registration database. This database stores information about network devices, such as set-top video players, that are connected to the client computer. The primary purpose of the device registration database is to manage devices that use the Windows Media DRM 10 for Network Devices protocol to receive secured data streams.

If your application supports Windows Media DRM 10 for Network Devices, you must use the interfaces of this object to register network devices, and to validate those devices. You can also use the device registration database to store information about network devices that do not use Windows Media DRM 10 for Network Devices, although not all of the information in the database will apply to such devices.

The device registration object is created by the [**WMCreateDeviceRegistration**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-wmcreatedeviceregistration) function, which sets a pointer to an **IWMDeviceRegistration** interface. The other methods of the device registration object can be obtained by calling the **QueryInterface** method.

The following interfaces are supported by the device registration object.



| Interface                                              | Description                               |
|--------------------------------------------------------|-------------------------------------------|
| [**IWMDeviceRegistration**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmdeviceregistration) | Manages the device registration database. |
| [**IWMDRMMessageParser**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmdrmmessageparser)     | Parses messages sent by devices.          |
| [**IWMProximityDetection**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmproximitydetection) | Manages device validation.                |



 

The following callback interface must be implemented by the application in order to use the methods of the **IWMProximityDetection** interface.



| Interface                                      | Description                                                                |
|------------------------------------------------|----------------------------------------------------------------------------|
| [**IWMStatusCallback**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmstatuscallback) | Receives status messages from processes that execute in a separate thread. |



 

## Related topics

<dl> <dt>

[**Objects**](objects.md)
</dt> </dl>

 

 




