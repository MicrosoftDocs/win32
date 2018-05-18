---
Description: 'Create an effect pool asynchronously.'
ms.assetid: '50c55751-26de-4002-9a89-8e5ab59dda79'
title: D3DX10CreateAsyncEffectCreateProcessor function
---

# D3DX10CreateAsyncEffectCreateProcessor function

Create an effect pool asynchronously.

## Syntax


```C++
HRESULT D3DX10CreateAsyncEffectCreateProcessor(
  _In_        LPCSTR               pFileName,
  _In_  const D3D10_SHADER_MACRO   *pDefines,
  _In_        LPD3D10INCLUDE       pInclude,
  _In_        LPCSTR               pProfile,
  _In_        UINT                 Flags,
  _In_        UINT                 FXFlags,
  _In_        ID3D10Device         *pDevice,
  _In_        ID3D10EffectPool     *pPool,
  _Out_       ID3D10Blob           **ppErrorBuffer,
  _Out_       ID3DX10DataProcessor **ppProcessor
);
```



## Parameters

<dl> <dt>

*pFileName* \[in\]
</dt> <dd>

Type: **[**LPCSTR**](winprog.windows_data_types)**

A string that contains the effect filename.

</dd> <dt>

*pDefines* \[in\]
</dt> <dd>

Type: **const [**D3D10\_SHADER\_MACRO**](d3d10-shader-macro.md)\***

A NULL-terminated array of shader macros (see [**D3D10\_SHADER\_MACRO**](d3d10-shader-macro.md)); set this to **NULL** to specify no macros.

</dd> <dt>

*pInclude* \[in\]
</dt> <dd>

Type: **[**LPD3D10INCLUDE**](id3d10include.md)**

A pointer to an include interface (see [**ID3D10Include Interface**](id3d10include.md)); set this to **NULL** to specify there is no include file.

</dd> <dt>

*pProfile* \[in\]
</dt> <dd>

Type: **[**LPCSTR**](winprog.windows_data_types)**

A string that specifies the [shader profile](direct3dhlsl.dx_graphics_hlsl_models) or shader model.

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

HLSL compile options (see [Shader Flags](d3d10-graphics-reference-effect-constants.md)).

</dd> <dt>

*FXFlags* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Effect compile options (see [Compile and Effect Flags](d3d10-graphics-reference-effect-constants.md)).

</dd> <dt>

*pDevice* \[in\]
</dt> <dd>

Type: **[**ID3D10Device**](id3d10device.md)\***

A pointer to the device (see [**ID3D10Device Interface**](id3d10device.md)) that will use the resources.

</dd> <dt>

*pPool* \[in\]
</dt> <dd>

Type: **[**ID3D10EffectPool**](id3d10effectpool.md)\***

A pointer to an effect pool (see [**ID3D10EffectPool Interface**](id3d10effectpool.md)) for sharing variables between effects.

</dd> <dt>

*ppErrorBuffer* \[out\]
</dt> <dd>

Type: **[**ID3D10Blob**](id3d10blob.md)\*\***

The address of a pointer to memory (see [**ID3D10Blob Interface**](id3d10blob.md)) that contains effect compile errors, if there were any.

</dd> <dt>

*ppProcessor* \[out\]
</dt> <dd>

Type: **[**ID3DX10DataProcessor**](id3dx10dataprocessor.md)\*\***

The address of a pointer to the asynchronous-data processor (see [**ID3DX10DataProcessor Interface**](id3dx10dataprocessor.md)).

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

The return value is one of the values listed in [Direct3D 10 Return Codes](d3d10-graphics-reference-returnvalues.md).

## Requirements



|                   |                                                                                          |
|-------------------|------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3DX10Async.h</dt> </dl> |



## See also

<dl> <dt>

[General Purpose Functions](d3d10-graphics-reference-d3dx10-functions-general-purpose.md)
</dt> </dl>

 

 




