---
title: NumberOfFrames
description: The NumberOfFrames attribute contains the number of frames in a video stream.
ms.assetid: 86bd2b2b-e3f7-4a0f-9681-974ce451d6f7
keywords:
- NumberOfFrames windows Media Format
topic_type:
- apiref
api_name:
- NumberOfFrames
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# NumberOfFrames

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **NumberOfFrames** attribute contains the number of frames in a video stream.

## Global Constant

g\_wszWMNumberOfFrames

## Data Type

**WMT\_TYPE\_QWORD**

## Remarks

The writer adds this value for a video stream at the time of encoding. **NumberOfFrames** is not read-only. However, you should only change the value if you edit the file, changing the number of frames in a video stream.

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




