---
description: Codec Availability and Platform Support
ms.assetid: 6b3d09c9-e91f-4c62-92f7-c2643e51987f
title: Codec Availability and Platform Support
ms.topic: article
ms.date: 05/31/2018
---

# Codec Availability and Platform Support

Microsoft recommends that camera vendors include updated RAW Windows Imaging Component (WIC) codecs in the software distribution with new cameras and that the updated codec be installed with the default vendor software installation Windows 7, Windows Vista, and Windows XP. Camera vendors should also provide the latest WIC codec as a download from their support sites.

## Codec Discovery

Microsoft is doing the following to help point users to vendors' Web sites for codec downloads:

-   In Windows Explorer, if a user double-clicks a file that is not recognized (the default case when a RAW file is on the computer, but the codec is not installed yet), a dialog box reports that the file is not recognized and asks whether the user wants to find a program that understands the file. Microsoft maintains an existing redirection service to forward users to vendors' Web sites that can supply the program to understand the file. This facility exists in Windows XP and in Windows Vista.
-   The Windows Photo Gallery, Windows Live Photo Gallery, and the Windows 7 Photo Viewer recognize a set of file extensions as RAW files. If files from that set are found in folders that any of these applications are looking at, and a codec for the file is not already installed, then a dialog box appears, as described in the preceding paragraph.

For more information about codec discovery, see Codec Availability and Platform Support.

## Windows XP Platform Support

Microsoft has released Windows XP SP3 with WIC, and a standalone WIC installer for Windows XP SP2. These use WIC codecs to enable support for thumbnails and previews on those platforms. Therefore, it is important that codec download and installation be supported and tested on the Windows 7, Windows Vista, and Windows XP.

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[Windows Imaging Component Overview](-wic-about-windows-imaging-codec.md)
</dt> <dt>

[WIC Guidelines for Camera RAW Image Formats](-wic-rawguidelines.md)
</dt> <dt>

[How to Write a WIC-Enabled CODEC](-wic-howtowriteacodec.md)
</dt> </dl>

 

 



