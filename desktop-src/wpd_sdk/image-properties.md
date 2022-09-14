---
description: Windows Portable Devices supports the following image properties.
ms.assetid: fb1707a7-16b0-4073-b21d-2ba2f4fd76f7
title: Image Properties (PortableDevice.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Image
api_type: 
- HeaderDef
api_location: 
- PortableDevice.h
---

# Image Properties

Windows Portable Devices supports the following image properties.



| Property                                                                                                                                       | VarType     | Description                                                                                                                                                                                                                                                                                                                                     |
|------------------------------------------------------------------------------------------------------------------------------------------------|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **WPD\_IMAGE\_BITDEPTH**                                                                                                                       | **VT\_UI4** | The bit depth of the image.                                                                                                                                                                                                                                                                                                                     |
| <span id="wpd_image_color_corrected_status"></span><span id="WPD_IMAGE_COLOR_CORRECTED_STATUS"></span>**WPD\_IMAGE\_COLOR\_CORRECTED\_STATUS** | **VT\_UI4** | A [**WPD\_COLOR\_CORRECTED\_STATUS\_VALUES**](wpd-color-corrected-status-values.md) enumeration that specifies whether the file has been color-corrected.This prevents multiple devices from automatically color-correcting the image during post-processing.<br/>                                                                       |
| **WPD\_IMAGE\_CROPPED\_STATUS**                                                                                                                | **VT\_UI4** | A [**WPD\_CROPPED\_STATUS\_VALUES**](wpd-cropped-status-values.md) enumeration that specifies whether the file has been cropped.This prevents multiple devices from automatically cropping the image during post-processing.<br/>                                                                                                        |
| **WPD\_IMAGE\_EXPOSURE\_INDEX**                                                                                                                | **VT\_UI4** | A value that identifies the film speed settings when this image was captured.The settings correspond to the ISO designations of ASA/DIN.<br/> Typically, a device supports discrete enumerated values, but continuous control over a range is possible.<br/> A value of 0xFFFFFFFF corresponds to automatic ISO setting.<br/> |
| **WPD\_IMAGE\_EXPOSURE\_TIME**                                                                                                                 | **VT\_UI4** | Identifies the shutter speed of the device when this image was captured.Units are in seconds scaled by 10000.<br/>                                                                                                                                                                                                                        |
| **WPD\_IMAGE\_FNUMBER**                                                                                                                        | **VT\_UI4** | Identifies the aperture setting of the lens when this image was captured.Units are equal to the f-number scaled by 100.<br/>                                                                                                                                                                                                              |
| **WPD\_IMAGE\_HORIZONTAL\_RESOLUTION**                                                                                                         | **VT\_R8**  | Indicates the horizontal resolution of an image, in dots per inch (DPI) .                                                                                                                                                                                                                                                                       |
| **WPD\_IMAGE\_VERTICAL\_RESOLUTION**                                                                                                           | **VT\_R8**  | Indicates the vertical resolution of an image, in dots per inch (DPI) .                                                                                                                                                                                                                                                                         |



 

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>PortableDevice.h</dt> </dl> |



## See also

<dl> <dt>

[**WPD Properties and Attributes**](properties-and-attributes.md)
</dt> </dl>

 

 




