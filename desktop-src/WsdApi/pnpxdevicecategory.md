---
description: Specifies the PnP-X category to which the device belongs. More than one category can be specified.
ms.assetid: 1ca46000-4700-4326-8f49-1b9a22d45bfa
title: PnPXDeviceCategory element
ms.topic: reference
ms.date: 05/31/2018
---

# PnPXDeviceCategory element

Specifies the PnP-X category to which the device belongs. More than one category can be specified.

## Usage

``` syntax
<PnPXDeviceCategory/>
```

## Attributes

There are no attributes.

## Child elements

There are no child elements.

## Parent elements



| Element                                                   | Description                                                                                          |
|-----------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| [**thisModelMetadata**](thismodelmetadata.md)<br/> | Defines the manufacturer and model metadata for the device to be implemented.<br/> <br/> |



## Remarks

Devices can also specify a device subcategory for a more descriptive device category. For example, "Phones.WindowsMobile Cameras.DigitalStillCamera MediaDevices.MusicPlayer" identifies a device that is a Microsoft Windows Mobile  device with a camera and music player. The primary device category for this device would be "Phones".

To specify more than one device category, separate the categories with a space. For example, "Printers Storage" identifies a device with a primary category of "Printers" and a secondary category of "Storage".

If a **PnPXDeviceCategory** element is present, then at least one [**hosted**](hosted.md) element should contain both [**PnPXHardwareId**](pnpxhardwareid.md) and [**PnPXCompatibleId**](pnpxcompatibleid.md) elements. Similarly, if **PnPXHardwareId** and **PnPXCompatibleId** elements are present in a **hosted** element, at least one **PnPXDeviceCategory** element should be present inside the [**thisModelMetadata**](thismodelmetadata.md) element.

## Element information



| Label | Value |
|-------------------------------------|---------------|
| Minimum supported system<br/> | Windows Vista |
| Can be empty                        | Yes           |



 

 




