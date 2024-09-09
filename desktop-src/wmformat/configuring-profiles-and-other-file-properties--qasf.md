---
title: Configuring Profiles and Other File Properties (QASF)
description: Configuring Profiles and Other File Properties (QASF)
ms.assetid: a462fc8b-5a2e-4c93-828d-177d1965b734
keywords:
- Windows Media Format SDK,configuring profiles (QASF)
- Windows Media Format SDK,configuring file properties (QASF)
- Windows Media Format SDK,metadata (QASF)
- Advanced Systems Format (ASF),configuring profiles (QASF)
- ASF (Advanced Systems Format),configuring profiles (QASF)
- Advanced Systems Format (ASF),configuring file properties (QASF)
- ASF (Advanced Systems Format),configuring file properties (QASF)
- Advanced Systems Format (ASF),metadata (QASF)
- ASF (Advanced Systems Format),metadata (QASF)
- Windows Media Format SDK,QASF
- Advanced Systems Format (ASF),QASF
- ASF (Advanced Systems Format),QASF
- metadata,QASF
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Configuring Profiles and Other File Properties (QASF)

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The following items describe how to perform various tasks related to the creation of ASF files.

## Creating a Profile (QASF)

To create a custom profile, use the Windows Media Format SDK directly to create a profile manager object by using the [**WMCreateProfileManager**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-wmcreateprofilemanager) function. Next, create the profile, and pass it to the [WM ASF Writer](wm-asf-writer-filter.md) by using the [**IConfigASFWriter::ConfigureFilterUsingProfile**](iconfigasfwriter-configurefilterusingprofile.md) method. This is the only way to configure the filter with a profile that uses the Windows Media Audio and Video 9 Series codecs. System profiles for earlier versions of these codecs can be added by using the [**IConfigASFWriter::ConfigureFilterUsingProfileGuid**](iconfigasfwriter-configurefilterusingprofileguid.md) method.

## Adding Metadata (QASF)

To add metadata to a file, call **QueryInterface** from the **IBaseFilter** interface on the [WM ASF Writer](wm-asf-writer-filter.md) to retrieve the [**IWMHeaderInfo**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmheaderinfo) interface. After the filter has been given a profile, use the **IWMHeaderInfo** interface methods to write the metadata.

## Indexing a File (QASF)

The WM ASF Writer creates temporally indexed files by default. To create a frame-indexed file, use the [**IConfigAsfWriter::SetIndexMode**](iconfigasfwriter-setindexmode.md) method to disable all indexing, then create the file. When it is complete, use the Windows Media Format SDK directly to create a frame-based index for the file.

## Performing Two-Pass Encoding (QASF)

Two-pass encoding is supported only on Windows Media codecs of version 8 and later. Put the WM ASF Writer into preprocess mode by calling [**IConfigAsfWriter2::SetParam**](iconfigasfwriter2-setparam.md) and specifying AM\_CONFIGASFWRITER\_PARAM\_MULTIPASS in the *dwParam* parameter and **TRUE** in the *dwParam1* parameter.

Then run the filter graph. When all the preprocessing passes are done (typically only one preprocessing pass will be performed), the application will receive an **EC\_PREPROCESS\_COMPLETE** event from the filter. When this event is received, use **IMediaSeeking::SetPositions** to reset the stream pointer back to the beginning, and run the filter graph again. After the last pass (typically the second pass), the application will receive an **EC\_COMPLETE** event to signify that the encoding process is complete. If a preprocessing pass is canceled before the **EC\_PREPROCESS\_COMPLETE** event is received, call [**IConfigAsfWriter2::ResetMultiPassState**](iconfigasfwriter2-resetmultipassstate.md) to reset the filter before attempting another preprocessing run.

It is only necessary to call **IConfigAsfWriter::SetParam**(AM\_CONFIGASFWRITER\_PARAM\_MULTIPASS, **FALSE**) if you want to put the filter out of preprocessing mode completely.

> [!IMPORTANT]
> It is the application's responsibility to enable preprocessing mode based on the profile that will be used for encoding. Some profiles require two-pass encoding; if you attempt to encode a file with such a profile, and do not set AM\_CONFIGASFWRITER\_PARAM\_MULTIPASS to **TRUE**, an EC\_USERABORT error will result. For more information on how to determine whether a given profile requires two-pass encoding, see [Using Two-Pass Encoding](using-two-pass-encoding.md) or [Writing Variable Bit Rate Streams](writing-variable-bit-rate-streams.md).

 

## Getting and Setting Buffer Properties at Run Time (QASF)

In some scenarios, for example if you want to force key-frame insertion when writing a file, an application may need to get or set information about a Windows Media buffer at run time. The [WM ASF Reader](wm-asf-reader-filter.md) and [WM ASF Writer](wm-asf-writer-filter.md) filters both support a callback mechanism that enables an application to access the [**INSSBuffer3**](/previous-versions/windows/desktop/api/wmsbuffer/nn-wmsbuffer-inssbuffer3) interface on each individual media buffer during file reading or file writing. Applications can use this interface to designate specific samples as key frames, or [*cleanpoints*](wmformat-glossary.md), to set SMPTE time codes, to specify interlace settings, or add any type of private data to a stream.

Use the [**IAMWMBufferPass**](/previous-versions/windows/desktop/api/dshowasf/nn-dshowasf-iamwmbufferpass) interface to register for callbacks from the pin that is handling the video stream. When the pin calls your [**IAMWMBufferPassCallback::Notify**](iamwmbufferpasscallback-notify.md) method, examine the time stamps on the buffer and, if appropriate, call [**INSSBuffer3::SetProperty**](/previous-versions/windows/desktop/api/Wmsbuffer/nf-wmsbuffer-inssbuffer3-setproperty) to set the **WM\_SampleExtensionGUID\_OutputCleanPoint** property on the buffer to **TRUE**.

## Non-Square Pixel Support (QASF)

The WM ASF Writer connects to an upstream filter, such as the DV Decoder, that outputs pixel aspect ratio information. The WM ASF Writer will write this information as data unit extensions for every sample in the file.

When the WM ASF Reader encounters pixel aspect ratio information in the file header or in data unit extensions for the samples, it will offer a **VIDEOINFOHEADER2** media type as a first choice on its output pin. The **dwPictAspectRatioX** and **dwPictAspectRatioY** members of the structure, which describe the video rectangle's aspect ratio, will be correctly adjusted to account for the pixel aspect ratio.

## Maintaining Interlaced Format

If you capture interlaced video from a television or a DV camera, you might wish to preserve the original video as independent fields if you expect the encoded file to be played back on a television or other interlaced display device. (Computer monitors are progressive scanning devices.) If you deinterlace a video, and then reinterlace it for playback on a television, some loss of data will be incurred. In an ASF file, interlacing information is stored as data unit extensions that the application applies to each sample using the **IAMWMBufferPassCallback** method described previously. To encode a file that preserves the original interlace settings, follow these steps:

-   Implement a class that supports **IAMWMBufferPassCallback** and write a Notify function that sets the interlace flags for each sample. This function will be called by the WM ASF Writer before it processes each sample.


```C++
// Set to WM_CT_TOP_FIELD_FIRST if that is your format.
BYTE flag = WM_CT_INTERLACED | WM_CT_BOTTOM_FIELD_FIRST;
            HRESULT hr = pNSSBuffer3->SetProperty(WM_SampleExtensionGUID_ContentType, (void*) &flag, WM_SampleExtension_ContentType_Size);
           
```



-   Set the data unit extensions on the profile before you pass the profile to the filter.


```C++
hr = pWMStreamConfig2->AddDataUnitExtension( WM_SampleExtensionGUID_ContentType, WM_SampleExtension_ContentType_Size, NULL, 0 );
```



-   After you configure the filter with the profile, obtain the **IWMWriterAdvanced2** interface from the WM ASF Writer and call the **SetInputSettings** method.

`// Must do this first.`

`hr = pConfigAsfWriter2->ConfigureFilterUsingProfile(pProfile);`


```C++
  
CComPtr<IServiceProvider> pProvider;
  CComPtr<IWMWriterAdvanced2> pWMWA2;
  hr = pConfigAsfWriter2->QueryInterface( __uuidof(IServiceProvider),
                                         (void**)&pProvider);
  if (SUCCEEDED(hr))
  {
      hr = pProvider->QueryService(IID_IWMWriterAdvanced2,
                    IID_IWMWriterAdvanced2,
                    (void**)&pWMWA2);
  }
  BOOL pValue = TRUE;
 // Set the first parameter to your actual input number.
 hr = pWMWA2->SetInputSetting(0, g_wszInterlacedCoding,
              WMT_TYPE_BOOL, (BYTE*) &pValue, sizeof(WMT_TYPE_BOOL));
            
```



 

 