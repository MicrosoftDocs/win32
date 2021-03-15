---
description: Encapsulates a transform frame in a transformation frame hierarchy.
ms.assetid: 838d75c2-41b2-4703-961b-893c34104c55
title: D3DXFRAME structure (D3dx9anim.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXFRAME
api_type: 
- HeaderDef
api_location: 
- d3dx9anim.h
---

# D3DXFRAME structure

Encapsulates a transform frame in a transformation frame hierarchy.

## Syntax


```C++
typedef struct D3DXFRAME {
  LPSTR               Name;
  D3DXMATRIX          TransformationMatrix;
  LPD3DXMESHCONTAINER pMeshContainer;
  D3DXFRAME           *pFrameSibling;
  D3DXFRAME           *pFrameFirstChild;
} D3DXFRAME, *LPD3DXFRAME;
```



## Members

<dl> <dt>

**Name**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Name of the frame.

</dd> <dt>

**TransformationMatrix**
</dt> <dd>

Type: **[**D3DXMATRIX**](d3dxmatrix.md)**

</dd> <dd>

Transformation matrix.

</dd> <dt>

**pMeshContainer**
</dt> <dd>

Type: **[**LPD3DXMESHCONTAINER**](d3dxmeshcontainer.md)**

</dd> <dd>

Pointer to the mesh container.

</dd> <dt>

**pFrameSibling**
</dt> <dd>

Type: ****D3DXFRAME**\***

</dd> <dd>

Pointer to a sibling frame.

</dd> <dt>

**pFrameFirstChild**
</dt> <dd>

Type: ****D3DXFRAME**\***

</dd> <dd>

Pointer to a child frame.

</dd> </dl>

## Remarks

An application can derive from this structure to add other data.

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx9anim.h</dt> </dl> |



## See also

<dl> <dt>

[D3DX Structures](dx9-graphics-reference-d3dx-structures.md)
</dt> </dl>

 

 




