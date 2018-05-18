---
Description: 'The ASF file sink is an implementation of IMFMediaSink provided by Media Foundation that an application can use to archive ASF media data to a file. For information about ASF Media Sinks'' object model and general usage, see ASF Media Sinks.'
ms.assetid: '21cbde27-a2ca-4298-9197-43bcaf05588d'
title: Adding Stream Information to the ASF File Sink
---

# Adding Stream Information to the ASF File Sink

The ASF file sink is an implementation of [**IMFMediaSink**](imfmediasink.md) provided by Media Foundation that an application can use to archive ASF media data to a file. For information about ASF Media Sinks' object model and general usage, see [ASF Media Sinks](asf-media-sinks.md).

After instantiating the file sink, it must be configured before building the topology. The file sink needs to know about the streams in the output file, the encoding mode information, and the metadata. This topic describes the process of adding stream in the file sink.

-   [Adding Streams in the ASF File Sink](#adding-streams-in-the-asf-file-sink)
-   [Enumerating Stream Sinks](#enumerating-stream-sinks)
-   [Related topics](#related-topics)

## Adding Streams in the ASF File Sink

The file sink must know of the output streams and their properties so that it can generate output samples accordingly and add them to the output ASF file. These settings are written to the final ASF Header Object.

To set stream information, you must have a reference to the file sink's ASF ContentInfo object. For information, see [Creating the ASF File Sink](creating-the-asf-file-sink.md).

The following procedure summarizes the general steps for configuring stream by using the ASF profile object.

**To configure stream information in the ASF file sink**

1.  Create an ASF profile object by calling [**MFCreateASFProfile**](mfcreateasfprofile.md).
2.  For each stream in the output file, create a media type for the target stream to be added in the file sink. The media type must be compatible with the output types supported by the Windows Media encoders.

    For information about adding audio streams to the profile, see Creating Audio Streams for ASF Encoding.

    For information about adding video streams to the profile, see Creating Video Streams for ASF Encoding.

3.  Create streams based on the media types created in step 2 by calling [**IMFASFProfile::CreateStream**](imfasfprofile-createstream.md).
4.  Assign a stream number for the newly created stream by calling [**IMFASFStreamConfig**](imfasfstreamconfig.md) interface pointer received in step 3.
5.  Optionally configure the stream with the following information:
    -   Leaky bucket parameters by setting the attributes: [**MF\_ASFSTREAMCONFIG\_LEAKYBUCKET1**](mf-asfstreamconfig-leakybucket1-attribute.md) or [**MF\_ASFSTREAMCONFIG\_LEAKYBUCKET2**](mf-asfstreamconfig-leakybucket2-attribute.md)
    -   Payload extension, mutual exclusion by calling [**IMFASFStreamConfig**](imfasfstreamconfig.md) methods.
6.  Optionally set data packet size for the profile by setting [**MF\_ASFPROFILE\_MINPACKETSIZE**](mf-asfprofile-minpacketsize-attribute.md) and [**MF\_ASFPROFILE\_MAXPACKETSIZE**](mf-asfprofile-maxpacketsize-attribute.md) attributes. The ASF profile exposes the [**IMFAttributes**](imfattributes.md) interface, which an application can get reference to by calling **IMFASFProfile::QueryInterface**.
7.  Set encoding information for the stream in the file sink. Discussed in [Setting Properties in the File Sink](setting-properties-in-the-file-sink.md).
8.  Add the stream to the profile by calling [**IMFASFProfile::SetStream**](imfasfprofile-setstream.md).
9.  Associate the profile with the ContentInfo object by calling [**IMFASFContentInfo::SetProfile**](imfasfcontentinfo-setprofile.md).

To modify an existing stream, the application can get a reference to the stream's [**IMFASFStreamConfig**](imfasfstreamconfig.md) interface and reconfigure it according to the requirements. To add or remove streams, the application must call [**IMFASFProfile::RemoveStream**](imfasfprofile-removestream.md). To apply these changes, stream modifications or removal, you must set the profile again in the ContentInfo object. This overwrites the existing profile that is already associated with the ContentInfo object.


```C++
//-------------------------------------------------------------------
//  CreateVideoStream
//  Create an video stream and add it to the profile.
//
//  pProfile: A pointer to the ASF profile.
//  wStreamNumber: Stream number to assign for the new stream.
//    pType: A pointer to the source's video media type.
//-------------------------------------------------------------------

HRESULT CreateVideoStream(IMFASFProfile* pProfile, WORD wStreamNumber, IMFMediaType* pType)
{
    if (!pProfile)
    {
        return E_INVALIDARG;
    }
    if (wStreamNumber < 1 || wStreamNumber > 127 )
    {
        return MF_E_INVALIDSTREAMNUMBER;
    }

    HRESULT hr = S_OK;

    
    IMFMediaType* pVideoType = NULL;
    IMFASFStreamConfig* pVideoStream = NULL;

    UINT32 dwBitRate = 0;
        
    //Create a new video type from the source type
    hr = CreateCompressedVideoType(pType, &amp;pVideoType);
    if (FAILED(hr))
    {
        goto done;
    }

    //Create a new stream with the video type
    hr = pProfile->CreateStream(pVideoType, &amp;pVideoStream);
    if (FAILED(hr))
    {
        goto done;
    }
    

    //Set a valid stream number
    hr = pVideoStream->SetStreamNumber(wStreamNumber);
    if (FAILED(hr))
    {
        goto done;
    }

    //Add the stream to the profile
    hr = pProfile->SetStream(pVideoStream);
    if (FAILED(hr))
    {
        goto done;
    }

    wprintf_s(L"Video Stream created. Stream Number: %d .\n", wStreamNumber);

done:

    SafeRelease(&amp;pVideoStream);
    SafeRelease(&amp;pVideoType);

    return hr;
}
```



## Enumerating Stream Sinks

For each stream in the profile that the ContentInfo object is aware of, the ASF file sink creates and adds a stream sink that contains all the properties of the encoded stream. The ASF file sink is designed to contain fixed streams. This means that you cannot add or remove streams by calling [**IMFMediaSink::AddStreamSink**](imfmediasink-addstreamsink.md) or [**IMFMediaSink::RemoveStreamSink**](imfmediasink-removestreamsink.md). These calls on the file sink fail with the MF\_E\_STREAMSINKS\_FIXED error code. Adding or removing streams in the profile does not automatically add or remove the stream sinks in the file sink. You must discard the existing instance of the file and recreate it with new stream information if your streams in the profile have changed.

The following procedure summarizes the general steps for enumerating stream sinks in the ASF file sink.

**To enumerate stream sinks**

1.  Call [**IMFMediaSink::GetStreamSinkCount**](imfmediasink-getstreamsinkcount.md) to get the total number of stream sinks in the ASF file sink.
2.  Loop through the stream sinks ang get a reference to the stream sink's [**GetStreamSinkByIndex**](imfmediasink-getstreamsinkbyindex.md) interface.

    -or-

    Call [**IMFMediaSink::GetStreamSinkById**](imfmediasink-getstreamsinkbyid.md) to get the stream sink by specifying the stream number. Each stream sink is identified with the stream number you set while creating the stream in the profile.

If you are building a partial topology for encoding a media file, you must add the file sink to the topology as an output topology node. You can do so either by specifying each steam sink in the file sink or by setting the file sink activation object and the stream sink identifiers. For more information and code example, see [Creating Output Nodes](creating-output-nodes.md).

## Related topics

<dl> <dt>

[ASF Media Sinks](asf-media-sinks.md)
</dt> <dt>

[ASF Support in Media Foundation](asf-support-in-media-foundation.md)
</dt> </dl>

 

 



