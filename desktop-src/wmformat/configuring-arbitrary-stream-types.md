---
title: Configuring Arbitrary Stream Types
description: Configuring Arbitrary Stream Types
ms.assetid: d745ec4b-9ce5-4288-bc24-0c1220c4d510
keywords:
- streams,configuring arbitrary stream types
- codecs,configuring arbitrary stream types
- streams,GenProfile
- codecs,GenProfile
- GenProfile
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Configuring Arbitrary Stream Types

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Most arbitrary stream types just need a bit rate, a buffer window, and a proper major media type in the [**WM\_MEDIA\_TYPE**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-wm_media_type) structure. However, some arbitrary types require additional configuration.

If you have trouble configuring a stream, refer to the sample application called GenProfile, which is included with this SDK. The library defined in GenProfile contains code for including all types of streams. For more information about GenProfile and the other samples, see [Sample Applications](sample-applications.md).

The following sections describe how to configure arbitrary stream types.



| Section                                                                                                                                        | Description                                                                                 |
|------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| [Configuring Script Streams](configuring-script-streams.md)                                                                                   | Describes how to configure script streams.                                                  |
| [Configuring File Transfer Streams](configuring-file-transfer-streams.md)                                                                     | Describes how to configure file transfer streams.                                           |
| [Configuring Web Streams](configuring-web-streams.md)                                                                                         | Describes how to configure Web streams.                                                     |
| [Configuring Text Streams](configuring-text-streams.md)                                                                                       | Describes how to configure text streams.                                                    |
| [Configuring Custom Arbitrary Streams](configuring-custom-arbitrary-streams.md)                                                               | Describes how to configure streams for custom arbitrary stream types.                       |
| [Calculating Bit Rate and Buffer Window Values for Arbitrary Streams](calculating-bit-rate-and-buffer-window-values-for-arbitrary-streams.md) | Describes how to calculate the bit rate and buffer window settings for an arbitrary stream. |



 

## Related topics

<dl> <dt>

[**Arbitrary Streams**](arbitrary-streams.md)
</dt> <dt>

[**Configuring Streams**](configuring-streams.md)
</dt> </dl>

 

 




