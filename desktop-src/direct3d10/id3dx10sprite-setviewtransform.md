---
Description: Set the view transform that applies to all sprites.
ms.assetid: 0420b141-46c7-4409-a0c4-67d1e8e02cd4
title: ID3DX10Sprite::SetViewTransform method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ID3DX10Sprite::SetViewTransform method

Set the view transform that applies to all sprites.

## Syntax


```C++
HRESULT SetViewTransform(
  [in] D3DXMATRIX *pViewTransform
);
```



## Parameters

<dl> <dt>

*pViewTransform* \[in\]
</dt> <dd>

Type: **[**D3DXMATRIX**](https://msdn.microsoft.com/VS|directx_sdk|~\d3dxmatrix.htm)\***

Pointer to a D3DXMATRIX that contains a transform of the sprite from the original world space. Use this transform to scale, rotate, or transform the sprite.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/windows/desktop/455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is S\_OK. If the method fails, the following value will be returned: D3DERR\_INVALIDCALL.

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl> |



## See also

<dl> <dt>

[ID3DX10Sprite](id3dx10sprite.md)
</dt> <dt>

[D3DX Interfaces](d3d10-graphics-reference-d3dx10-interfaces.md)
</dt> </dl>

 

 




