---
title: Software Layers
description: The Direct3D 11 runtime is constructed with layers, starting with the basic functionality at the core and building optional and developer-assist functionality in outer layers. This section describes the functionality of each layer.
ms.assetid: c545983c-5351-42a9-82e5-deea73aa035f
ms.topic: article
ms.date: 05/31/2018
---

# Software Layers

The Direct3D 11 runtime is constructed with layers, starting with the basic functionality at the core and building optional and developer-assist functionality in outer layers. This section describes the functionality of each layer.

As a general rule, layers add functionality, but do not modify existing behavior. For example, core functions will have the same return values independent of the debug layer being instantiated, although additional debug output may be provided if the debug layer is instantiated.

To create layers when a device is created, call [**D3D11CreateDevice**](/windows/desktop/api/D3D11/nf-d3d11-d3d11createdevice) or [**D3D11CreateDeviceAndSwapChain**](/windows/desktop/api/D3D11/nf-d3d11-d3d11createdeviceandswapchain) and supply one or more [**D3D11\_CREATE\_DEVICE\_FLAG**](/windows/desktop/api/D3D11/ne-d3d11-d3d11_create_device_flag) values.

Direct3D 11 provides the following runtime layers:

-   [Core Layer](#core-layer)
-   [Debug Layer](#debug-layer)
-   [Related topics](#related-topics)

## Core Layer

The core layer exists by default; providing a very thin mapping between the API and the device driver, minimizing overhead for high-frequency calls. As the core layer is essential for performance, it only performs critical validation. The remaining layers are optional.

## Debug Layer

The debug layer provides extensive additional parameter and consistency validation (such as validating shader linkage and resource binding, validating parameter consistency, and reporting error descriptions).

To create a device that supports the debug layer, you must install the DirectX SDK (to get D3D11SDKLayers.dll), and then specify the **D3D11\_CREATE\_DEVICE\_DEBUG** flag when calling the [**D3D11CreateDevice**](/windows/desktop/api/D3D11/nf-d3d11-d3d11createdevice) function or the [**D3D11CreateDeviceAndSwapChain**](/windows/desktop/api/D3D11/nf-d3d11-d3d11createdeviceandswapchain) function. If you run your application with the debug layer enabled, the application will be substantially slower. But, to ensure that your application is clean of errors and warnings before you ship it, use the debug layer. For more info, see [Using the debug layer to debug apps](using-the-debug-layer-to-test-apps.md).


> [!Note]  
> For Windows 7 with Platform Update for Windows 7 (KB2670838) or Windows 8.x, to create a device that supports the debug layer, install the Windows Software Development Kit (SDK) for Windows 8.x to get D3D11\_1SDKLayers.dll.


> [!Note]  
> For Windows 10, to create a device that supports the debug layer, enable the "Graphics Tools" optional feature. Go to the Settings panel, under System, Apps & features, Manage optional Features, Add a feature, and then look for "Graphics Tools".


> [!Note]  
> For info about how to debug DirectX apps remotely, see [Debugging DirectX apps remotely](/windows/desktop/direct3dtools/debugging-directx-apps-remotely).

 

Alternately, you can enable/disable the debug flag using the [DirectX Control Panel](/previous-versions//bb219725(v=vs.85)) included as part of the DirectX SDK.

When the debug layer lists memory leaks, it outputs a list of object interface pointers along with their friendly names. The default friendly name is "&lt;unnamed&gt;". You can set the friendly name by using the [**ID3D11DeviceChild::SetPrivateData**](/windows/desktop/api/D3D11/nf-d3d11-id3d11devicechild-setprivatedata) method and the **WKPDID\_D3DDebugObjectName** GUID that is in D3Dcommon.h. For example, to name pTexture with a SDKLayer name of mytexture.jpg, use the following code:


```
const char c_szName[] = "mytexture.jpg";
pTexture->SetPrivateData( WKPDID_D3DDebugObjectName, sizeof( c_szName ) - 1, c_szName );
```



Typically, you should compile these calls out of your production version.

## Related topics

<dl> <dt>

[Devices](overviews-direct3d-11-devices.md)
</dt> </dl>

 

 