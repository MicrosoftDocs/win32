---
Description: 'Gets information about a specific callback in the animation set.'
ms.assetid: 'e8388bfc-5438-4216-a98f-dd0dbca12c87'
title: 'ID3DXAnimationSet::GetCallback method'
---

# ID3DXAnimationSet::GetCallback method

Gets information about a specific callback in the animation set.

## Syntax


```C++
HRESULT GetCallback(
  [in]  DOUBLE Position,
  [in]  DWORD  Flags,
  [out] DOUBLE *pCallbackPosition,
  [out] LPVOID *ppCallbackData
);
```



## Parameters

<dl> <dt>

*Position* \[in\]
</dt> <dd>

Type: **[**DOUBLE**](winprog.windows_data_types)**

Position from which to find callbacks.

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

Callback search flags. This parameter can be set to a combination of one or more flags from [**D3DXCALLBACK\_SEARCH\_FLAGS**](direct3d9.d3dxcallback_search_flags).

</dd> <dt>

*pCallbackPosition* \[out\]
</dt> <dd>

Type: **[**DOUBLE**](winprog.windows_data_types)\***

Pointer to the position of the callback.

</dd> <dt>

*ppCallbackData* \[out\]
</dt> <dd>

Type: **[**LPVOID**](winprog.windows_data_types)\***

Address of the callback data pointer.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

The return values of this method are implemented by an application programmer. In general, if no error occurs, program the method to return D3D\_OK. Otherwise, program the method to return an appropriate error message from [D3DERR](d3derr.md) or [**D3DXERR**](direct3d9.d3dxerr).

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9anim.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXAnimationSet](id3dxanimationset.md)
</dt> </dl>

 

 




