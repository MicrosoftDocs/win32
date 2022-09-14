---
title: ID3DX11DataLoader Decompress method (D3DX11core.h)
description: Note The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps. Decompresses encoded data.
ms.assetid: 68579c86-9f77-444b-86b3-746cff745be8
keywords:
- Decompress method Direct3D 11
- Decompress method Direct3D 11 , ID3DX11DataLoader interface
- ID3DX11DataLoader interface Direct3D 11 , Decompress method
topic_type:
- apiref
api_name:
- ID3DX11DataLoader.Decompress
api_location:
- D3DX11.lib
- D3DX11.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ID3DX11DataLoader::Decompress method

> [!Note]  
> The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.

 

Decompresses encoded data.

## Syntax


```C++
HRESULT Decompress(
  [out] void   **ppData,
  [in]  SIZE_T *pcBytes
);
```



## Parameters

<dl> <dt>

*ppData* \[out\]
</dt> <dd>

Type: **void\*\***

Pointer to the raw data to decompress.

</dd> <dt>

*pcBytes* \[in\]
</dt> <dd>

Type: **[**SIZE\_T**](/windows/desktop/WinProg/windows-data-types)\***

The size of the data pointed to by ppData.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

The return value is one of the values listed in [Direct3D 11 Return Codes](d3d11-graphics-reference-returnvalues.md).

## Remarks

Use this method to load resources from file systems, such as ZIP files. When loading from an uncompressed resource, the decompression stage does not have to do any work.

[**ID3DX11DataLoader Interface**](id3dx11dataloader.md) can be inherited and its members redefined to support custom file formats.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX11core.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3DX11.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DX11DataLoader](id3dx11dataloader.md)
</dt> <dt>

[D3DX Interfaces](d3d11-graphics-reference-d3dx11-interfaces.md)
</dt> </dl>

 

