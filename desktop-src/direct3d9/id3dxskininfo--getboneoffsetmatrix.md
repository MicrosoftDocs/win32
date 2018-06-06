---
Description: Gets the bone offset matrix.
ms.assetid: 99d47635-ffae-4668-a37c-b15442148fa1
title: ID3DXSkinInfo::GetBoneOffsetMatrix method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ID3DXSkinInfo::GetBoneOffsetMatrix method

Gets the bone offset matrix.

## Syntax


```C++
LPD3DXMATRIX GetBoneOffsetMatrix(
  [in] DWORD Bone
);
```



## Parameters

<dl> <dt>

*Bone* \[in\]
</dt> <dd>

Type: **[**DWORD**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

Bone number.

</dd> </dl>

## Return value

Type: **[**LPD3DXMATRIX**](d3dxmatrix.md)**

Returns a pointer to the bone offset matrix. Do not free this pointer.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXSkinInfo](id3dxskininfo.md)
</dt> <dt>

[**SetBoneOffsetMatrix**](id3dxskininfo--setboneoffsetmatrix.md)
</dt> <dt>

[**GetNumBones**](id3dxskininfo--getnumbones.md)
</dt> </dl>

 

 




