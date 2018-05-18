---
Description: 'Sets an array of Boolean values.'
ms.assetid: '323ad654-81e3-4986-a667-8333dd44a2d1'
title: 'ID3DXConstantTable::SetBoolArray method'
---

# ID3DXConstantTable::SetBoolArray method

Sets an array of Boolean values.

## Syntax


```C++
HRESULT SetBoolArray(
  [in]       LPDIRECT3DDEVICE9 pDevice,
  [in]       D3DXHANDLE        hConstant,
  [in] const BOOL              *pB,
  [in]       UINT              Count
);
```



## Parameters

<dl> <dt>

*pDevice* \[in\]
</dt> <dd>

Type: **[**LPDIRECT3DDEVICE9**](idirect3ddevice9.md)**

Pointer to an [**IDirect3DDevice9**](idirect3ddevice9.md) interface, representing the device associated with the constant table.

</dd> <dt>

*hConstant* \[in\]
</dt> <dd>

Type: **[D3DXHANDLE](dx9-graphics-reference-effects-constants.md)**

Unique identifier to the array of constants. See [D3DXHANDLE](dx9-graphics-reference-effects-constants.md).

</dd> <dt>

*pB* \[in\]
</dt> <dd>

Type: **const [**BOOL**](winprog.windows_data_types)\***

Array of Boolean values.

</dd> <dt>

*Count* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Number of Boolean values in the array.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be D3DERR\_INVALIDCALL.

## Requirements



|                    |                                                                                          |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Shader.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXConstantTable](id3dxconstanttable.md)
</dt> </dl>

 

 




