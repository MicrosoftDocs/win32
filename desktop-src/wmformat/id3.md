---
title: ID3 Support
description: ID3 is an organization that has defined a set of standards for including metadata in MPEG Layer-3 (MP3) audio files.
ms.assetid: 8c1f1114-48d8-4dce-b7ab-0293265a875c
keywords:
- Windows Media Format SDK,ID3 support
- Advanced Systems Format (ASF),ID3 support
- ASF (Advanced Systems Format),ID3 support
- metadata,ID3
- ID3
ms.topic: article
ms.date: 05/31/2018
---

# ID3 Support

ID3 is an organization that has defined a set of standards for including metadata in MPEG Layer-3 (MP3) audio files. The objects of the Windows Media Format SDK provide support for ID3 compatible attributes. Three distinct ID3 versions are supported: ID3v1.x, ID3v2.2, and ID3v2.3/v2,4. For a list of the attributes that equate to ID3 frames, see [ID3 Tag Support](id3-tag-support.md).

Unless otherwise noted, no validation of ID3 frame data is performed by the objects of this SDK. For example, the metadata attribute [**WM/Lyrics\_Synchronised**](wm-lyrics-synchronised.md) stores the song lyrics with corresponding time stamps. When writing a **WM/Lyrics\_Synchronised** attribute, the objects of this SDK will not check to ensure that the time stamps are in chronological order or perform validation of any kind.

## Related topics

<dl> <dt>

[**Attributes**](attributes.md)
</dt> <dt>

[**Metadata Features**](metadata-features.md)
</dt> <dt>

[**Working with Metadata**](working-with-metadata.md)
</dt> </dl>

 

 




