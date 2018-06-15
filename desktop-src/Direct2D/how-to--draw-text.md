---
title: How to Draw Text
description: Shows how to render text with Direct2D.
ms.assetid: 914dd9d0-78c8-44a3-8504-837faf3201d2
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# How to Draw Text

To draw text with Direct2D, use the [**ID2D1RenderTarget::DrawText**](https://msdn.microsoft.com/en-us/library/Dd371919(v=VS.85).aspx) method for text that has a single format. Or, use the [**ID2D1RenderTarget::DrawTextLayout**](https://msdn.microsoft.com/en-us/library/Dd371913(v=VS.85).aspx) method for multiple formats, advanced OpenType features, or hit testing. These methods use the DirectWrite API to provide high-quality text display.

## The DrawText Method

To draw text that has a single format, use the [**DrawText**](https://msdn.microsoft.com/en-us/library/Dd371919(v=VS.85).aspx) method. To use this method, first use an [**IDWriteFactory**](https://msdn.microsoft.com/library/windows/desktop/dd368183) to create an [**IDWriteTextFormat**](https://msdn.microsoft.com/library/windows/desktop/dd316628) instance.

The following code creates an [**IDWriteTextFormat**](https://msdn.microsoft.com/en-us/library/Dd371919(v=VS.85).aspx) object and stores it in the *m\_pTextFormat* variable.


```C++
// Create resources which are not bound
// to any device. Their lifetime effectively extends for the
// duration of the app. These resources include the Direct2D and
// DirectWrite factories,  and a DirectWrite Text Format object
// (used for identifying particular font characteristics).
//
HRESULT DemoApp::CreateDeviceIndependentResources()
{
    static const WCHAR msc_fontName[] = L"Verdana";
    static const FLOAT msc_fontSize = 50;
    HRESULT hr;

    // Create a Direct2D factory.
    hr = D2D1CreateFactory(D2D1_FACTORY_TYPE_SINGLE_THREADED, &amp;m_pD2DFactory);

    if (SUCCEEDED(hr))
    {
        
        // Create a DirectWrite factory.
        hr = DWriteCreateFactory(
            DWRITE_FACTORY_TYPE_SHARED,
            __uuidof(m_pDWriteFactory),
            reinterpret_cast<IUnknown **>(&amp;m_pDWriteFactory)
            );
    }
    if (SUCCEEDED(hr))
    {
        // Create a DirectWrite text format object.
        hr = m_pDWriteFactory->CreateTextFormat(
            msc_fontName,
            NULL,
            DWRITE_FONT_WEIGHT_NORMAL,
            DWRITE_FONT_STYLE_NORMAL,
            DWRITE_FONT_STRETCH_NORMAL,
            msc_fontSize,
            L"", //locale
            &amp;m_pTextFormat
            );
    }
    if (SUCCEEDED(hr))
    {
        // Center the text horizontally and vertically.
        m_pTextFormat->SetTextAlignment(DWRITE_TEXT_ALIGNMENT_CENTER);

        m_pTextFormat->SetParagraphAlignment(DWRITE_PARAGRAPH_ALIGNMENT_CENTER);
       

    }

    return hr;
}
```



Because [**IDWriteFactory**](https://msdn.microsoft.com/library/windows/desktop/dd368183) and [**IDWriteTextFormat**](https://msdn.microsoft.com/en-us/library/Dd371919(v=VS.85).aspx) objects are [device-independent resources](resources-and-resource-domains.md), you can improve an application's performance by creating them only one time, instead of re-creating them every time that a frame is rendered.

After you create the text format object, you can use it with a render target. The following code draws the text by using the [**DrawText**](https://msdn.microsoft.com/en-us/library/Dd371919(v=VS.85).aspx) method of the render target (the *m\_pRenderTarget* variable).


```C++
//  Called whenever the application needs to display the client
//  window. This method writes "Hello, World"
//
//  Note that this function will automatically discard device-specific
//  resources if the Direct3D device disappears during function
//  invocation, and will recreate the resources the next time it's
//  invoked.
//
HRESULT DemoApp::OnRender()
{
    HRESULT hr;

    hr = CreateDeviceResources();

    if (SUCCEEDED(hr))
    {
        static const WCHAR sc_helloWorld[] = L"Hello, World!";

        // Retrieve the size of the render target.
        D2D1_SIZE_F renderTargetSize = m_pRenderTarget->GetSize();

        m_pRenderTarget->BeginDraw();

        m_pRenderTarget->SetTransform(D2D1::Matrix3x2F::Identity());

        m_pRenderTarget->Clear(D2D1::ColorF(D2D1::ColorF::White));

        m_pRenderTarget->DrawText(
            sc_helloWorld,
            ARRAYSIZE(sc_helloWorld) - 1,
            m_pTextFormat,
            D2D1::RectF(0, 0, renderTargetSize.width, renderTargetSize.height),
            m_pBlackBrush
            );

        hr = m_pRenderTarget->EndDraw();

        if (hr == D2DERR_RECREATE_TARGET)
        {
            hr = S_OK;
            DiscardDeviceResources();
        }
    }

    return hr;
}
```



## The DrawTextLayout Method

The [**DrawTextLayout**](https://msdn.microsoft.com/en-us/library/Dd371913(v=VS.85).aspx) method renders an [**IDWriteTextLayout**](https://msdn.microsoft.com/library/windows/desktop/dd316718) object. Use this method to apply multiple formats to a block of text (such as underlining a part of text), to use advanced OpenType features, or to perform hit testing support.

The [**DrawTextLayout**](https://msdn.microsoft.com/en-us/library/Dd371913(v=VS.85).aspx) method also provides performance benefits for drawing the same text repeatedly. The [**IDWriteTextLayout**](https://msdn.microsoft.com/library/windows/desktop/dd316718) object measures and lays out its text when you create it. If you create an **IDWriteTextLayout** object only one time and reuse it every time that you have to redraw the text, the performance improves because the system does not have to measure and lay out the text again.

Before you can use the [**DrawTextLayout**](https://msdn.microsoft.com/en-us/library/Dd371913(v=VS.85).aspx) method, you must use an [**IDWriteFactory**](https://msdn.microsoft.com/library/windows/desktop/dd368183) to create [**IDWriteTextFormat**](https://msdn.microsoft.com/en-us/library/Dd371919(v=VS.85).aspx) and [**IDWriteTextLayout**](https://msdn.microsoft.com/library/windows/desktop/dd316718) objects. After these objects are created, call the **DrawTextLayout** method.

For more information and examples, see the [Text Formatting and Layout](https://msdn.microsoft.com/library/windows/desktop/dd742752) overview.

## Related topics

<dl> <dt>

[**DrawText**](https://msdn.microsoft.com/en-us/library/Dd371919(v=VS.85).aspx)
</dt> <dt>

[**DrawTextLayout**](https://msdn.microsoft.com/en-us/library/Dd371913(v=VS.85).aspx)
</dt> <dt>

[**IDWriteTextFormat**](https://msdn.microsoft.com/library/windows/desktop/dd316628)
</dt> <dt>

[**IDWriteTextLayout**](https://msdn.microsoft.com/library/windows/desktop/dd316718)
</dt> <dt>

[Text Formatting and Layout](https://msdn.microsoft.com/library/windows/desktop/dd742752)
</dt> </dl>

 

 




