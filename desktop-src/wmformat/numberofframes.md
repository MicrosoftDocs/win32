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
ms.date: 05/31/2018
---

# NumberOfFrames

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

 

 




