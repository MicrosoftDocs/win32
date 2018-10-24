---
Description: Create an asynchronous-data processor for an effect.
ms.assetid: 90a0dcd1-e495-4068-9f28-e2645370b984
title: D3DX10CreateAsyncEffectCompilerProcessor function
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DX10CreateAsyncEffectCompilerProcessor
api_type: 
- HeaderDef
api_location: 
- D3DX10Async.h
---

# D3DX10CreateAsyncEffectCompilerProcessor function

Create an asynchronous-data processor for an effect.

## Syntax


```C++
HRESULT D3DX10CreateAsyncEffectCompilerProcessor(
  _In_        LPCSTR               pFileName,
  _In_  const D3D10_SHADER_MACRO   *pDefines,
  _In_        LPD3D10INCLUDE       pInclude,
  _In_        UINT                 Flags,
  _In_        UINT                 FXFlags,
  _Out_       ID3D10Blob           **ppCompiledShader,
  _Out_       ID3D10Blob           **ppErrorBuffer,
  _Out_       ID3DX10DataProcessor **ppDataProcessor
);
```



## Parameters

<dl> <dt>

*pFileName* \[in\]
</dt> <dd>

Type: **[**LPCSTR**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

A string that contains the effect filename.

</dd> <dt>

*pDefines* \[in\]
</dt> <dd>

Type: **const [**D3D10\_SHADER\_MACRO**](https://msdn.microsoft.com/en-us/library/Bb172436(v=VS.85).aspx)\***

A NULL-terminated array of shader macros (see [**D3D10\_SHADER\_MACRO**](https://msdn.microsoft.com/en-us/library/Bb172436(v=VS.85).aspx)); set this to **NULL** to specify no macros.

</dd> <dt>

*pInclude* \[in\]
</dt> <dd>

Type: **[**LPD3D10INCLUDE**](https://msdn.microsoft.com/en-us/library/Bb173775(v=VS.85).aspx)**

A pointer to an include interface (see [**ID3D10Include Interface**](https://msdn.microsoft.com/en-us/library/Bb173775(v=VS.85).aspx)). This parameter can be **NULL**.

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

[HLSL compile options](d3d10-graphics-reference-effect-constants.md).

</dd> <dt>

*FXFlags* \[in\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

[Effect compile options](d3d10-graphics-reference-effect-constants.md)).

</dd> <dt>

*ppCompiledShader* \[out\]
</dt> <dd>

Type: **[**ID3D10Blob**](/windows/desktop/api/D3DCommon/nn-d3dcommon-id3d10blob)\*\***

Address of a pointer to buffer (see [**ID3D10Blob Interface**](/windows/desktop/api/D3DCommon/nn-d3dcommon-id3d10blob)) that contains the compiled effect.

</dd> <dt>

*ppErrorBuffer* \[out\]
</dt> <dd>

Type: **[**ID3D10Blob**](/windows/desktop/api/D3DCommon/nn-d3dcommon-id3d10blob)\*\***

Address of a pointer to a buffer (see [**ID3D10Blob Interface**](/windows/desktop/api/D3DCommon/nn-d3dcommon-id3d10blob)) that contains compile errors.

</dd> <dt>

*ppDataProcessor* \[out\]
</dt> <dd>

Type: **[**ID3DX10DataProcessor**](id3dx10dataprocessor.md)\*\***

Address of a pointer to a buffer that contains the data processor created (see [**ID3DX10DataProcessor Interface**](id3dx10dataprocessor.md)).

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

 

 




