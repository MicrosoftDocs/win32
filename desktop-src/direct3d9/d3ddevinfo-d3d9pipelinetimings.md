---
Description: Percent of time processing data in the pipeline.
ms.assetid: eb9dec27-2e45-4897-92af-8415c8fa08d4
title: D3DDEVINFO\_D3D9PIPELINETIMINGS structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
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

Type: **[**FLOAT**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

</dd> <dd>

Percent of time spent running vertex shaders.

</dd> <dt>

**PixelProcessingTimePercent**
</dt> <dd>

Type: **[**FLOAT**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

</dd> <dd>

Percent of time spent running pixel shaders.

</dd> <dt>

**OtherGPUProcessingTimePercent**
</dt> <dd>

Type: **[**FLOAT**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

</dd> <dd>

Percent of time spent doing other processing.

</dd> <dt>

**GPUIdleTimePercent**
</dt> <dd>

Type: **[**FLOAT**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

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

[**GetData**](/windows/desktop/api/d3d9helper/nf-d3d9-idirect3dquery9-getdata)
</dt> </dl>

 

 




