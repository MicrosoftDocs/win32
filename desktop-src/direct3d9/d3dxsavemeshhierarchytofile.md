---
description: Creates a .x file and saves the mesh hierarchy and corresponding animations in it.
ms.assetid: 803926fe-8cb7-422a-9920-56f7d0b0d0ea
title: D3DXSaveMeshHierarchyToFile function (D3dx9anim.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXSaveMeshHierarchyToFile
api_type: 
- LibDef
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# D3DXSaveMeshHierarchyToFile function

Creates a .x file and saves the mesh hierarchy and corresponding animations in it.

## Syntax


```C++
HRESULT D3DXSaveMeshHierarchyToFile(
  _In_       LPCSTR                    pFilename,
  _In_       DWORD                     XFormat,
  _In_ const D3DXFRAME                 *pFrameRoot,
  _In_       LPD3DXANIMATIONCONTROLLER pAnimController,
  _In_       LPD3DXSAVEUSERDATA        pUserDataSaver
);
```



## Parameters

<dl> <dt>

*pFilename* \[in\]
</dt> <dd>

Type: **[**LPCSTR**](../winprog/windows-data-types.md)**

Pointer to a string that specifies the name of the .x file identifying the saved mesh. If the compiler settings require Unicode, the data type LPCTSTR resolves to LPCWSTR. Otherwise, the string data type resolves to LPCSTR. See Remarks.

</dd> <dt>

*XFormat* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

Format of the .x file (text or binary, compressed or not). See D3DXF\_FILEFORMAT. D3DXF\_FILEFORMAT\_COMPRESSED can be combined (using a logical OR) with either the D3DXF\_FILEFORMAT\_BINARY or D3DXF\_FILEFORMAT\_TEXT flags to reduce the output file size.

</dd> <dt>

*pFrameRoot* \[in\]
</dt> <dd>

Type: **const [**D3DXFRAME**](d3dxframe.md)\***

Root node of the hierarchy to be saved. See [**D3DXFRAME**](d3dxframe.md).

</dd> <dt>

*pAnimController* \[in\]
</dt> <dd>

Type: **[**LPD3DXANIMATIONCONTROLLER**](id3dxanimationcontroller.md)**

Animation controller that has animation sets to be stored. See [**ID3DXAnimationController**](id3dxanimationcontroller.md).

</dd> <dt>

*pUserDataSaver* \[in\]
</dt> <dd>

Type: **[**LPD3DXSAVEUSERDATA**](id3dxsaveuserdata.md)**

Application-provided interface that allows saving of user data. See [**ID3DXSaveUserData**](id3dxsaveuserdata.md).

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be: D3DERR\_INVALIDCALL.

## Remarks

The compiler setting also determines the function version. If Unicode is defined, the function call resolves to D3DXSaveMeshHierarchyToFileW. Otherwise, the function call resolves to D3DXSaveMeshHierarchyToFileA.

This function does not save compressed animation sets.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9anim.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Animation Functions](dx9-graphics-reference-d3dx-functions-animation.md)
</dt> <dt>

[X File Reference](dx9-graphics-reference-d3dx-x-file.md)
</dt> </dl>

 

 
