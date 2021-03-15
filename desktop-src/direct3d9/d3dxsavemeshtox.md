---
description: Saves a mesh to a .x file.
ms.assetid: 6d9cbca8-3847-4e15-95d4-9df3f8269665
title: D3DXSaveMeshToX function (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXSaveMeshToX
api_type: 
- LibDef
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# D3DXSaveMeshToX function

Saves a mesh to a .x file.

## Syntax


```C++
HRESULT D3DXSaveMeshToX(
  _In_       LPCTSTR            pFilename,
  _In_       LPD3DXMESH         pMesh,
  _In_ const DWORD              *pAdjacency,
  _In_ const D3DXMATERIAL       *pMaterials,
  _In_ const D3DXEFFECTINSTANCE *pEffectInstances,
  _In_       DWORD              NumMaterials,
  _In_       DWORD              Format
);
```



## Parameters

<dl> <dt>

*pFilename* \[in\]
</dt> <dd>

Type: **[**LPCTSTR**](../winprog/windows-data-types.md)**

Pointer to a string that specifies the filename. If the compiler settings require Unicode, the data type LPCTSTR resolves to LPCWSTR. Otherwise, the string data type resolves to LPCSTR. See Remarks.

</dd> <dt>

*pMesh* \[in\]
</dt> <dd>

Type: **[**LPD3DXMESH**](id3dxmesh.md)**

Pointer to an [**ID3DXMesh**](id3dxmesh.md) interface, representing the mesh to save to a .x file.

</dd> <dt>

*pAdjacency* \[in\]
</dt> <dd>

Type: **const [**DWORD**](../winprog/windows-data-types.md)\***

Pointer to an array of three DWORDs per face that specify the three neighbors for each face in the mesh. This parameter may be **NULL**.

</dd> <dt>

*pMaterials* \[in\]
</dt> <dd>

Type: **const [**D3DXMATERIAL**](d3dxmaterial.md)\***

Pointer to an array of [**D3DXMATERIAL**](d3dxmaterial.md) structures, containing material information to be saved in the .x file.

</dd> <dt>

*pEffectInstances* \[in\]
</dt> <dd>

Type: **const [**D3DXEFFECTINSTANCE**](d3dxeffectinstance.md)\***

Pointer to an array of effect instances, one per attribute group in the mesh. This parameter may be **NULL**. An effect instance is a particular instance of state information used to initialize an effect. For more information, see [**D3DXEFFECTINSTANCE**](d3dxeffectinstance.md).

</dd> <dt>

*NumMaterials* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

Number of [**D3DXMATERIAL**](d3dxmaterial.md) structures in the *pMaterials* array.

</dd> <dt>

*Format* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

A combination of file format and save options when saving an .x file. See [D3DX X File Constants](dx9-graphics-reference-d3dx-x-file-constants.md).

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be one of the following: D3DERR\_INVALIDCALL.

## Remarks

The compiler setting also determines the function version. If Unicode is defined, the function call resolves to D3DXSaveMeshToXW. Otherwise, the function call resolves to D3DXSaveMeshToXA because ANSI strings are being used.

The default file format is binary; however, if a file is specified as both a binary and a text file, it will be saved as a text file. Regardless of the file format, you may also use the compressed format to reduce the file size.

The following is a typical code example of how to use this function.


```
ID3DXMesh*    m_pMesh;           // Mesh object to be saved to a .x file
D3DXMATERIAL* m_pMaterials;      // Array of material structs in the mesh
DWORD         m_dwNumMaterials;  // Number of material structs in the mesh
    
DWORD dwFormat = D3DXF_FILEFORMAT_BINARY;  // Binary-format .x file (default)
// DWORD dwFormat = D3DXF_FILEFORMAT_TEXT; // Text-format .x file
    
// Load mesh into m_pMesh and determine values of m_pMaterials and 
// m_dwNumMaterials with calls to D3DXLoadMeshxxx or other D3DX functions
    
// ...
        
D3DXSaveMeshToX(
    L"outputxfilename.x",
    m_pMesh,
    NULL,
    m_pMaterials,
    NULL,
    m_dwNumMaterials,
    dwFormat );
```



## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Mesh Functions](dx9-graphics-reference-d3dx-functions-mesh.md)
</dt> <dt>

[**D3DXEFFECTDEFAULT**](d3dxeffectdefault.md)
</dt> <dt>

[**D3DXEFFECTINSTANCE**](d3dxeffectinstance.md)
</dt> </dl>

 

 
