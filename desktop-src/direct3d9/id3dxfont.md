---
description: The ID3DXFont interface encapsulates the textures and resources needed to render a specific font on a specific device.
ms.assetid: ac40b600-3b9f-4e6e-8563-18597b3dd602
title: ID3DXFont interface (D3dx9core.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXFont
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXFont interface

The ID3DXFont interface encapsulates the textures and resources needed to render a specific font on a specific device.

## Members

The **ID3DXFont** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **ID3DXFont** also has these types of members:

-   [Methods](#methods)

### Methods

The **ID3DXFont** interface has these methods.



| Method                                                    | Description                                                                                                                                                                                                                                   |
|:----------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DrawText**](id3dxfont--drawtext.md)                   | Draws formatted text. This method supports ANSI and Unicode strings.<br/>                                                                                                                                                               |
| [**GetDC**](id3dxfont--getdc.md)                         | Returns a handle to a display device context (DC) that has the font set.<br/>                                                                                                                                                           |
| [**GetDesc**](id3dxfont--getdesc.md)                     | Gets a description of the current font object. GetDescW and GetDescA are identical to this method, except that a pointer is returned to a [**D3DXFONT\_DESCW**](d3dxfont-desc.md) or **D3DXFONT\_DESCA** structure, respectively.<br/> |
| [**GetDevice**](id3dxfont--getdevice.md)                 | Retrieves the Direct3D device associated with the font object.<br/>                                                                                                                                                                     |
| [**GetGlyphData**](id3dxfont--getglyphdata.md)           | Returns information about the placement and orientation of a glyph in a character cell.<br/>                                                                                                                                            |
| [**GetTextMetrics**](id3dxfont--gettextmetrics.md)       | Retrieves font characteristics that are identified in a [**TEXTMETRIC**](/windows/win32/api/wingdi/ns-wingdi-textmetrica) structure. This method supports ANSI and Unicode compiler settings.<br/>                                                                       |
| [**OnLostDevice**](id3dxfont--onlostdevice.md)           | Use this method to release all references to video memory resources and delete all stateblocks. This method should be called whenever a device is lost, or before resetting a device.<br/>                                              |
| [**OnResetDevice**](id3dxfont--onresetdevice.md)         | Use this method to re-acquire resources and save initial state.<br/>                                                                                                                                                                    |
| [**PreloadCharacters**](id3dxfont--preloadcharacters.md) | Loads a series of characters into video memory to improve the efficiency of rendering to the device.<br/>                                                                                                                               |
| [**PreloadGlyphs**](id3dxfont--preloadglyphs.md)         | Loads a series of glyphs into video memory to improve the efficiency of rendering to the device.<br/>                                                                                                                                   |
| [**PreloadText**](id3dxfont--preloadtext.md)             | Loads formatted text into video memory to improve the efficiency of rendering to the device. This method supports ANSI and Unicode strings.<br/>                                                                                        |



 

## Remarks

The **ID3DXFont** interface is obtained by calling [**D3DXCreateFont**](d3dxcreatefont.md) or [**D3DXCreateFontIndirect**](d3dxcreatefontindirect.md).

The LPD3DXFONT type is defined as a pointer to the **ID3DXFont** interface.


```
typedef interface ID3DXFont ID3DXFont;
typedef interface ID3DXFont *LPD3DXFONT;
```



## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9core.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[D3DX Interfaces](dx9-graphics-reference-d3dx-interfaces.md)
</dt> </dl>

 

 
