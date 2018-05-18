---
title: How to Create a Bitmap Brush
description: Shows how to create a bitmap brush using Direct2D.
ms.assetid: '8f78b30a-7507-4dd8-b6f4-12d88e3c9a1d'
---

# How to Create a Bitmap Brush

To create a bitmap brush, use the [**ID2D1RenderTarget::CreateBitmapBrush**](id2d1rendertarget-createbitmapbrush.md) method and specify the bitmap brush properties. Some overloads enable you to specify the brush properties. The following code shows how to create a bitmap brush to fill a square, and a solid black brush to draw the outline of the square. The code produces the output shown in the following screen shot.

> [!Note]  
> Starting with Windows 8, you can use the [**CreateBitmapBrush**](id2d1devicecontext-createbitmapbrush.md) method on the [**ID2D1DeviceContext**](id2d1devicecontext.md) interface to create a [**ID2D1BitmapBrush**](id2d1bitmapbrush.md) instead of a **ID2D1BitmapBrush**. **ID2D1BitmapBrush** adds high-quality scaling modes to the bitmap brush.

 

![screen shot of a square filled with a plant bitmap](images/brushes-ovw-bitmap.png)

1.  Declare a variable of type [**ID2D1BitmapBrush**](id2d1bitmapbrush.md).
    ```C++
        ID2D1BitmapBrush *m_pBitmapBrush;
    ```

    

2.  Load a bitmap from a resource. For more information, see [How to Load a Bitmap from a Resource](how-to-load-a-bitmap-from-a-resource.md).
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
    ```

    

3.  Choose the extend modes ([**D2D1\_EXTEND\_MODE**](d2d1-extend-mode.md)) and interpolation mode ([**D2D1\_BITMAP\_INTERPOLATION\_MODE**](d2d1-bitmap-interpolation-mode.md)) of the bitmap brush and then call the [**CreateBitmapBrush**](id2d1rendertarget-createbitmapbrush.md) method to create a brush, as shown in the following code.
    ```C++
    hr = m_pRenderTarget->CreateBitmapBrush(
        m_pBitmap,
        &amp;m_pBitmapBrush
        );
    ```

    

## Related topics

<dl> <dt>

[Direct2D Reference](reference.md)
</dt> </dl>

 

 




