---
title: Reading Streams with Non-Square Pixels
description: Reading Streams with Non-Square Pixels
ms.assetid: 32114c81-cb78-43de-9ea7-f210056f5aab
keywords:
- Windows Media Format SDK,reading video streams
- Windows Media Format SDK,video streams
- Windows Media Format SDK,non-square pixels
- Windows Media Format SDK,pixels (non-square)
- Advanced Systems Format (ASF),reading video streams
- ASF (Advanced Systems Format),reading video streams
- Advanced Systems Format (ASF),video streams
- ASF (Advanced Systems Format),video streams
- Advanced Systems Format (ASF),non-square pixels
- ASF (Advanced Systems Format),non-square pixels
- Advanced Systems Format (ASF),pixels (non-square)
- ASF (Advanced Systems Format),pixels (non-square)
- reading video streams
- video streams,reading
- video streams,non-square pixels
- non-square pixels
- pixels (non-square)
ms.topic: article
ms.date: 05/31/2018
---

# Reading Streams with Non-Square Pixels

Reader applications that need to correctly handle non-square pixels should examine both the stream-level attributes in the ASF header and the data unit extensions on each sample. There are two cases when the output rectangle must be adjusted to compensate for non-square pixels.

When the source content has been captured from a device such as a DV (digital video) camera with non-square pixels in its CCD, a reader application must adjust its video output rectangle so that the image displays correctly on a computer monitor with square pixels.

When your reader application outputs video that will be played back on an NTSC television, for example through an S-Video out connection on the video card, you must adjust the video rectangle so that the image displays correctly on the television's non-square pixels.

## Related topics

<dl> <dt>

[**To Read and Write Video Streams with Non-Square Pixels**](to-read-and-write-video-streams-with-non-square-pixels.md)
</dt> </dl>

 

 




