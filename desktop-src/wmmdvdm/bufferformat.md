---
title: BufferFormat structure
description: The BufferFormat structure describes the format of a buffer.
ms.assetid: 9d183063-d036-4be4-ab86-83a12666f634
keywords:
- BufferFormat structure Windows Movie Maker and DVD Maker
topic_type:
- apiref
api_name:
- BufferFormat
api_location:
- GPUPipelineTime.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# BufferFormat structure

The **BufferFormat** structure describes the format of a buffer.

## Syntax


```C++
typedef struct stcBufferFormat {
  FORMAT_TYPE   dwFlags;
  DWORD         dwInputPin;
  PIPELINE_TIME prerollTime;
  double        dblWidthRatio;
  double        dblHeightRatio;
} BufferFormat;
```



## Members

<dl> <dt>

**dwFlags**
</dt> <dd>

One or more values from the [**FORMAT\_TYPE**](format-type.md) enumeration, combined with a bitwise **OR**, that describe the format of the data in the buffer and how it should be treated.

</dd> <dt>

**dwInputPin**
</dt> <dd>

A **DWORD** that specifies the one-based input stream on the node.

</dd> <dt>

**prerollTime**
</dt> <dd>

A [PIPELINE\_TIME](pipeline-time.md) structure that specifies the preroll time. This value gives the transform extra time to initialize. Microsoft advises against specifying this value.

</dd> <dt>

**dblWidthRatio**
</dt> <dd>

A **double** that specifies the width ratio of video objects.

</dd> <dt>

**dblHeightRatio**
</dt> <dd>

A **double** that specifies the height ratio of video objects.

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

 

 





