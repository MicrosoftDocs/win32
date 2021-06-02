---
title: Using The Color Mapping Process with WCS
description: WCS color mapping is based on device profiles.
ms.assetid: df4d390e-0c9e-40dc-864a-2177934895db
keywords:
- Windows Color System (WCS),color mapping
- WCS (Windows Color System),color mapping
- image color management,color mapping
- color management,color mapping
- colors,color mapping
- color mapping
- Windows Color System (WCS),device profiles
- WCS (Windows Color System),device profiles
- image color management,device profiles
- color management,device profiles
- colors,device profiles
- Windows Color System (WCS),profiles
- WCS (Windows Color System),profiles
- image color management,profiles
- color management,profiles
- colors,profiles
- device profiles
ms.localizationpriority: high


ms.topic: article
ms.date: 05/31/2018
---

# Using The Color Mapping Process with WCS

WCS color mapping is based on [device profiles](d.md). These are supplied by vendors of color hardware devices and installed when a device is installed. When color mapping is used by an application program, WCS accesses the device profile of the image to get the information needed to convert the image to the PCS. The conversion is done by the CMM.

A device profile can be embedded into the image itself. So the device profile travels with the image, even across the Internet. A user does not need the source device to get an accurate color mapping. If an image does not have a device profile, the sRGB space is used as a default. For more details, see [Using Color Management on the Internet](using-color-management-on-the-internet.md).

Note that applications which use WCS should never embed the sRGB profile into an image. The sRGB color space provides a standardized color space that is portable across all devices. It is automatically available to users of Windows 98 and later as well as Windows 2000 and later. Therefore, it does not need to travel with the image.

After the image colors are in the [PCS](p.md), WCS accesses the device profile of the destination device. It gets the CMM to convert the image colors from PCS to the gamut of the destination device.

More complex color mapping can also be done with WCS. For example, it can be used to get an idea of what an image created on a video display would look like when printed on a high resolution laser printer. The example gets more complex if there is only a standard inkjet printer on which to preview it. The image can be converted from the gamut of the display, into the gamut of the inkjet printer. From there it can converted into the gamut of the laser printer. The resulting image can be printed on the inkjet printer. Of course the image would be at a higher resolution when printed on the color laser printer. However, the colors of the proofing image printed on the inkjet printer would be a close match to the colors that the laser printer would print.

The way the conversions in the example are accomplished is to convert the image colors from the display's gamut into the PCS. After the image colors are converted into the PCS, the device profile of the inkjet printer would be used to transform them into the gamut of the inkjet printer. Next, the gamut to PCS transform would be used to move the colors back to the PCS. From there, the laser printer's device profile is used to convert the colors from PCS into the gamut of the laser printer.

The ability to easily transform colors from a device gamut to the PCS and back again enables image colors intended for one color output device to be proofed on almost any other.

In the preceding example, the description varies from the actual procedure somewhat for clarity. In reality, all of the transformations mentioned in the preceding paragraph would be concatenated into a single transformation.

 

 




