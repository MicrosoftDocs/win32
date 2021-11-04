---
title: Using Device Profiles with WCS
description: Device profiles are a basic tool for color management.
ms.assetid: 9ea420ad-dcf1-4ba9-b739-308be7a56a6c
keywords:
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
- color conversion
- device link profiles
ms.localizationpriority: high


ms.topic: article
ms.date: 05/31/2018
---

# Using Device Profiles with WCS

Device profiles are a basic tool for color management. A [device profile](d.md) is a file that contains information about how to convert colors in the color space and the color [gamut](./g.md) of a specific device into a device-independent color space. The device-independent color space that ICM2 uses is called a Profile Connection Space (PCS). A device profile also contains information about how to convert colors from the PCS into the color space and color gamut of a specific device.

These two sets of conversion information are used for [color conversion](c.md) and color management. For instance, an image may be created in the color space and color gamut of a video display. The information in the device profile files can be used to display a representation of a printed image. Users often want to see on the screen how colors will change when an image is printed. This is called proofing. An image can be proofed by converting the colors from the source color gamut (the screen) into [PCS](p.md) colors, and then converting them from the PCS into the destination color gamut (the printer). The resulting image can be displayed on the screen, allowing the user to see what the final image will look like when it is printed.

Device profiles allow more complex uses as well. For example, they can be used to get an idea of what an image created on a video display would look like when printed on a high resolution laser printer. The example gets more complex if there is only a standard inkjet printer on which to proof it. ICM2 will convert the image from the [gamut](./g.md) of the display, into the gamut of the inkjet printer. From there it is converted into the gamut of the laser printer. The resulting image can be printed on the inkjet printer. Of course the image would be at a higher resolution when printed on the color laser printer. However, the colors of the proofing image printed on the inkjet printer would be a close match to the colors that the laser printer would print.

The conversions from a device profile can be concatenated together into a single file, called a *device link profile*. If a series of conversions is used repeatedly, creating a device link profile for them will shorten conversion time.

Device profiles themselves can be managed. Profile management is the process of associating color profiles with device instances. Any color output device can have a set of one or more color profiles associated with it. Hardware manufacturers and third parties who provide color profiles need to perform profile management.

Profile sets can be shared between devices, or can be dedicated to specific devices. For example, suppose that you have two color printers of the same model. Each printer would require a set of color profiles to be associated with it. The set of color profiles for a printer corresponds to the various configurations possible in that model. Being of the same model, both printers could share one set of profiles. The alternative is to give each printer its own distinct profile set. In the latter case, the color profiles in the set can be calibrated precisely to the printer's individual output, not just the general output characteristics of the model.

There are three different classes of ICC profiles: input profiles, display profiles, and output profiles. Input profiles are usually associated with a device, such as a scanner. Display profiles are typically associated with a computer monitor. Output profiles are commonly associated with printers.

The specification also allows for device profiles, abstract profiles, device link profiles, named color profiles, and color space profiles.

A device profile describes the color space of a particular device.

An abstract profile provides a generic method for users to make subjective color changes to images or graphic objects by transforming the color data within the PCS.

As mentioned previously, a device link profile concatenates a series of profiles into one transformation.

Named color profiles can be thought of as sibling profiles to device profiles. For a given device there would be one or more device profiles to handle process color conversions and one or more named color profiles to handle named colors. There might be multiple named color profiles to account for different consumables or multiple named color vendors.

A color space profile describes a device-independent color space.

The following table summarizes the various types of profiles.



| Profile Type        | Description                                                                                                                   |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Abstract Profile    | A profile that has been adjusted to suit a user's particular preferences.                                                     |
| Color Space Profile | A profile that describes a device-independent color space.                                                                    |
| Device Link Profile | A series of profiles that are concatenated together into a single profile.                                                    |
| Device Profile      | A profile that describes the color space of a particular device.                                                              |
| Display Profile     | A class or category of profiles that includes any type of profile associated with a display.                                  |
| Input Profile       | A class or category of profiles that includes any type of profile associated with an input device such as a scanner.          |
| Named Color Profile | A profile for a color space that consists of named colors.                                                                    |
| Output Profiles     | A class or category of profiles that includes any type of profile associated with a hardcopy output device such as a printer. |



 

Color transforms can be created with one or more profiles. If a transform is created with only one profile, the profile must be a device link profile. A transform may also have two or more profiles in a chain. If it does, it can contain no device link profiles. Abstract profiles can only be in the middle of the chain. The first and last profiles must be device profiles or color space profiles.

 

 