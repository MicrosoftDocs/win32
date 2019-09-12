---
title: Render Using Direct2D
description: Direct2D provides methods for rendering either text with formatting described by only an IDWriteTextFormat or an IDWriteTextLayout to a Direct2D surface.
ms.assetid: 4acd1aee-98bf-4ca3-b4dc-b73c96c6ca63
ms.topic: article
ms.date: 05/31/2018
---

# Render Using Direct2D

Direct2D provides methods for rendering either text with formatting described by only an [**IDWriteTextFormat**](https://msdn.microsoft.com/en-us/library/Dd316628(v=VS.85).aspx) or an [**IDWriteTextLayout**](https://msdn.microsoft.com/en-us/library/Dd316718(v=VS.85).aspx) to a Direct2D surface.

## Rendering Text Described by IDWriteTextFormat

To render a string using an [**IDWriteTextFormat**](https://msdn.microsoft.com/en-us/library/Dd316628(v=VS.85).aspx) object to describe the formatting for the entire string, use the [**ID2D1RenderTarget::DrawText**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-drawtext(constwchar_uint32_idwritetextformat_constd2d1_rect_f__id2d1brush_d2d1_draw_text_options_dwrite_measuring_mode)) method provided by [Direct2D](https://msdn.microsoft.com/en-us/library/Dd370990(v=VS.85).aspx).

1.  Define the area for the text layout by retrieving the dimensions of the rendering area, and create a [Direct2D](https://msdn.microsoft.com/en-us/library/Dd370990(v=VS.85).aspx) rectangle that has the same dimensions.
    ```C++
    D2D1_RECT_F layoutRect = D2D1::RectF(
        static_cast<FLOAT>(rc.left) / dpiScaleX_,
        static_cast<FLOAT>(rc.top) / dpiScaleY_,
        static_cast<FLOAT>(rc.right - rc.left) / dpiScaleX_,
        static_cast<FLOAT>(rc.bottom - rc.top) / dpiScaleY_
        );
    
    ```

    

2.  Use the [**ID2D1RenderTarget::DrawText**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-drawtext(constwchar_uint32_idwritetextformat_constd2d1_rect_f__id2d1brush_d2d1_draw_text_options_dwrite_measuring_mode)) method and the [**IDWriteTextFormat**](https://msdn.microsoft.com/en-us/library/Dd316628(v=VS.85).aspx) object to render text to the screen. The **ID2D1RenderTarget::DrawText** method takes the following parameters:
    -   A string to render.
    -   A pointer to an [**IDWriteTextFormat**](https://msdn.microsoft.com/en-us/library/Dd316628(v=VS.85).aspx) interface.
    -   A [Direct2D](https://msdn.microsoft.com/en-us/library/Dd370990(v=VS.85).aspx) layout rectangle.
    -   A pointer to an interface that exposes [**ID2D1Brush**](/windows/win32/api/d2d1/nn-d2d1-id2d1brush).

    ```C++
    pRT_->DrawText(
        wszText_,        // The string to render.
        cTextLength_,    // The string's length.
        pTextFormat_,    // The text format.
        layoutRect,       // The region of the window where the text will be rendered.
        pBlackBrush_     // The brush used to draw the text.
        );
    
    ```

    

## Rendering a IDWriteText Layout Object

To draw the text with the text layout settings specified by the [**IDWriteTextLayout**](https://msdn.microsoft.com/en-us/library/Dd316718(v=VS.85).aspx) object, change the code in the MultiformattedText::DrawText method to use [**IDWriteTextLayout::DrawTextLayout**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-drawtextlayout).

1.  Delcare a [**D2D1\_POINT\_2F**](/windows/win32/Direct2D/d2d1-point-2f) variable and set it to the upper-left point of the window.
    ```C++
    D2D1_POINT_2F origin = D2D1::Point2F(
        static_cast<FLOAT>(rc.left / dpiScaleX_),
        static_cast<FLOAT>(rc.top / dpiScaleY_)
        );
    
    ```

    

2.  Draw the text to the screen by calling the [**ID2D1RenderTarget::DrawTextLayout**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-drawtextlayout) method of the [Direct2D](https://msdn.microsoft.com/en-us/library/Dd370990(v=VS.85).aspx) render target and passing the [**IDWriteTextLayout**](https://msdn.microsoft.com/en-us/library/Dd316718(v=VS.85).aspx) pointer.
    ```C++
    pRT_->DrawTextLayout(
        origin,
        pTextLayout_,
        pBlackBrush_
        );
    
    ```

    

 

 




