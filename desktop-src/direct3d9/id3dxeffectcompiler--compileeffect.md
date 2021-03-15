---
description: Compile an effect.
ms.assetid: be6f862a-5091-4a06-a27a-308e81360129
title: ID3DXEffectCompiler::CompileEffect method (D3DX9Effect.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXEffectCompiler.CompileEffect
api_type: 
- COM
api_location: 
- D3dx9.lib
- D3dx9.dll
---

# ID3DXEffectCompiler::CompileEffect method

Compile an effect.

## Syntax


```C++
HRESULT CompileEffect(
  [in]          DWORD        Flags,
  [out, retval] LPD3DXBUFFER *ppEffect,
  [out, retval] LPD3DXBUFFER *ppErrorMsgs
);
```



## Parameters

<dl> <dt>

*Flags* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

Compile options identified by various flags. The Direct3D 10 HLSL compiler is now the default. See [D3DXSHADER Flags](d3dxshader-flags.md) for details.

</dd> <dt>

*ppEffect* \[out, retval\]
</dt> <dd>

Type: **[**LPD3DXBUFFER**](id3dxbuffer.md)\***

Buffer containing the compiled effect. For more information about accessing the buffer, see [**ID3DXBuffer**](id3dxbuffer.md).

</dd> <dt>

*ppErrorMsgs* \[out, retval\]
</dt> <dd>

Type: **[**LPD3DXBUFFER**](id3dxbuffer.md)\***

Buffer containing at least the first compile error message that occurred. This includes effect compiler errors and high-level language compile errors. For more information about accessing the buffer, see [**ID3DXBuffer**](id3dxbuffer.md).

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is S\_OK.

If the arguments are invalid, the method will return D3DERR\_INVALIDCALL.

If the method fails, the return value will be E\_FAIL.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Effect.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXEffectCompiler](id3dxeffectcompiler.md)
</dt> </dl>

 

 
