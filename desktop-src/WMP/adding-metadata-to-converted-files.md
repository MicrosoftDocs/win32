---
title: Adding Metadata to Converted Files
description: Adding Metadata to Converted Files
ms.assetid: 97588651-23de-43ab-b884-76d8af95ab93
keywords:
- Windows Media Player,conversion process
- Windows Media Player plug-ins,conversion
- plug-ins,conversion
- conversion plug-ins,adding metadata to converted files
- adding metadata to converted files
- metadata,adding to converted files
ms.topic: article
ms.date: 05/31/2018
---

# Adding Metadata to Converted Files

Converted files must contain certain metadata to ensure a good user experience. At a minimum, converted files must contain the primary attributes listed in the [Windows Media Metadata Usage Guidelines](/previous-versions/ms867702(v=msdn.10)).

For music files, set the value for **WM/MediaClassPrimaryID** to D1607DBC-E323-4BE2-86A1-48A42A28441E.

For voicemail files, set the value for **WM/MediaClassPrimaryID** to 01CD0F29-DA4E-4157-897B-6275D50C4F11, which is the primary class GUID for audio files. Set the value for **WM/MediaClassSecondaryID** to 193c8824-4d52-4178-90bd-305240b04636.

For voice notes, set the value for **WM/MediaClassPrimaryID** to 01CD0F29-DA4E-4157-897B-6275D50C4F11. Set the value for **WM/MediaClassSecondaryID** to 3A172A13-2BD9-4831-835B-114F6A95943F.

Set the value for **WM/ContentDistributor** to the key name for the music service that provided the content.

Set the value for **WM/UniqueFileIdentifier** to the content ID. This will enable you to retrieve specific content items at a future time.

Set a value for **WM/WMShadowFileSourceFileType**.

For protected content, use the Windows Media Format SDK to set the **DRM\_DRMHeader\_ContentID** attribute to the content ID.

For protected content, set a value for **WM/WMShadowFileSourceDRMType**.

## Related topics

<dl> <dt>

[**About Conversion Plug-ins**](about-conversion-plug-ins.md)
</dt> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> </dl>

 

 