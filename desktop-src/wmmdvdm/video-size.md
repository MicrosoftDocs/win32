---
title: VIDEO\_SIZE structure
description: The VIDEO\_SIZE structure describes the dimensions of a video frame, in pixels.
ms.assetid: '2f0dcf74-877d-43d5-8795-00ef67a4d724'
keywords: ["VIDEO_SIZE structure Windows Movie Maker and DVD Maker"]
topic_type:
- apiref
api_name:
- VIDEO_SIZE
api_location:
- GPUPipelineTime.h
api_type:
- HeaderDef
---

# VIDEO\_SIZE structure

The **VIDEO\_SIZE** structure describes the dimensions of a video frame, in pixels.

## Syntax


```C++
typedef struct stcVIDEO_SIZE {
  SIZE szVideoSize;
  SIZE szDisplaySize;
} VIDEO_SIZE;
```



## Members

<dl> <dt>

**szVideoSize**
</dt> <dd>

A Windows Graphics Device Interface (GDI) structure that specifies the width and height of the original video.

</dd> <dt>

**szDisplaySize**
</dt> <dd>

A Windows GDI structure that specifies the width and height of the video as displayed.

</dd> </dl>

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                         |
| Header<br/>                   | <dl> <dt>GPUPipelineTime.h</dt> </dl> |



## See also

<dl> <dt>

[**Structures**](structures.md)
</dt> </dl>

 

 





