---
description: The ID3DX10Font interface encapsulates the textures and resources needed to render a specific font on a specific device.
ms.assetid: 81f4ffe3-f50d-47ce-ae85-15a2a19cacbd
title: ID3DX10Font interface (D3DX10.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DX10Font
api_type: 
- COM
api_location: 
- D3DX10.lib
- D3DX10.dll
---

# ID3DX10Font interface

The ID3DX10Font interface encapsulates the textures and resources needed to render a specific font on a specific device.

## Members

The **ID3DX10Font** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **ID3DX10Font** also has these types of members:

-   [Methods](#methods)

### Methods

The **ID3DX10Font** interface has these methods.



| Method                                                     | Description                                                                                                                                           |
|:-----------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DrawText**](id3dx10font-drawtext.md)                   | Draw formatted text. This method supports ANSI and Unicode strings.<br/>                                                                        |
| [**GetDC**](id3dx10font-getdc.md)                         | Return a handle to a display device context (DC) that has the font set onto it.<br/>                                                            |
| [**GetDesc**](id3dx10font-getdesc.md)                     | Get a description of the current font object.<br/>                                                                                              |
| [**GetDevice**](id3dx10font-getdevice.md)                 | Retrieve the Direct3D device associated with the font object.<br/>                                                                              |
| [**GetGlyphData**](id3dx10font-getglyphdata.md)           | Return information about the placement and orientation of a glyph in a character cell.<br/>                                                     |
| [**GetTextMetrics**](id3dx10font-gettextmetrics.md)       | Retrieve font characteristics.<br/>                                                                                                             |
| [**PreloadCharacters**](id3dx10font-preloadcharacters.md) | Load a series of characters into video memory to improve the efficiency of rendering to the device.<br/>                                        |
| [**PreloadGlyphs**](id3dx10font-preloadglyphs.md)         | Load a series of glyphs into video memory to improve the efficiency of rendering to the device.<br/>                                            |
| [**PreloadText**](id3dx10font-preloadtext.md)             | Load formatted text into video memory to improve the efficiency of rendering to the device. This method supports ANSI and Unicode strings.<br/> |



 

## Remarks

The ID3DX10Font interface is obtained by calling [**D3DX10CreateFont**](d3dx10createfont.md) or [**D3DX10CreateFontIndirect**](d3dx10createfontindirect.md).

The LPD3DX10FONT type is defined as a pointer to the ID3DX10Font interface.


```
typedef interface ID3DX10Font ID3DX10Font;
typedef interface ID3DX10Font *LPD3DX10FONT;
```



## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl> |



## See also

<dl> <dt>

[D3DX Interfaces](d3d10-graphics-reference-d3dx10-interfaces.md)
</dt> </dl>

 

 
