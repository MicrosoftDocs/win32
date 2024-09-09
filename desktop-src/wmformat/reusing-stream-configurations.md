---
title: Reusing Stream Configurations
description: Reusing Stream Configurations
ms.assetid: e2263c3a-56cd-4505-acd7-510dc7bac166
keywords:
- streams,reusing configurations
- profiles,reusing stream configurations
- reusing stream configurations
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Reusing Stream Configurations

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

There are often times when you want to reuse a stream configuration object from an existing profile. You may have old profiles that need updating or you may need a stream identical to one in a system profile. It is easier to reuse stream configurations than to create new ones, and you can often change a few settings in a configuration to meet your needs rather than creating an entirely new one.

Be aware that there are limitations to how you can change stream configurations. If you change settings in the wrong way, your profile may not accept the stream configuration object. Incorrect stream configurations are frequently accepted by the profile but cause the writer object to reject the profile. Be aware of the following limitations and issues when using and modifying existing stream configurations.

-   Never alter the contents of a .prx file to change stream settings. When profiles are saved to XML strings and written to a .prx file they can be read with any text editor. Looking at a saved profile can help you understand how profiles work. However, you should never alter a .prx file in any way. Even seemingly trivial changes can invalidate the profile.
-   Several versions of the Windows Media Audio codec use the same stream configurations. If you have a stream configuration object that is configured as subtype WMMEDIASUBTYPE\_WMAudioV2, WMMEDIASUBTYPE\_WMAudioV7, or WMMEDIASUBTYPE\_WMAudioV8, the resulting stream will be compressed with the latest Windows Media Audio codec. However, you should evaluate your needs before using an existing audio codec. Many types of files can be improved by upgrading to the latest version of the Windows Media Audio Professional codec, or the Windows Media Audio Lossless codec.
-   Never change the subtype of a stream to upgrade to a new codec. When you use the methods of [**IWMCodecInfo3**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmcodecinfo3) to obtain a stream configuration, the codec attaches some data to it that identifies the bit stream format. If you change the subtype of an existing stream configuration object, the subtype will not match the codec data. A profile with such a stream configuration will not be accepted by the writer object.
-   Do not alter the settings of compressed audio stream configurations. If the settings of an audio stream do not suit your needs, obtain a new stream configuration from the codec using the methods of **IWMCodecInfo3**.

## Related topics

<dl> <dt>

[**Configuring Streams**](configuring-streams.md)
</dt> <dt>

[**Getting Stream Configuration Information from Codecs**](getting-stream-configuration-information-from-codecs.md)
</dt> </dl>

 

 




