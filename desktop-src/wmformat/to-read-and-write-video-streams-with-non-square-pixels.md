---
title: To Read and Write Video Streams with Non-Square Pixels
description: To Read and Write Video Streams with Non-Square Pixels
ms.assetid: fe66d13e-61cf-4bb6-9ca2-aafeabe320ec
keywords:
- Windows Media Format SDK,reading video streams
- Windows Media Format SDK,writing video streams
- Windows Media Format SDK,video streams
- Windows Media Format SDK,non-square pixels
- Windows Media Format SDK,pixels (non-square)
- Advanced Systems Format (ASF),reading video streams
- ASF (Advanced Systems Format),reading video streams
- Advanced Systems Format (ASF),writing video streams
- ASF (Advanced Systems Format),writing video streams
- Advanced Systems Format (ASF),video streams
- ASF (Advanced Systems Format),video streams
- Advanced Systems Format (ASF),non-square pixels
- ASF (Advanced Systems Format),non-square pixels
- Advanced Systems Format (ASF),pixels (non-square)
- ASF (Advanced Systems Format),pixels (non-square)
- reading video streams
- writing video streams
- video streams,reading
- video streams,writing
- video streams,non-square pixels
- non-square pixels
- pixels (non-square)
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# To Read and Write Video Streams with Non-Square Pixels

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Computer monitors have square pixels, but other types of video screens, including NTSC televisions, have rectangular or non-square pixels. Also, some input devices, such as Digital Video (DV) cameras, have charged couple devices with non-square pixels. When you are writing files that are either based on non-square pixel source data or else intended for display on devices with non-square pixels, the pixel aspect ratio information must be included in the ASF file. Reader applications must examine that information and use it to adjust the aspect ratio of the video rectangle as necessary.

## Related topics

<dl> <dt>

[**Advanced Topics**](advanced-topics.md)
</dt> <dt>

[**Reading Streams with Non-Square Pixels**](reading-streams-with-non-square-pixels.md)
</dt> <dt>

[**Writing Streams with Non-Square Pixels**](writing-streams-with-non-square-pixels.md)
</dt> </dl>

 

 




