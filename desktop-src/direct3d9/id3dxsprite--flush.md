---
description: Forces all batched sprites to be submitted to the device. Device states remain as they were after the last call to ID3DXSprite::Begin. The list of batched sprites is then cleared.
ms.assetid: e5717bde-e339-4344-8ce7-b0c3fe118887
title: ID3DXSprite::Flush method (D3dx9core.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXSprite.Flush
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXSprite::Flush method

Forces all batched sprites to be submitted to the device. Device states remain as they were after the last call to [**ID3DXSprite::Begin**](id3dxsprite--begin.md). The list of batched sprites is then cleared.

## Syntax


```C++
HRESULT Flush();
```



## Parameters

This method has no parameters.

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is S\_OK. If the method fails, the following value will be returned.D3DERR\_INVALIDCALL

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9core.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXSprite](id3dxsprite.md)
</dt> <dt>

[**ID3DXSprite::End**](id3dxsprite--end.md)
</dt> </dl>

 

 




