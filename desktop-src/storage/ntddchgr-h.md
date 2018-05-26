---
title: Ntddchgr.h
description: This section contains reference topics for the Ntddchgr.h header.
ms.assetid: 90E8664E-BB57-498C-8325-B747B4F02913
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Ntddchgr.h

This section contains reference topics for the Ntddchgr.h header.

## In this section



| Topic                                                                                             | Description                                                                                                                                                                                                                                                                                               |
|---------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Changer I/O Control Codes](changer-i-o-control-codes.md)<br/>                             |                                                                                                                                                                                                                                                                                                           |
| [Changer Class Driver Routines](changer-class-driver-routines.md)<br/>                     |                                                                                                                                                                                                                                                                                                           |
| [Changer Miniclass Driver Routines](changer-miniclass-driver-routines.md)<br/>             |                                                                                                                                                                                                                                                                                                           |
| [**CHANGER\_DEVICE\_PROBLEM\_TYPE**](changer-device-problem-type.md)<br/>                  | The CHANGER\_DEVICE\_PROBLEM\_TYPE data type contains the values returned by the [**ChangerPerformDiagnostics**](changerperformdiagnostics.md) routine.<br/>                                                                                                                                       |
| [**CHANGER\_ELEMENT**](changer-element.md)<br/>                                            | The CHANGER\_ELEMENT structure contains a description of a changer element. <br/>                                                                                                                                                                                                                   |
| [**CHANGER\_ELEMENT\_LIST**](changer-element-list.md)<br/>                                 | The CHANGER\_ELEMENT\_LIST structure indicates a range of elements of a single type. <br/>                                                                                                                                                                                                          |
| [**CHANGER\_ELEMENT\_STATUS**](changer-element-status.md)<br/>                             | The [**ChangerGetElementStatus**](changergetelementstatus.md) routine returns status information in this structure. <br/>                                                                                                                                                                          |
| [**CHANGER\_ELEMENT\_STATUS\_EX**](changer-element-status-ex.md)<br/>                      | The [**ChangerGetElementStatus**](changergetelementstatus.md) routine returns status information in this structure. <br/>                                                                                                                                                                          |
| [**CHANGER\_EXCHANGE\_MEDIUM**](changer-exchange-medium.md)<br/>                           | The CHANGER\_EXCHANGE\_MEDIUM structure is used with the [**IOCTL\_CHANGER\_EXCHANGE\_MEDIUM**](ioctl-changer-exchange-medium.md) request to exchange locations of two pieces of media.<br/>                                                                                                       |
| [**CHANGER\_INITIALIZE\_ELEMENT\_STATUS**](changer-initialize-element-status.md)<br/>      | The CHANGER\_INITIALIZE\_ELEMENT\_STATUS structure is used in conjunction with the [**IOCTL\_CHANGER\_INITIALIZE\_ELEMENT\_STATUS**](ioctl-changer-initialize-element-status.md) request to initialize the status of all elements or of a specified number of elements of a particular type. <br/> |
| [**CHANGER\_MOVE\_MEDIUM**](changer-move-medium.md)<br/>                                   | The CHANGER\_MOVE\_MEDIUM structure is used in conjunction with the [**IOCTL\_CHANGER\_MOVE\_MEDIUM**](ioctl-changer-move-medium.md) request to move a piece of media from a source element to a destination. <br/>                                                                                |
| [**CHANGER\_PRODUCT\_DATA**](changer-product-data.md)<br/>                                 | The CHANGER\_PRODUCT\_DATA structure is used in conjunction with the [**IOCTL\_CHANGER\_GET\_PRODUCT\_DATA**](ioctl-changer-get-product-data.md) request to retrieve product data for a device. <br/>                                                                                              |
| [**CHANGER\_READ\_ELEMENT\_STATUS**](changer-read-element-status.md)<br/>                  | The CHANGER\_READ\_ELEMENT\_STATUS structure is used in conjunction with the [**IOCTL\_CHANGER\_GET\_ELEMENT\_STATUS**](ioctl-changer-get-element-status.md) request to retrieve the status of all elements or the status of a specified number of elements of a particular type. <br/>            |
| [**CHANGER\_SEND\_VOLUME\_TAG\_INFORMATION**](changer-send-volume-tag-information.md)<br/> | This structure is passed to the [**ChangerQueryVolumeTags**](changerqueryvolumetags.md) routine and is used to specify a search criterion for retrieving changer elements. <br/>                                                                                                                   |
| [**CHANGER\_SET\_ACCESS**](changer-set-access.md)<br/>                                     | The CHANGER\_SET\_ACCESS structure is used in conjunction with the[**IOCTL\_CHANGER\_SET\_ACCESS**](ioctl-changer-set-access.md) request to set the state of the device's import/export port (IEport), door, or keypad. <br/>                                                                      |
| [**CHANGER\_SET\_POSITION**](changer-set-position.md)<br/>                                 | The CHANGER\_SET\_POSITION structure is used in conjunction with the[**IOCTL\_CHANGER\_SET\_POSITION**](ioctl-changer-set-position.md) request to set the changer's robotic transport mechanism to the specified element address.<br/>                                                             |
| [**ELEMENT\_TYPE**](element-type.md)<br/>                                                  | The ELEMENT\_TYPE enumeration provides a list of changer element types defined by the *SCSI-3* specification. <br/>                                                                                                                                                                                 |
| [**GET\_CHANGER\_PARAMETERS**](get-changer-parameters.md)<br/>                             | Retrieves the characteristics of the changer. <br/>                                                                                                                                                                                                                                                 |
| [**READ\_ELEMENT\_ADDRESS\_INFO**](read-element-address-info.md)<br/>                      | This structure is to retrieve changer elements based on a search criterion specified in a call to the [**ChangerQueryVolumeTags**](changerqueryvolumetags.md) routine. <br/>                                                                                                                       |



 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20Ntddchgr.h%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





