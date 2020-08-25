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
| [**GetAttributeValue(PCWSTR, FLOAT \*)**](/windows/win32/api/d2d1svg/nf-d2d1svg-id2d1svgelement-getattributevalue(pcwstr_float))                                         | Gets an attribute of this element as a float.<br/>                                                                                                    |
| [**GetAttributeValue(PCWSTR, D2D1\_COLOR\_F \*)**](/windows/win32/api/rrascfg/nn-rrascfg-ieapproviderconfig)                                | Gets an attribute of this element as a color.<br/>                                                                                                    |
| [**GetAttributeValue(PCWSTR, REFIID, void \*\*)**](/windows/win32/api/d2d1svg/nf-d2d1svg-id2d1svgelement-getattributevalue(pcwstr_refiid_void))                                | Gets an attribute of this element as an interface type. <br/>                                                                                         |
| [**GetAttributeValue(PCWSTR, D2D1\_FILL\_MODE \*)**](/windows/win32/api/d2d1svg/nf-d2d1svg-id2d1svgelement-getattributevalue(pcwstr_d2d1_fill_mode))                              | Gets an attribute of this element as a fill mode. This method can be used to get the value of the fill-rule or clip-rule properties.<br/>             |
| [**GetAttributeValue(PCWSTR, ID2D1SvgPaint \*\*)**](/windows/win32/api/d2d1svg/nf-d2d1svg-id2d1svgelement-getattributevalue(pcwstr_id2d1svgpaint))                              | Gets an attribute of this element as a paint. This method can be used to get the value of the fill or stroke properties.<br/>                         |
| [**GetAttributeValue(PCWSTR, D2D1\_SVG\_LENGTH \*)**](/windows/win32/api/d2d1svg/nf-d2d1svg-id2d1svgelement-getattributevalue(pcwstr_d2d1_svg_length))                            | Gets an attribute of this element as a length value.<br/>                                                                                             |
| [**GetAttributeValue(PCWSTR, D2D1\_SVG\_DISPLAY \*)**](/windows/win32/api/d2d1svg/nf-d2d1svg-id2d1svgelement-getattributevalue(pcwstr_d2d1_svg_display))                            | Gets an attribute of this element as a display value. This method can be used to get the value of the display property.<br/>                          |
| [**GetAttributeValue(PCWSTR, D2D1\_EXTEND\_MODE \*)**](/windows/win32/api/d2d1svg/nf-d2d1svg-id2d1svgelement-getattributevalue(pcwstr_d2d1_extend_mode))                           | Gets an attribute of this element as a extend mode value. This method can be used to get the value of a spreadMethod attribute.<br/>                  |
| [**GetAttributeValue(PCWSTR, D2D1\_SVG\_OVERFLOW \*)**](/windows/win32/api/d2d1svg/nf-d2d1svg-id2d1svgelement-getattributevalue(pcwstr_d2d1_svg_overflow))                           | Gets an attribute of this element as an overflow value. This method can be used to get the value of the overflow property.<br/>                       |
| [**GetAttributeValue(PCWSTR, D2D1\_SVG\_LINE\_CAP \*)**](/windows/win32/api/d2d1svg/nf-d2d1svg-id2d1svgelement-getattributevalue(pcwstr_d2d1_svg_line_cap))                         | Gets an attribute of this element as a line cap value. This method can be used to get the value of the stroke-linecap property.<br/>                  |
| [**GetAttributeValue(PCWSTR, D2D1\_MATRIX\_3X2\_F \*)**](/windows/win32/api/d2d1svg/nf-d2d1svg-id2d1svgelement-getattributevalue(pcwstr_d2d1_matrix_3x2_f))                         | Gets an attribute of this element as a matrix value. This method can be used to get the value of a transform or gradientTransform attribute.<br/>     |
| [**GetAttributeValue(PCWSTR, ID2D1SvgPathData \*\*)**](/windows/win32/api/d2d1svg/nf-d2d1svg-id2d1svgelement-getattributevalue(pcwstr_id2d1svgpathdata))                           | Gets an attribute of this element as path data. This method can be used to get the value of the d attribute on a path element.<br/>                   |
| [**GetAttributeValue(PCWSTR, D2D1\_SVG\_LINE\_JOIN \*)**](/windows/win32/api/d2d1svg/nf-d2d1svg-id2d1svgelement-getattributevalue(pcwstr_d2d1_svg_line_join))                         | Gets an attribute of this element as a line join value. This method can be used to get the value of the stroke-linejoin property.<br/>                |
| [**GetAttributeValue(PCWSTR, D2D1\_SVG\_UNIT\_TYPE \*)**](/windows/win32/api/d2d1svg/nf-d2d1svg-id2d1svgelement-getattributevalue(pcwstr_d2d1_svg_unit_type))                        | Gets an attribute of this element as a unit type value. This method can be used to get the value of a gradientUnits or clipPathUnits attribute.<br/>  |
| [**GetAttributeValue(PCWSTR, ID2D1SvgAttribute \*\*)**](/windows/win32/api/d2d1svg/nf-d2d1svg-id2d1svgelement-getattributevalue(pcwstr_id2d1svgattribute))                          | Gets an attribute of this element.<br/>                                                                                                               |
| [**GetAttributeValue(PCWSTR, D2D1\_SVG\_VISIBILITY \*)**](/windows/win32/api/d2d1svg/nf-d2d1svg-id2d1svgelement-getattributevalue(pcwstr_d2d1_svg_visibility))                        | Gets an attribute of this element as a visibility value. This method can be used to get the value of the visibility property.<br/>                    |
| [**GetAttributeValue(PCWSTR, ID2D1SvgStrokeDashArray \*\*)**](/windows/win32/api/d2d1svg/nf-d2d1svg-id2d1svgelement-getattributevalue(pcwstr_id2d1svgstrokedasharray))                    | Gets an attribute of this element as a stroke dash array. This method can be used to get the value of the stroke-dasharray property.<br/>             |
| [**GetAttributeValue(PCWSTR, ID2D1SvgPointCollection \*\*)**](/windows/win32/api/d2d1svg/nf-d2d1svg-id2d1svgelement-getattributevalue(pcwstr_id2d1svgpointcollection))                    | Gets an attribute of this element as points. This method can be used to get the value of the points attribute on a polygon or polyline element.<br/>  |
| [**GetAttributeValue(PCWSTR, D2D1\_SVG\_PRESERVE\_ASPECT\_RATIO \*)**](/windows/win32/api/d2d1svg/nf-d2d1svg-id2d1svgelement-getattributevalue(pcwstr_d2d1_svg_preserve_aspect_ratio))           | Gets an attribute of this element as a preserve aspect ratio value. This method can be used to get the value of a preserveAspectRatio attribute.<br/> |
| [**GetAttributeValue(PCWSTR, D2D1\_SVG\_ATTRIBUTE\_POD\_TYPE, void \*, UINT32)**](/windows/win32/api/d2d1svg/nf-d2d1svg-id2d1svgelement-getattributevalue(pcwstr_d2d1_svg_attribute_pod_type_void_uint32)) | Gets an attribute of this element as a POD type.<br/>                                                                                                 |
| [**GetAttributeValue(PCWSTR, D2D1\_SVG\_ATTRIBUTE\_STRING\_TYPE, PWSTR, UINT32)**](/windows/win32/api/d2d1svg/nf-d2d1svg-id2d1svgelement-getattributevalue(pcwstr_d2d1_color_f))  | Gets an attribute of this element as a string. <br/>                                                                                                  |



## See also

<dl> <dt>

[**ID2D1SvgElement**](/windows/win32/api/d2d1svg/nn-d2d1svg-id2d1svgelement)
</dt> </dl>

 

