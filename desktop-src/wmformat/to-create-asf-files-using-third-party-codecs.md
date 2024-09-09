---
title: To Create ASF Files Using Third-Party Codecs
description: To Create ASF Files Using Third-Party Codecs
ms.assetid: 5cd348ca-1f86-429d-92ee-4eab4ced8571
keywords:
- Windows Media Format SDK,creating ASF files
- Windows Media Format SDK,third-party codecs
- Advanced Systems Format (ASF),creating files
- ASF (Advanced Systems Format),creating files
- Advanced Systems Format (ASF),third-party codecs
- ASF (Advanced Systems Format),third-party codecs
- third-party codecs
- codecs,third-party
- codecs,creating ASF files
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# To Create ASF Files Using Third-Party Codecs

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

You can use the Windows Media Format SDK to create ASF files that contain digital media encoded with any codec you choose. When using a codec other than one included with this SDK, you must perform the following steps.

1.  Encode the content with the desired codec.
2.  Find or create a GUID value to identify content encoded with the codec used in step 1.
3.  Create a new profile, or modify an existing profile for use with the encoded content.
    -   Create a stream for the encoded content with the appropriate major type. For more information about major media types, see [Media Types](media-types.md). Use the GUID identified in step 2 as the media subtype.
    -   Set the bit rate and buffer window for the stream to values that will not result in buffer overflow. You should be able to obtain these values from the codec at the time of encoding. The SDK runtime components check the bitrate/buffer window values and drop samples if necessary to make the given data fit in with these values. If you set the values incorrectly, the file will not stream properly, resulting in poor playback.
    -   For video streams, you must set the **biCompression** member of the **BITMAPINFOHEADER** structure contained in the [**WMVIDEOINFOHEADER**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-wmvideoinfoheader) structure to the appropriate FOURCC value for the content. This value must be equal to the first four bytes of the subtype GUID. For example, if **biCompression** is MAKEFOURCC('T','E','S','T')=0x54455354, then the subtype GUID will begin like this: 54455354-XXXX-XXXX-XXXX-XXXXXXXXXXXX.
4.  Create a writer object and load the profile created in the previous step. For more information about writing files, see [Writing ASF Files](writing-asf-files.md).
5.  Loop through the inputs of the file and assign input properties for each as you normally would. For more information about inputs, see [Working with Inputs](working-with-inputs.md). For the stream encoded with a third-party codec, set the [**IWMInputMediaProps**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwminputmediaprops) interface pointer to **NULL** before calling [**IWMWriter::BeginWriting**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriter-beginwriting).
6.  Use the new profile created in the previous step to write the file. Pass the compressed samples using [**IWMWriterAdvanced::WriteStreamSample**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriteradvanced-writestreamsample) instead of [**IWMWriter::WriteSample**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriter-writesample). For video, you must specify which samples are key frames by passing WM\_SF\_CLEANPOINT as the *dwFlags* parameter.

To process and decompress the stream encoded with a third-party codec, you must read compressed stream samples. Your reading application must handle sample decompression for the stream as well.

## Putting MPEG-2 streams into ASF

> [!Note]  
> This topic applies to applications that use the Windows Media Format SDK to put MPEG-2 (or other compression formats that use B frames) into the ASF file container.

 

The writer object requires that all input samples have time stamps, and it assumes that each input sample has a presentation time later than the one that preceded it. While virtually all uncompressed video and even some compressed video streams meet these conditions, MPEG-2 streams do not. In MPEG-2, not all samples are time stamped, and when B frames are present, the sample decoding order is not the same as the rendering order. When the writer object encounters out-of-order samples, it rearranges them into the "correct" order. Therefore, to store MPEG-2 streams natively (not decoded) in an ASF container, you must perform the following steps:

When writing the file:

1.  Add a fixed-size data unit extension (DUE) to each input sample that will hold a structure that contains the actual MPEG time-stamp start-time and stop-time values for the sample. Use -1 for these values if the sample has no time stamp.
2.  Give the writer object "dummy" input time stamps that are always increasing so that it will write the samples to the file in exactly the same order as they are received. The dummy time stamps should correspond approximately to the actual presentation times, as averaged over time. The dummy time stamps will form the seeking timeline, so if they diverge relative to the real time stamps, seek operations on the file will produce unexpected results. However, a limited amount of jitter between the sample times will not seriously affect seek operations.

When reading the file:

-   For each sample read from the file, examine the DUE. If it contains a start time that is greater than or equal to zero, copy that value to the time stamp for the output sample before it is delivered to the decoder. Set all other time stamps on the output samples to **NULL**. In DirectShow, this is done by calling **IMediaSample::SetTime**(**NULL**,**NULL**).

## Related topics

<dl> <dt>

[**Buffering Content**](buffering-content.md)
</dt> <dt>

[**IWMWriter Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmwriter)
</dt> <dt>

[**IWMWriterAdvanced Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmwriteradvanced)
</dt> <dt>

[**To Deliver Compressed Samples with the Asynchronous Reader**](to-deliver-compressed-samples-with-the-asynchronous-reader.md)
</dt> <dt>

[**To Retrieve Stream Samples with the Synchronous Reader**](to-retrieve-stream-samples-with-the-synchronous-reader.md)
</dt> <dt>

[**WMVIDEOINFOHEADER**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-wmvideoinfoheader)
</dt> <dt>

[**Working with Profiles**](working-with-profiles.md)
</dt> <dt>

[**Writing ASF Files**](writing-asf-files.md)
</dt> </dl>

 

 




