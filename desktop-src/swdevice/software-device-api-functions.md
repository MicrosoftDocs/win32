---
title: Software Device API Functions
description: This section describes Software Device API functions that a client app calls and a callback function that a client app implements.
ms.assetid: 68F142A9-08AD-4F74-A0C3-3DCC8F7449B2
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Software Device API Functions

This section describes Software Device API functions that a client app calls and a callback function that a client app implements.

## In this section



| Topic                                                                           | Description                                                                                                                                                      |
|---------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**SwDeviceClose**](/windows/win32/Swdevice/nf-swdevice-swdeviceclose?branch=master)<br/>                               | Closes the software device handle. When the handle is closed, PnP will initiate the process of removing the device.<br/>                                   |
| [**SW\_DEVICE\_CREATE\_CALLBACK**](/windows/win32/Swdevice/nc-swdevice-sw_device_create_callback?branch=master)<br/>    | Provides a device with backing in the registry and allows the caller to then make calls to Software Device API functions with the *hSwDevice* handle.<br/> |
| [**SwDeviceCreate**](/windows/win32/Swdevice/nf-swdevice-swdevicecreate?branch=master)<br/>                             | Initiates the enumeration of a software device.<br/>                                                                                                       |
| [**SwDeviceGetLifetime**](/windows/win32/Swdevice/nf-swdevice-swdevicegetlifetime?branch=master)<br/>                   | Gets the lifetime of a software device. <br/>                                                                                                              |
| [**SwDeviceInterfacePropertySet**](/windows/win32/Swdevice/nf-swdevice-swdeviceinterfacepropertyset?branch=master)<br/> | Sets properties on a software device interface. <br/>                                                                                                      |
| [**SwDeviceInterfaceRegister**](/windows/win32/Swdevice/nf-swdevice-swdeviceinterfaceregister?branch=master)<br/>       | Registers a device interface for a software device and optionally sets properties on that interface. <br/>                                                 |
| [**SwDeviceInterfaceSetState**](/windows/win32/Swdevice/nf-swdevice-swdeviceinterfacesetstate?branch=master)<br/>       | Enables or disables a device interface for a software device. <br/>                                                                                        |
| [**SwDevicePropertySet**](/windows/win32/Swdevice/nf-swdevice-swdevicepropertyset?branch=master)<br/>                   | Sets properties on a software device. <br/>                                                                                                                |
| [**SwDeviceSetLifetime**](/windows/win32/Swdevice/nf-swdevice-swdevicesetlifetime?branch=master)<br/>                   | Manages the lifetime of a software device. <br/>                                                                                                           |
| [**SwMemFree**](/windows/win32/Swdevice/nf-swdevice-swmemfree?branch=master)<br/>                                       | Frees memory that other Software Device API functions allocated.<br/>                                                                                      |



 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bswdevice\swdevice%5D:%20Software%20Device%20API%20Functions%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





