---
Description: Forces all batched sprites to be submitted to the device. Device states remain as they were after the last call to ID3DXSprite::Begin. The list of batched sprites is then cleared.
ms.assetid: e5717bde-e339-4344-8ce7-b0c3fe118887
title: ID3DXSprite::Flush method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

Type: **[**HRESULT**](https://msdn.microsoft.com/windows/desktop/455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is S\_OK. If the method fails, the following value will be returned.D3DERR\_INVALIDCALL

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9core.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXSprite](id3dxsprite.md)
</dt> <dt>

[**ID3DXSprite::End**](id3dxsprite--end.md)
</dt> </dl>

 

 




