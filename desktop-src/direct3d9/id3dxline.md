---
description: The ID3DXLine interface implements line drawing using textured triangles.
ms.assetid: 87472618-d3e4-4008-9009-ae17fc7b696d
title: ID3DXLine interface (D3dx9core.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXLine
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXLine interface

The ID3DXLine interface implements line drawing using textured triangles.

## Members

The **ID3DXLine** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **ID3DXLine** also has these types of members:

-   [Methods](#methods)

### Methods

The **ID3DXLine** interface has these methods.



| Method                                                | Description                                                                                                                                                                                      |
|:------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Begin**](id3dxline--begin.md)                     | Prepares a device for drawing lines.<br/>                                                                                                                                                  |
| [**Draw**](id3dxline--draw.md)                       | Draws a line strip in screen space. Input is in the form of an array that defines points (of [**D3DXVECTOR2**](d3dxvector2.md)) on the line strip.<br/>                                   |
| [**DrawTransform**](id3dxline--drawtransform.md)     | Draws a line strip in screen space with a specified input transformation matrix.<br/>                                                                                                      |
| [**End**](id3dxline--end.md)                         | Restores the device state to how it was when [**ID3DXLine::Begin**](id3dxline--begin.md) was called.<br/>                                                                                 |
| [**GetAntialias**](id3dxline--getantialias.md)       | Gets the line antialiasing state.<br/>                                                                                                                                                     |
| [**GetDevice**](id3dxline--getdevice.md)             | Retrieves the Direct3D device associated with the line object.<br/>                                                                                                                        |
| [**GetGLLines**](id3dxline--getgllines.md)           | Gets the OpenGL-style line-drawing mode.<br/>                                                                                                                                              |
| [**GetPattern**](id3dxline--getpattern.md)           | Gets the line stipple pattern.<br/>                                                                                                                                                        |
| [**GetPatternScale**](id3dxline--getpatternscale.md) | Gets the stipple-pattern scale value.<br/>                                                                                                                                                 |
| [**GetWidth**](id3dxline--getwidth.md)               | Gets the thickness of the line.<br/>                                                                                                                                                       |
| [**OnLostDevice**](id3dxline--onlostdevice.md)       | Use this method to release all references to video memory resources and delete all stateblocks. This method should be called whenever a device is lost, or before resetting a device.<br/> |
| [**OnResetDevice**](id3dxline--onresetdevice.md)     | Use this method to re-acquire resources and save initial state.<br/>                                                                                                                       |
| [**SetAntialias**](id3dxline--setantialias.md)       | Toggles line antialiasing.<br/>                                                                                                                                                            |
| [**SetGLLines**](id3dxline--setgllines.md)           | Toggles the mode to draw OpenGL-style lines.<br/>                                                                                                                                          |
| [**SetPattern**](id3dxline--setpattern.md)           | Applies a stipple pattern to the line.<br/>                                                                                                                                                |
| [**SetPatternScale**](id3dxline--setpatternscale.md) | Stretches the stipple pattern along the line direction.<br/>                                                                                                                               |
| [**SetWidth**](id3dxline--setwidth.md)               | Specifies the thickness of the line.<br/>                                                                                                                                                  |



 

## Remarks

Create a line drawing object with [**D3DXCreateLine**](d3dxcreateline.md).

The LPD3DXLINE type is defined as a pointer to the **ID3DXLine** interface.


```
typedef interface ID3DXLine ID3DXLine;
typedef interface ID3DXLine *LPD3DXLINE;
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

 

 
