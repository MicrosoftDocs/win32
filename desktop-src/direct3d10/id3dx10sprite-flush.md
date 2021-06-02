---
description: Force all batched sprites to be submitted to the device. Device states remain as they were after the last call to ID3DX10Sprite::Begin. The list of batched sprites is then cleared.
ms.assetid: ae03e17c-1a14-4a41-a9a9-8757d2f7a81d
title: ID3DX10Sprite::Flush method (D3DX10.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DX10Sprite.Flush
api_type: 
- COM
api_location: 
- D3DX10.lib
- D3DX10.dll
---

# ID3DX10Sprite::Flush method

Force all batched sprites to be submitted to the device. Device states remain as they were after the last call to ID3DX10Sprite::Begin. The list of batched sprites is then cleared.

## Syntax


```C++
HRESULT Flush();
```



## Parameters

This method has no parameters.

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is S\_OK. If the method fails, the following value will be returned: D3DERR\_INVALIDCALL.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl> |



## See also

<dl> <dt>

[ID3DX10Sprite](id3dx10sprite.md)
</dt> <dt>

[D3DX Interfaces](d3d10-graphics-reference-d3dx10-interfaces.md)
</dt> </dl>

 

 




