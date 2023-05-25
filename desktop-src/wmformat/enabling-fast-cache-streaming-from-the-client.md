---
title: Enabling Fast Cache Streaming from the Client
description: Enabling Fast Cache Streaming from the Client
ms.assetid: 2a850d6f-8e1d-4aeb-9791-c51c3debf118
keywords:
- Windows Media Format SDK,enabling Fast Cache streaming
- Windows Media Format SDK,Fast Cache streaming
- Advanced Systems Format (ASF),enabling Fast Cache streaming
- ASF (Advanced Systems Format),enabling Fast Cache streaming
- Advanced Systems Format (ASF),Fast Cache streaming
- ASF (Advanced Systems Format),Fast Cache streaming
- streams,enabling Fast Cache streaming
- Fast Cache streaming,enabling
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Enabling Fast Cache Streaming from the Client

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Fast Cache is a streaming technology in which the server opportunistically streams content at a higher bit rate than what is needed for playback.

If the available bandwidth is higher than the bit rate of the content, Fast Cache streams at the higher rate and buffers the content. This helps to reduce interruptions later if the network becomes congested. If network bandwidth is lower than the bit rate of the content, Fast Cache buffers a portion of the data before playback starts. Fast Cache is recommended for unreliable networks, such as wireless networks, or networks that experience large fluctuations in network traffic, such as cable modems. It is also recommended for variable bit rate (VBR) content. The bandwidth requirements for VBR content are not constant, and Fast Cache enables the reader to buffer the stream during the lower-bit-rate portions.

Fast Cache streaming is supported only for on-demand content. In addition, the server must be configured to use Fast Cache streaming.

To enable Fast Cache in the reader object, call the [**IWMReaderNetworkConfig2::SetEnableContentCaching**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreadernetworkconfig2-setenablecontentcaching) and [**IWMReaderNetworkConfig2::SetEnableFastCache**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreadernetworkconfig2-setenablefastcache) methods with the value **TRUE**. The first method enables the reader to cache streamed content. The second enables the use of Fast Cache in particular.

With these settings, the reader will activate Fast Cache by default if the network bandwidth is significantly higher or lower than the bit rate of the content, and if the server supports it. The user can also control whether the reader object uses Fast Cache by adding one or more of the following modifiers to the URL.



| Modifier         | Description                                                                                                                                                                                                                                                                                                                                      |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WMCache          | If this modifier is present, the value '0' explicitly disables Fast Cache, while the value '1' explicitly enables it.                                                                                                                                                                                                                            |
| WMBitrate        | This modifier specifies the maximum bit rate from the server. This modifier can be used to restrict Fast Cache to a certain bandwidth limit. This modifier is ignored if an explicit connection bandwidth is already set with a call to [**IWMReaderNetworkConfig::SetConnectionBandwidth**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreadernetworkconfig-setconnectionbandwidth). |
| WMContentBitrate | This modifier specifies the bit rate for the content. The reader uses this modifier, if present, when it selects streams from a multiple bit rate (MBR) file. This can cause the reader to receive high bit rate content over a slow connection, which results in very long buffering times and delays.                                          |



 

The modifier WMCache=1 forces the reader to use Fast Cache streaming, regardless of the network bandwith or the bit rate of the content and regardless of any previous calls to **SetEnableFastCache**. However, it does not override the **SetEnableContentCaching** setting on the reader; nor does it override the server configuration.

URL modifiers have the following form:

*url*?*modifier*=*value*

For example:

mms://MyServer/MyVideo.wmv?WMCache=1

More than one modifier can specified; use an ampersand (&) to separate them:

mms://MyServer/MyVideo.wmv?WMCache=1&WMContentBitrate=56000

 

 




