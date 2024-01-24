---
description: Windows Portable Devices defines the following event values.
ms.assetid: d73788a1-d0fe-4a69-b472-edf438a28f90
title: Event Constants (PortableDevice.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WPD_EVENT_DEVICE_CAPABILITIES_UPDATED
- WPD_EVENT_DEVICE_REMOVED
- WPD_EVENT_DEVICE_RESET
- WPD_EVENT_OBJECT_ADDED
- WPD_EVENT_OBJECT_REMOVED
- WPD_EVENT_OBJECT_TRANSFER_REQUESTED
- WPD_EVENT_OBJECT_UPDATED
- WPD_EVENT_SERVICE_METHOD_COMPLETE
- WPD_EVENT_STORAGE_FORMAT
api_type: 
- HeaderDef
api_location: 
- PortableDevice.h
---

# Event Constants (PortableDevice.h)

Windows Portable Devices defines the following event values.



| Constant                                                                                                                                                                                                                                 | Description                                                                                                                                                                                                                                                                                                                                                             |
|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="WPD_EVENT_DEVICE_CAPABILITIES_UPDATED"></span><span id="wpd_event_device_capabilities_updated"></span><dl> <dt>**WPD\_EVENT\_DEVICE\_CAPABILITIES\_UPDATED**</dt> </dl> | This event indicates that the device capabilities have changed. Clients should requery the device if they have made any decisions based on device capabilities.<br/>                                                                                                                                                                                              |
| <span id="WPD_EVENT_DEVICE_REMOVED"></span><span id="wpd_event_device_removed"></span><dl> <dt>**WPD\_EVENT\_DEVICE\_REMOVED**</dt> </dl>                                         | This event is sent when a driver for a device is being unloaded. Typically this is a result of the device being unplugged.<br/> Clients should release the **IPortableDevice** interface and any [**IPortableDeviceService**](/windows/desktop/api/PortableDeviceAPI/nn-portabledeviceapi-iportabledeviceservice) interfaces specified in **WPD\_EVENT\_PARAMETER\_PNP\_DEVICE\_ID**.<br/>                          |
| <span id="WPD_EVENT_DEVICE_RESET"></span><span id="wpd_event_device_reset"></span><dl> <dt>**WPD\_EVENT\_DEVICE\_RESET**</dt> </dl>                                               | This event indicates that the device is about to be reset, and all connected clients should close their connections to the device.<br/>                                                                                                                                                                                                                           |
| <span id="WPD_EVENT_OBJECT_ADDED"></span><span id="wpd_event_object_added"></span><dl> <dt>**WPD\_EVENT\_OBJECT\_ADDED**</dt> </dl>                                               | This event indicates that a new object is available on the device.<br/>                                                                                                                                                                                                                                                                                           |
| <span id="WPD_EVENT_OBJECT_REMOVED"></span><span id="wpd_event_object_removed"></span><dl> <dt>**WPD\_EVENT\_OBJECT\_REMOVED**</dt> </dl>                                         | This event is sent after a previously existing object has been removed from the device.<br/> The object might be a content object, for example, an image file was deleted; or it might be a functional object, for example, a new storage device was unplugged from the device.<br/>                                                                        |
| <span id="WPD_EVENT_OBJECT_TRANSFER_REQUESTED"></span><span id="wpd_event_object_transfer_requested"></span><dl> <dt>**WPD\_EVENT\_OBJECT\_TRANSFER\_REQUESTED**</dt> </dl>       | This event is sent to request an application to transfer a particular object from the device.<br/> The object is usually a content object, for example, an image file.<br/>                                                                                                                                                                                 |
| <span id="WPD_EVENT_OBJECT_UPDATED"></span><span id="wpd_event_object_updated"></span><dl> <dt>**WPD\_EVENT\_OBJECT\_UPDATED**</dt> </dl>                                         | This event is sent after an object has been updated, and any connected client should refresh its view of that object.<br/>                                                                                                                                                                                                                                        |
| <span id="WPD_EVENT_SERVICE_METHOD_COMPLETE"></span><span id="wpd_event_service_method_complete"></span><dl> <dt>**WPD\_EVENT\_SERVICE\_METHOD\_COMPLETE**</dt> </dl>             | This event is sent when a driver has completed invoking a service method. This event must be sent even when the method fails. This is an internal WPD DDI event, and will not be available to any applications through [**IPortableDevice::Advise**](/windows/desktop/api/PortableDeviceApi/nf-portabledeviceapi-iportabledevice-advise) or [**IPortableDeviceService::Advise**](/windows/desktop/api/PortableDeviceAPI/nf-portabledeviceapi-iportabledeviceservice-advise).<br/> |
| <span id="WPD_EVENT_STORAGE_FORMAT"></span><span id="wpd_event_storage_format"></span><dl> <dt>**WPD\_EVENT\_STORAGE\_FORMAT**</dt> </dl>                                         | This event indicates the progress of a format operation on a storage object.<br/>                                                                                                                                                                                                                                                                                 |



## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>PortableDevice.h</dt> </dl> |



## See also

<dl> <dt>

[Constants](constants.md)
</dt> </dl>

 

 




