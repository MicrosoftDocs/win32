---
title: Writing Streams with Non-Square Pixels
description: Writing Streams with Non-Square Pixels
ms.assetid: 4af7dedc-e2b8-4dc2-add4-84424e93c297
keywords:
- Windows Media Format SDK,writing video streams
- Windows Media Format SDK,video streams
- Windows Media Format SDK,non-square pixels
- Windows Media Format SDK,pixels (non-square)
- Advanced Systems Format (ASF),writing video streams
- ASF (Advanced Systems Format),writing video streams
- Advanced Systems Format (ASF),video streams
- ASF (Advanced Systems Format),video streams
- Advanced Systems Format (ASF),non-square pixels
- ASF (Advanced Systems Format),non-square pixels
- Advanced Systems Format (ASF),pixels (non-square)
- ASF (Advanced Systems Format),pixels (non-square)
- writing video streams
- video streams,writing
- video streams,non-square pixels
- non-square pixels
- pixels (non-square)
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Writing Streams with Non-Square Pixels

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

There are two ways to create video streams with non-square pixels that will be displayed correctly in Windows Media Player. The first technique involves setting stream-level attributes in the file header. The second technique involves adding a data unit extension to a stream in the profile, and then setting a value for it in every sample that is written.

## To Use Stream-level Header Attributes to Set Pixel Aspect Ratio

1.  Set up the writer object. For more information, see [Writing ASF Files](writing-asf-files.md).
2.  Create or load a profile with one or more video streams. For more information, see [To Use Profiles with the Writer](to-use-profiles-with-the-writer.md).
3.  Call [**IWMWriter::SetProfile**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriter-setprofile). (Always call this method before setting any header attributes.)
4.  Call **QueryInterface** to obtain the [**IWMHeaderInfo3**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmheaderinfo3) interface and call [**AddAttribute**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmheaderinfo3-addattribute) twice to add [**AspectRatioX**](aspectratiox.md) and [**AspectRatioY**](aspectratioy.md) as stream-level attributes of the video stream. These attributes are **DWORD** values.
5.  Write the file.

## To Use Data Unit Extensions to Set Pixel Aspect Ratio

**Before writing:**

1.  Set up the writer object. For more information, see [Writing ASF Files](writing-asf-files.md).
2.  Create or load a profile with one or more video streams. For more information, see [To Use Profiles with the Writer](to-use-profiles-with-the-writer.md).
3.  For each stream (of any media type) in the profile, call [**IWMStreamConfig::SetStreamName**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmstreamconfig-setstreamname) to specify a unique name of your choice. Do not give two streams the same name.
4.  Use [**IWMStreamConfig2::AddDataUnitExtension**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmstreamconfig2-adddataunitextension) on the video stream to add a data unit extension for pixel aspect ratio.
5.  Call [**IWMWriter::SetProfile**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriter-setprofile).
6.  Write the file.

**While writing:**

-   For each sample, call [**INSSBuffer3::SetProperty**](/previous-versions/windows/desktop/api/Wmsbuffer/nf-wmsbuffer-inssbuffer3-setproperty) and specify the WM\_SampleExtensionGUID\_PixelAspectRatio property along with the correct value. Aspect ratio values are written as two concatenated two-digit values. For example, 16:9 is written as 1609 or 0x0649. This is always a 2-byte value.

## Related topics

<dl> <dt>

[**To Read and Write Video Streams with Non-Square Pixels**](to-read-and-write-video-streams-with-non-square-pixels.md)
</dt> </dl>

 

 




