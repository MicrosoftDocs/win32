---
description: D3DXSHPRTSPLITMESHCLUSTERDATA structure
ms.assetid: 6a53420c-06bc-4f52-ac2e-5adda5e34cb2
title: D3DXSHPRTSPLITMESHCLUSTERDATA structure (D3dx9mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXSHPRTSPLITMESHCLUSTERDATA
api_type: 
- HeaderDef
api_location: 
- d3dx9mesh.h
---

# D3DXSHPRTSPLITMESHCLUSTERDATA structure

## Syntax


```C++
typedef struct D3DXSHPRTSPLITMESHCLUSTERDATA {
  UINT uVertStart;
  UINT uVertLength;
  UINT uFaceStart;
  UINT uFaceLength;
  UINT uClusterStart;
  UINT uClusterLength;
} D3DXSHPRTSPLITMESHCLUSTERDATA, *LPD3DXSHPRTSPLITMESHCLUSTERDATA;
```



## Members

<dl> <dt>

**uVertStart**
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

</dd> <dd>

Initial vertex into remapped vertex array.

</dd> <dt>

**uVertLength**
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

</dd> <dd>

Number of vertices in this supercluster.

</dd> <dt>

**uFaceStart**
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

</dd> <dd>

Initial index into face array.

</dd> <dt>

**uFaceLength**
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

</dd> <dd>

Number of faces in this supercluster.

</dd> <dt>

**uClusterStart**
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

</dd> <dd>

Initial index into cluster array.

</dd> <dt>

**uClusterLength**
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

</dd> <dd>

Number of clusters in this supercluster array.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx9mesh.h</dt> </dl> |



## See also

<dl> <dt>

[D3DX Structures](dx9-graphics-reference-d3dx-structures.md)
</dt> <dt>

[**D3DXSHPRTCompSplitMeshSC**](d3dxshprtcompsplitmeshsc.md)
</dt> </dl>

 

 
