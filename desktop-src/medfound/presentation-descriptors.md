---
Description: Presentation Descriptors
ms.assetid: 714c8bda-5ce1-47e2-ba73-9304e26b3129
title: Presentation Descriptors
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Presentation Descriptors

A *presentation* is a set of related media streams that share a common presentation time. For example, a presentation might consist of the audio and video streams from a movie. A *presentation descriptor* is an object that contains the description of a particular presentation. Presentation descriptors are used to configure media sources and some media sinks.

Each presentation descriptor contains a list of one or more *stream descriptors*. These describe the streams in the presentation. Streams can be either selected or deselected. Only the selected streams produce data. Deselected streams are not active and do not produce any data. Each stream descriptor has a *media type handler*, which is used to change the stream's media type or get the stream's current media type. (For more information about media types, see [Media Types](media-types.md).)

The following table shows the primary interfaces that each of these objects exposes.



| Object                  | Interface                                                      |
|-------------------------|----------------------------------------------------------------|
| Presentation descriptor | [**IMFPresentationDescriptor**](/windows/win32/mfidl/nn-mfidl-imfpresentationdescriptor?branch=master) |
| Stream descriptor       | [**IMFStreamDescriptor**](/windows/win32/mfidl/nn-mfidl-imfstreamdescriptor?branch=master)             |
| Media type handler      | [**IMFMediaTypeHandler**](/windows/win32/mfidl/nn-mfidl-imfmediatypehandler?branch=master)             |



 

## Media Source Presentations

Every media source provides a presentation descriptor that describes the default configuration for the source. In the default configuration, at least one stream is selected, and every selected stream has a media type. To get the presentation descriptor, call [**IMFMediaSource::CreatePresentationDescriptor**](/windows/win32/mfidl/nf-mfidl-imfmediasource-createpresentationdescriptor?branch=master). The method returns an [**IMFPresentationDescriptor**](/windows/win32/mfidl/nn-mfidl-imfpresentationdescriptor?branch=master) pointer.

You can modify the source's presentation descriptor to select a different set of streams. Do not modify the presentation descriptor unless the media source is stopped. The changes are applied when you call [**IMFMediaSource::Start**](/windows/win32/mfidl/nf-mfidl-imfmediasource-start?branch=master) to start the source.

To get the number of streams, call [**IMFPresentationDescriptor::GetStreamDescriptorCount**](/windows/win32/mfidl/nf-mfidl-imfpresentationdescriptor-getstreamdescriptorcount?branch=master). To get the stream descriptor for a stream, call [**IMFPresentationDescriptor::GetStreamDescriptorByIndex**](/windows/win32/mfidl/nf-mfidl-imfpresentationdescriptor-getstreamdescriptorbyindex?branch=master) and pass in the index of the stream. Streams are indexed from zero. The **GetStreamDescriptorByIndex** method returns an [**IMFStreamDescriptor**](/windows/win32/mfidl/nn-mfidl-imfstreamdescriptor?branch=master) pointer. It also returns a Boolean flag indicating whether the stream is selected. If the stream is selected, the media source produces data for that stream. Otherwise, the source does not produce any data for that stream. To select a stream, call [**IMFPresentationDescriptor::SelectStream**](/windows/win32/mfidl/nf-mfidl-imfpresentationdescriptor-selectstream?branch=master) with the index of the stream. To deselect a stream, call [**IMFPresentationDescriptor::DeselectStream**](/windows/win32/mfidl/nf-mfidl-imfpresentationdescriptor-deselectstream?branch=master).

The following code shows how to get the presentation descriptor from a media source and enumerate the streams.


```C++
HRESULT hr = S_OK;
DWORD cStreams = 0;
BOOL  fSelected = FALSE;

IMFPresentationDescriptor *pPresentation = NULL;
IMFStreamDescriptor *pStreamDesc = NULL;

hr = pSource->CreatePresentationDescriptor(&amp;pPresentation);

if (SUCCEEDED(hr))
{
    hr = pPresentation->GetStreamDescriptorCount(&amp;cStreams);
}

if (SUCCEEDED(hr))
{
    for (DWORD iStream = 0; iStream < cStreams; iStream++)
    {
        hr = pPresentation->GetStreamDescriptorByIndex(
            iStream, &amp;fSelected, &amp;pStreamDesc);

        if (FAILED(hr))
        {
            break;
        }

        /*  Use the stream descriptor. (Not shown.) */

        SAFE_RELEASE(pStreamDesc);
    }
}
SAFE_RELEASE(pPresentation);
SAFE_RELEASE(pStreamDesc);
```



## Media Type Handlers

To change the stream's media type or to get the stream's current media type, use the stream descriptor's media type handler. Call [**IMFStreamDescriptor::GetMediaTypeHandler**](/windows/win32/mfidl/nf-mfidl-imfstreamdescriptor-getmediatypehandler?branch=master) to get the media type handler. This method returns an [**IMFMediaTypeHandler**](/windows/win32/mfidl/nn-mfidl-imfmediatypehandler?branch=master) pointer.

If you simply want to know what kind of data is in the stream, such as audio or video, call [**IMFMediaTypeHandler::GetMajorType**](/windows/win32/mfidl/nf-mfidl-imfmediatypehandler-getmajortype?branch=master). This method returns the GUID for the major media type. For example, a playback application typically connects an audio stream to the audio renderer and a video stream to the video renderer. If you use the Media Session or the topology loader to build a topology, the major type GUID might be the only format information that you need.

If your application needs more detailed information about the current format, call [**IMFMediaTypeHandler::GetCurrentMediaType**](/windows/win32/mfidl/nf-mfidl-imfmediatypehandler-getcurrentmediatype?branch=master). This method returns a pointer to the [**IMFMediaType**](/windows/win32/mfobjects/nn-mfobjects-imfmediatype?branch=master) interface of the media type. Use this interface to get the details of the format.

The media type handler also contains a list of supported media types for the stream. To get the size of the list, call [**IMFMediaTypeHandler::GetMediaTypeCount**](/windows/win32/mfidl/nf-mfidl-imfmediatypehandler-getmediatypecount?branch=master). To get a media type from the list, call [**IMFMediaTypeHandler::GetMediaTypeByIndex**](/windows/win32/mfidl/nf-mfidl-imfmediatypehandler-getmediatypebyindex?branch=master) with the index of the media type. Media types are returned in the approximate order of preference. For example, for audio formats, higher sample rates are preferred over lower sample rates. However, there is no definitive rule that governs the ordering, so you should treat it simply as a guideline.

The list of supported types might not contain every possible media type that the stream supports. To test whether a particular media type is supported, call [**IMFMediaTypeHandler::IsMediaTypeSupported**](/windows/win32/mfidl/nf-mfidl-imfmediatypehandler-ismediatypesupported?branch=master). To set the media type, call [**IMFMediaTypeHandler::SetCurrentMediaType**](/windows/win32/mfidl/nf-mfidl-imfmediatypehandler-setcurrentmediatype?branch=master). If the method succeeds, the stream will contain data that conforms to the specified format. The **SetCurrentMediaType** method does not change the list of preferred types.

The following code shows how to get the media type handler, enumerate the preferred media types, and set the media type. This example assumes that the application has some algorithm, not shown here, for selecting the media type. The specifics will depend greatly on your application.


```C++
HRESULT hr = S_OK;
DWORD cTypes = 0;
BOOL  bTypeOK = FALSE;

IMFMediaTypeHandler *pHandler = NULL;
IMFMediaType *pMediaType = NULL;

hr = pStreamDesc->GetMediaTypeHandler(&amp;pHandler);

if (SUCCEEDED(hr))
{
    hr = pHandler->GetMediaTypeCount(&amp;cTypes);
}

if (SUCCEEDED(hr))
{
    for (DWORD iType = 0; iType < cTypes; iType++)
    {   
        hr = pHandler->GetMediaTypeByIndex(iType, &amp;pMediaType);

        if (FAILED(hr))
        {
            break;
        }

        /* Examine the media type. (Not shown.)  */

        /* If this media type is acceptable, set the media type. */

        if (bTypeOK)
        {
            hr = pHandler->SetCurrentMediaType(pMediaType);
            break;
        }

        SAFE_RELEASE(pMediaType);
    }
}    

SAFE_RELEASE(pMediaType);
SAFE_RELEASE(pHandler);
```



## Related topics

<dl> <dt>

[Media Sources](media-sources.md)
</dt> <dt>

[Media Foundation Platform APIs](media-foundation-platform-apis.md)
</dt> </dl>

 

 



