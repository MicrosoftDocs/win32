---
Description: Create an effect from a file.
ms.assetid: 1418857e-bda1-4ffb-bbb9-dfa3709313b1
title: D3DX10CreateEffectFromFile function
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DX10CreateEffectFromFile
api_type: 
- HeaderDef
api_location: 
- D3DX10Async.h
---

# D3DX10CreateEffectFromFile function

Create an effect from a file.

## Syntax


```C++
HRESULT D3DX10CreateEffectFromFile(
  _In_        LPCTSTR            pFileName,
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

*pFileName* \[in\]
</dt> <dd>

Type: **[**LPCTSTR**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

Name of the ASCII effect file. If the compiler settings require Unicode, the data type LPCTSTR resolves to LPCWSTR. Otherwise, the data type resolves to LPCSTR.

</dd> <dt>

*pDefines* \[in\]
</dt> <dd>

Type: **const [**D3D10\_SHADER\_MACRO**](https://msdn.microsoft.com/en-us/library/Bb172436(v=VS.85).aspx)\***

A NULL-terminated array of shader macros (see [**D3D10\_SHADER\_MACRO**](https://msdn.microsoft.com/en-us/library/Bb172436(v=VS.85).aspx)); set this to **NULL** to specify no macros.

</dd> <dt>

*pInclude* \[in\]
</dt> <dd>

Type: **[**ID3D10Include**](https://msdn.microsoft.com/en-us/library/Bb173775(v=VS.85).aspx)\***

A pointer to an include interface (see [**ID3D10Include Interface**](https://msdn.microsoft.com/en-us/library/Bb173775(v=VS.85).aspx)). This parameter can be **NULL**.

</dd> <dt>

*pProfile* \[in\]
</dt> <dd>

Type: **[**LPCSTR**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

A string that specifies the [shader profile](https://msdn.microsoft.com/en-us/library/Bb509626(v=VS.85).aspx), or shader model.

</dd> <dt>

*HLSLFlags* \[in\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

HLSL compile options (see [D3D10\_SHADER Constants](d3d10-shader.md)).

</dd> <dt>

*FXFlags* \[in\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

Effect compile options (see [Compile and Effect Flags](d3d10-graphics-reference-effect-constants.md)).

</dd> <dt>

*pDevice* \[in\]
</dt> <dd>

Type: **[**ID3D10Device**](/windows/desktop/api/D3D10/nn-d3d10-id3d10device)\***

A pointer to the device (see [**ID3D10Device Interface**](/windows/desktop/api/D3D10/nn-d3d10-id3d10device)) that will use the resources.

</dd> <dt>

*pEffectPool* \[in\]
</dt> <dd>

Type: **[**ID3D10EffectPool**](/windows/desktop/api/D3D10Effect/nn-d3d10effect-id3d10effectpool)\***

Pointer to an effect pool (see [**ID3D10EffectPool Interface**](/windows/desktop/api/D3D10Effect/nn-d3d10effect-id3d10effectpool)) for sharing variables between effects.

</dd> <dt>

*pPump* \[in\]
</dt> <dd>

Type: **[**ID3DX10ThreadPump**](id3dx10threadpump.md)\***

A pointer to a thread pump interface (see [**ID3DX10ThreadPump Interface**](id3dx10threadpump.md)). Use **NULL** to specify that this function should not return until it is completed.

</dd> <dt>

*ppEffect* \[out\]
</dt> <dd>

Type: **[**ID3D10Effect**](/windows/desktop/api/D3D10Effect/nn-d3d10effect-id3d10effect)\*\***

Address of a pointer to the effect (see [**ID3D10Effect Interface**](/windows/desktop/api/D3D10Effect/nn-d3d10effect-id3d10effect)) that is created.

</dd> <dt>

*ppErrors* \[out\]
</dt> <dd>

Type: **[**ID3D10Blob**](/windows/desktop/api/D3DCommon/nn-d3dcommon-id3d10blob)\*\***

The address of a pointer to memory (see [**ID3D10Blob Interface**](/windows/desktop/api/D3DCommon/nn-d3dcommon-id3d10blob)) that contains effect compile errors, if there were any.

</dd> <dt>

*pHResult* \[out\]
</dt> <dd>

Type: **[**HRESULT**](https://msdn.microsoft.com/en-us/library/Bb401631(v=MSDN.10).aspx)\***

A pointer to the return value. May be **NULL**. If *pPump* is not **NULL**, then *pHResult* must be a valid memory location until the asynchronous execution completes.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/en-us/library/Bb401631(v=MSDN.10).aspx)**

The return value is one of the values listed in [Direct3D 10 Return Codes](d3d10-graphics-reference-returnvalues.md).

## Requirements



|                   |                                                                                          |
|-------------------|------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3DX10Async.h</dt> </dl> |



## See also

<dl> <dt>

[General Purpose Functions](d3d10-graphics-reference-d3dx10-functions-general-purpose.md)
</dt> </dl>

 

 




