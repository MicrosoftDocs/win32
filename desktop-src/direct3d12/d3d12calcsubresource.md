---
title: D3D12CalcSubresource function (D3dx12.h)
description: Calculates a subresource index for a texture.
ms.assetid: 5C63A315-E21E-498B-A832-6BA2D17FF9A7
keywords:
- D3D12CalcSubresource function
topic_type:
- apiref
api_name:
- D3D12CalcSubresource
api_location:
- D3D12.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# D3D12CalcSubresource function

Calculates a subresource index for a texture.

## Syntax


```C++
UINT inline D3D12CalcSubresource(
   UINT MipSlice,
   UINT ArraySlice,
   UINT PlaneSlice,
   UINT MipLevels,
   UINT ArraySize
);
```



## Parameters

<dl> <dt>

*MipSlice* 
</dt> <dd>

Type: **[**UINT**](/windows/desktop/WinProg/windows-data-types)**

The zero-based index for the mipmap level to address; 0 indicates the first, most detailed mipmap level.

</dd> <dt>

*ArraySlice* 
</dt> <dd>

Type: **[**UINT**](/windows/desktop/WinProg/windows-data-types)**

The zero-based index for the array level to address; always use 0 for volume (3D) textures.

</dd> <dt>

*PlaneSlice* 
</dt> <dd>

Type: **[**UINT**](/windows/desktop/WinProg/windows-data-types)**

The zero-based index for the plane level to address.

</dd> <dt>

*MipLevels* 
</dt> <dd>

Type: **[**UINT**](/windows/desktop/WinProg/windows-data-types)**

The number of mipmap levels in the resource.

</dd> <dt>

*ArraySize* 
</dt> <dd>

Type: **[**UINT**](/windows/desktop/WinProg/windows-data-types)**

The number of elements in the array.

</dd> </dl>

## Return value

Type: **[**UINT**](/windows/desktop/WinProg/windows-data-types)**

The index which equals MipSlice + (ArraySlice \* MipLevels).

## Remarks

A buffer is an unstructured resource and is therefore defined as containing a single subresource. APIs that take buffers do not need a subresource index. A texture on the other hand is highly structured. Each texture object may contain one or more subresources depending on the size of the array and the number of mipmap levels.

For volume (3D) textures, all slices for a given mipmap level are a single subresource index.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx12.h</dt> </dl>  |
| Library<br/> | <dl> <dt>D3D12.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>D3D12.dll</dt> </dl> |



## See also

<dl> <dt>

[Helper Functions for D3D12](helper-functions-for-d3d12.md)
</dt> <dt>

[Subresources](subresources.md)
</dt> </dl>

 

