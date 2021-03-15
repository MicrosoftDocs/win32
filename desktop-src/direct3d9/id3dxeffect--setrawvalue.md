---
description: Set a contiguous range of shader constants with a memory copy.
ms.assetid: 8a3b5141-c67a-45b9-91c2-1877642164e3
title: ID3DXEffect::SetRawValue method (D3DX9Effect.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXEffect.SetRawValue
api_type: 
- COM
api_location: 
- D3dx9.lib
- D3dx9.dll
---

# ID3DXEffect::SetRawValue method

Set a contiguous range of shader constants with a memory copy.

## Syntax


```C++
HRESULT SetRawValue(
  [in] D3DXHANDLE Handle,
  [in] void       *pData,
  [in] DWORD      OffsetInBytes,
  [in] DWORD      Bytes
);
```



## Parameters

<dl> <dt>

*Handle* \[in\]
</dt> <dd>

Type: **[D3DXHANDLE](dx9-graphics-reference-effects-constants.md)**

Handle to the value to set, or the name of the value passed in as a string. Passing in a handle is more efficient. See [Handles (Direct3D 9)](handles.md).

</dd> <dt>

*pData* \[in\]
</dt> <dd>

Type: **void\***

Pointer to a buffer containing the data to be set. SetRawValue checks for valid memory, but does not do any checking for valid data.

</dd> <dt>

*OffsetInBytes* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

Number of bytes between the beginning of the effect data and the beginning of the effect constants you are going to set.

</dd> <dt>

*Bytes* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

The size of the buffer to be set, in bytes.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is S\_OK. If the method fails, the return value can be one of the following:E\_INVALIDCALL.

## Remarks

SetRawValue is a very fast way to set effect constants since it performs a memory copy without performing validation or any data conversion (like converting a row-major matrix to a column-major matrix). Use SetRawValue to set a series of contiguous effect constants. For instance, you could set an array of twenty matrices with 20 calls to [**ID3DXBaseEffect::SetMatrix**](id3dxbaseeffect--setmatrix.md) or by using a single SetRawValue.

All values are expected to be either matrix4x4s or float4s and all matrices are expected to be in column-major order. Int or float values are cast into a float4; therefore, it is highly recommended that you use SetRawValue with only float4 or matrix4x4 data.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Effect.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXEffect](id3dxeffect.md)
</dt> </dl>

 

 
