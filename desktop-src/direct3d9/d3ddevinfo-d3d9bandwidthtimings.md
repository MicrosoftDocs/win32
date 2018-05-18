---
Description: 'Throughput metrics for help in understanding the performance of an application.'
ms.assetid: 'c0bcf060-a0ed-4c85-9554-398ffe4b4235'
title: 'D3DDEVINFO\_D3D9BANDWIDTHTIMINGS structure'
---

# D3DDEVINFO\_D3D9BANDWIDTHTIMINGS structure

Throughput metrics for help in understanding the performance of an application.

## Syntax


```C++
typedef struct D3DDEVINFO_D3D9BANDWIDTHTIMINGS {
  FLOAT MaxBandwidthUtilized;
  FLOAT FrontEndUploadMemoryUtilizedPercent;
  FLOAT VertexRateUtilizedPercent;
  FLOAT TriangleSetupRateUtilizedPercent;
  FLOAT FillRateUtilizedPercent;
} D3DDEVINFO_D3D9BANDWIDTHTIMINGS, *LPD3DDEVINFO_D3D9BANDWIDTHTIMINGS;
```



## Members

<dl> <dt>

**MaxBandwidthUtilized**
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)**

</dd> <dd>

The bandwidth or maximum data transfer rate from the host CPU to the GPU. This is typically the bandwidth of the PCI or AGP bus which connects the CPU and the GPU.

</dd> <dt>

**FrontEndUploadMemoryUtilizedPercent**
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)**

</dd> <dd>

Memory utilized percentage when uploading data from the host CPU to the GPU.

</dd> <dt>

**VertexRateUtilizedPercent**
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)**

</dd> <dd>

Vertex throughput percentage. This is the number of vertices processed compared to the theoretical maximum vertex processing rate.

</dd> <dt>

**TriangleSetupRateUtilizedPercent**
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)**

</dd> <dd>

Triangle set-up throughput percentage. This is the number of triangles that are set up for rasterization compared to the theoretical maximum triangle set-up rate.

</dd> <dt>

**FillRateUtilizedPercent**
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)**

</dd> <dd>

Pixel fill throughput percentage. This is the number of pixels that are filled compared to the theoretical pixel fill.

</dd> </dl>

## Requirements



|                   |                                                                                        |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3D9Types.h</dt> </dl> |



## See also

<dl> <dt>

[Direct3D Structures](dx9-graphics-reference-d3d-structures.md)
</dt> <dt>

[**GetData**](idirect3dquery9--getdata.md)
</dt> </dl>

 

 




