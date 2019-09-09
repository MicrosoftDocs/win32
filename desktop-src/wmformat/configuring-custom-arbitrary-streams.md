---
title: Configuring Custom Arbitrary Streams
description: Configuring Custom Arbitrary Streams
ms.assetid: 09b28fd3-a0a3-44d9-b664-7421290abf02
keywords:
- streams,configuring custom arbitrary streams
- codecs,configuring custom arbitrary streams
ms.topic: article
ms.date: 05/31/2018
---

# Configuring Custom Arbitrary Streams

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

 

 




