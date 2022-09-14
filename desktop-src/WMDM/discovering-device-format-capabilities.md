---
title: Discovering Device Format Capabilities
description: Discovering Device Format Capabilities
ms.assetid: dd139816-dc8c-4e73-9a21-67287bfe6405
keywords:
- Windows Media Device Manager,device capabilities
- Device Manager,device capabilities
- programming guide,device capabilities
- desktop applications,device capabilities
- creating Windows Media Device Manager applications,device capabilities
- writing files to devices,device capabilities
ms.topic: article
ms.date: 05/31/2018
---

# Discovering Device Format Capabilities

Your application might try to determine a device's playback capabilities before sending a file to it. If a device cannot handle the format of a file you want to send, your application might attempt to transcode the file into a format that the device can use, or notify the user that the device cannot support the requested file.

Note that some devices, such as mass storage class devices, might serve only as removable storage media without playback capabilities. In this case, it would be inappropriate for your application to transcode a file before sending it to the device.

Although the [**IWMDMDevice::GetType**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmdevice-gettype) method enables a device to report its capabilities, some devices return incorrect values for this method. Before copying a file to a device, you might want to ask the user whether playback is intended, and if so, attempt to transcode the file to one of the device's reported formats (or a reasonable format, if the device claims support for any format). Another approach is to assume that any formats specifically listed as supported by the device are intended for playback, and all other files should be transferred unmodified.

After discovering the format of the file to be transferred, and the formats supported by a device, you can decide which is the best target format for transcoding.

In the past, it was common for an application to return zero for a property to indicate support for any values of that property. For example, a value of zero for [**\_WAVEFORMATEX**](-waveformatex.md).nSamplesPerSec would indicate support for any bit rate. Now, the recommended way to indicate support for any value is to specify WMDM\_ENUM\_PROP\_VALID\_VALUES\_ANY in [**WMDM\_PROP\_DESC**](wmdm-prop-desc.md).ValidValuesForm. Some properties, though, can legitimately return zero to indicate specific support. For example, if [**\_BITMAPINFOHEADER**](-bitmapinfoheader.md).biSizeImage is set to zero, this indicates a BI\_RGB bitmap. Exceptions for zero values are noted in the documentation for the relevant structures.

However, it is important to note that devices often do not report their format capabilities properly, or in a standard way. For example, devices often report that they support any format, when in fact they can only handle specific formats, or specific bit rates within a format type. It is up to you to decide whether your application should accept such reports, or whether it should assume some kind of upper limit to a device's playback abilities (for example, 192 kbps).

The recommended method for requesting a device's format support is [**IWMDMDevice3::GetFormatCapability**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmdevice3-getformatcapability). If this method is not supported, your application should fall back on [**IWMDMDevice::GetFormatSupport**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmdevice-getformatsupport). **GetFormatSupport**, unlike **GetFormatSupport2**, does not return video information.

How an application requests a device's format capabilities depends on which interface the application supports. For more details, see the following topics:

-   [Getting Format Capabilities on Devices That Support IWMDMDevice3](getting-format-capabilities-on-devices-that-support-iwmdmdevice3.md)
-   [Getting Format Capabilities on Devices That Support Only IWMDMDevice](getting-format-capabilities-on-devices-that-support-only-iwmdmdevice.md)

## Related topics

<dl> <dt>

[**Writing Files to the Device**](writing-files-to-the-device.md)
</dt> </dl>

 

 




