---
title: Markers
description: Markers
ms.assetid: ba9bc93e-76a9-4a49-951f-c38dbcceef8c
keywords:
- Windows Media Format SDK,markers
- Advanced Systems Format (ASF),markers
- ASF (Advanced Systems Format),markers
- markers,about
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Markers

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Markers are named places on the timeline of an ASF file. Each marker has a name and a presentation time that you assign. You can specify as many markers as you need for a file.

Markers are useful for breaking up large ASF files in to logical pieces. An application that uses the reader object to play ASF files can provide the user with the option to skip from marker to marker, simplifying navigation of digital media. For example, if you are making an ASF file out of a presentation, you can put markers in the timeline for each major topic that is discussed. On playback, instead of getting one long timeline and having to guess at the location to seek to, a user can simply pick a topic from a list and go right to the pertinent portion of the file.

Markers are manipulated by the metadata editor object. You can add, remove, and view the markers in a file at any time after the file has been written.

## Related topics

<dl> <dt>

[**ASF File Features**](asf-file-features.md)
</dt> <dt>

[**To Seek to Markers**](to-seek-to-markers.md)
</dt> <dt>

[**Using Markers**](using-markers.md)
</dt> </dl>

 

 




