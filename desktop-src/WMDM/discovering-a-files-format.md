---
title: Discovering a File's Format
description: Discovering a File's Format
ms.assetid: f1b3f811-8161-41ca-a92c-2735c0bec2e8
keywords:
- Windows Media Device Manager,file formats
- Device Manager,file formats
- programming guide,file formats
- desktop applications,file formats
- creating Windows Media Device Manager applications,file formats
- writing files to devices,file formats
ms.topic: article
ms.date: 05/31/2018
---

# Discovering a File's Format

Before sending a file to the device, an application should determine whether the device supports that file format.

Discovering the format of a file can be complex. The simplest way is to create a list of file extensions mapped to specific WMDM\_FORMATCODE enumeration values. However, there are a few problems with this system: one is that a single format can have multiple extensions (such as .jpg, .jpe, and .jpeg for JPEG images). Also, the same file extension can be used by different programs for different formats.

To overcome the limitations of a strict mapping, it is best for an application to verify that the format matches the extension. The DirectShow SDK provides tools that enable an application to discover a limited set of details about most media file types. The Windows Media Format SDK exposes a large number of details, but only about ASF files. Because all file types should have their format code verified if possible, it is therefore best to use DirectShow to discover or verify the basic format code, and use the Windows Media Format SDK to discover any additional metadata desired about ASF files. DirectShow can also be used to discover basic metadata for non-ASF files.

The following is one way to discover a file format using extension mapping and DirectShow.

First, compare the file name extension to a list of known extensions. Be sure to make your comparison case-insensitive. If the extension is not mapped, set the format to WMDM\_FORMATCODE\_UNDEFINED.

-   If the format code was not found (or you want to verify that a file is a media file), you can perform the following steps:
    1.  Create a DirectShow Media Detector object using **CoCreateInstance**(CLSID\_MediaDet), and retrieving the **IMediaDet** interface.
    2.  Open the file by calling **IMediaDet::put\_Filename**. This call will fail if the file is protected.
    3.  Get the media type of the default stream by calling **IMediaDet::get\_StreamMediaType**, which returns an **AM\_MEDIA\_TYPE**.
    4.  Get the number of streams by calling **IMediaDet::get\_OutputStreams**.
        -   If there is only one stream and it is audio, the file type is WMDM\_FORMATCODE\_UNDEFINEDAUDIO
        -   If there is only one stream and it is video, the file type is WMDM\_FORMATCODE\_UNDEFINEDVIDEO
        -   If there is only one stream and it is video and the bit rate is zero, the file type is WMDM\_FORMATCODE\_WINDOWSIMAGEFORMAT.

You could also try matching audio or video codecs from the **VIDEOINFOHEADER** or **WAVEFORMATEX** members retrieved from **get\_StreamMediaType**.

The following C++ function demonstrates file extension matching and using DirectShow to try to analyze unknown files.


```C++
// For IMediaDet, you must link to strmiids.lib. Also include the following:
//#include <Qedit.h>  // for IMediaDet declaration.
//#include <Dshow.h>  // for VIDEOINFOHEADER declaration.
WMDM_FORMATCODE CWMDMController::myGetWMDM_FORMATCODE(LPCWSTR pFileName)
{
    HRESULT hr = S_OK;

    // Declare the variable to hold the WMDM format code.
    WMDM_FORMATCODE fmt = WMDM_FORMATCODE_UNDEFINED;
    
    // Get the file extension.
    wstring ext = pFileName;
    ext = ext.substr(ext.find_last_of(L".") + 1);

    // This is not an exhaustive list. 
    // It is also case-sensitive.
    if (ext == L"js" || ext == L"vb")
        fmt = WMDM_FORMATCODE_SCRIPT;
    else if (ext == L".exe")
        fmt = WMDM_FORMATCODE_EXECUTABLE;
    else if (ext == L"txt")
        fmt = WMDM_FORMATCODE_TEXT;
    else if (ext == L"html" || ext == L"htm" || ext == L"shtm")
        fmt = WMDM_FORMATCODE_HTML;
    else if (ext == L"aiff")
        fmt = WMDM_FORMATCODE_AIFF;
    else if (ext == L"wav")
        fmt = WMDM_FORMATCODE_WAVE;
    else if (ext == L"mp3")
        fmt = WMDM_FORMATCODE_MP3;
    else if (ext == L"mpg" || ext == L"mpeg" || ext == L"mp2")
        fmt = WMDM_FORMATCODE_MPEG;
    else if (ext == L"bmp")
        fmt = WMDM_FORMATCODE_IMAGE_BMP;
    else if (ext == L"avi")
        fmt = WMDM_FORMATCODE_AVI;
    else if (ext == L"asf")
        fmt = WMDM_FORMATCODE_ASF;
    else if (ext == L"tif")
        fmt = WMDM_FORMATCODE_IMAGE_TIFF;
    else if (ext == L"gif")
        fmt = WMDM_FORMATCODE_IMAGE_GIF;
    else if (ext == L"pct")
        fmt = WMDM_FORMATCODE_IMAGE_PICT;
    else if (ext == L"png")
        fmt = WMDM_FORMATCODE_IMAGE_PNG;
    else if (ext == L"wma")
        fmt = WMDM_FORMATCODE_WMA;
    else if (ext == L"wpl")
        fmt = WMDM_FORMATCODE_WPLPLAYLIST;
    else if (ext == L"asx")
        fmt = WMDM_FORMATCODE_ASXPLAYLIST;
    else if (ext == L"m3u")
        fmt = WMDM_FORMATCODE_M3UPLAYLIST;
    else if (ext == L"wmv")
        fmt = WMDM_FORMATCODE_WMV;
    else if (ext == L"jpg" || ext == L"jpeg" || ext == L"jpe")
        fmt = WMDM_FORMATCODE_IMAGE_EXIF;
    else if (ext == L"jp2")
        fmt = WMDM_FORMATCODE_IMAGE_JP2;
    else if (ext == L"jpx" || ext == L"jpf")
        fmt = WMDM_FORMATCODE_IMAGE_JPX;

    // If we couldn't get the type from the extension, perhaps DirectShow 
    // can determine the type. You could also modify this to verify that 
    // the major media type matches the file extension (for example, that 
    // a .gif file has a video image stream with a bit rate of zero).
    if (fmt == WMDM_FORMATCODE_UNDEFINED)
    {
        CComPtr<IMediaDet> pIMediaDet;
        hr = pIMediaDet.CoCreateInstance(CLSID_MediaDet, NULL);
        if (hr == S_OK && pIMediaDet != NULL)
        {
            hr = pIMediaDet->put_Filename(BSTR(pFileName));
            if (FAILED(hr)) return WMDM_FORMATCODE_UNDEFINED;

            AM_MEDIA_TYPE mediaType;
            if (hr == S_OK)
            {
                hr = pIMediaDet->get_StreamMediaType(&mediaType);
                CHECK_HR(hr, 
                  "get_StreamMediaType succeeded in myGetWMDM_FORMATCODE.", 
                  "get_StreamMediaType failed in myGetWMDM_FORMATCODE.");
            }

            if (hr == S_OK)
            {
                LONG numStreams = 0;
                hr = pIMediaDet->get_OutputStreams(&numStreams);

                // If there is at least one video stream, the file is video. 
                // If there are only audio streams, it is audio.
                // Loop through all streams or until first video stream is found.
                for (int i = 0; i < numStreams; i++)
                {
                    // Choices are either VIDEOINFOHEADER or WAVEFORMATEX. 
                    // VIDEOINFOHEADER2 is not supported.
                    if (IsEqualGUID(mediaType.formattype, 
                        FORMAT_VideoInfo))
                    {
                        VIDEOINFOHEADER* data = 
                            (VIDEOINFOHEADER*) mediaType.pbFormat;

                        // If only one stream and there was no matching 
                        // extension, it is undefined video. If no 
                        // bit rate, it's a still image.
                        if (data->dwBitRate == 0) fmt = 
                            WMDM_FORMATCODE_WINDOWSIMAGEFORMAT;
                        else fmt = WMDM_FORMATCODE_UNDEFINEDVIDEO;
                        break; // Found video--any additional streams are soundtracks.
                    }
                    if (IsEqualGUID(mediaType.formattype, FORMAT_WaveFormatEx))
                    {
                        // If only one stream and there was no matching 
                        // extension, it is undefined audio. 
                        if (fmt == WMDM_FORMATCODE_UNDEFINED)
                        {
                            fmt = WMDM_FORMATCODE_UNDEFINEDAUDIO;
                        }
                        WAVEFORMATEX* data = 
                            (WAVEFORMATEX*) mediaType.pbFormat;
                    }
                } // Loop through streams.
            }     // Got a stream media type.
        }         // Created a media detector object.
    }
    return fmt;
}
```



## Related topics

<dl> <dt>

[**Writing Files to the Device**](writing-files-to-the-device.md)
</dt> </dl>

 

 




