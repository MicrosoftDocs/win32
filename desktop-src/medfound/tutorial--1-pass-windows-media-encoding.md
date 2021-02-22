---
description: Encoding refers to the process of converting digital media from one format into another. For example, converting MP3 audio into Windows Media Audio format as defined by the Advanced Systems Format (ASF) specification.
ms.assetid: 4fe202d8-c8f5-4e9a-ad40-1aea8f767362
title: 'Tutorial: 1-Pass Windows Media Encoding'
ms.topic: article
ms.date: 05/31/2018
---

# Tutorial: 1-Pass Windows Media Encoding

Encoding refers to the process of converting digital media from one format into another. For example, converting MP3 audio into Windows Media Audio format as defined by the Advanced Systems Format (ASF) specification.

**Note**  The ASF specification defines a container type for the output file (.wma or .wmv) that can contain media data in any format, compressed or uncompressed. For example, an ASF container such as a .wma file can contain media data in MP3 format. The encoding process converts the actual format of the data contained within the file.

This tutorial demonstrates encoding clear content (non DRM-protected) input source into Windows Media content and writing the data in a new ASF file (.wm\*) by using Pipeline Layer ASF Components. These components will be used to build a partial encoding topology, which will be controlled by an instance of the Media Session.

In this tutorial, you will create a console application that takes the input and output filenames, and the encoding mode as arguments. The input file can be in a compressed or an uncompressed media format. The valid encoding modes are "CBR" (constant bit rate) or "VBR" (variable bit rate). The application creates a media source to represent the source specified by the input filename, and the ASF file sink to archive the encoded contents of source file into an ASF file. To keep the scenario simple to implement, the output file will have only one audio stream and one video stream. The application inserts the Windows Media Audio 9.1 Professional codec for the audio stream format conversion and Windows Media Video 9 codec for the video stream.

For constant bit rate encoding, before the encoding session begins, the encoder must know the target bit rate that it must achieve. In this tutorial, for "CBR" mode, the application uses the bit rate available with the first output media type that is retrieved from the encoder during media type negotiation as the target bit rate. For variable bit rate encoding, this tutorial demonstrates encoding with variable bit rate by setting a quality level. The audio streams are encoded at the quality level of 98 and video streams at the quality level of 95.

The following procedure summarizes the steps for encoding Windows Media content in an ASF container by using a 1-pass encoding mode.

1.  Create a media source for the specified by using the source resolver.
2.  Enumerate the streams in the media source.
3.  Create the ASF media sink and add stream sinks depending on the streams in the media source that need to be encoded.
4.  Configure the media sink with the required encoding properties.
5.  Create the Windows Media encoders for the streams in the output file.
6.  Configure the encoders with the properties that are set on the media sink.
7.  Build a partial encoding topology.
8.  Instantiate the Media Session and set the topology on the Media Session.
9.  Start the encoding session by controlling the Media Session and getting all the relevant events from the Media Session.
10. For VBR encoding, get the encoding property values from the encoder and set them on the media sink.
11. Close and shutdown the encoding session.

This tutorial contains the following sections:

-   [Prerequisites](#prerequisites)
-   [Set up the Project](#set-up-the-project)
-   [Create the Media Source](#create-the-media-source)
-   [Create the ASF File Sink](#create-the-asf-file-sink)
    -   [Create the ASF Profile Object](#create-the-asf-profile-object)
    -   [Create a Compressed Audio Media Type](#create-a-compressed-audio-media-type)
    -   [Create a Compressed Video Media Type](#create-a-compressed-video-media-type)
    -   [Create the ASF ContentInfo Object](#create-the-asf-contentinfo-object)
    -   [Create the ASF File Sink](#create-the-asf-file-sink)
-   [Build the Partial Encoding Topology](#build-the-partial-encoding-topology)
    -   [Create the Source Topology Node for the Media Source](#create-the-source-topology-node-for-the-media-source)
    -   [Instantiate the Required Encoders and Create the Transform Nodes](#instantiate-the-required-encoders-and-create-the-transform-nodes)
    -   [Create the Output Topology Nodes for the File Sink](#create-the-output-topology-nodes-for-the-file-sink)
    -   [Connect the Source, Transform, and Sink Nodes](#connect-the-source-transform-and-sink-nodes)
-   [Handling the Encoding Session](#handling-the-encoding-session)
-   [Update Encoding Properties in the File Sink](#update-encoding-properties-in-the-file-sink)
-   [Implement Main](#implement-main)
-   [Test the Output File](#test-the-output-file)
-   [Common Error Codes and Debugging Tips](#common-error-codes-and-debugging-tips)
-   [Related topics](#related-topics)

## Prerequisites

This tutorial assumes the following:

-   You are familiar with the [ASF File Structure](asf-file-structure.md), the [Pipeline Layer ASF Components](pipeline-layer-asf-components.md) provided by Media Foundation to work with ASF Objects. These components include the following objects:
    -   [Media Sources](media-sources.md)

        **Note**  If you are performing transrating (converting a higher bit-rate file to a lower bit-rate file without changing formats), you will use the [ASF Media Source](asf-media-source.md).

    -   [Windows Media Encoders](windows-media-encoders.md)
    -   [ASF Media Sinks](asf-media-sinks.md)
    -   [ASF ContentInfo Object](asf-contentinfo-object.md)
    -   [ASF Profile](asf-profile.md)

-   You are familiar with Windows Media encoders, and the various encoding types, particularly [Constant Bit Rate Encoding](constant-bit-rate-encoding.md) and [Quality-Based Variable Bit Rate Encoding](quality-based-variable-bit-rate--vbr--encoding.md).
-   You are familiar with encoder MFT operations. Specifically, creating an instance of the encoder and setting input and output types on the encoder.
-   You are familiar with topology objects and how to build an encoding topology. For more information about topologies and topology nodes, see [Creating Topologies](creating-topologies.md).
-   You are familiar with [Media Session](media-session.md)'s event model and the flow control operations. For information, see [Media Session Events](media-session-events.md).

## Set up the Project

1.  Include the following headers in your source file:

    ```C++
    #include <new>
    #include <mfidl.h>            // Media Foundation interfaces
    #include <mfapi.h>            // Media Foundation platform APIs
    #include <mferror.h>        // Media Foundation error codes
    #include <wmcontainer.h>    // ASF-specific components
    #include <wmcodecdsp.h>        // Windows Media DSP interfaces
    #include <Dmo.h>            // DMO objects
    #include <uuids.h>            // Definition for FORMAT_VideoInfo
    #include <propvarutil.h>
    
    ```

    

2.  Link to the following library files:

    ```C++
    // The required link libraries 
    #pragma comment(lib, "mfplat")
    #pragma comment(lib, "mf")
    #pragma comment(lib, "mfuuid")
    #pragma comment(lib, "msdmo")
    #pragma comment(lib, "strmiids")
    #pragma comment(lib, "propsys")
    
    ```

    

3.  Declare the [SafeRelease](saferelease.md) function.

    ```C++
    template <class T> void SafeRelease(T **ppT)
    {
        if (*ppT)
        {
            (*ppT)->Release();
            *ppT = NULL;
        }
    }
    ```

    

4.  Declare the ENCODING\_MODE enumeration to define CBR and VBR encoding types.

    ```C++
    // Encoding mode
    typedef enum ENCODING_MODE {
      NONE  = 0x00000000,
      CBR   = 0x00000001,
      VBR   = 0x00000002,
    } ;
    
    ```

    

5.  Define a constant for buffer window for a video stream.

    ```C++
    // Video buffer window
    const INT32 VIDEO_WINDOW_MSEC = 3000;
    
    ```

    

## Create the Media Source

Create a media source for the input source. Media Foundation provides built-in media sources for various media formats: MP3, MP4/3GP, AVI/WAVE. For information about the formats supported by Media Foundation, see [Supported Media Formats in Media Foundation](supported-media-formats-in-media-foundation.md).

To create the media source, use the [Source Resolver](source-resolver.md). This object analyzes the URL that was specified for the source file and creates the appropriate media source.

Make the following calls:

-   [**MFCreateSourceResolver**](/windows/desktop/api/mfidl/nf-mfidl-mfcreatesourceresolver)
-   [**IMFSourceResolver::CreateObjectFromURL**](/windows/desktop/api/mfidl/nf-mfidl-imfsourceresolver-createobjectfromurl)

    For more information about these calls, see [Using the Source Resolver](using-the-source-resolver.md).

    If your input file is in ASF format and you want to convert it to a different bit-rate file without changing formats, the source solver creates an instance of the [ASF Media Source](asf-media-source.md).

The following code example shows a function CreateMediaSource that creates a media source for the specified file.


```C++
//  Create a media source from a URL.
HRESULT CreateMediaSource(PCWSTR sURL, IMFMediaSource **ppSource)
{
    MF_OBJECT_TYPE ObjectType = MF_OBJECT_INVALID;

    IMFSourceResolver* pSourceResolver = NULL;
    IUnknown* pSource = NULL;

    // Create the source resolver.
    HRESULT hr = MFCreateSourceResolver(&pSourceResolver);
    if (FAILED(hr))
    {
        goto done;
    }

    // Use the source resolver to create the media source.

    // Note: For simplicity this sample uses the synchronous method to create 
    // the media source. However, creating a media source can take a noticeable
    // amount of time, especially for a network source. For a more responsive 
    // UI, use the asynchronous BeginCreateObjectFromURL method.

    hr = pSourceResolver->CreateObjectFromURL(
        sURL,                       // URL of the source.
        MF_RESOLUTION_MEDIASOURCE,  // Create a source object.
        NULL,                       // Optional property store.
        &ObjectType,        // Receives the created object type. 
        &pSource            // Receives a pointer to the media source.
        );
    if (FAILED(hr))
    {
        goto done;
    }

    // Get the IMFMediaSource interface from the media source.
    hr = pSource->QueryInterface(IID_PPV_ARGS(ppSource));

done:
    SafeRelease(&pSourceResolver);
    SafeRelease(&pSource);
    return hr;
}
```



## Create the ASF File Sink

Create an instance of the ASF file sink that will archive encoded media data to an ASF file at the end of the encoding session.

In this tutorial, you will create an activation object for the ASF file sink. The file sink needs the following information in order to create the required stream sinks.

-   The streams to be encoded and written in the final file.
-   The encoding properties that are used to encode the media content, such as, type of encoding, number of encoding passes, and the related properties.
-   The global file properties that indicate to the media sink whether it should adjust the leaky bucket parameters (bit rate and buffer size) automatically.

The stream information is configured in the ASF Profile object and the encoding and global properties are set in a property store managed by the ASF ContentInfo Object.

For an overview of the ASF file sink, see [ASF Media Sinks](asf-media-sinks.md).

### Create the ASF Profile Object

For the ASF file sink to write encoded media data into an ASF file, the sink needs to know the number of streams and the type of streams for which to create stream sinks. In this tutorial you will extract that information from the media source and create corresponding output streams. Restrict your output streams to one audio stream and one video stream. For each selected stream in the source, create a target stream and add it to the profile.

To implement this step, you need the following objects.

-   [ASF Profile](asf-profile.md)
-   Presentation Descriptor for the media source
-   Stream descriptors for the selected streams in the media source.
-   Media Types for the selected streams.

The following steps describe the process of creating the ASF profile and the target streams.

**To create the ASF profile**

1.  Call [**MFCreateASFProfile**](/windows/desktop/api/wmcontainer/nf-wmcontainer-mfcreateasfprofile) to create an empty profile object.
2.  Call [**IMFMediaSource::CreatePresentationDescriptor**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasource-createpresentationdescriptor) to create the presentation descriptor for the media source created in the step described in the "Create the Media Source" section of this tutorial.
3.  Call [**IMFPresentationDescriptor::GetStreamDescriptorCount**](/windows/desktop/api/mfidl/nf-mfidl-imfpresentationdescriptor-getstreamdescriptorcount) to get the number of streams in the media source.
4.  Call [**IMFPresentationDescriptor::GetStreamDescriptorByIndex**](/windows/desktop/api/mfidl/nf-mfidl-imfpresentationdescriptor-getstreamdescriptorbyindex) for each stream in the media source, get the stream's stream descriptor.
5.  Call [**IMFStreamDescriptor::GetMediaTypeHandler**](/windows/desktop/api/mfidl/nf-mfidl-imfstreamdescriptor-getmediatypehandler) followed by [**IMFMediaTypeHandler::GetMediaTypeByIndex**](/windows/desktop/api/mfidl/nf-mfidl-imfmediatypehandler-getmediatypebyindex) and get the first media type for the stream.

    **Note**   To avoid complex calls, assume that only one media type exists per stream and select the first media type of the stream. For complex streams, you need to enumerate each media type from the media type handler and choose the media type that you would like to encode.

6.  Call I[**IMFMediaType::GetMajorType**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediatype-getmajortype) to get the major type of the stream to determine whether the stream is contains audio or video.
7.  Depending on the major type of the stream, create target media types. These media types will hold format information that the encoder will use during the encoding session. The following sections of this tutorial describe the process of creating the target media types.
    -   Create a Compressed Audio Media Type
    -   Create a Compressed Video Media Type
8.  Create a stream based on the target media type, configure the stream according to the application's requirements, and add the stream to the profile. For more information, see [Adding Stream Information to the ASF File Sink](adding-stream-information-to-the-asf-file-sink.md).

    1.  Call [**IMFASFProfile::CreateStream**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfprofile-createstream) and pass the target media type to create the output stream. The method retrieves the IMFASFStreamConfig interface of the stream object.
    2.  Configure the stream.
        -   Call [**IMFASFStreamConfig::SetStreamNumber**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfstreamconfig-setstreamnumber) to assign a number to the stream. This setting is mandatory.
        -   Optionally configure the leaky bucket parameters, payload extension, mutual exclusion on each stream by calling [**IMFASFStreamConfig**](/windows/desktop/api/wmcontainer/nn-wmcontainer-imfasfstreamconfig) methods and relevant stream configuration attributes.
    3.  Add the stream level encoding properties by using the ASF ContentInfo object. For more information about this step, see the "Create the ASF ContentInfo Object" section in this tutorial.
    4.  Call [**IMFASFProfile::SetStream**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfprofile-setstream) to add the stream to the profile.

    The following code example creates an output audio stream.

    ```C++
    //-------------------------------------------------------------------
    //  CreateAudioStream
    //  Create an audio stream and add it to the profile.
    //
    //  pProfile: A pointer to the ASF profile.
    //  wStreamNumber: Stream number to assign for the new stream.
    //-------------------------------------------------------------------

    HRESULT CreateAudioStream(IMFASFProfile* pProfile, WORD wStreamNumber)
    {
        if (!pProfile)
        {
            return E_INVALIDARG;
        }
        if (wStreamNumber < 1 || wStreamNumber > 127 )
        {
            return MF_E_INVALIDSTREAMNUMBER;
        }

        IMFMediaType* pAudioType = NULL;
        IMFASFStreamConfig* pAudioStream = NULL;
        
        //Create an output type from the encoder
        HRESULT hr = GetOutputTypeFromWMAEncoder(&pAudioType);
        if (FAILED(hr))
        {
            goto done;
        }
        
        //Create a new stream with the audio type
        hr = pProfile->CreateStream(pAudioType, &pAudioStream);
        if (FAILED(hr))
        {
            goto done;
        }

        //Set stream number
        hr = pAudioStream->SetStreamNumber(wStreamNumber);
        if (FAILED(hr))
        {
            goto done;
        }
        
        //Add the stream to the profile
        hr = pProfile->SetStream(pAudioStream);
        if (FAILED(hr))
        {
            goto done;
        }

        wprintf_s(L"Audio Stream created. Stream Number: %d.\n", wStreamNumber);

    done:
        SafeRelease(&pAudioStream);
        SafeRelease(&pAudioType);
        return hr;
    }
    ```

    

    The following code example creates an output video stream.

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
        hr = CreateCompressedVideoType(pType, &pVideoType);
        if (FAILED(hr))
        {
            goto done;
        }

        //Create a new stream with the video type
        hr = pProfile->CreateStream(pVideoType, &pVideoStream);
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

        SafeRelease(&pVideoStream);
        SafeRelease(&pVideoType);

        return hr;
    }
    ```

    

The following code example creates output streams depending on the streams in the source.


```C++
    //For each stream in the source, add target stream information in the profile
    for (DWORD iStream = 0; iStream < dwSrcStream; iStream++)
    {
        hr = pPD->GetStreamDescriptorByIndex(
            iStream, &fSelected, &pStreamDesc);
        if (FAILED(hr))
        {
            goto done;
        }

        if (!fSelected)
        {
            continue;
        }

        //Get the media type handler
        hr = pStreamDesc->GetMediaTypeHandler(&pHandler);
        if (FAILED(hr))
        {
            goto done;
        }

        //Get the first media type 
        hr = pHandler->GetMediaTypeByIndex(0, &pMediaType);
        if (FAILED(hr))
        {
            goto done;
        }

        //Get the major type
        hr = pMediaType->GetMajorType(&guidMajor);
        if (FAILED(hr))
        {
            goto done;
        }

        // If this is a video stream, create the target video stream
        if (guidMajor == MFMediaType_Video)
        {
            //The stream level encoding properties will be set in this call
            hr = CreateVideoStream(pProfile, wStreamID, pMediaType);

            if (FAILED(hr))
            {
                goto done;
            }
        }
        
        // If this is an audio stream, create the target audio stream
        if (guidMajor == MFMediaType_Audio)
        {
            //The stream level encoding properties will be set in this call
            hr = CreateAudioStream(pProfile, wStreamID);

            if (FAILED(hr))
            {
                goto done;
            }
        }

        //Get stream's encoding property
        hr = pContentInfo->GetEncodingConfigurationPropertyStore(wStreamID, &pContentInfoProps);
        if (FAILED(hr))
        {
            goto done;
        }

        //Set the stream-level encoding properties
        hr = SetEncodingProperties(guidMajor, pContentInfoProps);       
        if (FAILED(hr))
        {
            goto done;
        }


        SafeRelease(&pMediaType);
        SafeRelease(&pStreamDesc);
        SafeRelease(&pContentInfoProps);
        wStreamID++;
    }
```



### Create a Compressed Audio Media Type

If you want to include an audio stream in the output file, create an audio type by specifying the characteristics of the encoded type by setting the required attributes. To make sure that the audio type is compatible with the Windows Media audio encoder, instantiate the encoder MFT, set the encoding properties, and get a media type by calling [**IMFTransform::GetOutputAvailableType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getoutputavailabletype). Get the required output type by looping through all the available types, getting the attributes of each media type, and selecting the type that is closest to your requirements. In this tutorial, get the first available type from the list of output media types supported by the encoder.

**Note**  For Windows 7, Media Foundation provides a new function, [**MFTranscodeGetAudioOutputAvailableTypes**](/windows/desktop/api/mfidl/nf-mfidl-mftranscodegetaudiooutputavailabletypes) that retrieves a list of the compatible audio types. This function only gets media types for CBR encoding.

A complete audio type must have the following attributes set:

-   [**MF\_MT\_MAJOR\_TYPE**](mf-mt-major-type-attribute.md)
-   [**MF\_MT\_SUBTYPE**](mf-mt-subtype-attribute.md)
-   [**MF\_MT\_AUDIO\_NUM\_CHANNELS**](mf-mt-audio-num-channels-attribute.md)
-   [**MF\_MT\_AUDIO\_SAMPLES\_PER\_SECOND**](mf-mt-audio-samples-per-second-attribute.md)
-   [**MF\_MT\_AUDIO\_BLOCK\_ALIGNMENT**](mf-mt-audio-block-alignment-attribute.md)
-   [**MF\_MT\_AUDIO\_AVG\_BYTES\_PER\_SECOND**](mf-mt-audio-avg-bytes-per-second-attribute.md)
-   [**MF\_MT\_AUDIO\_BITS\_PER\_SAMPLE**](mf-mt-audio-bits-per-sample-attribute.md)

The following code example creates a compressed audio type by getting a compatible type from the Windows Media Audio encoder. The implementation for SetEncodingProperties is shown in the "Create the ASF ContentInfo Object" section of this tutorial.


```C++
//-------------------------------------------------------------------
//  GetOutputTypeFromWMAEncoder
//  Gets a compatible output type from the Windows Media audio encoder.
//
//  ppAudioType: Receives a pointer to the media type.
//-------------------------------------------------------------------

HRESULT GetOutputTypeFromWMAEncoder(IMFMediaType** ppAudioType)
{
    if (!ppAudioType)
    {
        return E_POINTER;
    }

    IMFTransform* pMFT = NULL;
    IMFMediaType* pType = NULL;
    IPropertyStore* pProps = NULL;

    //We need to find a suitable output media type
    //We need to create the encoder to get the available output types
    //and discard the instance.

    CLSID *pMFTCLSIDs = NULL;   // Pointer to an array of CLISDs. 
    UINT32 cCLSID = 0;            // Size of the array.

    MFT_REGISTER_TYPE_INFO tinfo;
    
    tinfo.guidMajorType = MFMediaType_Audio;
    tinfo.guidSubtype = MFAudioFormat_WMAudioV9;

    // Look for an encoder.
    HRESULT hr = MFTEnum(
        MFT_CATEGORY_AUDIO_ENCODER,
        0,                  // Reserved
        NULL,                // Input type to match. None.
        &tinfo,             // WMV encoded type.
        NULL,               // Attributes to match. (None.)
        &pMFTCLSIDs,        // Receives a pointer to an array of CLSIDs.
        &cCLSID             // Receives the size of the array.
        );
    if (FAILED(hr))
    {
        goto done;
    }

    // MFTEnum can return zero matches.
    if (cCLSID == 0)
    {
        hr = MF_E_TOPO_CODEC_NOT_FOUND;
        goto done;
    }
    else
    {
        // Create the MFT decoder
        hr = CoCreateInstance(pMFTCLSIDs[0], NULL,
            CLSCTX_INPROC_SERVER, IID_PPV_ARGS(&pMFT));

        if (FAILED(hr))
        {
            goto done;
        }

    }

    // Get the encoder's property store

    hr = pMFT->QueryInterface(IID_PPV_ARGS(&pProps));
    if (FAILED(hr))
    {
        goto done;
    }
    
    //Set encoding properties
    hr = SetEncodingProperties(MFMediaType_Audio, pProps);
    if (FAILED(hr))
    {
        goto done;
    }

    //Get the first output type
    //You can loop through the available output types to choose 
    //the one that meets your target requirements
    hr = pMFT->GetOutputAvailableType(0, 0, &pType);
    if (FAILED(hr))
    {
        goto done;
    }

    //Return to the caller
    *ppAudioType = pType;
    (*ppAudioType)->AddRef();
    
done:
    SafeRelease(&pProps);
    SafeRelease(&pType);
    SafeRelease(&pMFT);
    CoTaskMemFree(pMFTCLSIDs);
    return hr;
}
```



### Create a Compressed Video Media Type

If you want to include a video stream in the output file, create a complete-encoded video type. The complete media type must include the desired bit rate and codec private data.

There are two ways you can create a complete video media type.

-   Create an empty media type and copy the media type attributes from the source video type and overwrite the [**MF\_MT\_SUBTYPE**](mf-mt-subtype-attribute.md) attribute with the GUID constant MFVideoFormat\_WMV3.

    A complete video type must have the following attributes set:

    -   MF\_MT\_MAJOR\_TYPE
    -   MF\_MT\_SUBTYPE
    -   MF\_MT\_FRAME\_RATE
    -   MF\_MT\_FRAME\_SIZE
    -   MF\_MT\_INTERLACE\_MODE
    -   MF\_MT\_PIXEL\_ASPECT\_RATIO
    -   MF\_MT\_AVG\_BITRATE
    -   MF\_MT\_USER\_DATA

    The following code example creates a compressed video type from the source's video type.

    ```C++
    //-------------------------------------------------------------------
    //  CreateCompressedVideoType
    //  Creates an output type from source's video media type.
    //
    //    pType: A pointer to the source's video media type.
    //  ppVideoType: Receives a pointer to the media type.
    //-------------------------------------------------------------------

    HRESULT CreateCompressedVideoType(
            IMFMediaType* pType, 
            IMFMediaType** ppVideoType)
    {
        if (!pType)
        {
            return E_INVALIDARG;
        }
        if (!ppVideoType)
        {
            return E_POINTER;
        }
        
        HRESULT hr = S_OK;
        MFRatio fps = { 0 };
        MFRatio par = { 0 };
        UINT32 width = 0, height = 0;
        UINT32 interlace = MFVideoInterlace_Unknown;
        UINT32 fSamplesIndependent = 0;
        UINT32 cBitrate = 0;

        IMFMediaType* pMediaType = NULL;

        GUID guidMajor = GUID_NULL;

        hr = pType->GetMajorType(&guidMajor);
        if (FAILED(hr))
        {
            goto done;
        }

        if (guidMajor != MFMediaType_Video )
        {
            hr = MF_E_INVALID_FORMAT;
            goto done;
        }

        hr = MFCreateMediaType(&pMediaType);
        if (FAILED(hr))
        {
            goto done;
        }

        hr = pType->CopyAllItems(pMediaType);
        if (FAILED(hr))
        {
            goto done;
        }

        //Fill the missing attributes
        //1. Frame rate
        hr = MFGetAttributeRatio(pMediaType, MF_MT_FRAME_RATE, (UINT32*)&fps.Numerator, (UINT32*)&fps.Denominator);
        if (hr == MF_E_ATTRIBUTENOTFOUND)
        {
            fps.Numerator = 30000;
            fps.Denominator = 1001;

            hr = MFSetAttributeRatio(pMediaType, MF_MT_FRAME_RATE, fps.Numerator, fps.Denominator);
            if (FAILED(hr))
            {
                goto done;
            }
        }

        ////2. Frame size
        hr = MFGetAttributeSize(pMediaType, MF_MT_FRAME_SIZE, &width, &height);
        if (hr == MF_E_ATTRIBUTENOTFOUND)
        {
            width = 1280;
            height = 720;
                
            hr = MFSetAttributeSize(pMediaType, MF_MT_FRAME_SIZE, width, height);
            if (FAILED(hr))
            {
                goto done;
            }
        }

        ////3. Interlace mode
        
        if (FAILED(pMediaType->GetUINT32(MF_MT_INTERLACE_MODE, &interlace)))
        {
            hr = pMediaType->SetUINT32(MF_MT_INTERLACE_MODE, MFVideoInterlace_Progressive);
            if (FAILED(hr))
            {
                goto done;
            }

        }

        ////4. Pixel aspect Ratio
        hr = MFGetAttributeRatio(pMediaType, MF_MT_PIXEL_ASPECT_RATIO, (UINT32*)&par.Numerator, (UINT32*)&par.Denominator);
        if (hr == MF_E_ATTRIBUTENOTFOUND)
        {
            par.Numerator = par.Denominator = 1;
            hr = MFSetAttributeRatio(pMediaType, MF_MT_PIXEL_ASPECT_RATIO, (UINT32)par.Numerator, (UINT32)par.Denominator);
            if (FAILED(hr))
            {
                goto done;
            }

        }

        //6. bit rate
        if (FAILED(pMediaType->GetUINT32(MF_MT_AVG_BITRATE, &cBitrate)))
        {
            hr = pMediaType->SetUINT32(MF_MT_AVG_BITRATE, 1000000);
            if (FAILED(hr))
            {
                goto done;
            }

        }

        hr = pMediaType->SetGUID(MF_MT_SUBTYPE, MFVideoFormat_WMV3);
        if (FAILED(hr))
        {
            goto done;
        }

        // Return the pointer to the caller.
        *ppVideoType = pMediaType;
        (*ppVideoType)->AddRef();


    done:
        SafeRelease(&pMediaType);
        return hr;
    }
    
    ```

    

-   Get a compatible media type from the Windows Media video encoder by setting the encoding properties and then calling [**IMFTransform::GetOutputAvailableType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getoutputavailabletype). This method returns the partial type. Make sure you convert the partial type to a complete type by adding the following information:

    -   Set the video bit rate in the [**MF\_MT\_AVG\_BITRATE**](mf-mt-avg-bitrate-attribute.md) attribute.
    -   Add codec private data by setting the [**MF\_MT\_USER\_DATA**](mf-mt-user-data-attribute.md) attribute. For detailed instructions, see "Private Codec Data" in [Configuring a WMV Encoder](configuring-a-wmv-encoder.md).

    Because [**IWMCodecPrivateData::GetPrivateData**](../wmformat/iwmcodecprivatedata-getprivatedata.md) checks the bit rate before returning the codec private data, make sure that you set the bit rate before getting the codec private data.

    The following code example creates a compressed video type by getting a compatible type from the Windows Media Video encoder. It also creates an uncompressed video type and sets it as the encoder's input. This is implemented in the helper function CreateUncompressedVideoType. GetOutputTypeFromWMVEncoder converts the returned partial type into a complete type by adding codec private data. The implementation for SetEncodingProperties is shown in the "Create the ASF ContentInfo Object" section of this tutorial.

    ```C++
    //-------------------------------------------------------------------
    //  GetOutputTypeFromWMVEncoder
    //  Gets a compatible output type from the Windows Media video encoder.
    //
    //  pType: A pointer to the source video stream's media type.
    //  ppVideoType: Receives a pointer to the media type.
    //-------------------------------------------------------------------

    HRESULT GetOutputTypeFromWMVEncoder(IMFMediaType* pType, IMFMediaType** ppVideoType)
    {
        if (!ppVideoType)
        {
            return E_POINTER;
        }

        IMFTransform* pMFT = NULL;
        IPropertyStore* pProps = NULL;
        IMFMediaType* pInputType = NULL;
        IMFMediaType* pOutputType = NULL;
        
        UINT32 cBitrate = 0;

        //We need to find a suitable output media type
        //We need to create the encoder to get the available output types
        //and discard the instance.

        CLSID *pMFTCLSIDs = NULL;   // Pointer to an array of CLISDs. 
        UINT32 cCLSID = 0;          // Size of the array.

        MFT_REGISTER_TYPE_INFO tinfo;
        
        tinfo.guidMajorType = MFMediaType_Video;
        tinfo.guidSubtype = MFVideoFormat_WMV3;

        // Look for an encoder.
        HRESULT hr = MFTEnum(
            MFT_CATEGORY_VIDEO_ENCODER,
            0,                  // Reserved
            NULL,               // Input type to match. None.
            &tinfo,             // WMV encoded type.
            NULL,               // Attributes to match. (None.)
            &pMFTCLSIDs,        // Receives a pointer to an array of CLSIDs.
            &cCLSID             // Receives the size of the array.
            );
        if (FAILED(hr))
        {
            goto done;
        }

        // MFTEnum can return zero matches.
        if (cCLSID == 0)
        {
            hr = MF_E_TOPO_CODEC_NOT_FOUND;
            goto done;
        }
        else
        {
            //Create the MFT decoder
            hr = CoCreateInstance(pMFTCLSIDs[0], NULL,
                CLSCTX_INPROC_SERVER, IID_PPV_ARGS(&pMFT));
            if (FAILED(hr))
            {
                goto done;
            }

        }
        
        //Get the video encoder property store
        hr = pMFT->QueryInterface(IID_PPV_ARGS(&pProps));
        if (FAILED(hr))
        {
            goto done;
        }

        //Set encoding properties
        hr = SetEncodingProperties(MFMediaType_Video, pProps);
        if (FAILED(hr))
        {
            goto done;
        }

        hr = CreateUncompressedVideoType(pType, &pInputType);
        if (FAILED(hr))
        {
            goto done;
        }

        hr = pMFT->SetInputType(0, pInputType, 0);

        //Get the first output type
        //You can loop through the available output types to choose 
        //the one that meets your target requirements
        hr =  pMFT->GetOutputAvailableType(0, 0, &pOutputType);
        if (FAILED(hr))
        {
            goto done;
        }
        
        hr = pType->GetUINT32(MF_MT_AVG_BITRATE, &cBitrate);
        if (FAILED(hr))
        {
            goto done;
        }

        //Now set the bit rate
        hr = pOutputType->SetUINT32(MF_MT_AVG_BITRATE, cBitrate);
        if (FAILED(hr))
        {
            goto done;
        }

        hr = AddPrivateData(pMFT, pOutputType);
        if (FAILED(hr))
        {
            goto done;
        }

        //Return to the caller
        *ppVideoType = pOutputType;
        (*ppVideoType)->AddRef();
        
    done:
        SafeRelease(&pProps);
        SafeRelease(&pOutputType);
        SafeRelease(&pInputType);
        SafeRelease(&pMFT);
        CoTaskMemFree(pMFTCLSIDs);
        return hr;
    }
    ```

    

    The following code example creates an uncompressed video type.

    ```C++
    //-------------------------------------------------------------------
    //  CreateUncompressedVideoType
    //  Creates an uncompressed video type.
    //
    //    pType: A pointer to the source's video media type.
    //  ppVideoType: Receives a pointer to the media type.
    //-------------------------------------------------------------------

    HRESULT CreateUncompressedVideoType(IMFMediaType* pType, IMFMediaType** ppMediaType)
    {
        if (!pType)
        {
            return E_INVALIDARG;
        }
        if (!ppMediaType)
        {
            return E_POINTER;
        }
        
        MFRatio fps = { 0 };
        MFRatio par = { 0 };
        UINT32 width = 0, height = 0;
        UINT32 interlace = MFVideoInterlace_Unknown;
        UINT32 cBitrate = 0;

        IMFMediaType* pMediaType = NULL;

        GUID guidMajor = GUID_NULL;

        HRESULT hr = pType->GetMajorType(&guidMajor);
        if (FAILED(hr))
        {
            goto done;
        }

        if (guidMajor != MFMediaType_Video )
        {
            hr = MF_E_INVALID_FORMAT;
            goto done;
        }

        hr = MFGetAttributeRatio(pType, MF_MT_FRAME_RATE, (UINT32*)&fps.Numerator, (UINT32*)&fps.Denominator);
        if (hr == MF_E_ATTRIBUTENOTFOUND)
        {
            fps.Numerator = 30000;
            fps.Denominator = 1001;

        }
        hr = MFGetAttributeSize(pType, MF_MT_FRAME_SIZE, &width, &height);
        if (hr == MF_E_ATTRIBUTENOTFOUND)
        {
            width = 1280;
            height = 720;

        }

        interlace = MFGetAttributeUINT32(pType, MF_MT_INTERLACE_MODE, MFVideoInterlace_Progressive);

        hr = MFGetAttributeRatio(pType, MF_MT_PIXEL_ASPECT_RATIO, (UINT32*)&par.Numerator, (UINT32*)&par.Denominator);
        if (FAILED(hr))
        {
            par.Numerator = par.Denominator = 1;
        }

        cBitrate = MFGetAttributeUINT32(pType, MF_MT_AVG_BITRATE, 1000000);

        hr = MFCreateMediaType(&pMediaType);
        if (FAILED(hr))
        {
            goto done;
        }
        hr = pMediaType->SetGUID(MF_MT_MAJOR_TYPE, guidMajor);
        if (FAILED(hr))
        {
            goto done;
        }
        hr = pMediaType->SetGUID(MF_MT_SUBTYPE, MFVideoFormat_RGB32);
        if (FAILED(hr))
        {
            goto done;
        }
        hr = MFSetAttributeRatio(pMediaType, MF_MT_FRAME_RATE, fps.Numerator, fps.Denominator);
        if (FAILED(hr))
        {
            goto done;
        }
        hr = MFSetAttributeSize(pMediaType, MF_MT_FRAME_SIZE, width, height);
        if (FAILED(hr))
        {
            goto done;
        }
        hr = pMediaType->SetUINT32(MF_MT_INTERLACE_MODE, 2);
        if (FAILED(hr))
        {
            goto done;
        }

        hr = pMediaType->SetUINT32(MF_MT_ALL_SAMPLES_INDEPENDENT, TRUE);
        if (FAILED(hr))
        {
            goto done;
        }

        hr = pMediaType->SetUINT32(MF_MT_AVG_BITRATE, cBitrate);
        if (FAILED(hr))
        {
            goto done;
        }

        // Return the pointer to the caller.
        *ppMediaType = pMediaType;
        (*ppMediaType)->AddRef();


    done:
        SafeRelease(&pMediaType);
        return hr;
    }
    ```

    

    The following code example adds codec private data to the specified video media type.

    ```C++
    //
    // AddPrivateData
    // Appends the private codec data to a media type.
    //
    // pMFT: The video encoder
    // pTypeOut: A video type from the encoder's type list.
    //
    // The function modifies pTypeOut by adding the codec data.
    //

    HRESULT AddPrivateData(IMFTransform *pMFT, IMFMediaType *pTypeOut)
    {
        HRESULT hr = S_OK;
        ULONG cbData = 0;
        BYTE *pData = NULL;

        IWMCodecPrivateData *pPrivData = NULL;

        DMO_MEDIA_TYPE mtOut = { 0 };

        // Convert the type to a DMO type.
        hr = MFInitAMMediaTypeFromMFMediaType(
            pTypeOut, 
            FORMAT_VideoInfo, 
            (AM_MEDIA_TYPE*)&mtOut
            );
        
        if (SUCCEEDED(hr))
        {
            hr = pMFT->QueryInterface(IID_PPV_ARGS(&pPrivData));
        }

        if (SUCCEEDED(hr))
        {
            hr = pPrivData->SetPartialOutputType(&mtOut);
        }

        //
        // Get the private codec data
        //

        // First get the buffer size.
        if (SUCCEEDED(hr))
        {
            hr = pPrivData->GetPrivateData(NULL, &cbData);
        }

        if (SUCCEEDED(hr))
        {
            pData = new BYTE[cbData];

            if (pData == NULL)
            {
                hr = E_OUTOFMEMORY;
            }
        }

        // Now get the data.
        if (SUCCEEDED(hr))
        {
            hr = pPrivData->GetPrivateData(pData, &cbData);
        }

        // Add the data to the media type.
        if (SUCCEEDED(hr))
        {
            hr = pTypeOut->SetBlob(MF_MT_USER_DATA, pData, cbData);
        }

        delete [] pData;
        MoFreeMediaType(&mtOut);
        SafeRelease(&pPrivData);
        return hr;
    }
    ```

    

### Create the ASF ContentInfo Object

The ASF ContentInfo object is a WMContainer level component that is primarily designed to store ASF Header Object information. The ASF file sink, implements the ContentInfo object in order to store information (in a property store) that will be used to write the ASF Header Object of the encoded file. To do so, you must create and configure the following set of information on the ContentInfo object before starting the encoding session.

1.  Call [**MFCreateASFContentInfo**](/windows/desktop/api/wmcontainer/nf-wmcontainer-mfcreateasfcontentinfo) to create an empty ContentInfo object.

    The following code example creates an empty ContentInfo object.

    ```C++
        // Create an empty ContentInfo object
        hr = MFCreateASFContentInfo(&pContentInfo);
        if (FAILED(hr))
        {
            goto done;
        }
    
    ```

    

2.  Call [**IMFASFContentInfo::GetEncodingConfigurationPropertyStore**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfcontentinfo-getencodingconfigurationpropertystore) to get the file sink's stream-level property store. In this call, you need to pass the stream number that you assigned for the stream while creating the ASF profile.
3.  Set the stream-level [Encoding Properties](configuring-the-encoder.md) in the file sink's stream property store. For more information, see "Stream Encoding Properties" in [Setting Properties in the File Sink](setting-properties-in-the-file-sink.md).

    The following code example sets the stream level properties in the file sink's property store.

    ```C++
            //Get stream's encoding property
            hr = pContentInfo->GetEncodingConfigurationPropertyStore(wStreamID, &pContentInfoProps);
            if (FAILED(hr))
            {
                goto done;
            }

            //Set the stream-level encoding properties
            hr = SetEncodingProperties(guidMajor, pContentInfoProps);       
            if (FAILED(hr))
            {
                goto done;
            }

    
    ```

    

    The following code example shows the implementation for SetEncodingProperties. This function sets stream level encoding properties for CBR and VBR.

    ```C++
    //-------------------------------------------------------------------
    //  SetEncodingProperties
    //  Create a media source from a URL.
    //
    //  guidMT:  Major type of the stream, audio or video
    //  pProps:  A pointer to the property store in which 
    //           to set the required encoding properties.
    //-------------------------------------------------------------------

    HRESULT SetEncodingProperties (const GUID guidMT, IPropertyStore* pProps)
    {
        if (!pProps)
        {
            return E_INVALIDARG;
        }

        if (EncodingMode == NONE)
        {
            return MF_E_NOT_INITIALIZED;
        }
       
        HRESULT hr = S_OK;

        PROPVARIANT var;

        switch (EncodingMode)
        {
            case CBR:
                // Set VBR to false.
                hr = InitPropVariantFromBoolean(FALSE, &var);
                if (FAILED(hr))
                {
                    goto done;
                }

                hr = pProps->SetValue(MFPKEY_VBRENABLED, var);
                if (FAILED(hr))
                {
                    goto done;
                }

                // Set the video buffer window.
                if (guidMT == MFMediaType_Video)
                {
                    hr = InitPropVariantFromInt32(VIDEO_WINDOW_MSEC, &var);
                    if (FAILED(hr))
                    {
                        goto done;
                    }

                    hr = pProps->SetValue(MFPKEY_VIDEOWINDOW, var);    
                    if (FAILED(hr))
                    {
                        goto done;
                    }
                }
                break;

            case VBR:
                //Set VBR to true.
                hr = InitPropVariantFromBoolean(TRUE, &var);
                if (FAILED(hr))
                {
                    goto done;
                }

                hr = pProps->SetValue(MFPKEY_VBRENABLED, var);
                if (FAILED(hr))
                {
                    goto done;
                }

                // Number of encoding passes is 1.

                hr = InitPropVariantFromInt32(1, &var);
                if (FAILED(hr))
                {
                    goto done;
                }

                hr = pProps->SetValue(MFPKEY_PASSESUSED, var);
                if (FAILED(hr))
                {
                    goto done;
                }

                // Set the quality level.

                if (guidMT == MFMediaType_Audio)
                {
                    hr = InitPropVariantFromUInt32(98, &var);
                    if (FAILED(hr))
                    {
                        goto done;
                    }

                    hr = pProps->SetValue(MFPKEY_DESIRED_VBRQUALITY, var);    
                    if (FAILED(hr))
                    {
                        goto done;
                    }
                }
                else if (guidMT == MFMediaType_Video)
                {
                    hr = InitPropVariantFromUInt32(95, &var);
                    if (FAILED(hr))
                    {
                        goto done;
                    }

                    hr = pProps->SetValue(MFPKEY_VBRQUALITY, var);    
                    if (FAILED(hr))
                    {
                        goto done;
                    }
                }
                break;

            default:
                hr = E_UNEXPECTED;
                break;
        }    

    done:
        PropVariantClear(&var);
        return hr;
    }
    ```

    

4.  Call [**IMFASFContentInfo::GetEncodingConfigurationPropertyStore**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfcontentinfo-getencodingconfigurationpropertystore) to get the file sink's global property store. In this call, you need to pass 0 in the first parameter. For more information, see "Global File Sink Properties" in [Setting Properties in the File Sink](setting-properties-in-the-file-sink.md).
5.  Set the [**MFPKEY\_ASFMEDIASINK\_AUTOADJUST\_BITRATE**](mfpkey-asfmediasink-autoadjust-bitrate-property.md) to VARIANT\_TRUE to ensure the leaky bucket values in the ASF multiplexer are adjusted properly. For information about this property, see "Multiplexer Initialization and Leaky Bucket Settings" in [Creating the Multiplexer Object](creating-the-multiplexer-object.md).

    The following code example sets the stream level properties in the file sink's property store.

    ```C++
        //Now we need to set global properties that will be set on the media sink
        hr = pContentInfo->GetEncodingConfigurationPropertyStore(0, &pContentInfoProps);
        if (FAILED(hr))
        {
            goto done;
        }

        //Auto adjust Bitrate
        var.vt = VT_BOOL;
        var.boolVal = VARIANT_TRUE;

        hr = pContentInfoProps->SetValue(MFPKEY_ASFMEDIASINK_AUTOADJUST_BITRATE, var);
        
        //Initialize with the profile
        hr = pContentInfo->SetProfile(pProfile);
        if (FAILED(hr))
        {
            goto done;
        }
    ```

    

    > [!Note]  
    > There are other properties that you can set at the global level for the file sink. For more information, see "Configuring the ContentInfo Object with Encoder Settings" in [Setting Properties in the ContentInfo Object](setting-properties-in-the-contentinfo-object.md).

     

You will use the configured ASF ContentInfo to create an activation object for the ASF file sink (described in the next section).

If you are creating an out-of-process file sink ([**MFCreateASFMediaSinkActivate**](/windows/desktop/api/wmcontainer/nf-wmcontainer-mfcreateasfmediasinkactivate)), that is by using an activation object, you can use the configured ContentInfo object to instantiate the ASF media sink (described in the next section). If you are creating an in-process file sink ([**MFCreateASFMediaSink**](/windows/desktop/api/wmcontainer/nf-wmcontainer-mfcreateasfmediasink)), instead of creating the empty ContentInfo object as described in step 1, get a reference to the [**IMFASFContentInfo**](/windows/desktop/api/wmcontainer/nn-wmcontainer-imfasfcontentinfo) interface by calling **IMFMediaSink::QueryInterface** on the file sink. You must then configure the ContentInfo object as described in this section.

### Create the ASF File Sink

In this step of the tutorial, you will use the configured ASF ContentInfo, which you created in the previous step, to create an activation object for the ASF file sink by calling the [**MFCreateASFMediaSinkActivate**](/windows/desktop/api/wmcontainer/nf-wmcontainer-mfcreateasfmediasinkactivate) function. For more information, see [Creating the ASF File Sink](creating-the-asf-file-sink.md).

The following code example creates the activation object for the file sink.


```C++
    //Create the activation object for the  file sink
    hr = MFCreateASFMediaSinkActivate(sURL, pContentInfo, &pActivate);
    if (FAILED(hr))
    {
        goto done;
    }

```



## Build the Partial Encoding Topology

Next, you will build a partial encoding topology by creating topology nodes for the media source, the required Windows Media encoders, and the ASF file sink. After adding the topology nodes, you will connect the source, transform, and the sink nodes. Before adding topology nodes, you must create an empty topology object by calling [**MFCreateTopology**](/windows/desktop/api/mfidl/nf-mfidl-mfcreatetopology).

### Create the Source Topology Node for the Media Source

In this step, you will create the source topology node for the media source.

To create this node you need the following references:

-   A pointer to the media source that you created in the step described in the "Create the Media Source" section of this tutorial.
-   A pointer to the presentation descriptor for the media source. You can get a reference to IMFPresentationDescriptor interface of the media source by calling [**IMFMediaSource::CreatePresentationDescriptor**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasource-createpresentationdescriptor).
-   A pointer to the stream descriptor for each stream in the media source for which you have created a target stream in the step described in the "Create the ASF Profile Object" section of this tutorial.

For more information about creating source nodes and code example, see [Creating Source Nodes](creating-source-nodes.md).

The following code example creates a partial topology by adding the source node and the required transform nodes. This code calls the helper functions AddSourceNode, and AddTransformOutputNodes. These functions are included later in this tutorial.


```C++
//-------------------------------------------------------------------
//  BuildPartialTopology
//  Create a partial encoding topology by adding the source and the sink.
//
//  pSource:  A pointer to the media source to enumerate the source streams.
//  pSinkActivate: A pointer to the activation object for ASF file sink.
//  ppTopology:  Receives a pointer to the topology.
//-------------------------------------------------------------------

HRESULT BuildPartialTopology(
       IMFMediaSource *pSource, 
       IMFActivate* pSinkActivate,
       IMFTopology** ppTopology)
{
    if (!pSource || !pSinkActivate)
    {
        return E_INVALIDARG;
    }
    if (!ppTopology)
    {
        return E_POINTER;
    }

    HRESULT hr = S_OK;

    IMFPresentationDescriptor* pPD = NULL;
    IMFStreamDescriptor *pStreamDesc = NULL;
    IMFMediaTypeHandler* pMediaTypeHandler = NULL;
    IMFMediaType* pSrcType = NULL;

    IMFTopology* pTopology = NULL;
    IMFTopologyNode* pSrcNode = NULL;
    IMFTopologyNode* pEncoderNode = NULL;
    IMFTopologyNode* pOutputNode = NULL;


    DWORD cElems = 0;
    DWORD dwSrcStream = 0;
    DWORD StreamID = 0;
    GUID guidMajor = GUID_NULL;
    BOOL fSelected = FALSE;


    //Create the topology that represents the encoding pipeline
    hr = MFCreateTopology (&pTopology);
    if (FAILED(hr))
    {
        goto done;
    }

        
    hr = pSource->CreatePresentationDescriptor(&pPD);
    if (FAILED(hr))
    {
        goto done;
    }

    hr = pPD->GetStreamDescriptorCount(&dwSrcStream);
    if (FAILED(hr))
    {
        goto done;
    }

    for (DWORD iStream = 0; iStream < dwSrcStream; iStream++)
    {
        hr = pPD->GetStreamDescriptorByIndex(
            iStream, &fSelected, &pStreamDesc);
        if (FAILED(hr))
        {
            goto done;
        }

        if (!fSelected)
        {
            continue;
        }

        hr = AddSourceNode(pTopology, pSource, pPD, pStreamDesc, &pSrcNode);
        if (FAILED(hr))
        {
            goto done;
        }

        hr = pStreamDesc->GetMediaTypeHandler (&pMediaTypeHandler);
        if (FAILED(hr))
        {
            goto done;
        }
        
        hr = pStreamDesc->GetStreamIdentifier(&StreamID);
        if (FAILED(hr))
        {
            goto done;
        }

        hr = pMediaTypeHandler->GetMediaTypeByIndex(0, &pSrcType);
        if (FAILED(hr))
        {
            goto done;
        }

        hr = pSrcType->GetMajorType(&guidMajor);
        if (FAILED(hr))
        {
            goto done;
        }

        hr = AddTransformOutputNodes(pTopology, pSinkActivate, pSrcType, &pEncoderNode);
        if (FAILED(hr))
        {
            goto done;
        }

        //now we have the transform node, connect it to the source node
        hr = pSrcNode->ConnectOutput(0, pEncoderNode, 0);
        if (FAILED(hr))
        {
            goto done;
        }
                

        SafeRelease(&pStreamDesc);
        SafeRelease(&pMediaTypeHandler);
        SafeRelease(&pSrcType);
        SafeRelease(&pEncoderNode);
        SafeRelease(&pOutputNode);
        guidMajor = GUID_NULL;
    }

    *ppTopology = pTopology;
   (*ppTopology)->AddRef();


    wprintf_s(L"Partial Topology Built.\n");

done:
    SafeRelease(&pStreamDesc);
    SafeRelease(&pMediaTypeHandler);
    SafeRelease(&pSrcType);
    SafeRelease(&pEncoderNode);
    SafeRelease(&pOutputNode);
    SafeRelease(&pTopology);

    return hr;
}
```



The following code example creates and adds the source topology node to the encoding topology. It takes pointers to a previously topology object, the media source to enumerate the source streams, the media source's presentation descriptor, and the media source's stream descriptor. The caller receives a pointer to the source topology node.


```C++
// Add a source node to a topology.
HRESULT AddSourceNode(
    IMFTopology *pTopology,           // Topology.
    IMFMediaSource *pSource,          // Media source.
    IMFPresentationDescriptor *pPD,   // Presentation descriptor.
    IMFStreamDescriptor *pSD,         // Stream descriptor.
    IMFTopologyNode **ppNode)         // Receives the node pointer.
{
    IMFTopologyNode *pNode = NULL;

    // Create the node.
    HRESULT hr = MFCreateTopologyNode(MF_TOPOLOGY_SOURCESTREAM_NODE, &pNode);
    if (FAILED(hr))
    {
        goto done;
    }

    // Set the attributes.
    hr = pNode->SetUnknown(MF_TOPONODE_SOURCE, pSource);
    if (FAILED(hr))
    {
        goto done;
    }

    hr = pNode->SetUnknown(MF_TOPONODE_PRESENTATION_DESCRIPTOR, pPD);
    if (FAILED(hr))
    {
        goto done;
    }

    hr = pNode->SetUnknown(MF_TOPONODE_STREAM_DESCRIPTOR, pSD);
    if (FAILED(hr))
    {
        goto done;
    }
    
    // Add the node to the topology.
    hr = pTopology->AddNode(pNode);
    if (FAILED(hr))
    {
        goto done;
    }

    // Return the pointer to the caller.
    *ppNode = pNode;
    (*ppNode)->AddRef();

done:
    SafeRelease(&pNode);
    return hr;
}
```



### Instantiate the Required Encoders and Create the Transform Nodes

The Media Foundation pipeline does not automatically insert the required Windows Media encoders for the streams that it must encode. The application must add the encoders manually. To do so, enumerate the streams in the ASF profile that you created in the step described in the "Create the ASF Profile Object" section of this tutorial. For each stream in the source and the corresponding stream in the profile, instantiate the required encoders. For this step, you need a pointer to the activation object for the file sink that you created in the step described in the "Create the ASF File Sink" section of this tutorial.

For an overview on creating encoders through activation objects, see [Using an Encoder's Activation Objects](using-an-encoder-s-activation-objects.md).

The following procedure describes the steps required to instantiate the required encoders.

1.  Get a reference to the sink's ContentInfo object by calling [**IMFActivate::ActivateObject**](/windows/desktop/api/mfobjects/nf-mfobjects-imfactivate-activateobject) on the file sink activate and then querying for [**IMFASFContentInfo**](/windows/desktop/api/wmcontainer/nn-wmcontainer-imfasfcontentinfo) from the file sink by calling **QueryInterface**.
2.  Get the ASF profile associated with the ContentInfo object by calling [**IMFASFContentInfo::GetProfile**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfcontentinfo-getprofile).
3.  Enumerate the streams in the profile. For this you will need the stream count and a reference to each stream's [**IMFASFStreamConfig**](/windows/desktop/api/wmcontainer/nn-wmcontainer-imfasfstreamconfig) interface.

    Call the following methods:

    -   [**IMFASFProfile::GetStreamCount**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfprofile-getstreamcount)
    -   [**IMFASFProfile::GetStream**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfprofile-getstream)

4.  For each stream get the major type and the stream's encoding properties from the ContentInfo object.

    Call the following methods:

    -   [**IMFASFStreamConfig::GetMediaType**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfstreamconfig-getmediatype)
    -   [**IMFMediaType::GetMajorType**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediatype-getmajortype)
    -   [**IMFASFContentInfo::GetEncodingConfigurationPropertyStore**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfcontentinfo-getencodingconfigurationpropertystore)

        For this call you need the stream number retrieved by the [**IMFASFProfile::GetStream**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfprofile-getstream) call.

5.  Depending on the type of the stream, audio or video, instantiate the activation object for the encoder by calling [**MFCreateWMAEncoderActivate**](/windows/desktop/api/wmcontainer/nf-wmcontainer-mfcreatewmaencoderactivate) or [**MFCreateWMVEncoderActivate**](/windows/desktop/api/wmcontainer/nf-wmcontainer-mfcreatewmvencoderactivate).

    To call these functions, you need the following references:

    -   A pointer to the stream's media type retrieved by [**IMFASFStreamConfig::GetMediaType**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfstreamconfig-getmediatype) in the previous step.
    -   A pointer to the stream's encoding property store retrieved by [**IMFASFContentInfo::GetEncodingConfigurationPropertyStore**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfcontentinfo-getencodingconfigurationpropertystore). By passing a pointer to the property store, the stream properties set in the file sink are copied on the encoder MFT.

6.  Update the leaky bucket parameter for the audio stream.

    [**MFCreateWMAEncoderActivate**](/windows/desktop/api/wmcontainer/nf-wmcontainer-mfcreatewmaencoderactivate) sets the output type on the underlying encoder MFT for the Windows Media audio codec. After the output media type is set, the encoder gets the average bit rate from the output media type, calculates the buffer window rage bit rate, and sets the leaky bucket values that will be used during the encoding session. You can update these values in the file sink by either querying the encoder or setting custom values. To update values you need the following set of information:

    -   Average bit rate: Get the average bit rate from the [**MF\_MT\_AUDIO\_AVG\_BYTES\_PER\_SECOND**](mf-mt-audio-avg-bytes-per-second-attribute.md) attribute set on the output media type that is selected during media type negotiation.
    -   Buffer window: you can retrieve it by calling [**IWMCodecLeakyBucket::GetBufferSizeBits**](../wmformat/iwmcodecleakybucket-getbuffersizebits.md).
    -   Initial buffer size: Set to 0.

    Create an array of DWORDs and set the value in the [**MFPKEY\_ASFSTREAMSINK\_CORRECTED\_LEAKYBUCKET**](mfpkey-asfstreamsink-corrected-leakybucket-property.md) property of the audio stream sink. If you do not provide the updated values, the Media Session sets them appropriately.

    For more information, see [The Leaky Bucket Buffer Model](the-leaky-bucket-buffer-model.md).

The activation objects created in step 5 must be added to the topology as transform topology nodes. For more information and code example, see "Creating a Transform Node from an Activation Object" in [Creating Transform Nodes](creating-transform-nodes.md).

The following code example creates and adds the required encoder activates. It takes pointers to a previously created topology object, the file sink's activation object and the source stream's media type. It also calls AddOutputNode (see next code example) that creates and adds the sink node to the encoding topology. It The caller receives a pointer to the source topology node.


```C++
//-------------------------------------------------------------------
//  AddTransformOutputNodes
//  Creates and adds the sink node to the encoding topology.
//  Creates and adds the required encoder activates.

//  pTopology:  A pointer to the topology.
//  pSinkActivate:  A pointer to the file sink's activation object.
//  pSourceType: A pointer to the source stream's media type.
//  ppNode:  Receives a pointer to the topology node.
//-------------------------------------------------------------------

HRESULT AddTransformOutputNodes(
    IMFTopology* pTopology,
    IMFActivate* pSinkActivate,
    IMFMediaType* pSourceType,
    IMFTopologyNode **ppNode    // Receives the node pointer.
    )
{
    if (!pTopology || !pSinkActivate || !pSourceType)
    {
        return E_INVALIDARG;
    }

    IMFTopologyNode* pEncNode = NULL;
    IMFTopologyNode* pOutputNode = NULL;
    IMFASFContentInfo* pContentInfo = NULL;
    IMFASFProfile* pProfile = NULL;
    IMFASFStreamConfig* pStream = NULL;
    IMFMediaType* pMediaType = NULL;
    IPropertyStore* pProps = NULL;
    IMFActivate *pEncoderActivate = NULL;
    IMFMediaSink *pSink = NULL; 

    GUID guidMT = GUID_NULL;
    GUID guidMajor = GUID_NULL;

    DWORD cStreams = 0;
    WORD wStreamNumber = 0;

    HRESULT hr = S_OK;
        
    hr = pSourceType->GetMajorType(&guidMajor);
    if (FAILED(hr))
    {
        goto done;
    }

    // Create the node.
    hr = MFCreateTopologyNode(MF_TOPOLOGY_TRANSFORM_NODE, &pEncNode);
    if (FAILED(hr))
    {
        goto done;
    }
    
    //Activate the sink
    hr = pSinkActivate->ActivateObject(__uuidof(IMFMediaSink), (void**)&pSink);
    if (FAILED(hr))
    {
        goto done;
    }
    //find the media type in the sink
    //Get content info from the sink
    hr = pSink->QueryInterface(__uuidof(IMFASFContentInfo), (void**)&pContentInfo);
    if (FAILED(hr))
    {
        goto done;
    }
    

    hr = pContentInfo->GetProfile(&pProfile);
    if (FAILED(hr))
    {
        goto done;
    }

    hr = pProfile->GetStreamCount(&cStreams);
    if (FAILED(hr))
    {
        goto done;
    }

    for(DWORD index = 0; index < cStreams ; index++)
    {
        hr = pProfile->GetStream(index, &wStreamNumber, &pStream);
        if (FAILED(hr))
        {
            goto done;
        }
        hr = pStream->GetMediaType(&pMediaType);
        if (FAILED(hr))
        {
            goto done;
        }
        hr = pMediaType->GetMajorType(&guidMT);
        if (FAILED(hr))
        {
            goto done;
        }
        if (guidMT!=guidMajor)
        {
            SafeRelease(&pStream);
            SafeRelease(&pMediaType);
            guidMT = GUID_NULL;

            continue;
        }
        //We need to activate the encoder
        hr = pContentInfo->GetEncodingConfigurationPropertyStore(wStreamNumber, &pProps);
        if (FAILED(hr))
        {
            goto done;
        }

        if (guidMT == MFMediaType_Audio)
        {
             hr = MFCreateWMAEncoderActivate(pMediaType, pProps, &pEncoderActivate);
            if (FAILED(hr))
            {
                goto done;
            }
            wprintf_s(L"Audio Encoder created. Stream Number: %d .\n", wStreamNumber);

            break;
        }
        if (guidMT == MFMediaType_Video)
        {
            hr = MFCreateWMVEncoderActivate(pMediaType, pProps, &pEncoderActivate);
            if (FAILED(hr))
            {
                goto done;
            }
            wprintf_s(L"Video Encoder created. Stream Number: %d .\n", wStreamNumber);

            break;
        }
    }

    // Set the object pointer.
    hr = pEncNode->SetObject(pEncoderActivate);
    if (FAILED(hr))
    {
        goto done;
    }

    // Add the node to the topology.
    hr = pTopology->AddNode(pEncNode);
    if (FAILED(hr))
    {
        goto done;
    }

    //Add the output node to this node.
    hr = AddOutputNode(pTopology, pSinkActivate, wStreamNumber, &pOutputNode);
    if (FAILED(hr))
    {
        goto done;
    }

    //now we have the output node, connect it to the transform node
    hr = pEncNode->ConnectOutput(0, pOutputNode, 0);
    if (FAILED(hr))
    {
        goto done;
    }

   // Return the pointer to the caller.
    *ppNode = pEncNode;
    (*ppNode)->AddRef();


done:
    SafeRelease(&pEncNode);
    SafeRelease(&pOutputNode);
    SafeRelease(&pEncoderActivate);
    SafeRelease(&pMediaType);
    SafeRelease(&pProps);
    SafeRelease(&pStream);
    SafeRelease(&pProfile);
    SafeRelease(&pContentInfo);
    SafeRelease(&pSink);
    return hr;
}
```



### Create the Output Topology Nodes for the File Sink

In this step, you will create the output topology node for the ASF file sink.

To create this node you need the following references:

-   A pointer to the activation object that you created in the step described in the "Create the ASF File Sink" section of this tutorial.
-   The stream numbers to identify the stream sinks added to the file sink. The stream numbers match the stream's identification that was set during stream creation.

For more information about creating output nodes and code example, see "Creating an Output Node from an Activation Object" in [Creating Output Nodes](creating-output-nodes.md).

If you are not using activation object for the file sink, you must enumerate the stream sinks in the ASF file sink and set each stream sink as the output node in the topology. For information about stream sink enumeration, see "Enumerating Stream Sinks" in [Adding Stream Information to the ASF File Sink](adding-stream-information-to-the-asf-file-sink.md).

The following code example creates and adds the sink node to the encoding topology. It takes pointers to a previously created topology object, the file sink's activation object and the stream's identification number. It The caller receives a pointer to the source topology node.


```C++
// Add an output node to a topology.
HRESULT AddOutputNode(
    IMFTopology *pTopology,     // Topology.
    IMFActivate *pActivate,     // Media sink activation object.
    DWORD dwId,                 // Identifier of the stream sink.
    IMFTopologyNode **ppNode)   // Receives the node pointer.
{
    IMFTopologyNode *pNode = NULL;

    // Create the node.
    HRESULT hr = MFCreateTopologyNode(MF_TOPOLOGY_OUTPUT_NODE, &pNode);
    if (FAILED(hr))
    {
        goto done;
    }

    // Set the object pointer.
    hr = pNode->SetObject(pActivate);
    if (FAILED(hr))
    {
        goto done;
    }

    // Set the stream sink ID attribute.
    hr = pNode->SetUINT32(MF_TOPONODE_STREAMID, dwId);
    if (FAILED(hr))
    {
        goto done;
    }

    hr = pNode->SetUINT32(MF_TOPONODE_NOSHUTDOWN_ON_REMOVE, FALSE);
    if (FAILED(hr))
    {
        goto done;
    }

    // Add the node to the topology.
    hr = pTopology->AddNode(pNode);
    if (FAILED(hr))
    {
        goto done;
    }

    // Return the pointer to the caller.
    *ppNode = pNode;
    (*ppNode)->AddRef();

done:
    SafeRelease(&pNode);
    return hr;
}
```



The following code example enumerates the stream sinks for a given media sink.


```C++
//-------------------------------------------------------------------
//  EnumerateStreamSinks
//  Enumerates the stream sinks within the specified media sink.
//
//  pSink:  A pointer to the media sink.
//-------------------------------------------------------------------
HRESULT EnumerateStreamSinks (IMFMediaSink* pSink)
{
    if (!pSink)
    {
        return E_INVALIDARG;
    }
    
    IMFStreamSink* pStreamSink = NULL;
    DWORD cStreamSinks = 0;

    HRESULT hr = pSink->GetStreamSinkCount(&cStreamSinks);
    if (FAILED(hr))
    {
        goto done;
    }

    for(DWORD index = 0; index < cStreamSinks; index++)
    {
        hr = pSink->GetStreamSinkByIndex (index, &pStreamSink);
        if (FAILED(hr))
        {
            goto done;
        }

        //Use the stream sink
        //Not shown.
    }
done:
    SafeRelease(&pStreamSink);

    return hr;
}
```



### Connect the Source, Transform, and Sink Nodes

In this step, you will connect the source node to the transform node referencing the encoding activates that you created in the step described in the "Instantiate the Required Encoders and Create the Transform Nodes" section of this tutorial. The transform node will be connected to the output node containing the activation object for the file sink.

## Handling the Encoding Session

In the step, you will perform the following steps:

1.  Call [**MFCreateMediaSession**](/windows/desktop/api/mfidl/nf-mfidl-mfcreatemediasession) to create an encoding session.
2.  Call [**IMFMediaSession::SetTopology**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasession-settopology) to set the encoding topology on the session. If the call completes, the Media Session evaluates the topology nodes and inserts additional transform objects such as a decoder that converts the specified compressed source to uncompressed samples to feed as input to the encoder.
3.  Call [**IMFMediaSession::GetEvent**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaeventgenerator-getevent) to request for the events raised by the Media Session.

    In the event loop you will start and close the encoding session depending on the events raised by the Media Session. The [**IMFMediaSession::SetTopology**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasession-settopology) call results in Media Session raising the [MESessionTopologyStatus](mesessiontopologystatus.md) event with the MF\_TOPOSTATUS\_READY flag set. All events are generated asynchronously and an application can retrieve these events synchronously or asynchronously. Because the application in this tutorial is a console application and blocking user interface threads is not a concern, we will get the events from Media Session synchronously.

    To get the events asynchronously, your application must implement the [**IMFAsyncCallback**](/windows/desktop/api/mfobjects/nn-mfobjects-imfasynccallback) interface. For more information and an example implementation of this interface, see "Handling Session Events" in [How to Play Media Files with Media Foundation](how-to-play-unprotected-media-files.md).

In the event loop for getting Media Session events, wait for the [MESessionTopologyStatus](mesessiontopologystatus.md) event that is raised when the [**IMFMediaSession::SetTopology**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasession-settopology) completes and the topology is resolved. Upon getting the MESessionTopologyStatus event, start the encoding session by calling [**IMFMediaSession::Start**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasession-start). The Media Session generates the [MEEndOfPresentation](meendofpresentation.md) event when all of the encoding operations are complete. This event must be handled for VBR encoding and is discussed in the next section "Update Encoding Properties on the File Sink for VBR Encoding" of this tutorial.

The Media Session generates the ASF Header Object and finalizes the file when the encoding session completes and then raises the [MESessionClosed](mesessionclosed.md) event. This event must be handled by performing proper shutdown operations on the Media Session. To begin the shutdown operations, call [**IMFMediaSession::Shutdown**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasession-shutdown). After the encoding session is closed, you cannot set another topology for encoding on the same Media Session instance. To encode another file, the current Media Session must be closed and released and the new topology must be set on a newly created Media Session. The following code example creates the Media Session, sets the encoding topology and handles the Media Session events.

The following code example creates the Media Session, sets the encoding topology, and controls the encoding session by handling events from the Media Session.


```C++
//-------------------------------------------------------------------
//  Encode
//  Controls the encoding session and handles events from the media session.
//
//  pTopology:  A pointer to the encoding topology.
//-------------------------------------------------------------------

HRESULT Encode(IMFTopology *pTopology)
{
    if (!pTopology)
    {
        return E_INVALIDARG;
    }
    
    IMFMediaSession *pSession = NULL;
    IMFMediaEvent* pEvent = NULL;
    IMFTopology* pFullTopology = NULL;
    IUnknown* pTopoUnk = NULL;


    MediaEventType meType = MEUnknown;  // Event type

    HRESULT hr = S_OK;
    HRESULT hrStatus = S_OK;            // Event status
                
    MF_TOPOSTATUS TopoStatus = MF_TOPOSTATUS_INVALID; // Used with MESessionTopologyStatus event.    
        

    hr = MFCreateMediaSession(NULL, &pSession);
    if (FAILED(hr))
    {
        goto done;
    }

    hr = pSession->SetTopology(MFSESSION_SETTOPOLOGY_IMMEDIATE, pTopology);
    if (FAILED(hr))
    {
        goto done;
    }

    //Get media session events synchronously
    while (1)
    {
        hr = pSession->GetEvent(0, &pEvent);
        if (FAILED(hr))
        {
            goto done;
        }

        hr = pEvent->GetType(&meType);
        if (FAILED(hr))
        {
            goto done;
        }

        hr = pEvent->GetStatus(&hrStatus);
        if (FAILED(hr))
        {
            goto done;
        }
        if (FAILED(hrStatus))
        {
            hr = hrStatus;
            goto done;
        }

       switch(meType)
        {
            case MESessionTopologyStatus:
                {
                    // Get the status code.
                    MF_TOPOSTATUS status = (MF_TOPOSTATUS)MFGetAttributeUINT32(
                                             pEvent, MF_EVENT_TOPOLOGY_STATUS, MF_TOPOSTATUS_INVALID);

                    if (status == MF_TOPOSTATUS_READY)
                    {
                        PROPVARIANT var;
                        PropVariantInit(&var);
                        wprintf_s(L"Topology resolved and set on the media session.\n");

                        hr = pSession->Start(NULL, &var);
                        if (FAILED(hr))
                        {
                            goto done;
                        }

                    }
                    if (status == MF_TOPOSTATUS_STARTED_SOURCE)
                    {
                        wprintf_s(L"Encoding started.\n");
                        break;
                    }
                    if (status == MF_TOPOSTATUS_ENDED)
                    {
                        wprintf_s(L"Encoding complete.\n");
                        hr = pSession->Close();
                        if (FAILED(hr))
                        {
                            goto done;
                        }

                        break;
                    }
                }
                break;


            case MESessionEnded:
                wprintf_s(L"Encoding complete.\n");
                hr = pSession->Close();
                if (FAILED(hr))
                {
                    goto done;
                }
                break;

            case MEEndOfPresentation:
                {
                    if (EncodingMode == VBR)
                    {
                        hr = pSession->GetFullTopology(MFSESSION_GETFULLTOPOLOGY_CURRENT, 0, &pFullTopology);
                        if (FAILED(hr))
                        {
                            goto done;
                        }
                        hr = PostEncodingUpdate(pFullTopology);
                        if (FAILED(hr))
                        {
                            goto done;
                        }
                        wprintf_s(L"Updated sinks for VBR. \n");
                    }
                }
                break;

            case MESessionClosed:
                wprintf_s(L"Encoding session closed.\n");

                hr = pSession->Shutdown();
                goto done;
        }
        if (FAILED(hr))
        {
            goto done;
        }

        SafeRelease(&pEvent);

    }
done:
    SafeRelease(&pEvent);
    SafeRelease(&pSession);
    SafeRelease(&pFullTopology);
    SafeRelease(&pTopoUnk);
    return hr;
}
```



## Update Encoding Properties in the File Sink

Certain encoding properties such as the encoding bit rate and the accurate leaky bucket values are not known until the encoding is complete, especially for VBR encoding. To get the correct values the application must wait for the [MEEndOfPresentation](meendofpresentation.md) event that indicates that the encoding session is complete. The leaky bucket values must be updated in the sink so that the ASF Header Object can reflect the accurate values.

The following procedure describes the steps required to traverse the nodes in the encoding topology to get the file sink node and set the required leaky bucket properties.

**To update the post encoding property values on the ASF file sink**

1.  Call [**IMFTopology::GetOutputNodeCollection**](/windows/desktop/api/mfidl/nf-mfidl-imftopology-getoutputnodecollection) to get the output node collection from the encoding topology.
2.  For each node, get a pointer to the stream sink in the node by calling [**IMFTopologyNode::GetObject**](/windows/desktop/api/mfidl/nf-mfidl-imftopologynode-getobject). Query for the [**IMFStreamSink**](/windows/desktop/api/mfidl/nn-mfidl-imfstreamsink) interface on the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) pointer returned by **IMFTopologyNode::GetObject**.
3.  For each stream sink get the downstream node (encoder) by calling [**IMFTopologyNode::GetInput**](/windows/desktop/api/mfidl/nf-mfidl-imftopologynode-getinput).
4.  Query the node to get the [**IMFTransform**](/windows/desktop/api/mftransform/nn-mftransform-imftransform) pointer from the encoder node.
5.  Query the encoder for the [**IPropertyStore**](/windows/win32/api/propsys/nn-propsys-ipropertystore) pointer to get the encoding property store from the encoder.
6.  Query the stream sink for the [**IPropertyStore**](/windows/win32/api/propsys/nn-propsys-ipropertystore) pointer to get the stream sink's property store.
7.  Call [**IPropertyStore::GetValue**](/windows/win32/api/propsys/nn-propsys-ipropertystore) to get the required property values from the encoder's property store and copy them to the stream sink's property store by calling **IPropertyStore::SetValue**.

The following table shows the post encoding property values that must be set on the stream sink for the video stream.



| Encoding type                                                                                  | Property name (GetValue)                                                                        | Property name (SetValue)                                                                                                |
|------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| [Constant Bit Rate Encoding](constant-bit-rate-encoding.md)                                   | MFPKEY\_BAVG<br/> MFPKEY\_RAVG<br/>                                                 | MFPKEY\_STAT\_BAVG<br/> MFPKEY\_STAT\_RAVG<br/>                                                             |
| [Quality-Based Variable Bit Rate Encoding](quality-based-variable-bit-rate--vbr--encoding.md) | MFPKEY\_BAVG<br/> MFPKEY\_RAVG<br/> MFPKEY\_BMAX<br/> MFPKEY\_RMAX<br/> | MFPKEY\_STAT\_BAVG<br/> MFPKEY\_STAT\_RAVG<br/> MFPKEY\_STAT\_BMAX<br/> MFPKEY\_STAT\_RMAX<br/> |



 

The following code example sets the post-encoding property values.


```C++
//-------------------------------------------------------------------
//  PostEncodingUpdate
//  Updates the file sink with encoding properties set on the encoder
//  during the encoding session.
    //1. Get the output nodes
    //2. For each node, get the downstream node
    //3. For the downstream node, get the MFT
    //4. Get the property store
    //5. Get the required values
    //6. Set them on the stream sink
//
//  pTopology: A pointer to the full topology retrieved from the media session.
//-------------------------------------------------------------------

HRESULT PostEncodingUpdate(IMFTopology *pTopology)
{
    if (!pTopology)
    {
        return E_INVALIDARG;
    }

    HRESULT hr = S_OK;

    IMFCollection* pOutputColl = NULL;
    IUnknown* pNodeUnk = NULL;
    IMFMediaType* pType = NULL;
    IMFTopologyNode* pNode = NULL;
    IUnknown* pSinkUnk = NULL;
    IMFStreamSink* pStreamSink = NULL;
    IMFTopologyNode* pEncoderNode = NULL;
    IUnknown* pEncoderUnk = NULL;
    IMFTransform* pEncoder = NULL;
    IPropertyStore* pStreamSinkProps = NULL;
    IPropertyStore* pEncoderProps = NULL;

    GUID guidMajorType = GUID_NULL;

    PROPVARIANT var;
    PropVariantInit( &var );

    DWORD cElements = 0;

    hr = pTopology->GetOutputNodeCollection( &pOutputColl);
    if (FAILED(hr))
    {
        goto done;
    }


    hr = pOutputColl->GetElementCount(&cElements);
    if (FAILED(hr))
    {
        goto done;
    }


    for(DWORD index = 0; index < cElements; index++)
    {
        hr = pOutputColl->GetElement(index, &pNodeUnk);
        if (FAILED(hr))
        {
            goto done;
        }

        hr = pNodeUnk->QueryInterface(IID_IMFTopologyNode, (void**)&pNode);
        if (FAILED(hr))
        {
            goto done;
        }

        hr = pNode->GetInputPrefType(0, &pType);
        if (FAILED(hr))
        {
            goto done;
        }

        hr = pType->GetMajorType( &guidMajorType );
        if (FAILED(hr))
        {
            goto done;
        }

        hr = pNode->GetObject(&pSinkUnk);
        if (FAILED(hr))
        {
            goto done;
        }

        hr = pSinkUnk->QueryInterface(IID_IMFStreamSink, (void**)&pStreamSink);
        if (FAILED(hr))
        {
            goto done;
        }

        hr = pNode->GetInput( 0, &pEncoderNode, NULL );
        if (FAILED(hr))
        {
            goto done;
        }

        hr = pEncoderNode->GetObject(&pEncoderUnk);
        if (FAILED(hr))
        {
            goto done;
        }

        hr = pEncoderUnk->QueryInterface(IID_IMFTransform, (void**)&pEncoder);
        if (FAILED(hr))
        {
            goto done;
        }

        hr = pStreamSink->QueryInterface(IID_IPropertyStore, (void**)&pStreamSinkProps);
        if (FAILED(hr))
        {
            goto done;
        }

        hr = pEncoder->QueryInterface(IID_IPropertyStore, (void**)&pEncoderProps);
        if (FAILED(hr))
        {
            goto done;
        }

        if( guidMajorType == MFMediaType_Video )
        {            
            hr = pEncoderProps->GetValue( MFPKEY_BAVG, &var );
            if (FAILED(hr))
            {
                goto done;
            }
            hr = pStreamSinkProps->SetValue( MFPKEY_STAT_BAVG, var );
            if (FAILED(hr))
            {
                goto done;
            }

            PropVariantClear( &var );
            hr = pEncoderProps->GetValue( MFPKEY_RAVG, &var );
            if (FAILED(hr))
            {
                goto done;
            }
            hr = pStreamSinkProps->SetValue( MFPKEY_STAT_RAVG, var);
            if (FAILED(hr))
            {
                goto done;
            }

            PropVariantClear( &var );
            hr = pEncoderProps->GetValue( MFPKEY_BMAX, &var );
            if (FAILED(hr))
            {
                goto done;
            }
            hr = pStreamSinkProps->SetValue( MFPKEY_STAT_BMAX, var);
            if (FAILED(hr))
            {
                goto done;
            }

            PropVariantClear( &var );
            hr = pEncoderProps->GetValue( MFPKEY_RMAX, &var );
            if (FAILED(hr))
            {
                goto done;
            }
            hr = pStreamSinkProps->SetValue( MFPKEY_STAT_RMAX, var);
            if (FAILED(hr))
            {
                goto done;
            }
        }
        else if( guidMajorType == MFMediaType_Audio )
        {      
            hr = pEncoderProps->GetValue( MFPKEY_STAT_BAVG, &var );
            if (FAILED(hr))
            {
                goto done;
            }
            hr = pStreamSinkProps->SetValue( MFPKEY_STAT_BAVG, var );
            if (FAILED(hr))
            {
                goto done;
            }
            
            PropVariantClear( &var );
            hr = pEncoderProps->GetValue( MFPKEY_STAT_RAVG, &var );
            if (FAILED(hr))
            {
                goto done;
            }
            hr = pStreamSinkProps->SetValue( MFPKEY_STAT_RAVG, var );
            if (FAILED(hr))
            {
                goto done;
            }
            
            PropVariantClear( &var );
            hr = pEncoderProps->GetValue( MFPKEY_STAT_BMAX, &var);
            if (FAILED(hr))
            {
                goto done;
            }
            hr = pStreamSinkProps->SetValue( MFPKEY_STAT_BMAX, var);
            if (FAILED(hr))
            {
                goto done;
            }

            PropVariantClear( &var );
            hr = pEncoderProps->GetValue( MFPKEY_STAT_RMAX, &var );
            if (FAILED(hr))
            {
                goto done;
            }
            hr = pStreamSinkProps->SetValue( MFPKEY_STAT_RMAX, var );         
            if (FAILED(hr))
            {
                goto done;
            }

            PropVariantClear( &var );
            hr = pEncoderProps->GetValue( MFPKEY_WMAENC_AVGBYTESPERSEC, &var );
            if (FAILED(hr))
            {
                goto done;
            }
            hr = pStreamSinkProps->SetValue( MFPKEY_WMAENC_AVGBYTESPERSEC, var );         
            if (FAILED(hr))
            {
                goto done;
            }
        } 
        PropVariantClear( &var ); 
   }
done:
    SafeRelease (&pOutputColl);
    SafeRelease (&pNodeUnk);
    SafeRelease (&pType);
    SafeRelease (&pNode);
    SafeRelease (&pSinkUnk);
    SafeRelease (&pStreamSink);
    SafeRelease (&pEncoderNode);
    SafeRelease (&pEncoderUnk);
    SafeRelease (&pEncoder);
    SafeRelease (&pStreamSinkProps);
    SafeRelease (&pEncoderProps);

    return hr;
   
}
```



## Implement Main

The following code example shows the main function of your console application.


```C++
int wmain(int argc, wchar_t* argv[])
{
    HeapSetInformation(NULL, HeapEnableTerminationOnCorruption, NULL, 0);

    if (argc != 4)
    {
        wprintf_s(L"Usage: %s inputaudio.mp3, %s output.wm*, %Encoding Type: CBR, VBR\n");
        return 0;
    }


    HRESULT             hr = S_OK;

    IMFMediaSource* pSource = NULL;
    IMFTopology* pTopology = NULL;
    IMFActivate* pFileSinkActivate = NULL;

    hr = CoInitializeEx(NULL, COINIT_APARTMENTTHREADED | COINIT_DISABLE_OLE1DDE);
    if (FAILED(hr))
    {
        goto done;
    }

    //Set the requested encoding mode
    if (wcscmp(argv[3], L"CBR")==0)
    {
        EncodingMode = CBR;
    }
    else if (wcscmp(argv[3], L"VBR")==0)
    {
        EncodingMode = VBR;
    }
    else
    {
        EncodingMode = CBR;
    }

    // Start up Media Foundation platform.
    hr = MFStartup(MF_VERSION);
    if (FAILED(hr))
    {
        goto done;
    }

    //Create the media source
    hr = CreateMediaSource(argv[1], &pSource);
    if (FAILED(hr))
    {
        goto done;
    }

    //Create the file sink activate
    hr = CreateMediaSink(argv[2], pSource, &pFileSinkActivate);
    if (FAILED(hr))
    {
        goto done;
    }

    //Build the encoding topology.
    hr = BuildPartialTopology(pSource, pFileSinkActivate, &pTopology);
    if (FAILED(hr))
    {
        goto done;
    }

    //Instantiate the media session and start encoding
    hr = Encode(pTopology);
    if (FAILED(hr))
    {
        goto done;
    }


done:
    // Clean up.
    SafeRelease(&pSource);
    SafeRelease(&pTopology);
    SafeRelease(&pFileSinkActivate);

    MFShutdown();
    CoUninitialize();

    if (FAILED(hr))
    {
        wprintf_s(L"Could not create the output file due to 0x%X\n", hr);
    }
    return 0;
}
```



## Test the Output File

The following list describes a check list for testing the encoded file. These values can be checked in the file properties dialog box that you can display by right-clicking the encoded file and selecting **Properties** from the context menu.

-   The path of the encoded file is accurate.
-   The size of the file is more than zero KB and the play duration matches the source file's duration.
-   For the video stream, check the frame width and height, frame rate. These values should match the values that you specified in the ASF profile that you created in the step described in the section "Create the ASF Profile Object".
-   For the audio stream, the bit rate must be close to the value you specified on the target media type.
-   Open the file in Windows Media Player and check the quality of the encoding.
-   Open the ASF file in ASFViewer to see the structure of an ASF file. This tool can be downloaded from this [Microsoft website](https://www.microsoft.com/downloads/details.aspx?displaylang=en&FamilyID=56de5ee4-51ca-46c6-903b-97390ad14fea).

## Common Error Codes and Debugging Tips

The following list describes the common error codes that your might receive and the debugging tips.

-   The call to [**IMFSourceResolver::CreateObjectFromURL**](/windows/desktop/api/mfidl/nf-mfidl-imfsourceresolver-createobjectfromurl) stalls the application.

    Make sure that you have initialized the Media Foundation platform by calling [**MFStartup**](/windows/desktop/api/mfapi/nf-mfapi-mfstartup). This function sets up the asynchronous platform that is used by all methods that start asynchronous operations, such as [**IMFSourceResolver::CreateObjectFromURL**](/windows/desktop/api/mfidl/nf-mfidl-imfsourceresolver-createobjectfromurl), internally.

-   [**IMFSourceResolver::CreateObjectFromURL**](/windows/desktop/api/mfidl/nf-mfidl-imfsourceresolver-createobjectfromurl) returns HRESULT 0x80070002 "The system cannot find the file specified.

    Make sure that the input file name specified by the user in the first argument exists.

-   HRESULT 0x80070020 "The process cannot access the file because it is being used by another process. "

    Make sure that the input and the output files are not currently in use by another resource in the system.

-   Calls to [**IMFTransform**](/windows/desktop/api/mftransform/nn-mftransform-imftransform) methods return MF\_E\_INVALIDMEDIATYPE.

    Make sure that the following conditions are true:

    -   The input type or the output type that you specified is compatible with media types that the encoder supports.
    -   The media types that you specified are complete. For media types to be complete, see the required attributes in the "Create a Compressed Audio Media Type" and "Create a Compressed Video Media Type" sections of this tutorial.
    -   Make sure that you have set the target bit rate on the partial media type to which you are adding the codec private data.

-   The Media Session returns MF\_E\_UNSUPPORTED\_D3D\_TYPE in the event status.

    This error is returned when the source's media type indicates a mixed interlace mode that is not supported by Windows Media Video encoder. If your compressed video media type is set to use progressive mode, the pipeline must use a de-interlacing transform. Because the pipeline is unable to find a match (indicated by this error code), you must insert a de-interlacer (transcode video processor) between the decoder and encoder nodes manually.

-   The Media Session returns E\_INVALIDARG in the event status.

    This error is returned when the source's media type attributes are not compatible with the attributes of the output media type set on the Windows Media encoder.

-   [**IWMCodecPrivateData::GetPrivateData**](../wmformat/iwmcodecprivatedata-getprivatedata.md) returns HRESULT 0x80040203 "A syntax error occurred trying to evaluate a query string"

    Make sure that the input type is set on the encoder MFT.

## Related topics

<dl> <dt>

[Pipeline Layer ASF Components](pipeline-layer-asf-components.md)
</dt> </dl>

 

 
