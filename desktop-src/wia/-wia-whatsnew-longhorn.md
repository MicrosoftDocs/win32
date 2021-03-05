---
description: Many new Windows Image Acquisition (WIA) API are included in Windows Image Acquisition (WIA) 2.0.
ms.assetid: d8e85c34-d8ce-4512-af71-102a21393fdf
title: What's New in Windows Image Acquisition (WIA) 2.0
ms.topic: article
ms.date: 05/31/2018
---

# What's New in Windows Image Acquisition (WIA) 2.0

Many new Windows Image Acquisition (WIA) API are included in Windows Image Acquisition (WIA) 2.0. Moreover, there are some forward and backward incompatibilities between Windows Image Acquisition (WIA) 1.0 and the WIA 2.0 service that ships with Windows Vista. Some interfaces, structures, properties, and property values of WIA 1.0 are not supported by, and applications using them will not run on, Windows Vista and later. Similarly, applications using the new interfaces, structures, properties, and property values introduced with WIA 2.0 (see below) will not run on OS versions prior to Windows Vista.

## New API for WIA 2.0

### Constants: Lists Updated for WIA 2.0

-   [**Common WIA Item Property Constants**](-wia-wiaitempropcommonitem.md)
-   [**Device Information Property Constants**](-wia-wiadeviceinfoprop.md)
-   [**Scanner Device Property Constants**](-wia-wiaitempropscannerdevice.md)
-   [**Scanner WIA Item Property Constants**](-wia-wiaitempropscanneritem.md)
-   [**WIA 2.0 Item Category GUIDs**](-wia-wia2-itemcategoryguids.md)
-   [**WIA 2.0 Page Size Constants**](-wia-wia2-pagesizeconstants.md)
-   [**WIA Item Type Flags**](-wia-wia-item-type-flags.md)

### New Structures in WIA 2.0



| Topic                                               | Contents                                                                                                                                                                                                                                                          |
|-----------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DEVICEDIALOGDATA2**](-wia-devicedialogdata2.md) | Defines the data needed to call a device dialog.<br/>                                                                                                                                                                                                       |
| [**WIA\_RAW\_HEADER**](-wia-wia-raw-header.md)     | The [**WIA\_RAW\_HEADER**](-wia-wia-raw-header.md) structure defines an image in the RAW data format of a device and enables applications to use RAW format in WIA transfers.<br/>                                                                         |
| [**WiaTransferParams**](-wia-wiatransferparams.md) | The [**WiaTransferParams**](-wia-wiatransferparams.md) is transmitted to an application during a data transfer by the WIA run-time system to the [**IWiaTransferCallback::TransferCallback**](-wia-iwiatransfercallback-transfercallback.md) method.<br/> |



 

### New Interfaces in WIA 2.0



| Topic                                                         | Contents                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|---------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IEnumWiaItem2**](-wia-ienumwiaitem2.md)                   | Used by applications to enumerate [**IWiaItem2**](-wia-iwiaitem2.md) objects in the item tree's current folder.<br/>                                                                                                                                                                                                                                                                                                                                                                                   |
| [**IScanProfile**](-wia-iscanprofile.md)                     | The [**IScanProfile**](-wia-iscanprofile.md) interface represents a single scan profile and enables applications to set and get the properties of the profile. <br/>                                                                                                                                                                                                                                                                                                                                   |
| [**IScanProfileMgr**](-wia-iscanprofilemgr.md)               | The [**IScanProfileMgr**](-wia-iscanprofilemgr.md) interface provides methods for creating, opening, deleting, and managing scan profiles. <br/>                                                                                                                                                                                                                                                                                                                                                       |
| [**IScanProfileUI**](-wia-iscanprofileui.md)                 | The [**IScanProfileUI**](-wia-iscanprofileui.md) interface enables applications to display a dialog box so that users can create, modify, and delete scan profiles.<br/>                                                                                                                                                                                                                                                                                                                               |
| [**IWiaAppErrorHandler**](-wia-iwiaapperrorhandler.md)       | The [**IWiaAppErrorHandler**](-wia-iwiaapperrorhandler.md) interface enables applications to display error windows (during data transfers) from which the user can choose whether to continue, cancel, or abort the transfer.<br/>                                                                                                                                                                                                                                                                     |
| [**IWiaDevMgr2**](-wia-iwiadevmgr2.md)                       | The [**IWiaDevMgr2**](-wia-iwiadevmgr2.md) interface is used to create and manage image acquisition devices and to register to receive device events.<br/>                                                                                                                                                                                                                                                                                                                                             |
| [**IWiaErrorHandler**](-wia-iwiaerrorhandler.md)             | The [**IWiaErrorHandler**](-wia-iwiaerrorhandler.md) interface provides methods to handle errors that may occur when an application requests image data, whether for preview or final bits. <br/>                                                                                                                                                                                                                                                                                                      |
| [**IWiaImageFilter**](-wia-iwiaimagefilter.md)               | The [**IWiaImageFilter**](-wia-iwiaimagefilter.md) interface is an extension interface implemented by image processing filter developers and called by WIA 2.0. <br/>                                                                                                                                                                                                                                                                                                                                  |
| [**IWiaItem2**](-wia-iwiaitem2.md)                           | The [**IWiaItem2**](-wia-iwiaitem2.md) interface provides applications with the same functionality as the [**IWiaItem**](/windows/desktop/api/wia_xp/nn-wia_xp-iwiaitem) interface (the ability to query devices to discover their capabilities, to access data transfer interfaces and item properties, and to control the device). It also provides application with the ability to dynamically create and use image processing filters that can come as extensions of the WIA 2.0 device drivers provided in Windows Vista.<br/> |
| [**IWiaPreview**](-wia-iwiapreview.md)                       | The [**IWiaPreview**](-wia-iwiapreview.md) interface caches unfiltered images internally and passes them through image processing filters. <br/>                                                                                                                                                                                                                                                                                                                                                       |
| [**IWiaSegmentationFilter**](-wia-iwiasegmentationfilter.md) | The [**IWiaSegmentationFilter**](-wia-iwiasegmentationfilter.md) interface detects sub-regions of an image stream and makes separate [**IWiaItem2**](-wia-iwiaitem2.md) items for each. <br/>                                                                                                                                                                                                                                                                                                         |
| [**IWiaTransfer**](-wia-iwiatransfer.md)                     | The [**IWiaTransfer**](-wia-iwiatransfer.md) interface provides stream-based transfer of data. <br/>                                                                                                                                                                                                                                                                                                                                                                                                   |
| [**IWiaTransferCallback**](-wia-iwiatransfercallback.md)     | The [**IWiaTransferCallback**](-wia-iwiatransfercallback.md) interface receives callbacks during a data transfer. <br/>                                                                                                                                                                                                                                                                                                                                                                                |
| [**IWiaUIExtension2**](-wia-iwiauiextension2.md)             | The IWiaUIExtension2 interface provides methods that replace the default, system-supplied user interface with a custom user interface, and that provide a custom device icon. Device vendors can implement this interface to provide custom user interfaces for their devices.<br/>                                                                                                                                                                                                                     |



 

### New and Changed Overviews for WIA 2.0



| Topic                                                                          | Contents |
|--------------------------------------------------------------------------------|----------|
| [Constants](-wia-constants.md)                                                |          |
| [Functions](-wia-functions.md)                                                |          |
| [Interfaces](-wia-interfaces.md)                                              |          |
| [Scan Profile Schema](-wia-scan-profile-schema.md)                            |          |
| [Structures](-wia-structures.md)                                              |          |
| [Transferring Image Data in WIA 2.0](-wia-transferring-image-data-in-wia2.md) |          |
| [WIA Device Type Specifiers](-wia-wia-device-type-specifiers.md)              |          |
| [WIA Property Constants](-wia-wia-property-constants.md)                      |          |



 

## Leave feedback

E-mail **sdkfdbk@microsoft.com** to make error reports and feature requests directly to Microsoft.

 

 




