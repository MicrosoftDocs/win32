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
ms.date: 05/31/2018
---

# Writing Image Streams

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

 

 




