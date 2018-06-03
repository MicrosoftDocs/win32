---
title: TIME\_INFO structure
description: The TIME\_INFO structure describes the current sample time.
ms.assetid: a5cc02dc-a894-4f7f-af16-dce82efd682a
keywords:
- TIME_INFO structure Windows Movie Maker and DVD Maker
topic_type:
- apiref
api_name:
- TIME_INFO
api_location:
- GPUPipelineTime.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# TIME\_INFO structure

The **TIME\_INFO** structure describes the current sample time.

## Syntax


```C++
typedef struct stcTIME_INFO {
  PIPELINE_TIME segmentTime;
  PIPELINE_TIME estimatedNextSegmentTime;
  PIPELINE_TIME timelineTime;
} TIME_INFO;
```



## Members

<dl> <dt>

**segmentTime**
</dt> <dd>

The location of the frame relative to the start time of the effect or transition, given in 1/10,000-second units.

</dd> <dt>

**estimatedNextSegmentTime**
</dt> <dd>

A guess at how long before Windows Movie Maker will call [**IMediaTransform::Process**](imediatransform-process.md) again, in 1/10,000-second units.

</dd> <dt>

**timelineTime**
</dt> <dd>

The location of the frame relative to the start time of the movie, in 1/10,000-second units.

</dd> </dl>

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                         |
| Header<br/>                   | <dl> <dt>GPUPipelineTime.h</dt> </dl> |



## See also

<dl> <dt>

[**Structures**](structures.md)
</dt> </dl>

 

 





