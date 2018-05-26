---
Description: Sets the (u, v) texture coordinates of each texel.
ms.assetid: b1f8f5d6-568f-4868-87c9-9d6b1034d898
title: ID3DXTextureGutterHelperSetTexelMap method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXTextureGutterHelper::SetTexelMap method

Sets the (u, v) texture coordinates of each texel.

## Syntax


```C++
HRESULT SetTexelMap(
  [in] D3DXVECTOR2 *pTexelData
);
```



## Parameters

<dl> <dt>

*pTexelData* \[in\]
</dt> <dd>

Type: **[**D3DXVECTOR2**](d3dxvector2.md)\***

Pointer to the location in pixel (u, v) texture coordinates where each texel is located.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is S\_OK. If the method fails, the following value will be returned.D3DERR\_INVALIDCALL

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXTextureGutterHelper](id3dxtexturegutterhelper.md)
</dt> </dl>

 

 




