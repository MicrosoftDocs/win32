---
title: ID2D1SvgElement SetAttributeValue methods (D2d1svg.h)
description: Sets an attribute of this element.
ms.assetid: 33403a07-28d1-4138-ea7f-04f3ac42a8f7
keywords:
- SetAttributeValue methods Direct2D
topic_type:
- apiref
api_location:
- d2d1svg.h
api_type:
- HeaderDef
ms.date: 07/02/2019
ms.topic: reference
---

# ID2D1SvgElement::SetAttributeValue methods

Sets an attribute of this element.

### Overload list



| Method                                                                                                                      | Description                                                                                                                                                 |
|:----------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**SetAttributeValue(PCWSTR, FLOAT)**](/windows/win32/api/d2d1svg/nf-d2d1svg-id2d1svgelement-setattributevalue(pcwstr_float))                                             | Sets an attribute of this element using a float.<br/>                                                                                                 |
| [**SetAttributeValue(PCWSTR, D2D1\_COLOR\_F &)**](/windows/win32/api/d2d1svg/nf-d2d1svg-id2d1svgelement-setattributevalue(pcwstr_constd2d1_color_f_))                                  | Sets an attribute of this element as a color.<br/>                                                                                                    |
| [**SetAttributeValue(PCWSTR, D2D1\_FILL\_MODE)**](/windows/win32/api/d2d1svg/nf-d2d1svg-id2d1svgelement-setattributevalue(pcwstr_d2d1_fill_mode))                                  | Sets an attribute of this element as a fill mode. This method can be used to set the value of the 'fill-rule' or 'clip-rule' properties.<br/>         |
| [**SetAttributeValue(PCWSTR, D2D1\_SVG\_DISPLAY)**](/windows/win32/api/d2d1svg/nf-d2d1svg-id2d1svgelement-setattributevalue(pcwstr_d2d1_svg_display))                                | Gets an attribute of this element as a display value. This method can be used to get the value of the display property.<br/>                          |
| [**SetAttributeValue(PCWSTR, D2D1\_EXTEND\_MODE)**](/windows/win32/api/d2d1svg/nf-d2d1svg-id2d1svgelement-setattributevalue(pcwstr_d2d1_extend_mode))                               | Sets an attribute of this element as an extend mode value. This method can be used to set the value of a spreadMethod attribute.<br/>                 |
| [**SetAttributeValue(PCWSTR, D2D1\_SVG\_OVERFLOW)**](/windows/win32/api/d2d1svg/nf-d2d1svg-id2d1svgelement-setattributevalue(pcwstr_d2d1_svg_overflow))                               | Sets an attribute of this element as an overflow value. This method can be used to set the value of the overflow property.<br/>                       |
| [**SetAttributeValue(PCWSTR, D2D1\_SVG\_LINE\_CAP)**](/windows/win32/api/d2d1svg/nf-d2d1svg-id2d1svgelement-setattributevalue(pcwstr_d2d1_svg_line_cap))                             | Sets an attribute of this element as a line cap value. This method can be used to set the value of the stroke-linecap property.<br/>                  |
| [**SetAttributeValue(PCWSTR, D2D1\_SVG\_LENGTH &)**](/windows/win32/api/d2d1svg/nf-d2d1svg-id2d1svgelement-setattributevalue(pcwstr_constd2d1_svg_length_))                              | Sets an attribute of this element as a length value.<br/>                                                                                             |
| [**SetAttributeValue(PCWSTR, D2D1\_SVG\_LINE\_JOIN)**](/windows/win32/api/d2d1svg/nf-d2d1svg-id2d1svgelement-setattributevalue(pcwstr_d2d1_svg_line_join))                             | Sets an attribute of this element as a line join value. This method can be used to set the value of the stroke-linejoin property.<br/>                |
| [**SetAttributeValue(PCWSTR, D2D1\_SVG\_UNIT\_TYPE)**](/windows/win32/api/d2d1svg/nf-d2d1svg-id2d1svgelement-setattributevalue(pcwstr_d2d1_svg_unit_type))                            | Sets an attribute of this element as a unit type value. This method can be used to set the value of a gradientUnits or clipPathUnits attribute.<br/>  |
| [**SetAttributeValue(PCWSTR, ID2D1SvgAttribute \*)**](/windows/win32/api/d2d1svg/nf-d2d1svg-id2d1svgelement-setattributevalue(pcwstr_id2d1svgattribute))                              | Sets an attribute of this element using an interface.<br/>                                                                                            |
| [**SetAttributeValue(PCWSTR, D2D1\_SVG\_VISIBILITY)**](/windows/win32/api/d2d1svg/nf-d2d1svg-id2d1svgelement-setattributevalue(pcwstr_d2d1_svg_visibility))                            | Sets an attribute of this element as a visibility value. This method can be used to set the value of the visibility property.<br/>                    |
| [**SetAttributeValue(PCWSTR, D2D1\_MATRIX\_3X2\_F &)**](/windows/win32/api/d2d1svg/nf-d2d1svg-id2d1svgelement-setattributevalue(pcwstr_constd2d1_matrix_3x2_f_))                           | Sets an attribute of this element as a matrix value. This method can be used to set the value of a transform or gradientTransform attribute.<br/>     |
| [**SetAttributeValue(PCWSTR, D2D1\_SVG\_PRESERVE\_ASPECT\_RATIO &)**](/windows/win32/api/d2d1svg/nf-d2d1svg-id2d1svgelement-setattributevalue(pcwstr_constd2d1_svg_preserve_aspect_ratio_))             | Sets an attribute of this element as a preserve aspect ratio value. This method can be used to set the value of a preserveAspectRatio attribute.<br/> |
| [**SetAttributeValue(PCWSTR, D2D1\_SVG\_ATTRIBUTE\_STRING\_TYPE, PCWSTR)**](/windows/win32/api/d2d1svg/nf-d2d1svg-id2d1svgelement-setattributevalue(pcwstr_d2d1_svg_attribute_string_type_pcwstr))          | Sets an attribute of this element using a string. <br/>                                                                                               |
| [**SetAttributeValue(PCWSTR, D2D1\_SVG\_ATTRIBUTE\_POD\_TYPE , void \*, UINT32)**](/windows/win32/api/d2d1svg/nf-d2d1svg-id2d1svgelement-setattributevalue(pcwstr_d2d1_svg_attribute_pod_type_constvoid_uint32)) | Sets an attribute of this element using a POD type.<br/>                                                                                              |



## Requirements



| Requirement | Value |
|-------------------|--------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D2d1svg.h</dt> </dl> |



## See also

<dl> <dt>

[**ID2D1SvgElement**](/windows/win32/api/d2d1svg/nn-d2d1svg-id2d1svgelement)
</dt> </dl>

�

�
