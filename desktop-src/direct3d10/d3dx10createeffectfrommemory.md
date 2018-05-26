---
Description: Create an effect from memory.
ms.assetid: 6903a695-bb87-45fe-9913-25beeaf17233
title: D3DX10CreateEffectFromMemory function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DX10CreateEffectFromMemory function

Create an effect from memory.

## Syntax


```C++
HRESULT D3DX10CreateEffectFromMemory(
  _In_        LPCVOID            pData,
  _In_        SIZE_T             DataLength,
  _In_        LPCSTR             pSrcFileName,
  _In_  const D3D10_SHADER_MACRO *pDefines,
  _In_        ID3D10Include      *pInclude,
  _In_        LPCSTR             pProfile,
  _In_        UINT               HLSLFlags,
  _In_        UINT               FXFlags,
  _In_        ID3D10Device       *pDevice,
  _In_        ID3D10EffectPool   *pEffectPool,
  _In_        ID3DX10ThreadPump  *pPump,
  _Out_       ID3D10Effect       **ppEffect,
  _Out_       ID3D10Blob         **ppErrors,
  _Out_       HRESULT            *pHResult
);
```



## Parameters

<dl> <dt>

*pData* \[in\]
</dt> <dd>

Type: **[**LPCVOID**](winprog.windows_data_types)**

Pointer to the effect in memory.

</dd> <dt>

*DataLength* \[in\]
</dt> <dd>

Type: **[**SIZE\_T**](winprog.windows_data_types)**

Size of the effect in memory.

</dd> <dt>

*pSrcFileName* \[in\]
</dt> <dd>

Type: **[**LPCSTR**](winprog.windows_data_types)**

Name of the effect file in memory.

</dd> <dt>

*pDefines* \[in\]
</dt> <dd>

Type: **const [**D3D10\_SHADER\_MACRO**](/windows/win32/D3D10Shader/?branch=master)\***

A NULL-terminated array of shader macros (see [**D3D10\_SHADER\_MACRO**](/windows/win32/D3D10Shader/?branch=master)); set this to **NULL** to specify no macros.

</dd> <dt>

*pInclude* \[in\]
</dt> <dd>

Type: **[**ID3D10Include**](/windows/win32/D3D10Shader/?branch=master)\***

A pointer to an include interface (see [**ID3D10Include Interface**](/windows/win32/D3D10Shader/?branch=master)). This parameter can be **NULL**.

</dd> <dt>

*pProfile* \[in\]
</dt> <dd>

Type: **[**LPCSTR**](winprog.windows_data_types)**

A string that specifies the [shader profile](direct3dhlsl.dx_graphics_hlsl_models), or shader model.

</dd> <dt>

*HLSLFlags* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

HLSL compile options (see [D3D10\_SHADER Constants](d3d10-shader.md)).

</dd> <dt>

*FXFlags* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Effect compile options (see [D3D10\_EFFECT Constants](d3d10-effect.md)).

</dd> <dt>

*pDevice* \[in\]
</dt> <dd>

Type: **[**ID3D10Device**](/windows/win32/D3D10/nn-d3d10-id3d10device?branch=master)\***

A pointer to the device (see [**ID3D10Device Interface**](/windows/win32/D3D10/nn-d3d10-id3d10device?branch=master)) that will use the resources.

</dd> <dt>

*pEffectPool* \[in\]
</dt> <dd>

Type: **[**ID3D10EffectPool**](/windows/win32/D3D10Effect/nn-d3d10effect-id3d10effectpool?branch=master)\***

Pointer to an effect pool (see [**ID3D10EffectPool Interface**](/windows/win32/D3D10Effect/nn-d3d10effect-id3d10effectpool?branch=master)) for sharing variables between effects.

</dd> <dt>

*pPump* \[in\]
</dt> <dd>

Type: **[**ID3DX10ThreadPump**](id3dx10threadpump.md)\***

A pointer to a thread pump interface (see [**ID3DX10ThreadPump Interface**](id3dx10threadpump.md)). Use **NULL** to specify that this function should not return until it is completed.

</dd> <dt>

*ppEffect* \[out\]
</dt> <dd>

Type: **[**ID3D10Effect**](/windows/win32/D3D10Effect/nn-d3d10effect-id3d10effect?branch=master)\*\***

Address of a pointer to the effect (see [**ID3D10Effect Interface**](/windows/win32/D3D10Effect/nn-d3d10effect-id3d10effect?branch=master)) that is created.

</dd> <dt>

*ppErrors* \[out\]
</dt> <dd>

Type: **[**ID3D10Blob**](/windows/win32/D3DCommon/nn-d3dcommon-id3d10blob?branch=master)\*\***

The address of a pointer to memory (see [**ID3D10Blob Interface**](/windows/win32/D3DCommon/nn-d3dcommon-id3d10blob?branch=master)) that contains effect compile errors, if there were any.

</dd> <dt>

*pHResult* \[out\]
</dt> <dd>

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)\***

A pointer to the return value. May be **NULL**. If *pPump* is not **NULL**, then *pHResult* must be a valid memory location until the asynchronous execution completes.

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

 

 




