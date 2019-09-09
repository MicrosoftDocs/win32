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
ms.date: 05/31/2018
---

# Configuring Arbitrary Stream Types

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

 

 




