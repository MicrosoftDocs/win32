---
description: The following control codes are used with changer devices.
ms.assetid: b3a3ffa1-e710-4d96-aff8-5b6876ab032b
title: Device Management Control Codes
ms.topic: article
ms.date: 05/31/2018
---

# Device Management Control Codes

The following control codes are used with changer devices.



| Value                                                                                          | Meaning                                                                                                                                              |
|------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IOCTL\_CHANGER\_EXCHANGE\_MEDIUM**](/windows/desktop/api/WinIoCtl/ni-winioctl-ioctl_changer_exchange_medium)                      | Moves a piece of media from a source element to one destination, and the piece of media originally in the first destination to a second destination. |
| [**IOCTL\_CHANGER\_GET\_ELEMENT\_STATUS**](/windows/desktop/api/WinIoCtl/ni-winioctl-ioctl_changer_get_element_status)               | Retrieves the status of all elements or a specified number of elements of a particular type.                                                         |
| [**IOCTL\_CHANGER\_GET\_PARAMETERS**](/windows/desktop/api/WinIoCtl/ni-winioctl-ioctl_changer_get_parameters)                        | Retrieves the parameters of the specified device.                                                                                                    |
| [**IOCTL\_CHANGER\_GET\_PRODUCT\_DATA**](/windows/desktop/api/WinIoCtl/ni-winioctl-ioctl_changer_get_product_data)                   | Retrieves the product data for the specified device.                                                                                                 |
| [**IOCTL\_CHANGER\_GET\_STATUS**](/windows/desktop/api/WinIoCtl/ni-winioctl-ioctl_changer_get_status)                                | Retrieves the current status of the specified device.                                                                                                |
| [**IOCTL\_CHANGER\_INITIALIZE\_ELEMENT\_STATUS**](/windows/desktop/api/WinIoCtl/ni-winioctl-ioctl_changer_initialize_element_status) | Initializes the status of all elements or the specified elements of a particular type.                                                               |
| [**IOCTL\_CHANGER\_MOVE\_MEDIUM**](/windows/desktop/api/WinIoCtl/ni-winioctl-ioctl_changer_move_medium)                              | Moves a piece of media to a destination.                                                                                                             |
| [**IOCTL\_CHANGER\_QUERY\_VOLUME\_TAGS**](/windows/desktop/api/WinIoCtl/ni-winioctl-ioctl_changer_query_volume_tags)                 | Retrieves the volume tag information for the specified elements.                                                                                     |
| [**IOCTL\_CHANGER\_REINITIALIZE\_TRANSPORT**](/windows/desktop/api/WinIoCtl/ni-winioctl-ioctl_changer_reinitialize_transport)        | Physically recalibrates a transport element.                                                                                                         |
| [**IOCTL\_CHANGER\_SET\_ACCESS**](/windows/desktop/api/WinIoCtl/ni-winioctl-ioctl_changer_set_access)                                | Sets the state of the device's insert/eject port, door, or keypad.                                                                                   |
| [**IOCTL\_CHANGER\_SET\_POSITION**](/windows/desktop/api/WinIoCtl/ni-winioctl-ioctl_changer_set_position)                            | Sets the changer's robotic transport mechanism to the specified element address.                                                                     |



 

The following control codes are used with device management.



| Control code                                                                                      | Operation                                                                                                    |
|---------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [**IOCTL\_STORAGE\_CHECK\_VERIFY**](/windows/desktop/api/WinIoCtl/ni-winioctl-ioctl_storage_check_verify)                               | Checks for change in a removable-media device.                                                               |
| [**IOCTL\_STORAGE\_EJECT\_MEDIA**](/windows/desktop/api/WinIoCtl/ni-winioctl-ioctl_storage_eject_media)                                 | Ejects media from a SCSI device.                                                                             |
| [**IOCTL\_STORAGE\_EJECTION\_CONTROL**](/windows/desktop/api/WinIoCtl/ni-winioctl-ioctl_storage_ejection_control)                       | Enables or disables the mechanism that ejects media.                                                         |
| [**IOCTL\_STORAGE\_GET\_DEVICE\_NUMBER**](/windows/desktop/api/WinIoCtl/ni-winioctl-ioctl_storage_get_device_number)                    | Retrieves the device type, device number, and, for a partitionable device, the partition number of a device. |
| [**IOCTL\_STORAGE\_GET\_HOTPLUG\_INFO**](/windows/desktop/api/WinIoCtl/ni-winioctl-ioctl_storage_get_hotplug_info)                      | Retrieves the hotplug configuration of the specified device.                                                 |
| [**IOCTL\_STORAGE\_GET\_MEDIA\_SERIAL\_NUMBER**](/windows/desktop/api/WinIoCtl/ni-winioctl-ioctl_storage_get_media_serial_number)       | Retrieves the serial number of a USB device.                                                                 |
| [**IOCTL\_STORAGE\_GET\_MEDIA\_TYPES**](/windows/desktop/api/WinIoCtl/ni-winioctl-ioctl_storage_get_media_types)                        | Retrieves the geometry information of the device.                                                            |
| [**IOCTL\_STORAGE\_GET\_MEDIA\_TYPES\_EX**](/windows/desktop/api/WinIoCtl/ni-winioctl-ioctl_storage_get_media_types_ex)                 | Retrieves information about the types of media supported by a device.                                        |
| [**IOCTL\_STORAGE\_LOAD\_MEDIA**](/windows/desktop/api/WinIoCtl/ni-winioctl-ioctl_storage_load_media)                                   | Loads media into a device.                                                                                   |
| [**IOCTL\_STORAGE\_MANAGE\_DATA\_SET\_ATTRIBUTES**](/windows/desktop/api/WinIoCtl/ni-winioctl-ioctl_storage_manage_data_set_attributes) |                                                                                                              |
| [**IOCTL\_STORAGE\_MCN\_CONTROL**](/windows/desktop/api/WinIoCtl/ni-winioctl-ioctl_storage_mcn_control)                                 | Enables or disables media change notification.                                                               |
| [**IOCTL\_STORAGE\_MEDIA\_REMOVAL**](/windows/desktop/api/WinIoCtl/ni-winioctl-ioctl_storage_media_removal)                             | Enables or disables the media eject mechanism.                                                               |
| [**IOCTL\_STORAGE\_READ\_CAPACITY**](/windows/desktop/api/WinIoCtl/ni-winioctl-ioctl_storage_read_capacity)                             | Retrieves the geometry information for the device.                                                           |
| [**IOCTL\_STORAGE\_SET\_HOTPLUG\_INFO**](/windows/desktop/api/WinIoCtl/ni-winioctl-ioctl_storage_set_hotplug_info)                      | Sets the hotplug configuration of the specified device.                                                      |



 

 

 



