---
description: This topic describes when and how to use a H.264/AVC Remux MFT and MP4 Sink.
ms.assetid: 1DD236D9-775B-4417-BC49-BF52A6B3C8AD
title: When and How to Use H.264/AVC Remux MFT and MP4 Sink
ms.topic: article
ms.date: 05/31/2018
---

# When and How to Use H.264/AVC Remux MFT and MP4 Sink

This topic describes when and how to use a H.264/AVC Remux MFT and MP4 Sink.

## When to use H.264/AVC Remux MFT

MPEG-4 file format requires that each compressed sample contains one primary picture with NAL units in the correct order. (Please refer to the definition of primary picture and mandatory NAL units order in section 7.4.1.2.3, **Order of NAL units and coded pictures and association to access units**, of the H.264 AVC specification.) It also requires each compressed sample is associated with a presentation time stamp, decoding time stamp, and sample duration.

In many scenarios when applications need to record H.264/AVC video in a MPEG-4 file container, the compressed sample may not satisfy the above requirements. For example, one compressed sample might not contain a complete primary picture or might not have a correct presentation time stamp associated with it. A few application examples are:

-   Write H.264/AVC streaming elementary video into MPEG-4 file container.
-   Record camera captured H.264/AVC elementary video in MPEG-4 file container.
-   Record H.264/AVC video conference in MPEG-4 file container.
-   Concatenate two H.264/AVC video in MPEG-2 TS or MP4 and write into MPEG-4 file container with correct time stamps.
-   Remux H.264/AVC video from AVCHD, MPEG-2 TS/PS file format to MPEG-4 file format.
-   Trim H.264/AVC video file without transcoding.

In this situation, the application needs to use a H.264/AVC remux MFT to convert the compressed samples not containing a complete primary picture before they are written into the MPEG-4 file container.

## How to use H.264/AVC Remux MFT and MP4 sink

Set the source output media type to **MFVideoFormat\_H264\_ES**, which indicates each sample might not contain a complete primary picture. Set the input media type of MP4 sink to **MFVideoFormat\_H264**. So, the input media type of the H.264/AVC remux MFT is **MFVideoFormat\_H264\_ES** and the output media type of the H.264/AVC remux MFT is **MFVideoFormat\_H264**, which will be automatically inserted into the topology resolver.

Sample duration is ignored by the H.264/AVC remux, because the sample duration for a sample not containing a complete primary picture does not have clear meaning. Instead, the sample duration is calculated from the frame rate. The frame rate is calculated from the sequence parameter. If the information does not exist in the sequence parameter, the frame rate is calculated from the parameters in the input media type. If frame rate information is not available, the default frame rate of 29.97 fps is used.

H.264/AVC remux MFT linearly interpolates the decoding time stamps (DTS) for each compressed picture according to the frame rate. H.264/AVC remux MFT honors the input presentation time stamps (PTS) in input samples and passes them to the output if they exist. It performs PTS interpolation according to frame rate, the previous PTS, and the picture output order through Decoded Picture Buffering (DBP) bumping process as specified in **Annex C.4.5.3 Bumping process** of the H.264 AVC specification. Each output sample from the H.264/AVC remux MFT shall have PTS, DTS, and sample duration. H.264/AVC remux MFT also identifies the IDR pictures in the bitstream and sets them as clean point with the MF attribute of [MFSampleExtension\_CleanPoint](mfsampleextension-cleanpoint-attribute.md).

Currently the H.264/AVC remux MFT can handle a maximum of 64 reordered frame. If the number of reordered frame exceeds 64 with a long term reference frame present, the H.264/AVC remux MFT will interpolate a wrong PTS for that frame and output that frame at a wrong time.

To instantiate a H.264/AVC remux MFT, set the correct input and output media types on the H.264/AVC remux MFT, set the input media type for the MP4 sink, and resolve the topology.

The following sample code show how to initialize the H.264/AVC remux MFT and MP4 sink.

For H.264/AVC remux MFT,


```C++
hr = CoCreateInstance(
            CLSID_CMSH264RemuxMFT,
            NULL,
            CLSCTX_INPROC_SERVER,
            IID_IMFTransform,
            (void**) &pIMFTransform
            );
```



No further configuration is necessary.

For MP4 sink,


```C++
IMFByteStream*  pMFBSOutputFile = NULL;
hr = MFCreateFile(
    MF_ACCESSMODE_READWRITE,
    MF_OPENMODE_DELETE_IF_EXIST,
    MF_FILEFLAGS_NONE,
    m_pszOutputFile,
    &pMFBSOutputFile);
if(FAILED(hr))
{
    Log(L"ERROR>> Failed to create output file for MP4 Sink (hr=0x%x)", hr);
    break;
}

hr = MFCreateMPEG4MediaSink(
    pMFBSOutputFile,
    (guidMajorType == MFMediaType_Video) ? pMediaType : NULL,  // pMediaType comes from the output type of the remux MFT
    (guidMajorType == MFMediaType_Audio) ? pMediaType : NULL,
    &m_pMediaSink);
if(FAILED(hr))
{
    Log(L"ERROR>> Failed to create MP4 Sink (hr=0x%x)", hr);
    break;
}
hr = m_pMediaSink->GetStreamSinkByIndex(0, &pStream);
```



## Related topics

<dl> <dt>

[Supported Media Formats in Media Foundation](supported-media-formats-in-media-foundation.md)
</dt> </dl>

 

 



