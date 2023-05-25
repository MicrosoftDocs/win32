---
title: Configuring the WM ASF Writer (QASF)
description: Configuring the WM ASF Writer (QASF)
ms.assetid: 0f49ed5a-c228-456a-9551-8d277adccd0e
keywords:
- Windows Media Format SDK,configuring WM ASF Writer (QASF)
- Windows Media Format SDK,DirectShow
- Windows Media Format SDK,WM ASF Writer
- Windows Media Format SDK,QASF
- Advanced Systems Format (ASF),configuring WM ASF Writer (QASF)
- ASF (Advanced Systems Format),configuring WM ASF Writer (QASF)
- Advanced Systems Format (ASF),WM ASF Writer
- ASF (Advanced Systems Format),WM ASF Writer
- Advanced Systems Format (ASF),DirectShow
- ASF (Advanced Systems Format),DirectShow
- Advanced Systems Format (ASF),QASF
- ASF (Advanced Systems Format),QASF
- DirectShow,configuring WM ASF Writer (QASF)
- DirectShow,WM ASF Writer
- DirectShow,QASF
- WM ASF Writer,configuring
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Configuring the WM ASF Writer (QASF)

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

When the [WM ASF Writer](wm-asf-writer-filter.md) filter is created, it is configured automatically with the WMProfile\_V80\_256Video profile as a default. Because this profile uses the Windows Media Audio and Windows Media Video version 8 codecs, it is recommended that you create a custom profile that uses the Windows Media 9 Series codecs, and then pass its [**IWMProfile**](iwmprofile.md) pointer to the filter using the [**IConfigAsfWriter::ConfigureFilterUsingProfile**](iconfigasfwriter-configurefilterusingprofile.md) method. The filter must be added to the graph before the filter can be configured, and it must be configured before it can be connected to upstream filters. The filter uses the profile to determine what kind of Windows Media Format file to write, how many input pins to set up, and what media types the pins can accept.

The filter allows profiles to be reset while its input pins are connected, as long as the new profile does not require any additional input pins. For example, if you change the profile from a one-input audio-only profile to a two-input audio and video profile, just the audio pin will be reconnectedAll input data must be time-stamped, and all input pins must be connected before the filter can be run or paused. This means that if you configure the filter with a profile that has an audio stream and a video stream, the filter will create an audio and a video input pin, and both pins must be connected before the filter can be run.

Adding Data Unit Extensions

You can configure a profile stream for data unit extensions, such as SMPTE time codes, either before or after the filter is connected, as long as you follow this order of operations:

1.  Add one or more data unit extensions to the stream using [**IWMStreamConfig2::AddDataUnitExtension**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmstreamconfig2-adddataunitextension).
2.  Call [**WMProfile::ReconfigStream**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofile-reconfigstream) to update the profile.
3.  Call [**IConfigAsfWriter::ConfigureFilterUsingProfile**](iconfigasfwriter-configurefilterusingprofile.md) with the updated profile object.
4.  Find the video input pin, and call its [**IAMWMBufferPass::SetNotify**](iamwmbufferpass-setnotify.md) method to register your application-defined [**IAMWMBufferPassCallback**](/previous-versions/windows/desktop/api/dshowasf/nn-dshowasf-iamwmbufferpasscallback) interface.

When the graph runs, your [**IAMWMBufferPassCallback::Notify**](iamwmbufferpasscallback-notify.md) method will be called for each frame, and you will be able to get and set properties on the sample using its [**INSSBuffer3**](/previous-versions/windows/desktop/api/wmsbuffer/nn-wmsbuffer-inssbuffer3) interface methods.

> [!Note]  
> In some processor-intensive scenarios such as inverse telecine, the WM ASF Writer may require more output buffers than some downstream filters can support. The DV Decoder, for example, will not accept more than one buffer for its output pin and the same is true for the AVI Decompressor in certain conditions. If you encounter problems when attempting to connect to these filters, or possibly when running the graph, it may be necessary to write an intermediary filter that accepts any number of buffers on its output pin.

 

 

 