---
title: D3D12DecomposeSubresource function (D3dx12.h)
description: Outputs the mip slice, array slice, and plane slice that correspond to the specified subresource index.
ms.assetid: 89FAD7C5-E732-4E74-AC2F-DEECD6ADDA7D
keywords:
- D3D12DecomposeSubresource function
topic_type:
- apiref
api_name:
- D3D12DecomposeSubresource
api_location:
- D3D12.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# D3D12DecomposeSubresource function

Outputs the mip slice, array slice, and plane slice that correspond to the specified subresource index.

## Syntax


```C++
void inline D3D12DecomposeSubresource(
        UINT Subresource,
        UINT MipLevels,
        UINT ArraySize,
  _Out_ T    &MipSlice,
  _Out_ U    &ArraySlice,
  _Out_ V    &PlaneSlice
);
```



## Parameters

<dl> <dt>

*Subresource* 
</dt> <dd>

Type: **[**UINT**](/windows/desktop/WinProg/windows-data-types)**

The index of the subresource.

</dd> <dt>

*MipLevels* 
</dt> <dd>

Type: **[**UINT**](/windows/desktop/WinProg/windows-data-types)**

The maximum number of mipmap levels in the subresource.

</dd> <dt>

*ArraySize* 
</dt> <dd>

Type: **[**UINT**](/windows/desktop/WinProg/windows-data-types)**

The number of elements in the array.

</dd> <dt>

*MipSlice* \[out, ref\]
</dt> <dd>

Type: **T**

Outputs the mip slice that corresponds to the given subresource index.

</dd> <dt>

*ArraySlice* \[out, ref\]
</dt> <dd>

Type: **U**

Outputs the array slice that corresponds to the given subresource index.

</dd> <dt>

*PlaneSlice* \[out, ref\]
</dt> <dd>

Type: **V**

Outputs the plane slice that corresponds to the given subresource index.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

This function determines which mip slice, array slice, and plane slice correspond to a given subresource index. This is a useful utility, though it is C++ specific.

This function is declared as follows, with C++ templatized parameters for types **T**, **U**, and **V**:


```c++
template <typename T, typename U, typename V>
inline void D3D12DecomposeSubresource( UINT Subresource, UINT MipLevels, UINT ArraySize, _Out_ T& MipSlice, _Out_ U& ArraySlice, _Out_ V& PlaneSlice )
{
    MipSlice = static_cast<T>(Subresource % MipLevels);
    ArraySlice = static_cast<U>((Subresource / MipLevels) % ArraySize);
    PlaneSlice = static_cast<V>(Subresource / (MipLevels * ArraySize));
}
```



## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx12.h</dt> </dl>  |
| Library<br/> | <dl> <dt>D3D12.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>D3D12.dll</dt> </dl> |



## See also

[Helper Functions for D3D12](helper-functions-for-d3d12.md)

[Subresources](subresources.md)
