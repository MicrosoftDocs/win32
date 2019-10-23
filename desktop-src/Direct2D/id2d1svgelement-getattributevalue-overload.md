---
title: ID2D1SvgElement GetAttributeValue methods
description: Gets an attribute of this element.
ms.assetid: 2f6ca40a-6c78-9c60-c06a-a31f6edf7663
keywords:
- GetAttributeValue methods Direct2D
topic_type:
- apiref
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_name: 
api_location: 
---

# ID2D1SvgElement::GetAttributeValue methods

Gets an attribute of this element.

### Overload list



| Method                                                                                                                     | Description                                                                                                                                                 |
|:---------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetAttributeValue(PCWSTR, FLOAT \*)**](https://msdn.microsoft.com/en-us/library/Mt797849(v=VS.85).aspx)                                         | Gets an attribute of this element as a float.<br/>                                                                                                    |
| [**GetAttributeValue(PCWSTR, D2D1\_COLOR\_F \*)**](https://msdn.microsoft.com/en-us/library/Mt797850(v=VS.85).aspx)                                | Gets an attribute of this element as a color.<br/>                                                                                                    |
| [**GetAttributeValue(PCWSTR, REFIID, void \*\*)**](https://msdn.microsoft.com/en-us/library/Mt797848(v=VS.85).aspx)                                | Gets an attribute of this element as an interface type. <br/>                                                                                         |
| [**GetAttributeValue(PCWSTR, D2D1\_FILL\_MODE \*)**](https://msdn.microsoft.com/en-us/library/Mt797851(v=VS.85).aspx)                              | Gets an attribute of this element as a fill mode. This method can be used to get the value of the fill-rule or clip-rule properties.<br/>             |
| [**GetAttributeValue(PCWSTR, ID2D1SvgPaint \*\*)**](https://msdn.microsoft.com/en-us/library/Mt797843(v=VS.85).aspx)                              | Gets an attribute of this element as a paint. This method can be used to get the value of the fill or stroke properties.<br/>                         |
| [**GetAttributeValue(PCWSTR, D2D1\_SVG\_LENGTH \*)**](https://msdn.microsoft.com/en-us/library/Mt797841(v=VS.85).aspx)                            | Gets an attribute of this element as a length value.<br/>                                                                                             |
| [**GetAttributeValue(PCWSTR, D2D1\_SVG\_DISPLAY \*)**](https://msdn.microsoft.com/en-us/library/Mt797852(v=VS.85).aspx)                            | Gets an attribute of this element as a display value. This method can be used to get the value of the display property.<br/>                          |
| [**GetAttributeValue(PCWSTR, D2D1\_EXTEND\_MODE \*)**](https://msdn.microsoft.com/en-us/library/Mt797839(v=VS.85).aspx)                           | Gets an attribute of this element as a extend mode value. This method can be used to get the value of a spreadMethod attribute.<br/>                  |
| [**GetAttributeValue(PCWSTR, D2D1\_SVG\_OVERFLOW \*)**](https://msdn.microsoft.com/en-us/library/Mt797853(v=VS.85).aspx)                           | Gets an attribute of this element as an overflow value. This method can be used to get the value of the overflow property.<br/>                       |
| [**GetAttributeValue(PCWSTR, D2D1\_SVG\_LINE\_CAP \*)**](https://msdn.microsoft.com/en-us/library/Mt797835(v=VS.85).aspx)                         | Gets an attribute of this element as a line cap value. This method can be used to get the value of the stroke-linecap property.<br/>                  |
| [**GetAttributeValue(PCWSTR, D2D1\_MATRIX\_3X2\_F \*)**](https://msdn.microsoft.com/en-us/library/Mt797837(v=VS.85).aspx)                         | Gets an attribute of this element as a matrix value. This method can be used to get the value of a transform or gradientTransform attribute.<br/>     |
| [**GetAttributeValue(PCWSTR, ID2D1SvgPathData \*\*)**](https://msdn.microsoft.com/en-us/library/Mt797847(v=VS.85).aspx)                           | Gets an attribute of this element as path data. This method can be used to get the value of the d attribute on a path element.<br/>                   |
| [**GetAttributeValue(PCWSTR, D2D1\_SVG\_LINE\_JOIN \*)**](https://msdn.microsoft.com/en-us/library/Mt797854(v=VS.85).aspx)                         | Gets an attribute of this element as a line join value. This method can be used to get the value of the stroke-linejoin property.<br/>                |
| [**GetAttributeValue(PCWSTR, D2D1\_SVG\_UNIT\_TYPE \*)**](https://msdn.microsoft.com/en-us/library/Mt797838(v=VS.85).aspx)                        | Gets an attribute of this element as a unit type value. This method can be used to get the value of a gradientUnits or clipPathUnits attribute.<br/>  |
| [**GetAttributeValue(PCWSTR, ID2D1SvgAttribute \*\*)**](https://msdn.microsoft.com/en-us/library/Mt797842(v=VS.85).aspx)                          | Gets an attribute of this element.<br/>                                                                                                               |
| [**GetAttributeValue(PCWSTR, D2D1\_SVG\_VISIBILITY \*)**](https://msdn.microsoft.com/en-us/library/Mt797836(v=VS.85).aspx)                        | Gets an attribute of this element as a visibility value. This method can be used to get the value of the visibility property.<br/>                    |
| [**GetAttributeValue(PCWSTR, ID2D1SvgStrokeDashArray \*\*)**](https://msdn.microsoft.com/en-us/library/Mt797844(v=VS.85).aspx)                    | Gets an attribute of this element as a stroke dash array. This method can be used to get the value of the stroke-dasharray property.<br/>             |
| [**GetAttributeValue(PCWSTR, ID2D1SvgPointCollection \*\*)**](https://msdn.microsoft.com/en-us/library/Mt797846(v=VS.85).aspx)                    | Gets an attribute of this element as points. This method can be used to get the value of the points attribute on a polygon or polyline element.<br/>  |
| [**GetAttributeValue(PCWSTR, D2D1\_SVG\_PRESERVE\_ASPECT\_RATIO \*)**](https://msdn.microsoft.com/en-us/library/Mt797840(v=VS.85).aspx)           | Gets an attribute of this element as a preserve aspect ratio value. This method can be used to get the value of a preserveAspectRatio attribute.<br/> |
| [**GetAttributeValue(PCWSTR, D2D1\_SVG\_ATTRIBUTE\_POD\_TYPE, void \*, UINT32)**](https://msdn.microsoft.com/en-us/library/Mt797845(v=VS.85).aspx) | Gets an attribute of this element as a POD type.<br/>                                                                                                 |
| [**GetAttributeValue(PCWSTR, D2D1\_SVG\_ATTRIBUTE\_STRING\_TYPE, PWSTR, UINT32)**](https://msdn.microsoft.com/en-us/library/Mt797833(v=VS.85).aspx)  | Gets an attribute of this element as a string. <br/>                                                                                                  |



## See also

<dl> <dt>

[**ID2D1SvgElement**](https://msdn.microsoft.com/en-us/library/Mt797830(v=VS.85).aspx)
</dt> </dl>

 

 





