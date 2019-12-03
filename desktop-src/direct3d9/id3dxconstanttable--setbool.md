---
Description: Sets a Boolean value.
ms.assetid: 652e5b68-88f3-4b05-959b-38bb530c546a
title: ID3DXConstantTable::SetBool method (D3DX9Shader.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- ID3DXConstantTable.SetBool
api_type:
- COM
api_location:
- d3dx9.lib
- d3dx9.dll
---

# ID3DXConstantTable::SetBool method

Sets a Boolean value.

## Syntax


```C++
HRESULT SetBool(
  [in] LPDIRECT3DDEVICE9 pDevice,
  [in] D3DXHANDLE        hConstant,
  [in] BOOL              b
);
```



## Parameters

<dl> <dt>

*pDevice* \[in\]
</dt> <dd>

Type: **[**LPDIRECT3DDEVICE9**](https://msdn.microsoft.com/library/Bb174336(v=VS.85).aspx)**

Pointer to an [**IDirect3DDevice9**](https://msdn.microsoft.com/library/Bb174336(v=VS.85).aspx) interface, representing the device associated with the constant table.

</dd> <dt>

*hConstant* \[in\]
</dt> <dd>

Type: **[D3DXHANDLE](dx9-graphics-reference-effects-constants.md)**

Unique identifier to the constant. See [D3DXHANDLE](dx9-graphics-reference-effects-constants.md).

</dd> <dt>

*b* \[in\]
</dt> <dd>

Type: **[**BOOL**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

Boolean value.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/en-us/library/Bb401631(v=MSDN.10).aspx)**

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

 

 




