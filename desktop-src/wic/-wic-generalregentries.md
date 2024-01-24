---
description: General Registry Entries
ms.assetid: 6a140c7f-df8c-4a8e-9e4d-dbb38901e14f
title: General Registry Entries
ms.topic: article
ms.date: 05/31/2018
---

# General Registry Entries


The following registry entries must be made separately for both the decoder and the encoder:

```
HKEY_CLASSES_ROOT
   CLSID
      {Your Encoder/Decoder CLSID}
         Author = Author's Name
         Description = Your Codec Description
         DeviceManufacturer = Manufacturer's Name
         DeviceModels = Device,Device
         FriendlyName = Codec Friendly Name
         Date = mm-dd-yyyy
         Vendor = {GUID_Vendor}
         ContainerFormat = {GUID_ContainerFormat}
         Version = Major.Minor.Build.Number
         SpecVersion = Major.Minor.Build.Number
         MimeTypes = Your Mime Type
         SupportAnimation = 0|1
         SupportChromakey = 0|1
         SupportLossless = 0|1
         SupportMultiframe = 0|1
         Formats
            {Supported PixelFormat GUID 1}
            {Supported PixelFormat GUID ...}
            {Supported PixelFormat GUID N}
         ArbitrationPriority  = 0-10
```

The FriendlyName, VendorGUID, ContainerFormat, MimeTypes, FileExtensions, and Formats entries are required. All of the others are optional.

Note that the DeviceManufacturer and DeviceModels entries are specific to raw codecs and refer to the camera manufacturer and camera models that the codec is applicable to. The spec version is the version of the image format specification with which the codec complies. The Formats entry specifies the pixel formats supported by the codec. A codec may support more than one pixel format. In that case, you would enter multiple keys under HKEY\_CLASSES\_ROOT\\CLSID\\{Encoder/Decoder CLSID}\\Formats.

## ArbitrationPriority

Starting in Windows 8, ArbitrationPriority is a new registry entry. Valid values are 0 through 10. When the ArbitrationPriority key is present, the value of this key will instruct WIC to prioritize the associated codec behind any other codecs with a lower ArbitrationPriority value. This evaluation occurs before the existing WIC codec arbitration occurs, and ensures the associated codec is prioritized below any competing codec, even if it is as or more capable. Any codec that doesn’t have an explicit ArbitrationPriority value defined in the registry will default to Priority 0.

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[CODEC Installation and Registration](-wic-codecinstallandreg.md)
</dt> <dt>

[Encoder-Specific Registry Entries](-wic-encoderregentries.md)
</dt> <dt>

[How to Write a WIC-Enabled CODEC](-wic-howtowriteacodec.md)
</dt> <dt>

[Windows Imaging Component Overview](-wic-about-windows-imaging-codec.md)
</dt> <dt>

[**How the Windows Imaging Component Works: Codec Discovery and Arbitration**](-wic-howwicworks.md)
</dt> </dl>

 

 



