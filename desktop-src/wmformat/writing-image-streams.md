---
title: Writing Image Streams
description: Writing Image Streams
ms.assetid: 3a017bdd-9723-4b7f-b5e1-22838c0ba4ff
keywords:
- Advanced Systems Format (ASF),writing image streams
- ASF (Advanced Systems Format),writing image streams
- Advanced Systems Format (ASF),image streams
- ASF (Advanced Systems Format),image streams
- image streams,writing
- streams,writing image streams
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Writing Image Streams

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The inputs for an image stream must be RGB-formatted bitmap images. The writer coordinates the compression of input image samples using the JPEG format. Before you begin writing a file containing an image stream, you must set an image quality for the input, using the g\_wszJPEGCompressionQuality setting. Use [**IWMWriterAdvanced2::SetInputSetting**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriteradvanced2-setinputsetting) to set the quality to a **DWORD** value ranging from 1 to 100. Low values represent a high compression ratio at the expense of quality, while high values produce high quality images that require more space.

Image streams often require larger buffer windows than ordinary video streams. The exact size required depends on the type of image and the image quality, among other factors. Use trial and error to determine the appropriate size for the images you intend to process.

## Related topics

<dl> <dt>

[**Image Streams**](image-streams.md)
</dt> <dt>

[**To Set Input Settings**](to-set-input-settings.md)
</dt> <dt>

[**Writing ASF Files**](writing-asf-files.md)
</dt> </dl>

 

 




