---
title: Sample Extension Types
description: Sample Extension Types
ms.assetid: 8de2e003-cb21-4be9-bcde-7f5909b6260a
keywords:
- Windows Media Format SDK,sample extensions
- Advanced Systems Format (ASF),sample extensions
- ASF (Advanced Systems Format),sample extensions
- Windows Media Format SDK,data unit extensions
- Advanced Systems Format (ASF),data unit extensions
- ASF (Advanced Systems Format),data unit extensions
- Windows Media Format SDK,buffer properties
- Advanced Systems Format (ASF),buffer properties
- ASF (Advanced Systems Format),buffer properties
- sample extensions,types
- data unit extensions,types
- buffer properties
ms.topic: article
ms.date: 05/31/2018
---

# Sample Extension Types

Sample extensions, also called data unit extensions (DUEs) or buffer properties, are items of data that are attached to the media samples in the data section of the ASF file. Several types of sample extensions are defined in the Windows Media Format SDK. You can also create your own extension types.

To use sample extensions, you must identify the extension type in the stream configuration data of the profile. Call the [**IWMStreamConfig2::AddDataUnitExtension**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmstreamconfig2-adddataunitextension) method to configure a stream to accept samples with extended data.

Individual sample extensions must be added to the input samples by calling the [**INSSBuffer3::SetProperty**](/previous-versions/windows/desktop/api/Wmsbuffer/nf-wmsbuffer-inssbuffer3-setproperty) method. When reading samples, you can call the [**INSSBuffer3::GetProperty**](/previous-versions/windows/desktop/api/Wmsbuffer/nf-wmsbuffer-inssbuffer3-getproperty) method to retrieve the extension data. You can also use the methods of the [**INSSBuffer4**](/previous-versions/windows/desktop/api/wmsbuffer/nn-wmsbuffer-inssbuffer4) interface to enumerate the data unit extensions attached to a sample.

The following table lists the predefined data unit extension identifiers, and describes the data that is attached to samples for each.




| Sample extension GUID | Description | 
|-----------------------|-------------|
| WM_SampleExtensionGUID_OutputCleanPoint | The data indicates whether the sample is a <a href="wmformat-glossary.md"><em>cleanpoint</em></a>. A value of zero indicates that the sample is not a cleanpoint. A non-zero value indicates that it is a cleanpoint. This sample data unit extension (DUE) type is used to keep track of cleanpoints when writing precompressed media streams that were encoded with third-party codecs. | 
| WM_SampleExtensionGUID_Timecode | The data is a <a href="/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-wmt_timecode_extension_data"><strong>WMT_TIMECODE_EXTENSION_DATA</strong></a> structure containing SMPTE time code data associated with the sample.The size for this DUE is always WM_SampleExtension_Timecode_Size, which is 14 bytes.<br /> | 
| WM_SampleExtensionGUID_FileName | This type of sample extension is used for file streams. The data in a file stream sample is a piece of a data file. The data in the sample extension specifies the name of the file from which the content in the sample was taken.The file name is a wide-character string containing the file name in name.extension format without any path information.<br /> | 
| WM_SampleExtensionGUID_ContentType | The data identifies the type of content that the sample contains. This type of sample extension is used with interlaced video streams.All interlaced content uses the WM_CT_INTERLACED flag combined by a bitwise <strong>OR</strong> with either WM_CT_BOTTOM_FIELD_FIRST, WM_CT_TOP_FIELD_FIRST, or WM_CT_REPEAT_FIRST_FIELD.<br /> The field order is not used in the encoding process, but is maintained with the compressed samples so that it can be passed to the rendering hardware. Playing interlaced content with the incorrect field order introduces artifacts such as motion jitter in the video.<br /> The size for this DUE is always WM_SampleExtension_ContentType_Size.<br /> | 
| WM_SampleExtensionGUID_PixelAspectRatio | The data indicates the pixel aspect ratio of the content in the sample. This applies only to video.This extension type is used to identify the aspect ratio of non-square pixels. For more information, see <a href="to-read-and-write-video-streams-with-non-square-pixels.md">To Read and Write Video Streams with Non-Square Pixels</a>.<br /> Aspect ratio values are stored as a word whose low byte is the X aspect and whose high byte is the Y aspect. For example, 16:9 is stored as 0x0910.<br /> The size for this DUE is always WM_SampleExtension_PixelAspectRatio_Size, which is 2 bytes.<br /> | 
| WM_SampleExtensionGUID_SampleDuration | The data indicates the duration, in milliseconds, of the sample contained in the buffer object. On playback, if this DUE is set the reader object will use it to overwrite the existing sample duration value.This DUE is set automatically by the SDK run-time components on video streams with bit rates of 100 kbps or greater, where the overhead of the DUE information is not significant. It is not set for streams with bit rates under 100 kbps. Applications should not set this DUE manually because the writer (on high-bit-rate streams) will overwrite the value with its own data.<br /> The size for this DUE is always WM_SampleExtension_SampleDuration_Size, which is 2 bytes.<br /> | 
| WM_SampleExtensionGUID_ChromaLocation | The data indicates the type of chroma subsampling used in the I420 video format.The value of this extension is set to one of the follow values:<br /><ul><li>WM_CL_INTERLACED420</li><li>WM_CL_PROGRESSIVE420</li></ul>This data unit extension is not configured in the profile. It is included in samples output from the decoder.<br /> The size of this DUE is always WM_SampleExtension_ChromaLocation_Size, which is 1 byte.<br /> | 
| WM_SampleExtensionGUID_ColorSpaceInfo | The data provides information about the color space used for the current video frame.The value of this extension is a <a href="/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-wmt_colorspaceinfo_extension_data"><strong>WMT_COLORSPACEINFO_EXTENSION_DATA</strong></a> structure.<br /> This data unit extension is not configured in the profile. It is included in samples output from the decoder.<br /> The size of this DUE is always WM_SampleExtension_ColorSpaceInfo_Size, which is 3 bytes.<br /> | 
| WM_SampleExtensionGUID_UserDataInfo | The data is custom user data.The first four bytes of the data contain the size of the custom data.<br /> The next byte contains the type of user data provided in the sample extension. The following types are supported:<br /><ul><li>0x1F - Sequence level user data</li><li>0x1E - Entry-point level user data</li><li>0x1D - Frame level user data</li><li>0x1C - Field level user data</li><li>0x1B - Slice level user data</li></ul>The sixth and subsequent bytes contain the user data. There are as many bytes of user data as specified by the number in the first four bytes.<br /> This data unit extension is not configured in the profile. It is included in samples that are output from the decoder.<br /> | 
| WM_SampleExtensionGUID_SampleProtectionSalt | The data is encrypted by sample. This sample extension type is used for content that is imported from a non-ASF file format and a rights protection scheme other than Windows Media DRM.When importing protected content, each sample must include a unique salt. Typically, this value is a monotonically increasing counter.<br /> | 




 

## Related topics

<dl> <dt>

[**Programming Reference**](programming-reference.md)
</dt> </dl>

 

 





