---
description: Applies stored texture gutter data to an ID3DXPRTBuffer texture buffer.
ms.assetid: 05cc0709-543a-4df5-980a-8549451d396b
title: ID3DXPRTBuffer::EvalGH method (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXPRTBuffer.EvalGH
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXPRTBuffer::EvalGH method

Applies stored texture gutter data to an [**ID3DXPRTBuffer**](id3dxprtbuffer.md) texture buffer.

## Syntax


```C++
HRESULT EvalGH();
```



## Parameters

This method has no parameters.

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is S\_OK. If the method fails, the following value will be returned.

## Remarks

This method makes an internal call to [**ID3DXTextureGutterHelper::ApplyGuttersFloat**](id3dxtexturegutterhelper--applyguttersfloat.md) to retrieve and apply texture gutter data.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXPRTBuffer](id3dxprtbuffer.md)
</dt> </dl>

 

 




