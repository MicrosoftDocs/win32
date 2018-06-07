---
Description: The device interface can be described by a GUID value. Windows Portable Devices defines the following device interface.
ms.assetid: 47b8d3dd-ea12-461d-935d-2de2c0157f88
title: Device Interface GUIDs
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Device Interface GUIDs

The device interface can be described by a **GUID** value. Windows Portable Devices defines the following device interface.



| Constant                                                                                                                                                                                                        | Description                                                                                                                                                                                                                                                                                   |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="GUID_DEVINTERFACE_WPD"></span><span id="guid_devinterface_wpd"></span><dl> <dt>**GUID\_DEVINTERFACE\_WPD**</dt> </dl>                          | Identifies devices that appear in a normal WPD enumeration. Any device that registers this interface GUID will be enumerated when an application calls the [**IPortableDeviceManager::GetDevices**](/windows/desktop/api/PortableDeviceApi/nf-portabledeviceapi-iportabledevicemanager-getdevices) method.<br/>                                 |
| <span id="GUID_DEVINTERFACE_WPD_PRIVATE"></span><span id="guid_devinterface_wpd_private"></span><dl> <dt>**GUID\_DEVINTERFACE\_WPD\_PRIVATE**</dt> </dl> | Identifies devices that will not appear during a normal WPD enumeration. Any device that registers this interface GUID will be enumerated only when an application calls the [**IPortableDeviceManager::GetPrivateDevices**](/windows/desktop/api/PortableDeviceApi/nf-portabledeviceapi-iportabledevicemanager-getprivatedevices) method.<br/> |
| <span id="GUID_DEVINTERFACE_WPD_SERVICE"></span><span id="guid_devinterface_wpd_service"></span><dl> <dt>**GUID\_DEVINTERFACE\_WPD\_SERVICE**</dt> </dl> | In Windows 7, applications can enumerate all WPD device services by calling [**IPortableDeviceServiceManager::GetDeviceServices**](/windows/desktop/api/PortableDeviceAPI/nf-portabledeviceapi-iportabledeviceservicemanager-getdeviceservices) and using this interface class as the service-type GUID.<br/>                                   |



## Requirements



|                   |                                                                                             |
|-------------------|---------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>PortableDevice.h</dt> </dl> |



## See also

<dl> <dt>

[Programming Reference](programming-reference.md)
</dt> </dl>

 

 




