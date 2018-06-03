---
Description: Prepare a device for drawing sprites.
ms.assetid: cffe5ac3-eeee-4ece-afcc-04a476b75863
title: ID3DX10Sprite::Begin method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ID3DX10Sprite::Begin method

Prepare a device for drawing sprites.

## Syntax


```C++
HRESULT Begin(
  [in] UINT flags
);
```



## Parameters

<dl> <dt>

*flags* \[in\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/windows/desktop/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

Flags that control how the sprites will be drawn. See [**D3DX10\_SPRITE\_FLAG**](d3dx10-sprite-flag.md).

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/windows/desktop/455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is S\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL, D3DERR\_OUTOFVIDEOMEMORY, D3DXERR\_INVALIDDATA, E\_OUTOFMEMORY.

## Remarks

Every call to Begin must be matched with a call to [**ID3DX10Sprite::End**](id3dx10sprite-end.md).

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

 

 




