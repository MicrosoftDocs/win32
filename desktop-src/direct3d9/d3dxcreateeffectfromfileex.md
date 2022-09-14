---
description: Create an effect from an ASCII or binary effect description. This function is an extended version of D3DXCreateEffectFromFile that allows an application to control which parameters are ignored by the effects system.
ms.assetid: 963caa1e-bc1a-4d4b-bdb1-50b17d8b4132
title: D3DXCreateEffectFromFileEx function (D3DX9Effect.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DXCreateEffectFromFileEx
api_type:
- LibDef
api_location:
- D3dx9.lib
- D3dx9.dll
---

# D3DXCreateEffectFromFileEx function

Create an effect from an ASCII or binary effect description. This function is an extended version of [**D3DXCreateEffectFromFile**](d3dxcreateeffectfromfile.md) that allows an application to control which parameters are ignored by the effects system.

## Syntax


```C++
HRESULT D3DXCreateEffectFromFileEx(
  _In_        LPDIRECT3DDEVICE9 pDevice,
  _In_        LPCTSTR           pSrcFile,
  _In_  const D3DXMACRO         *pDefines,
  _In_        LPD3DXINCLUDE     pInclude,
  _In_        LPCSTR            pSkipConstants,
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

Pointer to the device that will create the effect. See [**IDirect3DDevice9**](/windows/win32/api/d3d9helper/nn-d3d9helper-idirect3ddevice9).

</dd> <dt>

*pSrcFile* \[in\]
</dt> <dd>

Type: **[**LPCTSTR**](../winprog/windows-data-types.md)**

Pointer to the filename. This parameter supports both Unicode and ANSI strings. See Remarks.

</dd> <dt>

*pDefines* \[in\]
</dt> <dd>

Type: **const [**D3DXMACRO**](d3dxmacro.md)\***

Optional NULL-terminated array of preprocessor macro definitions. See [**D3DXMACRO**](d3dxmacro.md).

</dd> <dt>

*pInclude* \[in\]
</dt> <dd>

Type: **[**LPD3DXINCLUDE**](id3dxinclude.md)**

Optional interface pointer, [**ID3DXInclude**](id3dxinclude.md), to use for handling \#include directives. If this value is **NULL**, \#includes will either be honored when compiling from a file or will cause an error when compiled from a resource or memory.

</dd> <dt>

*pSkipConstants* \[in\]
</dt> <dd>

Type: **[**LPCSTR**](../winprog/windows-data-types.md)**

A string of effect parameters that will be ignored by the effect system. The string must be **NULL** terminated, and needs to contain the name of each application-managed constant separated by a semicolon.

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

If *pSrcFile* contains a text effect, flags can be a combination of [D3DXSHADER Flags](d3dxshader-flags.md) and [D3DXFX](d3dxfx.md) flags; otherwise, *pSrcFile* contains a binary effect and the only flags honored are D3DXFX flags. The Direct3D 10 HLSL compiler is now the default. See [Effect-Compiler Tool](../direct3dtools/fxc.md) for details.

</dd> <dt>

*pPool* \[in\]
</dt> <dd>

Type: **[**LPD3DXEFFECTPOOL**](id3dxeffectpool.md)**

Pointer to a [**ID3DXEffectPool**](id3dxeffectpool.md) object to use for shared parameters. If this value is **NULL**, no parameters will be shared.

</dd> <dt>

*ppEffect* \[out\]
</dt> <dd>

Type: **[**LPD3DXEFFECT**](id3dxeffect.md)\***

Returns a pointer to a buffer containing the compiled effect. See [**ID3DXEffect**](id3dxeffect.md).

</dd> <dt>

*ppCompilationErrors* \[out\]
</dt> <dd>

Type: **[**LPD3DXBUFFER**](id3dxbuffer.md)\***

Returns a pointer to a buffer containing a listing of compile errors. See [**ID3DXBuffer**](id3dxbuffer.md).

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be one of the following: D3DERR\_INVALIDCALL, D3DXERR\_INVALIDDATA, E\_OUTOFMEMORY.

## Remarks

This function is an extended version of [**D3DXCreateEffectFromFile**](d3dxcreateeffectfromfile.md) that allows an application to specify which effect constants will be managed by the application. A constant that is managed by the application is ignored by the effects system. That is, the application is responsible for initializing the constant as well as saving and restoring its state whenever appropriate.

This function checks each constant in pSkipConstants to see that:

-   It is bound to a constant register.
-   It is only used in HLSL shader code.

If a constant is named in the string that is not present in the effect, it is ignored.

If the compiler settings require Unicode, the data type LPCTSTR resolves to LPCWSTR. Otherwise, the LPCTSTR data type resolves to LPCSTR.

The compiler setting also determines the function version. If Unicode is defined, the function call resolves to D3DXCreateEffectFromFileW. Otherwise, the function call resolves to D3DXCreateEffectFromFileA because ANSI strings are being used.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Effect.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[Effect Functions](dx9-graphics-reference-effects-functions.md)
</dt> <dt>

[**D3DXCreateEffectEx**](d3dxcreateeffectex.md)
</dt> <dt>

[**D3DXCreateEffectFromResourceEx**](d3dxcreateeffectfromresourceex.md)
</dt> </dl>

 

 
