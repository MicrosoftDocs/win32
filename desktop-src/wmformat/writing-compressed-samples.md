---
title: Writing Compressed Samples
description: Writing Compressed Samples
ms.assetid: f85ca719-1b9d-404f-b2b1-c9e3524e4bc6
keywords:
- Advanced Systems Format (ASF),writing compressed samples
- ASF (Advanced Systems Format),writing compressed samples
- Advanced Systems Format (ASF),passing compressed samples
- ASF (Advanced Systems Format),passing compressed samples
ms.topic: article
ms.date: 05/31/2018
---

# Writing Compressed Samples

For some audio or video streams, you may want to pass samples that are already compressed instead of passing raw data. This feature is used to copy an existing stream or to write samples compressed with a third-party codec. The process of writing a compressed sample is identical to writing an uncompressed sample, except that you use [**IWMWriterAdvanced::WriteStreamSample**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriteradvanced-writestreamsample) instead of [**IWMWriter::WriteSample**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriter-writesample). For more information about writing uncompressed samples, see [To Write Samples](to-write-samples.md).

When you write compressed samples, for CBR profiles, the writer will drop some samples, if necessary, to keep the content within the specified bit rate and buffer window values. For VBR, the writer will not drop samples, but there is no way to be sure that the bit rate and buffer window values will be correct.

If you are copying a stream from one file to another, you should always copy the stream configuration object from the profile of the original file to the profile of the new file. This ensures that you have the correct bit rate and buffer window information. If you copy a compressed stream to a stream that has a lower buffer window set, samples will be dropped during file writing.

## Related topics

<dl> <dt>

[**Writing ASF Files**](writing-asf-files.md)
</dt> </dl>

 

 




