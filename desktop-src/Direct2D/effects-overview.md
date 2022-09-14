---
title: Effects (Direct2D)
description: An overview of Direct2D effects.
ms.assetid: 1446BDA9-AD4C-472C-8F1D-82ABC1880E13
ms.topic: article
ms.date: 05/31/2018
---

# Effects

## What are Direct2D effects?

You can use Direct2D to apply one or more high quality effects to an image or a set of images. The effects APIs are built on [Direct3D 11](/windows/desktop/direct3d11/direct3d-11-features) and take advantage of GPU features for image processing. You can chain effects in an effect graph and compose or blend the output of effects.

A Direct2D effect performs an imaging task, like changing brightness, de-saturating an image, or creating a drop shadow. Effects can accept zero or more input images, expose multiple properties that control their operation, and generate a single output image.

Each effect creates an internal transform graph made up of individual transforms. Each transform represents a single image operation. The main purpose of a transform is to house the shaders that are executed for each output pixel. These shaders can include pixel shaders, vertex shaders, the blend stage of a GPU, and compute shaders.

Both the [Direct2D](./direct2d-portal.md) [built-in effects](built-in-effects.md) and custom effects you can make using the [custom effects API](custom-effects.md) work this way.

There are a range of [built-in effects](built-in-effects.md) from categories like the ones here. See the [Built-in Effects](built-in-effects.md) section for a full list.

-   [Filtering](built-in-effects.md)
-   [Composition and Blending](built-in-effects.md)
-   [Transparency](built-in-effects.md)
-   [Color](built-in-effects.md)
-   [Lighting and Stylizing](built-in-effects.md)
-   [Transforming and Scaling](built-in-effects.md)
-   [Sources](built-in-effects.md)

You can apply effects to any bitmap, including: images loaded by the [Windows Imaging Component (WIC)](/windows/desktop/wic/-wic-api), primitives drawn by [Direct2D](./direct2d-portal.md), text from [DirectWrite](/windows/desktop/DirectWrite/direct-write-portal), or scenes rendered by [Direct3D](/windows/desktop/direct3d10/d3d10-graphics).

With Direct2D effects you can write your own effects that you can use for your applications. A custom effect framework allows you to use GPU features such as pixel shaders, vertex shaders, and the blending unit. You can also include other built-in or custom effects in your custom effect. The framework for building custom effects is the same one that was used to create the built-in effects of [Direct2D](./direct2d-portal.md). The [Direct2D effect author API](custom-effects.md) provides a set of interfaces to create and register effects.

### More effects topics

The rest of this topic explains the basics of Direct2D effects, like applying an effect to an image. The table here has links to additional topics about effects.

| Topic                                                                                                                    | Description                                                                                                                                                                                   |
|--------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Effect Shader Linking](effect-shader-linking.md)<br/>                                                            | Direct2D uses an optimization called effect shader linking which combines multiple effect graph rendering passes into a single pass.<br/>                                               |
| [Custom effects](custom-effects.md)<br/>                                                                          | Shows you how to write your own custom effects using standard HLSL.<br/>                                                                                                                |
| [How to load an image into Direct2D Effects using the FilePicker](load-a-id2d1image-using-the-filepicker.md)<br/> | Shows how to use the [**Windows::Storage::Pickers::FileOpenPicker**](/uwp/api/Windows.Storage.Pickers.FileOpenPicker) to load an image into Direct2D effects.<br/>                                      |
| [How to save Direct2D content to an image file](save-direct2d-content-to-an-image-file.md)<br/>                   | This topic shows how to use [**IWICImageEncoder**](/windows/desktop/api/wincodec/nn-wincodec-iwicimageencoder) to save content in the form of an [**ID2D1Image**](/windows/win32/api/d2d1/nn-d2d1-id2d1image) to an encoded image file such as JPEG.<br/> |
| [How to Apply Effects to Primitives](how-to-apply-effects-to-primitives.md)<br/>                                  | This topic shows how to apply a series of effect to [Direct2D](./direct2d-portal.md) and [DirectWrite](direct2d-and-directwrite.md) primitives.<br/>                           |
| [Controlling Precision and Numerical Clipping in Effect Graphs](precision-and-clipping-in-effect-graphs.md)<br/>  | Applications that render effects using Direct2D must take care to achieve the desired level of quality and predictability with respect to numerical precision. <br/>                    |

## Applying an effect to an image

You can use the Direct2D effects API to apply transforms to images.

> [!Note]  
> This example assumes that you already have [**ID2D1DeviceContext**](/windows/win32/api/d2d1_1/nn-d2d1_1-id2d1devicecontext) and [IWICBitmapSource](/windows/desktop/wic/-wic-imp-iwicbitmapsource) objects created. For more information on creating these objects see [How to load an image into Direct2D effects using the FilePicker](load-a-id2d1image-using-the-filepicker.md) and [Devices and Device Contexts](devices-and-device-contexts.md).

 

1.  Declare an [**ID2D1Effect**](/windows/win32/api/d2d1_1/nn-d2d1_1-id2d1effect) variable and then create a [bitmap source](bitmap-source.md) effect using the [**ID2DDeviceContext::CreateEffect**](/windows/win32/api/d2d1_1/nf-d2d1_1-id2d1devicecontext-createeffect) method.

    ```C++
        ComPtr<ID2D1Effect> bitmapSourceEffect;

        DX::ThrowIfFailed(m_d2dContext->CreateEffect(CLSID_D2D1BitmapSource, &bitmapSourceEffect));
    ```

    

2.  Set the BitmapSource property to the WIC bitmap source using the [**ID2D1Effect::SetValue**](/windows/win32/api/d2d1_1/nf-d2d1_1-id2d1properties-setvalue(uint32_constbyte_uint32)).

    ```C++
            DX::ThrowIfFailed(m_bitmapSourceEffect->SetValue(D2D1_BITMAPSOURCE_PROP_WIC_BITMAP_SOURCE, m_wicBitmapSource.Get()));
    ```

    

3.  Declare an [**ID2D1Effect**](/windows/win32/api/d2d1_1/nn-d2d1_1-id2d1effect) variable and then create the [gaussian blur](gaussian-blur.md) effect.

    ```C++
        ComPtr<ID2D1Effect> gaussianBlurEffect;

        DX::ThrowIfFailed(m_d2dContext->CreateEffect(CLSID_D2D1GaussianBlur, &gaussianBlurEffect));
    ```

    

4.  Set the input to receive the image from the bitmap source effect. Set the blur amount the [**SetValue**](/windows/win32/api/d2d1_1/nf-d2d1_1-id2d1properties-setvalue(uint32_constbyte_uint32)) method and the standard deviation property.

    ```C++
        gaussianBlurEffect->SetInputEffect(0, bitmapSourceEffect.Get());

        DX::ThrowIfFailed(gaussianBlurEffect->SetValue(D2D1_GAUSSIANBLUR_PROP_STANDARD_DEVIATION, 6.0f));
    ```

    

5.  Use the device context to draw the resulting image output.

    ```C++
        m_d2dContext->BeginDraw();

        m_d2dContext->Clear(D2D1::ColorF(D2D1::ColorF::CornflowerBlue));

        // Draw the blurred image.
        m_d2dContext->DrawImage(gaussianBlurEffect.Get());

        HRESULT hr = m_d2dContext->EndDraw();
    ```

    

    The [**DrawImage**](/windows/win32/api/d2d1_1/nf-d2d1_1-id2d1devicecontext-drawimage(id2d1image_constd2d1_point_2f_constd2d1_rect_f_d2d1_interpolation_mode_d2d1_composite_mode)) method must be called between the [**ID2DDeviceContext::BeginDraw**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-begindraw) and [**EndDraw**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-enddraw) calls like other Direct2D render operations. **DrawImage** can take an image or the output of an effect and render it to the target surface.

## Spatial Transforms

Direct2D provides built-in effects that can transform images in 2D and 3D space, as well as scaling. The scale and transform effects offer various quality levels like: nearest neighbor, linear, cubic, multi-sample linear, anisotropic, and high quality cubic.

> [!Note]  
> Anisotropic mode generates mipmaps when scaling, however, if you set the **Cached** property to true on the effects that are input to the transform the mipmaps won't be generated every time for sufficiently small images.

 


```C++
ComPtr<ID2D1Effect> affineTransformEffect;
DX::ThrowIfFailed(m_d2dContext->CreateEffect(CLSID_D2D12DAffineTransform, &affineTransformEffect));

affineTransformEffect->SetInput(0, bitmap.Get());

D2D1_MATRIX_3X2_F matrix = D2D1::Matrix3x2F(0.9f, -0.1f,  0.1f, 0.9f, 8.0f, 45.0f);
DX::ThrowIfFailed(affineTransformEffect->SetValue(D2D1_2DAFFINETRANSFORM_PROP_TRANSFORM_MATRIX, matrix));

m_d2dContext->BeginDraw();
m_d2dContext->DrawImage(affineTransformEffect.Get());
m_d2dContext->EndDraw();
```



This use of the 2D affine transform effect rotates the bitmap counterclockwise slightly.



| Before                                                            |
|-------------------------------------------------------------------|
| ![2d affine effect before image.](images/default-before.jpg)      |
| After                                                             |
| ![2d affine effect after image.](images/21-2daffinetransform.png) |



 

## Compositing images

Some effects accept multiple inputs and composite them into one resulting image.

The built-in composite and arithmetic composite effects provide various modes, for more info see the [composite](composite.md) topic. The [blend](blend.md) effect has a variety of GPU accelerated modes available.


```C++
ComPtr<ID2D1Effect> compositeEffect;
DX::ThrowIfFailed(m_d2dContext->CreateEffect(CLSID_D2D1Composite, &compositeEffect));

compositeEffect->SetInput(0, bitmap.Get());
compositeEffect->SetInput(1, bitmapTwo.Get());

m_d2dContext->BeginDraw();
m_d2dContext->DrawImage(compositeEffect.Get());
m_d2dContext->EndDraw();
```



The composite effect combines images in various different ways according to the mode you specify.

## Pixel adjustments

There are a few built-in Direct2D effects that allow you to alter the pixel data. For example, the color matrix effect can be used to change the color of an image.


```C++
ComPtr<ID2D1Effect> colorMatrixEffect;
DX::ThrowIfFailed(m_d2dContext->CreateEffect(CLSID_D2D1ColorMatrix, &colorMatrixEffect));

colorMatrixEffect->SetInput(0, bitmap.Get());

D2D1_MATRIX_5X4_F matrix = D2D1::Matrix5x4F(0, 0, 1, 0,   0, 1, 0, 0,   1, 0, 0, 0,   0, 0, 0, 1,   0, 0, 0, 0);
DX::ThrowIfFailed(colorMatrixEffect->SetValue(D2D1_COLORMATRIX_PROP_COLOR_MATRIX, matrix));

m_d2dContext->BeginDraw();
m_d2dContext->DrawImage(colorMatrixEffect.Get());
m_d2dContext->EndDraw();
```



This code takes the image and alters the color as shown in the example images here.



| Before                                                          |
|-----------------------------------------------------------------|
| ![color matrix effect before image.](images/default-before.jpg) |
| After                                                           |
| ![color matrix effect after image.](images/15-colormatrix.png)  |



 

See the [color built-in effects](how-to-create-a-solid-color-brush.md) section for more info.

## Building effect graphs

You can chain effects together to transform images. For example, the code here applies a shadow and a 2D transform, then composites the results together.


```C++
ComPtr<ID2D1Effect> shadowEffect;
ComPtr<ID2D1Effect> affineTransformEffect;
ComPtr<ID2D1Effect> compositeEffect;

DX::ThrowIfFailed(m_d2dContext->CreateEffect(CLSID_D2D1Shadow, &shadowEffect));
DX::ThrowIfFailed(m_d2dContext->CreateEffect(CLSID_D2D12DAffineTransform, &affineTransformEffect));
DX::ThrowIfFailed(m_d2dContext->CreateEffect(CLSID_D2D1Composite, &compositeEffect));

shadowEffect->SetInput(0, bitmap.Get());
affineTransformEffect->SetInputEffect(0, shadowEffect.Get());

D2D1_MATRIX_3X2_F matrix = D2D1::Matrix3x2F::Translation(20, 20));

affineTransformEffect->SetValue(D2D1_2DAFFINETRANSFORM_PROP_TRANSFORM_MATRIX, matrix);

compositeEffect->SetInputEffect(0, affineTransformEffect.Get());
compositeEffect->SetInput(1, bitmap.Get());

m_d2dContext->BeginDraw();
m_d2dContext->DrawImage(compositeEffect.Get());
m_d2dContext->EndDraw();
```



Here is the result.

![shadow effect output.](images/effect-overview-shadow.png)

Effects take [**ID2D1Image**](/windows/win32/api/d2d1/nn-d2d1-id2d1image) objects as input. You can use an [**ID2D1Bitmap**](/windows/win32/api/d2d1/nn-d2d1-id2d1bitmap) because the interface is derived from **ID2D1Image**. You can also use the [**ID2D1Effect::GetOutput**](/windows/win32/api/d2d1_1/nf-d2d1_1-id2d1effect-getoutput) to get the output of an [**ID2D1Effect**](/windows/win32/api/d2d1_1/nn-d2d1_1-id2d1effect) object as an **ID2D1Image** or use the **SetInputEffect** method, which converts the output for you. In most cases an effect graph consists of **ID2D1Effect** objects directly chained together, which makes it easy to apply multiple effects to an image to create compelling visuals.

See [How to apply effects to primitives](how-to-apply-effects-to-primitives.md) for more info.

## Related topics

[Direct2D basic image effects sample](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/master/Official%20Windows%20Platform%20Sample/Direct2D%20basic%20image%20effects%20sample)

[Built-in Effects](built-in-effects.md)