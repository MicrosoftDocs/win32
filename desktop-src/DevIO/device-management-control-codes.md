---
Description: The following control codes are used with changer devices.
ms.assetid: b3a3ffa1-e710-4d96-aff8-5b6876ab032b
title: Device Management Control Codes
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Device Management Control Codes

The following control codes are used with changer devices.



| Value                                                                                          | Meaning                                                                                                                                              |
|------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IOCTL\_CHANGER\_EXCHANGE\_MEDIUM**](/windows/win32/WinIoCtl/ni-winioctl-ioctl_changer_exchange_medium?branch=master)                      | Moves a piece of media from a source element to one destination, and the piece of media originally in the first destination to a second destination. |
| [**IOCTL\_CHANGER\_GET\_ELEMENT\_STATUS**](/windows/win32/WinIoCtl/ni-winioctl-ioctl_changer_get_element_status?branch=master)               | Retrieves the status of all elements or a specified number of elements of a particular type.                                                         |
| [**IOCTL\_CHANGER\_GET\_PARAMETERS**](/windows/win32/WinIoCtl/ni-winioctl-ioctl_changer_get_parameters?branch=master)                        | Retrieves the parameters of the specified device.                                                                                                    |
| [**IOCTL\_CHANGER\_GET\_PRODUCT\_DATA**](/windows/win32/WinIoCtl/ni-winioctl-ioctl_changer_get_product_data?branch=master)                   | Retrieves the product data for the specified device.                                                                                                 |
| [**IOCTL\_CHANGER\_GET\_STATUS**](/windows/win32/WinIoCtl/ni-winioctl-ioctl_changer_get_status?branch=master)                                | Retrieves the current status of the specified device.                                                                                                |
| [**IOCTL\_CHANGER\_INITIALIZE\_ELEMENT\_STATUS**](/windows/win32/WinIoCtl/ni-winioctl-ioctl_changer_initialize_element_status?branch=master) | Initializes the status of all elements or the specified elements of a particular type.                                                               |
| [**IOCTL\_CHANGER\_MOVE\_MEDIUM**](/windows/win32/WinIoCtl/ni-winioctl-ioctl_changer_move_medium?branch=master)                              | Moves a piece of media to a destination.                                                                                                             |
| [**IOCTL\_CHANGER\_QUERY\_VOLUME\_TAGS**](/windows/win32/WinIoCtl/ni-winioctl-ioctl_changer_query_volume_tags?branch=master)                 | Retrieves the volume tag information for the specified elements.                                                                                     |
| [**IOCTL\_CHANGER\_REINITIALIZE\_TRANSPORT**](/windows/win32/WinIoCtl/ni-winioctl-ioctl_changer_reinitialize_transport?branch=master)        | Physically recalibrates a transport element.                                                                                                         |
| [**IOCTL\_CHANGER\_SET\_ACCESS**](/windows/win32/WinIoCtl/ni-winioctl-ioctl_changer_set_access?branch=master)                                | Sets the state of the device's insert/eject port, door, or keypad.                                                                                   |
| [**IOCTL\_CHANGER\_SET\_POSITION**](/windows/win32/WinIoCtl/ni-winioctl-ioctl_changer_set_position?branch=master)                            | Sets the changer's robotic transport mechanism to the specified element address.                                                                     |



 

The following control codes are used with device management.



| Control code                                                                                      | Operation                                                                                                    |
|---------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [**IOCTL\_STORAGE\_CHECK\_VERIFY**](/windows/win32/WinIoCtl/ni-winioctl-ioctl_storage_check_verify?branch=master)                               | Checks for change in a removable-media device.                                                               |
| [**IOCTL\_STORAGE\_EJECT\_MEDIA**](/windows/win32/WinIoCtl/ni-winioctl-ioctl_storage_eject_media?branch=master)                                 | Ejects media from a SCSI device.                                                                             |
| [**IOCTL\_STORAGE\_EJECTION\_CONTROL**](/windows/win32/WinIoCtl/ni-winioctl-ioctl_storage_ejection_control?branch=master)                       | Enables or disables the mechanism that ejects media.                                                         |
| [**IOCTL\_STORAGE\_GET\_DEVICE\_NUMBER**](/windows/win32/WinIoCtl/ni-winioctl-ioctl_storage_get_device_number?branch=master)                    | Retrieves the device type, device number, and, for a partitionable device, the partition number of a device. |
| [**IOCTL\_STORAGE\_GET\_HOTPLUG\_INFO**](/windows/win32/WinIoCtl/ni-winioctl-ioctl_storage_get_hotplug_info?branch=master)                      | Retrieves the hotplug configuration of the specified device.                                                 |
| [**IOCTL\_STORAGE\_GET\_MEDIA\_SERIAL\_NUMBER**](/windows/win32/WinIoCtl/ni-winioctl-ioctl_storage_get_media_serial_number?branch=master)       | Retrieves the serial number of a USB device.                                                                 |
| [**IOCTL\_STORAGE\_GET\_MEDIA\_TYPES**](/windows/win32/WinIoCtl/ni-winioctl-ioctl_storage_get_media_types?branch=master)                        | Retrieves the geometry information of the device.                                                            |
| [**IOCTL\_STORAGE\_GET\_MEDIA\_TYPES\_EX**](/windows/win32/WinIoCtl/ni-winioctl-ioctl_storage_get_media_types_ex?branch=master)                 | Retrieves information about the types of media supported by a device.                                        |
| [**IOCTL\_STORAGE\_LOAD\_MEDIA**](/windows/win32/WinIoCtl/ni-winioctl-ioctl_storage_load_media?branch=master)                                   | Loads media into a device.                                                                                   |
| [**IOCTL\_STORAGE\_MANAGE\_DATA\_SET\_ATTRIBUTES**](/windows/win32/WinIoCtl/ni-winioctl-ioctl_storage_manage_data_set_attributes?branch=master) |                                                                                                              |
| [**IOCTL\_STORAGE\_MCN\_CONTROL**](/windows/win32/WinIoCtl/ni-winioctl-ioctl_storage_mcn_control?branch=master)                                 | Enables or disables media change notification.                                                               |
| [**IOCTL\_STORAGE\_MEDIA\_REMOVAL**](/windows/win32/WinIoCtl/ni-winioctl-ioctl_storage_media_removal?branch=master)                             | Enables or disables the media eject mechanism.                                                               |
| [**IOCTL\_STORAGE\_READ\_CAPACITY**](/windows/win32/WinIoCtl/ni-winioctl-ioctl_storage_read_capacity?branch=master)                             | Retrieves the geometry information for the device.                                                           |
| [**IOCTL\_STORAGE\_SET\_HOTPLUG\_INFO**](/windows/win32/WinIoCtl/ni-winioctl-ioctl_storage_set_hotplug_info?branch=master)                      | Sets the hotplug configuration of the specified device.                                                      |



 

 

 



