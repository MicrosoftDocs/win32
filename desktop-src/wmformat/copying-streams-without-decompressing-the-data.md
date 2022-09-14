---
title: Copying Streams Without Decompressing the Data
description: Copying Streams Without Decompressing the Data
ms.assetid: c268ce44-a09d-4304-bc39-8b6657da2bdb
keywords:
- Windows Media Format SDK,copying streams
- Advanced Systems Format (ASF),copying streams
- ASF (Advanced Systems Format),copying streams
- streams,copying without decompressing data
ms.topic: article
ms.date: 05/31/2018
---

# Copying Streams Without Decompressing the Data

The simplest and most common way to copy a stream from one file to another is to retrieve the samples in their compressed state and then write them to the new file without decompressing and recompressing them. Samples obtained from a file in their compressed state are called stream samples, because they are unaltered from their representation in the stream. It is recommended that you always use stream samples to copy streams, because decompressing and recompressing digital media data degrades quality. If you must copy a stream from decompressed data, see [Copying Streams Using Decompressed Samples](copying-streams-using-decompressed-samples.md).

It is possible to concatenate two or more streams into a single stream using compressed samples, but only if the bit rates are identical. The process is essentially the same as the steps described below, except that you must read multiple original files to get all of the content you need. However, you can only write compressed samples from multiple files to a single stream if the **WM\_MEDIA\_TYPE** structures (including all the **pbFormat** structure members) of all the compressed streams are identical. To combine data from multiple streams that are not of the same format, you must decompress the content and recompress it into the destination stream. Additionally, when you combine data from two or more streams into a single stream, you must add the buffer window values for all of the streams together to get the buffer window for the new stream. This is because it is impossible to determine how much of the buffer is taken up at the end of one stream and at the beginning of another.

You can retrieve stream samples with the asynchronous reader using [**IWMReaderAdvanced::SetReceiveStreamSamples**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreaderadvanced-setreceivestreamsamples). Stream samples are delivered to [**IWMReaderCallbackAdvanced::OnStreamSample**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreadercallbackadvanced-onstreamsample), not to [**IWMReaderCallback::OnSample**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreadercallback-onsample). If you are reading a file and retrieving some streams compressed and some decompressed, you must implement both callback methods.

The synchronous reader provides more flexibility for retrieving samples. You can switch between compressed and decompressed samples freely during playback using [**IWMSyncReader::SetReadStreamSamples**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmsyncreader-setreadstreamsamples).

To copy an entire stream from one ASF file to a new ASF file, perform the following steps. These steps use the synchronous reader because it is much simpler to use for this kind of operation.

1.  Create a synchronous reader object by calling the [**WMCreateSyncReader**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-wmcreatesyncreader) function.
2.  Open a file in the reader with a call to [**IWMSyncReader::Open**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmsyncreader-open).
3.  Get a pointer to the [**IWMProfile**](iwmprofile.md) interface of the synchronous reader object by calling **IWMSyncReader::QueryInterface**.
4.  Retrieve the properties of the desired stream by calling [**IWMProfile::GetStreamByNumber**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofile-getstreambynumber). This will retrieve a pointer to the [**IWMStreamConfig**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmstreamconfig) interface of the stream configuration object for the stream you want.
5.  Get a copy of the [**WM\_MEDIA\_TYPE**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-wm_media_type) structure for the stream. Make two calls to [**IWMMediaProps::GetMediaType**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmmediaprops-getmediatype): the first to get the size of the structure, the second to get the structure itself.
6.  Create a profile manager object by calling the [**WMCreateProfileManager**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-wmcreateprofilemanager) function.
7.  Call [**IWMProfileManager::CreateEmptyProfile**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofilemanager-createemptyprofile) to create a new profile (or open an existing profile to which you want to add the stream). Call [**IWMProfile::AddStream**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofile-addstream) on the new profile to add the stream from the existing file. When adding the stream, use the **IWMStreamConfig** pointer obtained in step 4.
8.  Create a writer object with a call to the [**WMCreateWriter**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-wmcreatewriter) function. Set the newly created profile as the active profile in the writer by calling [**IWMWriter::SetProfile**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriter-setprofile). Create a file for output by calling [**IWMWriter::SetOutputFilename**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriter-setoutputfilename).
9.  For each input associated with the stream or streams you are copying, call [**IWMWriter::SetInputProps**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriter-setinputprops), passing **NULL** for the [**IWMInputMediaProps**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwminputmediaprops) interface. This informs the writer object that it does not need to validate the data you are passing. You must make this call before calling **BeginWriting** (step 14), otherwise a reading object may not be able to decode the content.
10. Set the synchronous reader to deliver compressed stream samples for the selected stream by calling [**IWMSyncReader::SetReadStreamSamples**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmsyncreader-setreadstreamsamples) with the *fCompressed* parameter set to True.
11. Obtain codec information for every stream being copied and add the codec information to the header before writing. To obtain the codec information, call [**IWMHeaderInfo2::GetCodecInfoCount**](/previous-versions/windows/desktop/api/wmsdkidl/nf-wmsdkidl-iwmheaderinfo2-getcodecinfocount) and [**IWMHeaderInfo2::GetCodecInfo**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmheaderinfo2-getcodecinfo) to enumerate the codecs associated with the file in the reader. Select the codec information that matches the stream configuration. Then set the codec information in the writer by calling [**IWMHeaderInfo3::AddCodecInfo**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmheaderinfo3-addcodecinfo), passing the information obtained from the reader.
12. Obtain a pointer to the [**IWMWriterAdvanced**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmwriteradvanced) interface by calling **IWMWriter::QueryInterface**.
13. Set the writer to writing mode by calling [**IWMWriter::BeginWriting**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriter-beginwriting).
14. Make repeated calls to [**IWMSyncReader::GetNextSample**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmsyncreader-getnextsample), specifying the desired stream number. When samples are received, pass them to the writer with calls to [**IWMWriterAdvanced::WriteStreamSample**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriteradvanced-writestreamsample). For video streams, you should check the flags (if any) set by the writer on each call to **GetNextSample**. If WM\_SF\_CLEANPOINT is set, you must also set it on your call to **WriteStreamSample**.
15. When reading is complete, call [**IWMWriter::EndWriting**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriter-endwriting). The stream should be transferred.

> [!Note]  
> Image streams cannot be copied from one file to another using stream samples. To copy image stream data, retrieve the samples uncompressed and then process them through the writer as you normally would.

 

## Related topics

<dl> <dt>

[**Copying Data from One File to Another**](copying-data-from-one-file-to-another.md)
</dt> <dt>

[**Copying Streams Using Decompressed Samples**](copying-streams-using-decompressed-samples.md)
</dt> </dl>

 

 




