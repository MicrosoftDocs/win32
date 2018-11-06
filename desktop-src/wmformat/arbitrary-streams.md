---
title: Arbitrary Streams
description: Arbitrary Streams
ms.assetid: 81fd3b07-7cf2-4013-97ed-9718142ca4c3
keywords:
- Windows Media Format SDK,arbitrary streams
- Advanced Systems Format (ASF),arbitrary streams
- ASF (Advanced Systems Format),arbitrary streams
- Windows Media Format SDK,streams
- Advanced Systems Format (ASF),streams
- ASF (Advanced Systems Format),streams
- arbitrary streams
ms.topic: article
ms.date: 05/31/2018
---

# Arbitrary Streams

In addition to audio and video streams and image streams, an ASF file can accommodate streams containing a variety of data. The objects of the Windows Media Format SDK provide support for script streams, file transfer streams, Web streams, and arbitrary data streams. All of these stream types are arbitrary, meaning that no data validation is performed by the reading object. When you include streams of these types in your files, be sure that the reading application performs validation or data checking to ensure that your content has not been corrupted or intentionally mangled by a malicious third party.

Although the objects of this SDK do not verify or validate data in arbitrary streams, several types of arbitrary streams are natively supported. The following table lists the predefined arbitrary stream types. Script streams are also supported, but are discussed separately in the [Script Commands](script-commands.md) section. For more information about creating custom types, see [Custom Arbitrary Data Streams](custom-arbitrary-data-streams.md).



| Arbitrary type                   | Description                                                       |
|----------------------------------|-------------------------------------------------------------------|
| [Text Streams](text-streams.md) | Contain text strings.                                             |
| [File Streams](file-streams.md) | Contain one or more data files.                                   |
| [Web Streams](web-streams.md)   | Contain data files equivalent to the cached version of Web pages. |



 

## Related topics

<dl> <dt>

[**ASF File Features**](asf-file-features.md)
</dt> <dt>

[**Audio and Video Streams**](audio-and-video-streams.md)
</dt> <dt>

[**Configuring Arbitrary Stream Types**](configuring-arbitrary-stream-types.md)
</dt> </dl>

 

 




