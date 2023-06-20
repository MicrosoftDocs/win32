---
title: Configuring Image Streams
description: Configuring Image Streams
ms.assetid: 29325834-8766-47f4-8b33-b5fcbcc494c1
keywords:
- streams,configuring image streams
- codecs,configuring image streams
- image streams,configuring
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Configuring Image Streams

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Image streams contain still images in JPEG format. Even though image streams are like video streams in that they take uncompressed images as inputs, they require a slightly different configuration. To configure an image stream, you must set the values for the members of the video configuration structures as shown in the following table.



| Setting                                                           | Description                                                                                                                                                                      |
|-------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **WM\_MEDIA\_TYPE.majortype**                                     | Set to WMMEDIATYPE\_Image.                                                                                                                                                       |
| **WM\_MEDIA\_TYPE.subtype**                                       | Set to WMMEDIASUBTYPE\_RGB24.                                                                                                                                                    |
| **WM\_MEDIA\_TYPE.bFixedSizeSamples**                             | Set to **FALSE**.                                                                                                                                                                |
| **WM\_MEDIA\_TYPE.bTemporalCompression**                          | Set to **FALSE**.                                                                                                                                                                |
| **WM\_MEDIA\_TYPE.lSampleSize**                                   | Set to 0.                                                                                                                                                                        |
| **WM\_MEDIA\_TYPE.formattype**                                    | Set to WMFORMAT\_VideoInfo.                                                                                                                                                      |
| **WM\_MEDIA\_TYPE.pUnk**                                          | Set to **NULL**.                                                                                                                                                                 |
| **WM\_MEDIA\_TYPE.cbFormat**                                      | Set to `sizeof(WMVIDEOINFOHEADER)`.                                                                                                                                              |
| **WM\_MEDIA\_TYPE.pbFormat**                                      | Set to the address of a properly configured **WMVIDEOINFOHEADER** structure.                                                                                                     |
| **WMVIDEOINFOHEADER.rcSource** and **WMVIDEOINFOHEADER.rcTarget** | Set both rectangles so that the top left corners are coordinates (0, 0) and the bottom right corners are coordinates(x, y) where x is the image width and y is the image height. |
| **WMVIDEOINFOHEADER.dwBitRate**                                   | Set to the bit rate of the stream.                                                                                                                                               |
| **WMVIDEOINFOHEADER.dwErrorRate**                                 | Set to 0.                                                                                                                                                                        |
| **WMVIDEOINFOHEADER.dwBitErrorRate**                              | Set to 0.                                                                                                                                                                        |
| **WMVIDEOINFOHEADER.AvgTimePerFrame**                             | Set to 0.                                                                                                                                                                        |
| **BITMAPINFOHEADER.biWidth**                                      | Set to the width of the image.                                                                                                                                                   |
| **BITMAPINFOHEADER.biHeight**                                     | Set to the height of the image.                                                                                                                                                  |
| **BITMAPINFOHEADER.biPlanes**                                     | Set to 1.                                                                                                                                                                        |
| **BITMAPINFOHEADER.biBitCount**                                   | Set to 24.                                                                                                                                                                       |
| **BITMAPINFOHEADER.biCompression**                                | Set to BI\_RGB.                                                                                                                                                                  |
| **BITMAPINFOHEADER.biSizeImage**                                  | Set to ((x \* y \* c) / 8), where x is the width of the image, y is the height of the image, and c is the color depth of the image (in this case always 24).                     |
| **BITMAPINFOHEADER.biXPelsPerMeter**                              | Set to 0.                                                                                                                                                                        |
| **BITMAPINFOHEADER.biYPelsPerMeter**                              | Set to 0.                                                                                                                                                                        |
| **BITMAPINFOHEADER.biClrUsed**                                    | Set to 0.                                                                                                                                                                        |
| **BITMAPINFOHEADER.biClrImportant**                               | Set to 0.                                                                                                                                                                        |



 

## Related topics

<dl> <dt>

[**Configuration Common to All Streams**](configuration-common-to-all-streams.md)
</dt> <dt>

[**Configuring Streams**](configuring-streams.md)
</dt> <dt>

[**Getting Good Results with the Windows Media Video 9 Screen Codec**](getting-good-results-with-the-windows-media-video-9-screen-codec.md)
</dt> <dt>

[**Image Streams**](image-streams.md)
</dt> </dl>

 

 




