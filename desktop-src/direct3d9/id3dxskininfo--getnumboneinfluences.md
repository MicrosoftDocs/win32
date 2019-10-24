---
Description: Gets the number of influences for a bone.
ms.assetid: 6383f990-2989-46b3-a634-b3bb7bd1d65b
title: ID3DXSkinInfo::GetNumBoneInfluences method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXSkinInfo.GetNumBoneInfluences
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXSkinInfo::GetNumBoneInfluences method

Gets the number of influences for a bone.

## Syntax


```C++
DWORD GetNumBoneInfluences(
  [in] DWORD bone
);
```



## Parameters

<dl> <dt>

*bone* \[in\]
</dt> <dd>

Type: **[**DWORD**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

Bone number.

</dd> </dl>

## Return value

Type: **[**DWORD**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

Returns the number of influences for a bone.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXSkinInfo](id3dxskininfo.md)
</dt> </dl>

 

 




