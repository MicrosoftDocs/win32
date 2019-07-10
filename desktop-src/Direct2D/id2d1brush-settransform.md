---
title: ID2D1Brush SetTransform methods
description: Sets the transformation applied to the brush.
ms.assetid: 57afadc1-88c9-4a5b-a83f-63c4c69182a7
keywords:
- SetTransform methods Direct2D
topic_type:
- apiref
api_location:
- D2d1.dll
api_type:
- DllExport
ms.date: 07/02/2019
---

# ID2D1Brush::SetTransform methods

Sets the transformation applied to the brush.

### Overload list



| Method                                                                                       | Description                                              |
|:---------------------------------------------------------------------------------------------|:---------------------------------------------------------|
| [**SetTransform(D2D1\_MATRIX\_3X2\_F&)**](https://msdn.microsoft.com/en-us/library/Dd371186(v=VS.85).aspx)  | Sets the transformation applied to the brush.<br/> |
| [**SetTransform(D2D1\_MATRIX\_3X2\_F\*)**](https://msdn.microsoft.com/en-us/library/Dd371184(v=VS.85).aspx) | Sets the transformation applied to the brush.<br/> |



## Remarks

When you paint with a brush, it paints in the coordinate space of the render target. Brushes do not automatically position themselves to align with the object being painted; by default, they begin painting at the origin (0, 0) of the render target.

You can "move" the gradient defined by an [**ID2D1LinearGradientBrush**](https://msdn.microsoft.com/en-us/library/Dd371488(v=VS.85).aspx) to a target area by setting its start point and end point. Likewise, you can move the gradient defined by an [**ID2D1RadialGradientBrush**](https://msdn.microsoft.com/en-us/library/Dd371529(v=VS.85).aspx) by changing its center and radii.

To align the content of an [**ID2D1BitmapBrush**](https://msdn.microsoft.com/en-us/library/Dd371122(v=VS.85).aspx) to the area being painted, you can use the **SetTransform** method to translate the bitmap to the desired location. This transform only affects the brush; it does not affect any other content drawn by the render target.

The following illustrations show the effect of using an [**ID2D1BitmapBrush**](https://msdn.microsoft.com/en-us/library/Dd371122(v=VS.85).aspx) to fill a rectangle located at (100, 100). The illustration on the left illustration shows the result of filling the rectangle without transforming the brush: the bitmap is drawn at the render target's origin. As a result, only a portion of the bitmap appears in the rectangle.

The illustration on the right shows the result of transforming the [**ID2D1BitmapBrush**](https://msdn.microsoft.com/en-us/library/Dd371122(v=VS.85).aspx) so that its content is shifted 50 pixels to the right and 50 pixels down. The bitmap now fills the rectangle.

![illustration of two squares, one painted with a bitmap without a transformed brush and one painted with a transformed brush](images/brushes-ovw-transform.png)

## Examples

The following code examples show how to create the transformation shown in the right diagram in the preceding illustration. First apply a translation to the [**ID2D1BitmapBrush**](https://msdn.microsoft.com/en-us/library/Dd371122(v=VS.85).aspx), moving the brush 50 pixels right along the x-axis and 50 pixels down along the y-axis. Then use the **ID2D1BitmapBrush** to fill the rectangle that has the upper-left corner at (100, 100) and the lower-right corner at (200, 200).


```C++
// Create the bitmap to be used by the bitmap brush.
if (SUCCEEDED(hr))
{
    hr = LoadResourceBitmap(
        m_pRenderTarget,
        m_pWICFactory,
        L"FERN",
        L"Image",
        &amp;m_pBitmap
        );
   
}
```




```C++
if (SUCCEEDED(hr))
{
    hr = m_pRenderTarget->CreateBitmapBrush(
        m_pBitmap,
        &amp;m_pBitmapBrush
        );
}
```




```C++
D2D1_RECT_F rcTransformedBrushRect = D2D1::RectF(100, 100, 200, 200);



 // Demonstrate the effect of transforming a bitmap brush.
 m_pBitmapBrush->SetTransform(
     D2D1::Matrix3x2F::Translation(D2D1::SizeF(50,50))
     );

 // To see the content of the rcTransformedBrushRect, comment
 // out this statement.
 m_pRenderTarget->FillRectangle(
     &rcTransformedBrushRect, 
     m_pBitmapBrush
     );

 m_pRenderTarget-&gt;DrawRectangle(rcTransformedBrushRect, m_pBlackBrush, 1, NULL);
```





## Requirements



|                    |                                                                                                       |
|--------------------|-------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D2d1\_1.h (include D2d1.h)</dt> </dl> |
| Library<br/> | <dl> <dt>D2d1.lib</dt> </dl>                   |
| DLL<br/>     | <dl> <dt>D2d1.dll</dt> </dl>                   |



## See also

<dl> <dt>

[Brushes Overview](direct2d-brushes-overview.md)
</dt> <dt>

[**ID2D1Brush**](https://msdn.microsoft.com/en-us/library/Dd371173(v=VS.85).aspx)
</dt> </dl>

�

�





