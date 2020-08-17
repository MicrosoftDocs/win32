---
title: IWMDRMDeviceApp interface
description: The IWMDRMDeviceApp interface enables an application to meter, synchronize licenses, and update a device's DRM components.
ms.assetid: e47167c2-ea14-4173-8ce9-8d8540a0fc73
keywords:
- IWMDRMDeviceApp interface windows Media Device Manager
- IWMDRMDeviceApp interface windows Media Device Manager , described
topic_type:
- apiref
api_name:
- IWMDRMDeviceApp
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IWMDRMDeviceApp interface

\[The Windows Media DRM feature is deprecated and should not be used. Use [Microsoft PlayReady](/windows/uwp/audio-video-camera/playready-client-sdk) instead.\]

The **IWMDRMDeviceApp** interface enables an application to meter, synchronize licenses, and update a device's DRM components. This interface will only work with devices that support Windows Media DRM 10 for Portable Devices.

To get this interface, call **CoCreateInstance**, passing in CLSID\_WMDRMDeviceApp.

> [!Note]  
> This interface is defined in the header file built from WMDRMDeviceApp.idl. This header **\#include**s "wmdm.h". You might need to change this file name to match the header built from WMDM.idl.

 

## Members

The **IWMDRMDeviceApp** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IWMDRMDeviceApp** also has these types of members:

-   [Methods](#methods)

### Methods

The **IWMDRMDeviceApp** interface has these methods.



| Method                                                                   | Description                                                                                                                                |
|:-------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------|
| [**AcquireDeviceData**](iwmdrmdeviceapp-acquiredevicedata.md)           | Initializes or resets a device secure clock<br/>                                                                                     |
| [**GenerateMeterChallenge**](iwmdrmdeviceapp-generatemeterchallenge.md) | Acquires metering data from a device.<br/>                                                                                           |
| [**ProcessMeterResponse**](iwmdrmdeviceapp-processmeterresponse.md)     | Resets some or all of the metering counts on a device, after data from the device has been sent to and processed by the server.<br/> |
| [**QueryDeviceStatus**](iwmdrmdeviceapp-querydevicestatus.md)           | Queries a device for its current DRM status and capabilities.<br/>                                                                   |
| [**SynchronizeLicenses**](iwmdrmdeviceapp-synchronizelicenses.md)       | Updates licenses on a device when they are close to expiring.<br/>                                                                   |



 

## See also

<dl> <dt>

[**Handling Protected Content in the Application**](handling-protected-content-in-the-application.md)
</dt> <dt>

[**Interfaces for Applications**](interfaces-for-applications.md)
</dt> <dt>

[**Metering Content Usage**](metering-content-usage.md)
</dt> </dl>

 

