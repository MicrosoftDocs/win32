---
description: Create an effect from an ASCII or binary effect description.
ms.assetid: 8385512c-e93d-4c07-b353-87717eb58bcd
title: D3DXCreateEffectFromResource function (D3DX9Effect.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DXCreateEffectFromResource
api_type:
- LibDef
api_location:
- D3dx9.lib
- D3dx9.dll
---

# D3DXCreateEffectFromResource function

Create an effect from an ASCII or binary effect description.

## Syntax


```C++
HRESULT D3DXCreateEffectFromResource(
  _In_        LPDIRECT3DDEVICE9 pDevice,
  _In_        HMODULE           hSrcModule,
  _In_        LPCTSTR           pSrcResource,
  _In_  const D3DXMACRO         *pDefines,
  _In_        LPD3DXINCLUDE     pInclude,
  _In_        DWORD             Flags,
  _In_        LPD3DXEFFECTPOOL  pPool,
  _Out_       LPD3DXEFFECT      *ppEffect,
  _Out_       LPD3DXBUFFER      *ppCompilationErrors
);
```



## Parameters

<dl> <dt>

*pDevice* \[in\]
</dt> <dd>

Type: **[**LPDIRECT3DDEVICE9**](/windows/win32/api/d3d9helper/nn-d3d9helper-idirect3ddevice9)**

Pointer to the device.

</dd> <dt>

*hSrcModule* \[in\]
</dt> <dd>

Type: **[**HMODULE**](../winprog/windows-data-types.md)**

Handle to a module containing the effect description. If this parameter is **NULL**, the current module will be used.

</dd> <dt>

*pSrcResource* \[in\]
</dt> <dd>

Type: **[**LPCTSTR**](../winprog/windows-data-types.md)**

Pointer to the resource. This parameter supports both Unicode and ANSI strings. See Remarks.

</dd> <dt>

*pDefines* \[in\]
</dt> <dd>

Type: **const [**D3DXMACRO**](d3dxmacro.md)\***

An optional **NULL**-terminated array of [**D3DXMACRO**](d3dxmacro.md) structures that describe preprocessor definitions. This value can be **NULL**.

</dd> <dt>

*pInclude* \[in\]
</dt> <dd>

Type: **[**LPD3DXINCLUDE**](id3dxinclude.md)**

Optional interface pointer, [**ID3DXInclude**](id3dxinclude.md), to use for handling \#include directives. If this value is **NULL**, \#includes will either be honored when compiling from a file or will cause an error when compiled from a resource or memory.

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

If *hSrcModule* contains a text effect, flags can be a combination of [D3DXSHADER Flags](d3dxshader-flags.md) and [D3DXFX](d3dxfx.md) flags; otherwise, *hSrcModule* contains a binary effect and the only flags honored are D3DXFX flags. The Direct3D 10 HLSL compiler is now the default. See [Effect-Compiler Tool](../direct3dtools/fxc.md) for details.

</dd> <dt>

*pPool* \[in\]
</dt> <dd>

Type: **[**LPD3DXEFFECTPOOL**](id3dxeffectpool.md)**

Pointer to a [**ID3DXEffectPool**](id3dxeffectpool.md) object to use for shared parameters. If this value is **NULL**, no parameters will be shared.

</dd> <dt>

*ppEffect* \[out\]
</dt> <dd>

Type: **[**LPD3DXEFFECT**](id3dxeffect.md)\***

Returns a buffer containing the compiled effect.

</dd> <dt>

*ppCompilationErrors* \[out\]
</dt> <dd>

Type: **[**LPD3DXBUFFER**](id3dxbuffer.md)\***

Returns a buffer containing a listing of compile errors.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be one of the following: D3DERR\_INVALIDCALL, D3DXERR\_INVALIDDATA, E\_OUTOFMEMORY.

## Remarks

If the compiler settings require Unicode, the data type LPCTSTR resolves to LPCWSTR. Otherwise, the LPCTSTR data type resolves to LPCSTR.

The compiler setting also determines the function version. If Unicode is defined, the function call resolves to D3DXCreateEffectFromResourceW. Otherwise, the function call resolves to D3DXCreateEffectFromResourceA because ANSI strings are being used.

D3DXCreateEffectFromResource loads data from a resource of type RT\_RCDATA. See MSDN for more information about Windows resources.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Effect.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[Effect Functions](dx9-graphics-reference-effects-functions.md)
</dt> <dt>

[**D3DXCompileShader**](d3dxcompileshader.md)
</dt> <dt>

[**D3DXCompileShaderFromResource**](d3dxcompileshaderfromresource.md)
</dt> </dl>

 

 
