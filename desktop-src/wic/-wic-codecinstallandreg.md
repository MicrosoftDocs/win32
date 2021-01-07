---
description: When you install a codec, you must register it in the registry. You must also make sure the thumbnail cache gets updated in case any images in your format already exist on the computer.
ms.assetid: 7aec54cb-40ac-495c-99d9-9c397b740b21
title: Codec Installation and Registration
ms.topic: article
ms.date: 05/31/2018
---

# Codec Installation and Registration

When you install a codec, you must register it in the registry. You must also make sure the thumbnail cache gets updated in case any images in your format already exist on the computer.

This topic contains the following sections:

-   [Registering a Codec](#registering-a-codec)
-   [Updating the Thumbnail Cache When Installing Your Codec](#updating-the-thumbnail-cache-when-installing-your-codec)
-   [Making Your WIC-Enabled Codec Available To Users](#making-your-wic-enabled-codec-available-to-users)
-   [Related topics](#related-topics)

## Registering a Codec

When you register a codec, you are actually registering two components: the encoder and the decoder. You also need to make registry entries to register your container format with the metadata handlers for the metadata formats that your image format supports.

The following topics describe the registry entries you need to register your codec:

[General Registry Entries](-wic-generalregentries.md)

[Encoder-Specific Registry Entries](-wic-encoderregentries.md)

[Decoder-Specific Registry Entries](-wic-decoderregentries.md)

[Integration with Windows Photo Gallery and Windows Explorer](-wic-integrationregentries.md)

## Updating the Thumbnail Cache When Installing Your Codec

When a codec is installed, the installer needs to call the following function after writing its registry entries.


```C++
SHChangeNotify(SHCNE_ASSOCCHANGED, SHCNF_IDLIST, NULL, NULL)
```



This call notifies Windows that new file association information is available. If images in your image format already exist on the computer, the thumbnail cache will contain default thumbnails for them because no decoder was available to extract the thumbnails when the images were first acquired. When you notify Windows that a new file association is available, the thumbnail cache discards any empty thumbnails and extracts the actual thumbnails from the files that can now be decoded.

## Making Your WIC-Enabled Codec Available To Users

If you are a camera manufacturer, you can ship your raw codecs in the box with your cameras. You can also post your codecs on the Download page of your Web site. However, if a user acquires an image file in your format from some other source, such as a friend, business associate, or some other Web site, they may not know where to get the codec to decode it with.

Because of this issue, Windows offers an easier way for users of your image format to find your codec and download it onto their computer, starting with Windows Vista. If the Windows Photo Gallery recognizes a file name extension as an image format, and the codec for that format is not installed, a dialog box tells the user that the photo can’t be displayed, and asks whether the user wants to download the software required to display it. When the user accepts, a Microsoft-hosted Web site appears with a link to the codec manufacturer’s download site. (Optionally, you can request that users be taken directly to your download site.)

If you want your image format’s file name extensions to be recognized by the Windows Photo Gallery so that users can be directed to your download site, you must do the following:

1.  Provide a download site for your codec. (You can have a separate page for each codec you provide, or one page that provides downloads for all your codecs.)

    The download site should be localized and easily searchable by camera model.

2.  Provide Microsoft with a list of extensions for your image formats, and the URLs for your download sites.

You must inform Microsoft of the extensions for any new codecs you develop in the future, and of any changes to the URLs of your download sites, so that the new information can be added to the Windows Photo Gallery.

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[Implementing IWICMetadataBlockWriter](-wic-imp-iwicmetadatablockwriter.md)
</dt> <dt>

[Conclusion (How to Write a WIC-Enabled CODEC)](-wic-howtowriteacodec-conclusion.md)
</dt> <dt>

[How to Write a WIC-Enabled CODEC](-wic-howtowriteacodec.md)
</dt> <dt>

[Windows Imaging Component Overview](-wic-about-windows-imaging-codec.md)
</dt> </dl>

 

 



