---
title: ID2D1Factory CreateDxgiSurfaceRenderTarget methods
description: Creates a render target that draws to a DirectX Graphics Infrastructure (DXGI) surface.
ms.assetid: 101744ea-97bc-4f92-88b0-fcdf0e4aaf4e
keywords:
- CreateDxgiSurfaceRenderTarget methods Direct2D
topic_type:
- apiref
api_location:
- D2d1.dll
api_type:
- DllExport
ms.date: 07/02/2019
ms.topic: article
---

# ID2D1Factory::CreateDxgiSurfaceRenderTarget methods

Creates a render target that draws to a DirectX Graphics Infrastructure (DXGI) surface.

### Overload list



| Method                                                                                                                                                                                                                                    | Description                                                                                         |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------|
| [**CreateDxgiSurfaceRenderTarget(IDXGISurface\*,D2D1\_RENDER\_TARGET\_PROPERTIES&,ID2D1RenderTarget\*\*)**](https://msdn.microsoft.com/en-us/library/Dd371264(v=VS.85).aspx)  | Creates a render target that draws to a DirectX Graphics Infrastructure (DXGI) surface. <br/> |
| [**CreateDxgiSurfaceRenderTarget(IDXGISurface\*,D2D1\_RENDER\_TARGET\_PROPERTIES\*,ID2D1RenderTarget\*\*)**](https://msdn.microsoft.com/en-us/library/Dd371260(v=VS.85).aspx) | Creates a render target that draws to a DirectX Graphics Infrastructure (DXGI) surface. <br/> |



## Remarks

To write to a Direct3D surface, you obtain an [IDXGISurface](https://msdn.microsoft.com/library/bb174565(VS.85).aspx) and pass it to the **CreateDxgiSurfaceRenderTarget** method to create a DXGI surface render target; you can then use the DXGI surface render target to draw 2-D content to the DXGI surface.

A DXGI surface render target is a type of [**ID2D1RenderTarget**](https://msdn.microsoft.com/en-us/library/Dd371260(v=VS.85).aspx). Like other Direct2D render targets, you can use it to create resources and issue drawing commands.

The DXGI surface render target and the DXGI surface must use the same DXGI format. If you specify the [DXGI\_FORMAT\_UNKOWN](https://msdn.microsoft.com/library/bb173059(VS.85).aspx) format when you create the render target, it will automatically use the surface's format.

The DXGI surface render target does not perform DXGI surface synchronization.

To work with Direct2D, the Direct3D device that provides the [IDXGISurface](https://msdn.microsoft.com/library/bb174565(VS.85).aspx) must be created with the **D3D10\_CREATE\_DEVICE\_BGRA\_SUPPORT** flag.

For more information about creating and using DXGI surface render targets, see the [Direct2D and Direct3D Interoperability Overview](direct2d-and-direct3d-interoperation-overview.md).

When you create a render target and hardware acceleration is available, you allocate resources on the computer's GPU. By creating a render target once and retaining it as long as possible, you gain performance benefits. Your application should create render targets once and hold onto them for the life of the application or until the render target's [**EndDraw**](https://msdn.microsoft.com/en-us/library/Dd371924(v=VS.85).aspx) method returns the [**D2DERR\_RECREATE\_TARGET**](direct2d-error-codes.md) error. When you receive this error, you need to recreate the render target (and any resources it created).

## Examples

The following example obtains a DXGI surface (*pBackBuffer*) from an [IDXGISwapChain](https://msdn.microsoft.com/library/bb174569(VS.85).aspx) and uses it to create a DXGI surface render target.


```C++
// Get a surface in the swap chain
hr = m_pSwapChain->GetBuffer(
    0,
    IID_PPV_ARGS(&pBackBuffer)
    );

    if (SUCCEEDED(hr))
    {
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

    }
```


## Requirements



|                    |                                                                                     |
|--------------------|-------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D2d1.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D2d1.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>D2d1.dll</dt> </dl> |



## See also

[**ID2D1Factory**](https://msdn.microsoft.com/en-us/library/Dd371246(v=VS.85).aspx)

[Direct2D and Direct3D Interoperability Overview](direct2d-and-direct3d-interoperation-overview.md)
