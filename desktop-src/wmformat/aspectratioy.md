---
title: AspectRatioY
description: The AspectRatioY attribute contains the height component of the pixel aspect ratio for a video stream.
ms.assetid: e5b043d7-8fae-45d0-b140-a34d9bc6d2d8
keywords:
- AspectRatioY windows Media Format
topic_type:
- apiref
api_name:
- AspectRatioY
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# AspectRatioY

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **AspectRatioY** attribute contains the height component of the pixel aspect ratio for a video stream.

## Global Constant

g\_wszWMAspectRatioY

## Data Type

**WMT\_TYPE\_DWORD**

## Remarks

When accessing the **IWMHeaderInfo3** interface of the writer object, you can add or change this value. In other objects (metadata editor, reader, and synchronous reader), this value is read-only.

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> <dt>

[**To Read and Write Video Streams with Non-Square Pixels**](to-read-and-write-video-streams-with-non-square-pixels.md)
</dt> </dl>

 

 




