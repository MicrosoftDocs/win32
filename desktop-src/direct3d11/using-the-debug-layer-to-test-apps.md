---
title: Using the debug layer to debug apps
description: Here we talk about how to enable the debug layer and some of the issues that you can prevent by using the debug layer.
ms.assetid: 3C2B0A12-FB57-4400-BE39-05ED23F552C7
ms.topic: article
ms.date: 05/31/2018
---

# Using the debug layer to debug apps

We recommend that you use the [debug layer](overviews-direct3d-11-devices-layers.md) to debug your apps to ensure that they are clean of errors and warnings. The debug layer helps you write Direct3D code. In addition, your productivity can increase when you use the debug layer because you can immediately see the causes of obscure rendering errors or even black screens at their source. The debug layer provides warnings for many issues. For example, the debug layer provides warnings for these issues:

-   Forgot to set a texture but read from it in your pixel shader
-   Output depth but have no depth-stencil state bound
-   Texture creation failed with INVALIDARG

Here we talk about how to enable the [debug layer](overviews-direct3d-11-devices-layers.md) and some of the issues that you can prevent by using the debug layer.

-   [Enabling the debug layer](#enabling-the-debug-layer)
-   [Preventing errors in your app with the debug layer](#preventing-errors-in-your-app-with-the-debug-layer)
    -   [Don't pass NULL pointers to Map](#dont-pass-null-pointers-to-map)
    -   [Confine source box within source and destination resources](#confine-source-box-within-source-and-destination-resources)
    -   [Don't drop DiscardResource or DiscardView](#dont-drop-discardresource-or-discardview)
-   [Related topics](#related-topics)

## Enabling the debug layer

To enable the [debug layer](overviews-direct3d-11-devices-layers.md), specify the [**D3D11\_CREATE\_DEVICE\_DEBUG**](/windows/desktop/api/D3D11/ne-d3d11-d3d11_create_device_flag) flag in the *Flags* parameter when you call the [**D3D11CreateDevice**](/windows/desktop/api/D3D11/nf-d3d11-d3d11createdevice) function to create the rendering device. This example code shows how to enable the debug layer when your Microsoft Visual Studio project is in a debug build:


```C++
        UINT creationFlags = D3D11_CREATE_DEVICE_BGRA_SUPPORT;
#if defined(_DEBUG)
        // If the project is in a debug build, enable the debug layer.
        creationFlags |= D3D11_CREATE_DEVICE_DEBUG;
#endif
        // Define the ordering of feature levels that Direct3D attempts to create.
        D3D_FEATURE_LEVEL featureLevels[] =
        {
            D3D_FEATURE_LEVEL_11_1,
            D3D_FEATURE_LEVEL_11_0,
            D3D_FEATURE_LEVEL_10_1,
            D3D_FEATURE_LEVEL_10_0,
            D3D_FEATURE_LEVEL_9_3,
            D3D_FEATURE_LEVEL_9_1
        };

        ComPtr<ID3D11Device> d3dDevice;
        ComPtr<ID3D11DeviceContext> d3dDeviceContext;
        DX::ThrowIfFailed(
            D3D11CreateDevice(
                nullptr,                    // specify nullptr to use the default adapter
                D3D_DRIVER_TYPE_HARDWARE,
                nullptr,                    // specify nullptr because D3D_DRIVER_TYPE_HARDWARE 
                                            // indicates that this function uses hardware
                creationFlags,              // optionally set debug and Direct2D compatibility flags
                featureLevels,
                ARRAYSIZE(featureLevels),
                D3D11_SDK_VERSION,          // always set this to D3D11_SDK_VERSION
                &d3dDevice,
                nullptr,
                &d3dDeviceContext
                )
            );
```



## Preventing errors in your app with the debug layer

If you misuse the Direct3D 11 API or pass bad parameters, the debug output of the [debug layer](overviews-direct3d-11-devices-layers.md) reports an error or a warning. You can then correct your mistake. Next, we look at some coding issues that can cause undefined behavior or even the operating system to crash. You can catch and prevent these issues by using the debug layer.

### Don't pass NULL pointers to Map

If you pass **NULL** to the *pResource* or *pMappedResource* parameter of the [**ID3D11DeviceContext::Map**](/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-map) method, the behavior of **Map** is undefined. If you created a device that just supports the [core layer](overviews-direct3d-11-devices-layers.md), invalid parameters to **Map** can crash the operating system. If you created a device that supports the [debug layer](overviews-direct3d-11-devices-layers.md), the debug output reports an error on this invalid **Map** call.

### Confine source box within source and destination resources

In a call to the [**ID3D11DeviceContext::CopySubresourceRegion**](/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-copysubresourceregion) method, the source box must be within the source resource. The destination offsets, (x, y, and z) allow the source box to be offset when writing into the destination resource, but the dimensions of the source box and the offsets must be within the size of the resource. If you try to copy outside the destination resource or specify a source box that is larger than the source resource, the behavior of **CopySubresourceRegion** is undefined. If you created a device that supports the [debug layer](overviews-direct3d-11-devices-layers.md), the debug output reports an error on this invalid **CopySubresourceRegion** call. Invalid parameters to **CopySubresourceRegion** cause undefined behavior and might result in incorrect rendering, clipping, no copy, or even the removal of the rendering device.

### Don't drop DiscardResource or DiscardView

The runtime drops a call to [**ID3D11DeviceContext1::DiscardResource**](/windows/desktop/api/D3D11_1/nf-d3d11_1-id3d11devicecontext1-discardresource) or [**ID3D11DeviceContext1::DiscardView**](/windows/desktop/api/D3D11_1/nf-d3d11_1-id3d11devicecontext1-discardview) unless you correctly create the resource.

The resource that you pass to [**ID3D11DeviceContext1::DiscardResource**](/windows/desktop/api/D3D11_1/nf-d3d11_1-id3d11devicecontext1-discardresource) must have been created by using [**D3D11\_USAGE\_DEFAULT**](/windows/desktop/api/D3D11/ne-d3d11-d3d11_usage) or [**D3D11\_USAGE\_DYNAMIC**](/windows/desktop/api/D3D11/ne-d3d11-d3d11_usage), otherwise the runtime drops the call to **DiscardResource**.

The resource that underlies the view that you pass to [**ID3D11DeviceContext1::DiscardView**](/windows/desktop/api/D3D11_1/nf-d3d11_1-id3d11devicecontext1-discardview) must have been created using [**D3D11\_USAGE\_DEFAULT**](/windows/desktop/api/D3D11/ne-d3d11-d3d11_usage) or [**D3D11\_USAGE\_DYNAMIC**](/windows/desktop/api/D3D11/ne-d3d11-d3d11_usage), otherwise the runtime drops the call to **DiscardView**.

If you created a device that supports the [debug layer](overviews-direct3d-11-devices-layers.md), the debug output reports an error regarding the dropped call.

## Related topics

<dl> <dt>

[Software Layers](overviews-direct3d-11-devices-layers.md)
</dt> </dl>

 

 




