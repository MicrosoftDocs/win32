---
title: Custom Image Support for Devices
description: Custom Image Support for Devices
ms.assetid: 0ccc327c-e953-4348-9802-705331b574ac
keywords:
- Windows Media Player,custom image support for devices
- Windows Media Player,image support for devices
- device custom image support
- custom image support for devices
- image support for devices
ms.topic: article
ms.date: 05/31/2018
---

# Custom Image Support for Devices

> [!Note]  
> This section documents a feature of Windows Media Player 10 that is available when using the Windows XP operating system. It may be unavailable in subsequent versions.

 

Device manufacturers can provide two special image files to customize the way a device is represented in the Windows Media Player 10 user interface. These two files are:

-   DevIcon.fil. A Windows icon format file that represents the device hardware. This image displays in Windows Media Player 10 anywhere an icon is used to represent a device, such as the device list in the **Sync** feature.
-   DevLogo.fil. A PNG format file that represents the corporate logo of the device manufacturer. This image displays in Windows Media Player 10 anywhere corporate branding is used, such as the **Device Setup** dialog box.

## General Guidelines for Images

The following guidelines apply to custom image support in general:

-   This feature is optional. Devices that do not supply images will be represented by default images.
-   This feature is supported for MTP-enabled devices only.
-   To prevent changes to the files, it is recommended that the image files be stored in firmware or a protected storage medium, not with user-created files.
-   The files should not be returned to Windows Media Device Manager clients that enumerate the root storage of the device. Also, deleting, moving, or renaming the files should fail.
-   If the device provides more than one storage medium, the device should return the image files in response to file open requests from any medium. Different device icons may be returned from each storage medium.
-   For Windows Media Device Manager 1.2-enabled clients, these images will take precedence over icon properties supplied by Windows setup mechanisms, such as device node properties.
-   The images must not contain any information that requires localization.
-   For multi-function devices, only the music playback features of Windows XP will use these images.

## Creating the Device Icon Image

The device icon image file, DevIcon.fil, must contain a file in Windows icon format. The MSDN article [Icons in Win32](/previous-versions/ms997538(v=msdn.10)) describes how to create such a file. The MSDN article [Creating Windows XP Icons](/previous-versions/ms997636(v=msdn.10)) provides style guidelines for Windows XP icons. The device icon image file incorporates twelve images in a single file by providing four different sizes with three different color depths each.

Be certain to pay particular attention to the following guidelines:

-   Recommended sizes (in pixels) are 16x16, 32x32, 48x48, and 256x256.
-   Recommended color depths are 24-bit with 8-bit alpha channel, 8-bit with 1-bit transparency, and 4-bit with 1-bit transparency.
-   Use the perspective angle and drop shadow recommendations described in the MSDN articles mentioned previously.

Once you have created the icon file, simply rename it DevIcon.fil.

## Creating the Corporate Logo Image

The corporate logo image file, DevLogo.fil, must contain a file in PNG format. Use the following guidelines when creating the image:

-   The maximum dimensions for the image are 150x32 pixels.
-   The image should support alpha blending to enable a smooth transition between the Windows Media Player 10 user interface and the logo.

Once you have created the corporate logo file, simply rename it DevLogo.fil.

## Related topics

<dl> <dt>

[**Windows Media Player**](windows-media-player.md)
</dt> </dl>

 

 