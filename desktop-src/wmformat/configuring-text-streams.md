---
title: Configuring Text Streams
description: Configuring Text Streams
ms.assetid: d99baac5-69e5-4e0a-9cd6-35b288d8181a
keywords:
- streams,configuring text streams
- codecs,configuring text streams
- text streams,configuring
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Configuring Text Streams

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Text streams are essentially the same as custom arbitrary streams. There is no configuration information associated with a text stream to identify the type of text encoding, so the writer object cannot verify samples.

To configure a text stream, you must ensure that the [**WM\_MEDIA\_TYPE**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-wm_media_type) structure contains a major media type of WMMEDIATYPE\_TEXT. You must also set a bit rate and buffer window for the stream.

## Related topics

<dl> <dt>

[**Calculating Bit Rate and Buffer Window Values for Arbitrary Streams**](calculating-bit-rate-and-buffer-window-values-for-arbitrary-streams.md)
</dt> <dt>

[**Configuration Common to All Streams**](configuration-common-to-all-streams.md)
</dt> <dt>

[**Configuring Arbitrary Stream Types**](configuring-arbitrary-stream-types.md)
</dt> <dt>

[**Text Streams**](text-streams.md)
</dt> </dl>

 

 




