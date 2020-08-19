---
title: Debugging DirectX apps remotely
description: You can use Visual Studio and the Windows 8 SDK to debug DirectX apps remotely.
ms.assetid: CA471465-47C2-4706-B391-C9E6C2CD69D9
ms.topic: article
ms.date: 05/31/2018
---

# Debugging DirectX apps remotely

You can use Visual Studio and the Windows 8 SDK to debug DirectX apps remotely. The Windows 8 SDK provides a set of components that support DirectX development and provide error checking and parameter validation in addition to the debugging that Visual Studio provides. These components are D3D11\_1SDKLayers.dll, D2D1Debug1.dll, and Dxgidebug.dll.

If you want to debug remotely on a computer without the Windows 8 SDK installed and you want this additional debugging capability, you must install the remote debugging package that is appropriate for the architecture on which you want to debug. The Windows Installer Packages in `C:\Program Files (x86)\Windows Kits\8.0\Remote\<arch>` install the appropriate support.

To enable the additional debugging capabilities for Direct2D apps, use this code:

```cpp
    D2D1_FACTORY_OPTIONS options;
    ZeroMemory(&options, sizeof(D2D1_FACTORY_OPTIONS));

#if defined(_DEBUG)
     // If the project is in a debug build, enable Direct2D debugging via SDK Layers.
    options.debugLevel = D2D1_DEBUG_LEVEL_INFORMATION;
#endif

    DX::ThrowIfFailed(
        D2D1CreateFactory(
            D2D1_FACTORY_TYPE_SINGLE_THREADED,
            __uuidof(ID2D1Factory1),
            &options,
            &m_d2dFactory
            )
        );         
```

To enable the additional debugging capabilities for Direct3D apps, use this code:

```cpp
    // This flag supports surfaces with a different color channel ordering than the API default.
    // It is recommended usage, and is required for compatibility with Direct2D.
    UINT creationFlags = D3D11_CREATE_DEVICE_BGRA_SUPPORT;
    ComPtr<IDXGIDevice> dxgiDevice;

#if defined(_DEBUG)
    // If the project is in a debug build, enable debugging via SDK Layers with this flag.
    creationFlags |= D3D11_CREATE_DEVICE_DEBUG;
#endif
    DX::ThrowIfFailed(
        D3D11CreateDevice(
            nullptr,                    // specify null to use the default adapter
            D3D_DRIVER_TYPE_HARDWARE,
            0,                          // leave as 0 unless software device
            creationFlags,              // optionally set debug and Direct2D compatibility flags
            featureLevels,              // list of feature levels this app can support
            ARRAYSIZE(featureLevels),   // number of entries in above list
            D3D11_SDK_VERSION,          // always set this to D3D11_SDK_VERSION for modern
            &device,                    // returns the Direct3D device created
            &m_featureLevel,            // returns feature level of device created
            &context                    // returns the device immediate context
            )
        );
```

For more info about debugging Direct2D apps, see [Direct2D Debug Layer](/windows/desktop/Direct2D/direct2ddebuglayer-portal).

For more info about debugging Direct3D apps, see [Direct3D Debug Layer](/windows/desktop/direct3d11/overviews-direct3d-11-devices-layers).