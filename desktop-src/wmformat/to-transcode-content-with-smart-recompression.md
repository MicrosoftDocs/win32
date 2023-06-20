---
title: To Transcode Content with Smart Recompression
description: To Transcode Content with Smart Recompression
ms.assetid: 02398462-b0a4-4a17-84e3-4c6f9f26639f
keywords:
- Windows Media Format SDK,transcoding content
- Windows Media Format SDK,smart recompression
- Windows Media Format SDK,recompression
- Windows Media Format SDK,Windows Media Audio codecs
- Advanced Systems Format (ASF),transcoding content
- ASF (Advanced Systems Format),transcoding content
- Advanced Systems Format (ASF),smart recompression
- ASF (Advanced Systems Format),smart recompression
- Advanced Systems Format (ASF),recompression
- ASF (Advanced Systems Format),recompression
- Advanced Systems Format (ASF),Windows Media Audio codecs
- ASF (Advanced Systems Format),Windows Media Audio codecs
- transcoding content
- smart recompression
- recompression
- Windows Media Audio codecs,transcoding content
- codecs,Windows Media Audio codecs
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# To Transcode Content with Smart Recompression

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

You can transcode content from one bit rate to another using the Windows Media Format SDK. Normally, this involves simply decoding the content and encoding it again to the desired bit rate. The Windows Media Audio 9 codec supports smart recompression, which enables transcoding that achieves better quality than normal.

For smart recompression, the original audio stream must be encoded with the Windows Media Audio codec. All versions of the codec are supported, but the specialized audio codecs (Windows Media Audio 9 Professional and Windows Media Audio 9 Voice) are not. If the original audio was encoded with the Windows Media Audio 9 Lossless codec, there is no need to use smart recompression, because no information was lost in the original encoding.

To use smart recompression, perform the following steps.

1.  Set up a reader object with the source file for reading. For more information, see [Reading ASF Files](reading-asf-files.md).
2.  Set up a writer object to use for transcoding the file. Set the file name for the new file. Select a profile to use for the new file. Set the selected profile in the writer object. For more information, see [Writing ASF Files](writing-asf-files.md).
3.  Get a pointer to the [**IWMProfile**](iwmprofile.md) interface of the reader object by calling **IWMReader::QueryInterface**.
4.  Retrieve the [**IWMStreamConfig**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmstreamconfig) interface for the audio stream to be transcoded by calling [**IWMProfile::GetStream**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofile-getstream).
5.  Get the [**IWMMediaProps**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmmediaprops) interface for the stream configuration object by calling **IWMStreamConfig::QueryInterface**.
6.  Retrieve the [**WM\_MEDIA\_TYPE**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-wm_media_type) structure for the stream by making two calls to [**IWMMediaProps::GetMediaType**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmmediaprops-getmediatype). Get the size of the structure on the first call, and allocate memory for a buffer to pass on the second call.
7.  Get a pointer to the [**IWMInputMediaProps**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwminputmediaprops) interface for the input in the writer by calling [**IWMWriter::GetInputProps**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriter-getinputprops).
8.  Get the [**IWMPropertyVault**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmpropertyvault) interface for the input media properties object by calling **IWMInputMediaProps::QueryInterface**.
9.  Use the [**IWMPropertyVault::SetProperty**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmpropertyvault-setproperty) method to set the g\_wszOriginalWaveFormat property. Use the **WAVEFORMATEX** structure obtained in step 6 as the value of the property.
10. Include changes made to the input media properties by calling [**IWMWriter::SetInputProps**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriter-setinputprops) and passing it a pointer to the **IWMInputMediaProps** interface.
11. Begin reading samples from the original file and passing them to the writer with calls to [**IWMWriter::WriteSample**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriter-writesample).

## Related topics

<dl> <dt>

[**Advanced Topics**](advanced-topics.md)
</dt> <dt>

[**IWMInputMediaProps Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwminputmediaprops)
</dt> <dt>

[**IWMMediaProps Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmmediaprops)
</dt> <dt>

[**IWMProfile Interface**](iwmprofile.md)
</dt> <dt>

[**IWMPropertyVault Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmpropertyvault)
</dt> <dt>

[**IWMStreamConfig Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmstreamconfig)
</dt> </dl>

 

 




