---
Description: Percent of time processing data in the pipeline.
ms.assetid: eb9dec27-2e45-4897-92af-8415c8fa08d4
title: D3DDEVINFO_D3D9PIPELINETIMINGS structure
ms.topic: structure
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DDEVINFO_D3D9PIPELINETIMINGS
api_type:
- HeaderDef
api_location:
- D3D9Types.h
---

# D3DDEVINFO\_D3D9PIPELINETIMINGS structure

Percent of time processing data in the pipeline.

## Syntax


```C++
typedef struct D3DDEVINFO_D3D9PIPELINETIMINGS {
  FLOAT VertexProcessingTimePercent;
  FLOAT PixelProcessingTimePercent;
  FLOAT OtherGPUProcessingTimePercent;
  FLOAT GPUIdleTimePercent;
} D3DDEVINFO_D3D9PIPELINETIMINGS, *LPD3DDEVINFO_D3D9PIPELINETIMINGS;
```



## Members

<dl> <dt>

**VertexProcessingTimePercent**
</dt> <dd>

Type: **[**FLOAT**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

</dd> <dd>

Percent of time spent running vertex shaders.

</dd> <dt>

**PixelProcessingTimePercent**
</dt> <dd>

Type: **[**FLOAT**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

</dd> <dd>

Percent of time spent running pixel shaders.

</dd> <dt>

**OtherGPUProcessingTimePercent**
</dt> <dd>

Type: **[**FLOAT**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

</dd> <dd>

Percent of time spent doing other processing.

</dd> <dt>

**GPUIdleTimePercent**
</dt> <dd>

Type: **[**FLOAT**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

</dd> <dd>

Percent of time not processing anything.

</dd> </dl>

## Remarks

For best performance, a balanced load is recommended.

## Requirements



|                   |                                                                                        |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3D9Types.h</dt> </dl> |



## See also

<dl> <dt>

[Direct3D Structures](dx9-graphics-reference-d3d-structures.md)
</dt> <dt>

[**GetData**](https://msdn.microsoft.com/library/Bb205873(v=VS.85).aspx)
</dt> </dl>

 

 




