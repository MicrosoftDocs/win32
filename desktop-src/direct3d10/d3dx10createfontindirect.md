---
Description: Creates a font object.Note  Instead of using this function, we recommend that you use DirectWrite and the DirectXTK library, SpriteFont class.
ms.assetid: 057ee033-37d8-4fc1-9f35-776393fff008
title: D3DX10CreateFontIndirect function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# D3DX10CreateFontIndirect function

Creates a font object.

> [!Note]  
> Instead of using this function, we recommend that you use [DirectWrite](https://msdn.microsoft.com/62a8d723-ae1c-4cbc-a9da-3177e80d4a3a) and the [DirectXTK](http://go.microsoft.com/fwlink/p/?linkid=248929) library, **SpriteFont** class.

 

## Syntax


```C++
HRESULT D3DX10CreateFontIndirect(
  _In_        ID3D10Device     *pDevice,
  _In_  const D3DX10_FONT_DESC *pDesc,
  _Out_       LPD3DX10FONT     *ppFont
);
```



## Parameters

<dl> <dt>

*pDevice* \[in\]
</dt> <dd>

Type: **[**ID3D10Device**](/windows/desktop/api/D3D10/nn-d3d10-id3d10device)\***

Pointer to an [**ID3D10Device Interface**](/windows/desktop/api/D3D10/nn-d3d10-id3d10device) interface.

</dd> <dt>

*pDesc* \[in\]
</dt> <dd>

Type: **const [**D3DX10\_FONT\_DESC**](d3dx10-font-desc.md)\***

Pointer to a [**D3DX10\_FONT\_DESC**](d3dx10-font-desc.md) structure, describing the attributes of the font object to create. If Unicode is defined, the function call resolves to D3DXCreateFontIndirectW. Otherwise, the function call resolves to D3DXCreateFontIndirectA because ANSI strings are being used.

</dd> <dt>

*ppFont* \[out\]
</dt> <dd>

Type: **[**LPD3DX10FONT**](id3dx10font.md)\***

Returns a pointer to an [**ID3DX10Font Interface**](id3dx10font.md).

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/windows/desktop/455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

The return value is one of the values listed in [Direct3D 10 Return Codes](d3d10-graphics-reference-returnvalues.md).

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10Core.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl>   |



## See also

<dl> <dt>

[General Purpose Functions](d3d10-graphics-reference-d3dx10-functions-general-purpose.md)
</dt> </dl>

 

 




