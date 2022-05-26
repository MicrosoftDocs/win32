---
title: Direct2D and Direct3D Interoperability Overview
description: Direct2D and Direct3D Interoperability Overview
ms.assetid: 27680714-dc68-44eb-ab16-2cae3529b352
keywords:
- Direct2D,Direct3D interoperation
- Direct2D,interoperability
- interoperability,Direct2D
- interoperability,Direct3D
- Direct3D,interoperability
- Direct3D,Direct2D interoperation
- Direct2D,DXGI
- DXGI
ms.topic: article
ms.date: 05/31/2018
ms.custom: "seodec18"
---

# Direct2D and Direct3D Interoperability Overview

Hardware accelerated 2-D and 3-D graphics are increasingly becoming a part of non-gaming applications, and most gaming applications use 2-D graphics in the form of menus and Heads-Up Displays (HUDs). There is lots of value that can be added by enabling traditional 2-D rendering to be mixed with Direct3D rendering in an efficient manner.

This topic describes how to integrate 2-D and 3-D graphics by using Direct2D and [Direct3D](../graphics-and-multimedia.md).

It contains the following sections.

-   [Prerequisites](#prerequisites)
-   [Supported Direct3D Versions](#supported-direct3d-versions)
-   [Interoperability Through DXGI](#interoperability-through-dxgi)
-   [Writing to a Direct3D Surface with a DXGI Surface Render Target](#writing-to-a-direct3d-surface-with-a-dxgi-surface-render-target)
    -   [Creating a DXGI Surface](#creating-a-dxgi-surface)
-   [Writing Direct2D Content to a Swap Chain Buffer](#writing-direct2d-content-to-a-swap-chain-buffer)
    -   [Example: Draw a 2-D Background](#example-draw-a-2-d-background)
-   [Using Direct2D Content as a Texture](#using-direct2d-content-as-a-texture)
    -   [Example: Use Direct2D Content as a Texture](#example-use-direct2d-content-as-a-texture)
-   [Resizing a DXGI Surface Render Target](#resizing-a-dxgi-surface-render-target)
-   [Related topics](#related-topics)

## Prerequisites

This overview assumes that you are familiar with basic Direct2D drawing operations. For a tutorial, see [Create a simple Direct2D application](direct2d-quickstart.md). It also assumes that you can program by using [Direct3D 10.1](/windows/desktop/direct3d10/d3d10-graphics).

## Supported Direct3D Versions

With DirectX 11.0, Direct2D supports interoperability with Direct3D 10.1 devices only. With DirectX 11.1 or later, Direct2D supports interoperability with Direct3D 11 as well.

## Interoperability Through DXGI

As of Direct3D 10, the Direct3D runtime uses [DXGI](/windows/desktop/direct3ddxgi/d3d10-graphics-programming-guide-dxgi) for resource management. The DXGI runtime layer provides cross-process sharing of video memory surfaces and serves as the foundation for other video memory-based runtime platforms. Direct2D uses DXGI to interoperate with Direct3D.

There are two primary ways to use Direct2D and Direct3D together:

-   You can write Direct2D content to a Direct3D surface by obtaining an [**IDXGISurface**](/windows/desktop/api/dxgi/nn-dxgi-idxgisurface) and using it with the [**CreateDxgiSurfaceRenderTarget**](/windows/win32/api/d2d1/nf-d2d1-id2d1factory-createdxgisurfacerendertarget(idxgisurface_constd2d1_render_target_properties__id2d1rendertarget)) to create an [**ID2D1RenderTarget**](/windows/win32/api/d2d1/nn-d2d1-id2d1rendertarget). You can then use the render target to add a two-dimensional interface or background to three-dimensional graphics, or use a Direct2D drawing as a texture for a three dimensional object.
-   By using [**CreateSharedBitmap**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-createsharedbitmap) to create an [**ID2D1Bitmap**](/windows/win32/api/d2d1/nn-d2d1-id2d1bitmap) from an [**IDXGISurface**](/windows/desktop/api/dxgi/nn-dxgi-idxgisurface), you can write a Direct3D scene to a bitmap and render it with Direct2D.

## Writing to a Direct3D Surface with a DXGI Surface Render Target

To write to a Direct3D surface, you obtain an [**IDXGISurface**](/windows/desktop/api/dxgi/nn-dxgi-idxgisurface) and pass it to the [**CreateDxgiSurfaceRenderTarget**](/windows/win32/api/d2d1/nf-d2d1-id2d1factory-createdxgisurfacerendertarget(idxgisurface_constd2d1_render_target_properties__id2d1rendertarget)) method to create a DXGI surface render target. You can then use the DXGI surface render target to draw 2-D content to the DXGI surface.

A DXGI surface render target is a kind of [**ID2D1RenderTarget**](/windows/win32/api/d2d1/nn-d2d1-id2d1rendertarget). Like other Direct2D render targets, you can use it to create resources and issue drawing commands.

The DXGI surface render target and the DXGI surface must use the same DXGI format. If you specify the [**DXGI\_FORMAT\_UNKOWN**](/windows/desktop/api/dxgiformat/ne-dxgiformat-dxgi_format) format when you create the render target, it will automatically use the surface's format.

The DXGI surface render target does not perform DXGI surface synchronization.

### Creating a DXGI Surface

With Direct3D 10, there are several ways to obtain a DXGI surface. You can create an [**IDXGISwapChain**](/windows/desktop/api/dxgi/nn-dxgi-idxgiswapchain) for a device, then use the swap chain's [**GetBuffer**](/windows/desktop/api/dxgi/nf-dxgi-idxgiswapchain-getbuffer) method to obtain a DXGI surface. Or, you can use a device to create a texture, then use that texture as a DXGI surface.

Regardless of how you create the DXGI surface, the surface must use one of the DXGI formats supported by DXGI surface render targets. For a list, see [Supported Pixel Formats and Alpha Modes](supported-pixel-formats-and-alpha-modes.md).

Additionally, the [**ID3D10Device1**](/windows/desktop/api/d3d10_1/nn-d3d10_1-id3d10device1) associated with the DXGI surface must support BGRA DXGI formats for the surface to work with Direct2D. To ensure this support, use the [**D3D10\_CREATE\_DEVICE\_BGRA\_SUPPORT**](/windows/desktop/api/d3d10/ne-d3d10-d3d10_create_device_flag) flag when you call the [**D3D10CreateDevice1**](/windows/desktop/api/d3d10_1/nf-d3d10_1-d3d10createdevice1) method to create the device.

The following code defines a method that creates an [**ID3D10Device1**](/windows/desktop/api/d3d10_1/nn-d3d10_1-id3d10device1). It selects the best feature level available and falls back to [Windows Advanced Rasterization Platform (WARP)](./installing-the-direct2d-debug-layer.md) when hardware rendering is not available.


```C++
HRESULT DXGISampleApp::CreateD3DDevice(
    IDXGIAdapter *pAdapter,
    D3D10_DRIVER_TYPE driverType,
    UINT flags,
    ID3D10Device1 **ppDevice
    )
{
    HRESULT hr = S_OK;

    static const D3D10_FEATURE_LEVEL1 levelAttempts[] =
    {
        D3D10_FEATURE_LEVEL_10_0,
        D3D10_FEATURE_LEVEL_9_3,
        D3D10_FEATURE_LEVEL_9_2,
        D3D10_FEATURE_LEVEL_9_1,
    };

    for (UINT level = 0; level < ARRAYSIZE(levelAttempts); level++)
    {
        ID3D10Device1 *pDevice = NULL;
        hr = D3D10CreateDevice1(
            pAdapter,
            driverType,
            NULL,
            flags,
            levelAttempts[level],
            D3D10_1_SDK_VERSION,
            &pDevice
            );

        if (SUCCEEDED(hr))
        {
            // transfer reference
            *ppDevice = pDevice;
            pDevice = NULL;
            break;
        }

    }

    return hr;
}
```



The next code example uses the `CreateD3DDevice` method shown in the previous example to create a Direct3D device that can create DXGI surfaces for use with Direct2D.


```C++
// Create device
hr = CreateD3DDevice(
    NULL,
    D3D10_DRIVER_TYPE_HARDWARE,
    nDeviceFlags,
    &pDevice
    );

if (FAILED(hr))
{
    hr = CreateD3DDevice(
        NULL,
        D3D10_DRIVER_TYPE_WARP,
        nDeviceFlags,
        &pDevice
        );
}
```



## Writing Direct2D Content to a Swap Chain Buffer

The simplest way to add Direct2D content to a Direct3D scene is to use the [**GetBuffer**](/windows/desktop/api/dxgi/nf-dxgi-idxgiswapchain-getbuffer) method of an [**IDXGISwapChain**](/windows/desktop/api/dxgi/nn-dxgi-idxgiswapchain) to obtain a DXGI surface, then use the surface with the [**CreateDxgiSurfaceRenderTarget**](/windows/win32/api/d2d1/nf-d2d1-id2d1factory-createdxgisurfacerendertarget(idxgisurface_constd2d1_render_target_properties__id2d1rendertarget)) method to create an [**ID2D1RenderTarget**](/windows/win32/api/d2d1/nn-d2d1-id2d1rendertarget) with which to draw your 2-D content.

This approach does not render your content in three dimensions; it will not have perspective or depth. However, it is useful for several common tasks:

-   Creating a 2-D background for a 3-D scene.
-   Creating a 2-D interface in front of a 3-D scene.
-   Using Direct3D multisampling when rendering Direct2D content.

The next section shows how to create a 2-D background for a 3-D scene.

### Example: Draw a 2-D Background

The following steps describe how to create a DXGI surface render target and use it to draw a gradient background.

1.  Use the [**CreateSwapChain**](/windows/desktop/api/dxgi/nf-dxgi-idxgifactory-createswapchain) method to create a swap chain for an [**ID3D10Device1**](/windows/desktop/api/d3d10_1/nn-d3d10_1-id3d10device1) (the *m\_pDevice* variable). The swap chain uses the [**DXGI\_FORMAT\_B8G8R8A8\_UNORM**](/windows/desktop/api/dxgiformat/ne-dxgiformat-dxgi_format) DXGI format, one of the DXGI formats supported by Direct2D.

```C++
    if (SUCCEEDED(hr))
    {
        hr = pDevice->QueryInterface(&m_pDevice);
    }
    if (SUCCEEDED(hr))
    {
        hr = pDevice->QueryInterface(&pDXGIDevice);
    }
    if (SUCCEEDED(hr))
    {
        hr = pDXGIDevice->GetAdapter(&pAdapter);
    }
    if (SUCCEEDED(hr))
    {
        hr = pAdapter->GetParent(IID_PPV_ARGS(&pDXGIFactory));
    }
    if (SUCCEEDED(hr))
    {
        DXGI_SWAP_CHAIN_DESC swapDesc;
        ::ZeroMemory(&swapDesc, sizeof(swapDesc));

        swapDesc.BufferDesc.Width = nWidth;
        swapDesc.BufferDesc.Height = nHeight;
        swapDesc.BufferDesc.Format = DXGI_FORMAT_B8G8R8A8_UNORM;
        swapDesc.BufferDesc.RefreshRate.Numerator = 60;
        swapDesc.BufferDesc.RefreshRate.Denominator = 1;
        swapDesc.SampleDesc.Count = 1;
        swapDesc.SampleDesc.Quality = 0;
        swapDesc.BufferUsage = DXGI_USAGE_RENDER_TARGET_OUTPUT;
        swapDesc.BufferCount = 1;
        swapDesc.OutputWindow = m_hwnd;
        swapDesc.Windowed = TRUE;

        hr = pDXGIFactory->CreateSwapChain(m_pDevice, &swapDesc, &m_pSwapChain);
    }
```

    

2.  Use the swap chain's [**GetBuffer**](/windows/desktop/api/dxgi/nf-dxgi-idxgiswapchain-getbuffer) method to obtain a DXGI surface.

```C++
    // Get a surface in the swap chain
    hr = m_pSwapChain->GetBuffer(
        0,
        IID_PPV_ARGS(&pBackBuffer)
        );
```

    

3.  Use the DXGI surface to create a DXGI render target.
```C++
    // Create the DXGI Surface Render Target.
    FLOAT dpiX;
    FLOAT dpiY;
    m_pD2DFactory->GetDesktopDpi(&dpiX, &dpiY);

    D2D1_RENDER_TARGET_PROPERTIES props =
        D2D1::RenderTargetProperties(
            D2D1_RENDER_TARGET_TYPE_DEFAULT,
            D2D1::PixelFormat(DXGI_FORMAT_UNKNOWN, D2D1_ALPHA_MODE_PREMULTIPLIED),
            dpiX,
            dpiY
            );

    // Create a Direct2D render target which can draw into the surface in the swap chain

    
hr = m_pD2DFactory->CreateDxgiSurfaceRenderTarget(
        pBackBuffer,
        &props,
        &m_pBackBufferRT
        );
    
```



    

4.  Use the render target to draw a gradient background.

```C++
    // Swap chain will tell us how big the back buffer is
    DXGI_SWAP_CHAIN_DESC swapDesc;
    hr = m_pSwapChain->GetDesc(&swapDesc);

    if (SUCCEEDED(hr))
    {

    
// Draw a gradient background.
    if (m_pBackBufferRT)
    {
        D2D1_SIZE_F targetSize = m_pBackBufferRT->GetSize();

        m_pBackBufferRT->BeginDraw();

        m_pBackBufferGradientBrush->SetTransform(
            D2D1::Matrix3x2F::Scale(targetSize)
            );

        D2D1_RECT_F rect = D2D1::RectF(
            0.0f,
            0.0f,
            targetSize.width,
            targetSize.height
            );

        m_pBackBufferRT->FillRectangle(&rect, m_pBackBufferGradientBrush);

        hr = m_pBackBufferRT->EndDraw();
    }
```



    

Code is omitted from this sample.

## Using Direct2D Content as a Texture

Another way to use Direct2D content with Direct3D is to use Direct2D to generate a 2-D texture and then apply that texture to a 3-D model. You do this by creating an [**ID3D10Texture2D**](/windows/desktop/api/d3d10/nn-d3d10-id3d10texture2d), obtaining a DXGI surface from the texture, and then using the surface to create a DXGI surface render target. The **ID3D10Texture2D** surface must use the [**D3D10\_BIND\_RENDER\_TARGET**](/windows/desktop/api/d3d10/ne-d3d10-d3d10_bind_flag) bind flag and use a DXGI format supported by DXGI surface render targets. For a list of supported DXGI formats, see [Supported Pixel Formats and Alpha Modes](supported-pixel-formats-and-alpha-modes.md).

### Example: Use Direct2D Content as a Texture

The following examples show how to create a DXGI surface render target that renders to a 2-D texture (represented by an [**ID3D10Texture2D**](/windows/desktop/api/d3d10/nn-d3d10-id3d10texture2d)).

1.  First, use a Direct3D device to create a 2-D texture. The texture uses the [**D3D10\_BIND\_RENDER\_TARGET**](/windows/desktop/api/d3d10/ne-d3d10-d3d10_bind_flag) and **D3D10\_BIND\_SHADER\_RESOURCE** bind flags, and it uses the [**DXGI\_FORMAT\_B8G8R8A8\_UNORM**](/windows/desktop/api/dxgiformat/ne-dxgiformat-dxgi_format) DXGI format, one of the DXGI formats supported by Direct2D.

```C++
    // Allocate a offscreen D3D surface for D2D to render our 2D content into
    D3D10_TEXTURE2D_DESC texDesc;
    texDesc.ArraySize = 1;
    texDesc.BindFlags = D3D10_BIND_RENDER_TARGET | D3D10_BIND_SHADER_RESOURCE;
    texDesc.CPUAccessFlags = 0;
    texDesc.Format = DXGI_FORMAT_B8G8R8A8_UNORM;
    texDesc.Height = 512;
    texDesc.Width = 512;
    texDesc.MipLevels = 1;
    texDesc.MiscFlags = 0;
    texDesc.SampleDesc.Count = 1;
    texDesc.SampleDesc.Quality = 0;
    texDesc.Usage = D3D10_USAGE_DEFAULT;

    hr = m_pDevice->CreateTexture2D(&texDesc, NULL, &m_pOffscreenTexture);
```

    

2.  Use the texture to obtain a DXGI surface.

```C++
    IDXGISurface *pDxgiSurface = NULL;

    
hr = m_pOffscreenTexture->QueryInterface(&pDxgiSurface);
```



    

3.  Use the surface with the [**CreateDxgiSurfaceRenderTarget**](/windows/win32/api/d2d1/nf-d2d1-id2d1factory-createdxgisurfacerendertarget(idxgisurface_constd2d1_render_target_properties__id2d1rendertarget)) method to obtain a Direct2D render target.

```C++
    if (SUCCEEDED(hr))
    {
        // Create a D2D render target which can draw into our offscreen D3D
        // surface. Given that we use a constant size for the texture, we
        // fix the DPI at 96.
        D2D1_RENDER_TARGET_PROPERTIES props =
            D2D1::RenderTargetProperties(
                D2D1_RENDER_TARGET_TYPE_DEFAULT,
                D2D1::PixelFormat(DXGI_FORMAT_UNKNOWN, D2D1_ALPHA_MODE_PREMULTIPLIED),
                96,
                96
                );

    
    hr = m_pD2DFactory->CreateDxgiSurfaceRenderTarget(
            pDxgiSurface,
            &props,
            &m_pRenderTarget
            );
    }
```



    

Now that you have obtained a Direct2D render target and associated it with a Direct3D texture, you can use the render target to draw Direct2D content to that texture, and you can apply that texture to Direct3D primitives.

Code is omitted from this sample.

## Resizing a DXGI Surface Render Target

DXGI surface render targets do not support the [**ID2D1RenderTarget::Resize**](/windows/desktop/api/d2d1/nf-d2d1-id2d1hwndrendertarget-resize(constd2d1_size_u)) method. To resize a DXGI surface render target, the application must release and re-create it.

This operation can potentially create performance issues. The render target might be the last active Direct2D resource that keeps a reference to the [**ID3D10Device1**](/windows/desktop/api/d3d10_1/nn-d3d10_1-id3d10device1) associated with the render target's DXGI surface. If the application releases the render target and the **ID3D10Device1** reference is destroyed, a new one must be recreated.

You can avoid this potentially expensive operation by keeping at least one Direct2D resource that was created by the render target while you re-create that render target. The following are some Direct2D resources that work for this approach:

-   [**ID2D1Bitmap**](/windows/win32/api/d2d1/nn-d2d1-id2d1bitmap) (which may be held indirectly by an [**ID2D1BitmapBrush**](/windows/win32/api/d2d1/nn-d2d1-id2d1bitmapbrush))
-   [**ID2D1Layer**](/windows/win32/api/d2d1/nn-d2d1-id2d1layer)
-   [**ID2D1Mesh**](/windows/win32/api/d2d1/nn-d2d1-id2d1mesh)

To accommodate this approach, your resize method should test to see whether the Direct3D device is available. If it is available, release and re-create your DXGI surface render targets, but keep all the resources that they created previously and reuse them. This works because, as described in the [Resources Overview](resources-and-resource-domains.md), resources created by two render targets are compatible when both render targets are associated with the same Direct3D device.

## Related topics

<dl> <dt>

[Supported Pixel Formats and Alpha Modes](supported-pixel-formats-and-alpha-modes.md)
</dt> <dt>

[**CreateDxgiSurfaceRenderTarget**](/windows/win32/api/d2d1/nf-d2d1-id2d1factory-createdxgisurfacerendertarget(idxgisurface_constd2d1_render_target_properties__id2d1rendertarget))
</dt> <dt>

[Windows DirectX Graphics](../graphics-and-multimedia.md)
</dt> </dl>

 

 
