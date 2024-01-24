---
title: Configuring Custom Arbitrary Streams
description: Configuring Custom Arbitrary Streams
ms.assetid: 09b28fd3-a0a3-44d9-b664-7421290abf02
keywords:
- streams,configuring custom arbitrary streams
- codecs,configuring custom arbitrary streams
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Configuring Custom Arbitrary Streams

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

When using your own arbitrary data type, you must create a GUID value to serve as the major media type identifier for it. When the writer encounters a stream in a profile with a major type it does not recognize, it assumes that the stream is custom arbitrary data. It will accept your samples, packetize them, and combine them with samples from the other streams in the file without verifying the data in any way.

You can also create your own subtype GUID identifiers to define subcategories of your custom data. The writer will ignore these subtypes completely, but they will be preserved in the header section of the ASF file, so your reading application can retrieve them and make decisions based on them.

An arbitrary stream requires a bit rate and buffer window, and must have a [**WM\_MEDIA\_TYPE**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-wm_media_type) structure with the values cleared except for the major media type and subtype(if using one).

## Related topics

<dl> <dt>

[**Configuration Common to All Streams**](configuration-common-to-all-streams.md)
</dt> <dt>

[**Configuring Arbitrary Stream Types**](configuring-arbitrary-stream-types.md)
</dt> <dt>

[**Custom Arbitrary Data Streams**](custom-arbitrary-data-streams.md)
</dt> </dl>

 

 




