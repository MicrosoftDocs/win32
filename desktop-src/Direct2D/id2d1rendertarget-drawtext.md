---
title: ID2D1RenderTarget DrawText methods
description: Draws the specified text using the format information provided by an IDWriteTextFormat object.
ms.assetid: 7cda7854-f9df-48d3-bc62-6aaee769e6f9
keywords:
- DrawText methods Direct2D
topic_type:
- apiref
api_location:
- D2d1.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
api_name: 
---

# ID2D1RenderTarget::DrawText methods

Draws the specified text using the format information provided by an [**IDWriteTextFormat**](/windows/desktop/api/dwrite/nn-dwrite-idwritetextformat) object.

### Overload list



| Method                                                                                                                                                                                                                                                                               | Description                                                                                                                                     |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DrawText(WCHAR\*,IDWriteTextFormat\*,D2D1\_RECT\_F&,ID2D1Brush\*,D2D1\_DRAW\_TEXT\_OPTIONS,DWRITE\_TEXT\_MEASURING\_METHOD)**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-drawtext(constwchar_uint32_idwritetextformat_constd2d1_rect_f__id2d1brush_d2d1_draw_text_options_dwrite_measuring_mode))  | Draws the specified text using the format information provided by an [**IDWriteTextFormat**](/windows/desktop/api/dwrite/nn-dwrite-idwritetextformat) object.<br/>  |
| [**DrawText(WCHAR\*,IDWriteTextFormat\*,D2D1\_RECT\_F\*,ID2D1Brush\*,D2D1\_DRAW\_TEXT\_OPTIONS,DWRITE\_TEXT\_MEASURING\_METHOD)**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-drawtext(constwchar_uint32_idwritetextformat_constd2d1_rect_f_id2d1brush_d2d1_draw_text_options_dwrite_measuring_mode)) | Draws the specified text using the format information provided by an [**IDWriteTextFormat**](/windows/desktop/api/dwrite/nn-dwrite-idwritetextformat) object. <br/> |



## Remarks

To draw text with Direct2D, use the [**ID2D1RenderTarget::DrawText**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-drawtext(constwchar_uint32_idwritetextformat_constd2d1_rect_f__id2d1brush_d2d1_draw_text_options_dwrite_measuring_mode)) method for text that has a single format, or the [**ID2D1RenderTarget::DrawTextLayout**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-drawtextlayout) method when you need multiple formats, advanced OpenType features, or hit testing. These methods use the DirectWrite API to provide high-quality text display.

This method doesn't return an error code if it fails. To determine whether a drawing operation (such as **DrawText**) failed, check the result returned by the [**ID2D1RenderTarget::EndDraw**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-enddraw) or [**ID2D1RenderTarget::Flush**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-flush) methods.

## Examples

For an example, see [How to Draw Text](how-to--draw-text.md).

## Requirements



| Requirement | Value |
|--------------------|-------------------------------------------------------------------------------------|
| Library<br/> | <dl> <dt>D2d1.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>D2d1.dll</dt> </dl> |



## See also

<dl> <dt>

[**ID2D1RenderTarget**](/windows/win32/api/d2d1/nn-d2d1-id2d1rendertarget)
</dt> <dt>

[**IDWriteTextFormat**](/windows/desktop/api/dwrite/nn-dwrite-idwritetextformat)
</dt> <dt>

[How to Draw Text](how-to--draw-text.md)
</dt> <dt>

[Text Formatting and Layout Overview](/windows/desktop/DirectWrite/text-formatting-and-layout)
</dt> </dl>

 

