---
title: Render Using Direct2D
description: Direct2D provides methods for rendering either text with formatting described by only an IDWriteTextFormat or an IDWriteTextLayout to a Direct2D surface.
ms.assetid: 4acd1aee-98bf-4ca3-b4dc-b73c96c6ca63
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Render Using Direct2D

Direct2D provides methods for rendering either text with formatting described by only an [**IDWriteTextFormat**](/windows/desktop/api/dwrite/) or an [**IDWriteTextLayout**](/windows/desktop/api/dwrite/) to a Direct2D surface.

## Rendering Text Described by IDWriteTextFormat

To render a string using an [**IDWriteTextFormat**](/windows/desktop/api/dwrite/) object to describe the formatting for the entire string, use the [**ID2D1RenderTarget::DrawText**](https://msdn.microsoft.com/library/windows/desktop/dd371919) method provided by [Direct2D](https://msdn.microsoft.com/03b3b91c-9751-4f8d-af24-85067f06930b).

1.  Define the area for the text layout by retrieving the dimensions of the rendering area, and create a [Direct2D](https://msdn.microsoft.com/03b3b91c-9751-4f8d-af24-85067f06930b) rectangle that has the same dimensions.
    ```C++
    D2D1_RECT_F layoutRect = D2D1::RectF(
        static_cast<FLOAT>(rc.left) / dpiScaleX_,
        static_cast<FLOAT>(rc.top) / dpiScaleY_,
        static_cast<FLOAT>(rc.right - rc.left) / dpiScaleX_,
        static_cast<FLOAT>(rc.bottom - rc.top) / dpiScaleY_
        );
    
    ```

    

2.  Use the [**ID2D1RenderTarget::DrawText**](https://msdn.microsoft.com/library/windows/desktop/dd371919) method and the [**IDWriteTextFormat**](/windows/desktop/api/dwrite/) object to render text to the screen. The **ID2D1RenderTarget::DrawText** method takes the following parameters:
    -   A string to render.
    -   A pointer to an [**IDWriteTextFormat**](/windows/desktop/api/dwrite/) interface.
    -   A [Direct2D](https://msdn.microsoft.com/03b3b91c-9751-4f8d-af24-85067f06930b) layout rectangle.
    -   A pointer to an interface that exposes [**ID2D1Brush**](https://msdn.microsoft.com/library/windows/desktop/dd371173).

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

To draw the text with the text layout settings specified by the [**IDWriteTextLayout**](/windows/desktop/api/dwrite/) object, change the code in the MultiformattedText::DrawText method to use [**IDWriteTextLayout::DrawTextLayout**](https://msdn.microsoft.com/library/windows/desktop/dd371913).

1.  Delcare a [**D2D1\_POINT\_2F**](https://msdn.microsoft.com/library/windows/desktop/dd368140) variable and set it to the upper-left point of the window.
    ```C++
    D2D1_POINT_2F origin = D2D1::Point2F(
        static_cast<FLOAT>(rc.left / dpiScaleX_),
        static_cast<FLOAT>(rc.top / dpiScaleY_)
        );
    
    ```

    

2.  Draw the text to the screen by calling the [**ID2D1RenderTarget::DrawTextLayout**](https://msdn.microsoft.com/library/windows/desktop/dd371913) method of the [Direct2D](https://msdn.microsoft.com/03b3b91c-9751-4f8d-af24-85067f06930b) render target and passing the [**IDWriteTextLayout**](/windows/desktop/api/dwrite/) pointer.
    ```C++
    pRT_->DrawTextLayout(
        origin,
        pTextLayout_,
        pBlackBrush_
        );
    
    ```

    

 

 




