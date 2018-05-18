---
Description: 'The following control codes are used with changer devices.'
ms.assetid: 'b3a3ffa1-e710-4d96-aff8-5b6876ab032b'
title: Device Management Control Codes
---

# Device Management Control Codes

The following control codes are used with changer devices.



| Value                                                                                          | Meaning                                                                                                                                              |
|------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IOCTL\_CHANGER\_EXCHANGE\_MEDIUM**](ioctl-changer-exchange-medium.md)                      | Moves a piece of media from a source element to one destination, and the piece of media originally in the first destination to a second destination. |
| [**IOCTL\_CHANGER\_GET\_ELEMENT\_STATUS**](ioctl-changer-get-element-status.md)               | Retrieves the status of all elements or a specified number of elements of a particular type.                                                         |
| [**IOCTL\_CHANGER\_GET\_PARAMETERS**](ioctl-changer-get-parameters.md)                        | Retrieves the parameters of the specified device.                                                                                                    |
| [**IOCTL\_CHANGER\_GET\_PRODUCT\_DATA**](ioctl-changer-get-product-data.md)                   | Retrieves the product data for the specified device.                                                                                                 |
| [**IOCTL\_CHANGER\_GET\_STATUS**](ioctl-changer-get-status.md)                                | Retrieves the current status of the specified device.                                                                                                |
| [**IOCTL\_CHANGER\_INITIALIZE\_ELEMENT\_STATUS**](ioctl-changer-initialize-element-status.md) | Initializes the status of all elements or the specified elements of a particular type.                                                               |
| [**IOCTL\_CHANGER\_MOVE\_MEDIUM**](ioctl-changer-move-medium.md)                              | Moves a piece of media to a destination.                                                                                                             |
| [**IOCTL\_CHANGER\_QUERY\_VOLUME\_TAGS**](ioctl-changer-query-volume-tags.md)                 | Retrieves the volume tag information for the specified elements.                                                                                     |
| [**IOCTL\_CHANGER\_REINITIALIZE\_TRANSPORT**](ioctl-changer-reinitialize-transport.md)        | Physically recalibrates a transport element.                                                                                                         |
| [**IOCTL\_CHANGER\_SET\_ACCESS**](ioctl-changer-set-access.md)                                | Sets the state of the device's insert/eject port, door, or keypad.                                                                                   |
| [**IOCTL\_CHANGER\_SET\_POSITION**](ioctl-changer-set-position.md)                            | Sets the changer's robotic transport mechanism to the specified element address.                                                                     |



 

The following control codes are used with device management.



| Control code                                                                                      | Operation                                                                                                    |
|---------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [**IOCTL\_STORAGE\_CHECK\_VERIFY**](ioctl-storage-check-verify.md)                               | Checks for change in a removable-media device.                                                               |
| [**IOCTL\_STORAGE\_EJECT\_MEDIA**](ioctl-storage-eject-media.md)                                 | Ejects media from a SCSI device.                                                                             |
| [**IOCTL\_STORAGE\_EJECTION\_CONTROL**](ioctl-storage-ejection-control.md)                       | Enables or disables the mechanism that ejects media.                                                         |
| [**IOCTL\_STORAGE\_GET\_DEVICE\_NUMBER**](ioctl-storage-get-device-number.md)                    | Retrieves the device type, device number, and, for a partitionable device, the partition number of a device. |
| [**IOCTL\_STORAGE\_GET\_HOTPLUG\_INFO**](ioctl-storage-get-hotplug-info.md)                      | Retrieves the hotplug configuration of the specified device.                                                 |
| [**IOCTL\_STORAGE\_GET\_MEDIA\_SERIAL\_NUMBER**](ioctl-storage-get-media-serial-number.md)       | Retrieves the serial number of a USB device.                                                                 |
| [**IOCTL\_STORAGE\_GET\_MEDIA\_TYPES**](ioctl-storage-get-media-types.md)                        | Retrieves the geometry information of the device.                                                            |
| [**IOCTL\_STORAGE\_GET\_MEDIA\_TYPES\_EX**](ioctl-storage-get-media-types-ex.md)                 | Retrieves information about the types of media supported by a device.                                        |
| [**IOCTL\_STORAGE\_LOAD\_MEDIA**](ioctl-storage-load-media.md)                                   | Loads media into a device.                                                                                   |
| [**IOCTL\_STORAGE\_MANAGE\_DATA\_SET\_ATTRIBUTES**](ioctl-storage-manage-data-set-attributes.md) |                                                                                                              |
| [**IOCTL\_STORAGE\_MCN\_CONTROL**](ioctl-storage-mcn-control.md)                                 | Enables or disables media change notification.                                                               |
| [**IOCTL\_STORAGE\_MEDIA\_REMOVAL**](ioctl-storage-media-removal.md)                             | Enables or disables the media eject mechanism.                                                               |
| [**IOCTL\_STORAGE\_READ\_CAPACITY**](ioctl-storage-read-capacity.md)                             | Retrieves the geometry information for the device.                                                           |
| [**IOCTL\_STORAGE\_SET\_HOTPLUG\_INFO**](ioctl-storage-set-hotplug-info.md)                      | Sets the hotplug configuration of the specified device.                                                      |



 

 

 



