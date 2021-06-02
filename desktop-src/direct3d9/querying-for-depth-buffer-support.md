---
description: As with any feature, the driver that your application uses might not support all types of depth buffering.
ms.assetid: 8bf022f6-fd97-43f5-ac19-6a75ddb45f5e
title: Querying for Depth Buffer Support (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Querying for Depth Buffer Support (Direct3D 9)

As with any feature, the driver that your application uses might not support all types of depth buffering. Always check the driver's capabilities. Although most drivers support z-based depth buffering, not all will support w-based depth buffering. Drivers do not fail if you attempt to enable an unsupported scheme. They fall back on another depth buffering method instead, or sometimes disable depth buffering altogether, which can result in scenes rendered with extreme depth-sorting artifacts.

You can check for general support for depth buffers by querying Direct3D for the display device that your application will use before you create a Direct3D device. If the Direct3D object reports that it supports depth buffering, any hardware devices you create from this Direct3D object will support z-buffering.

To query for depth buffering support, you can use the [**IDirect3D9::CheckDeviceFormat**](/windows/win32/api/d3d9/nf-d3d9-idirect3d9-checkdeviceformat) method, as shown in the following code example.


```
// The following example assumes that pCaps is a valid pointer to an 
// initialized D3DCAPS9 structure
if(FAILED(m_pD3D->CheckDeviceFormat(pCaps->AdapterOrdinal, 
                                    pCaps->DeviceType, 
                                    AdapterFormat, 
                                    D3DUSAGE_DEPTHSTENCIL, 
                                    D3DRTYPE_SURFACE,
                                    D3DFMT_D16)))
    return E_FAIL;
```



[**IDirect3D9::CheckDeviceFormat**](/windows/win32/api/d3d9/nf-d3d9-idirect3d9-checkdeviceformat) allows you to choose a device to create based on the capabilities of that device. In this case, devices that do not support 16-bit depth buffers are rejected.

Using [**IDirect3D9::CheckDepthStencilMatch**](/windows/win32/api/d3d9/nf-d3d9-idirect3d9-checkdepthstencilmatch) to determine depth-stencil compatibility with a render target is illustrated in the following code example.


```
// Reject devices that cannot create a render target of RTFormat while
// the back buffer is of RTFormat and the depth-stencil buffer is
// at least 8 bits of stencil
if(FAILED(m_pD3D->CheckDepthStencilMatch(pCaps->AdapterOrdinal,
                                        pCaps->DeviceType, 
                                        AdapterFormat, 
                                        RTFormat, 
                                        D3DFMT_D24S8)))
    return E_FAIL;
```



When you know that the driver supports depth buffers, you can verify w-buffer support. Although depth buffers are supported for all software rasterizers, w-buffers are supported only by the reference rasterizer, which is not suited for use by real-world applications. Regardless of the type of device your application uses, verify support for w-buffers before you attempt to enable w-based depth buffering.

1.  After creating your device, call the [**IDirect3DDevice9::GetDeviceCaps**](/windows/desktop/api) method, passing an initialized [**D3DCAPS9**](/windows/desktop/api/D3D9Caps/ns-d3d9caps-d3dcaps9) structure.
2.  After the call, the LineCaps member contains information about the driver's support for rendering primitives.
3.  If the RasterCaps member of this structure contains the D3DPRASTERCAPS\_WBUFFER flag, then the driver supports w-based depth buffering for that primitive type.

## Related topics

<dl> <dt>

[Depth Buffers](depth-buffers.md)
</dt> </dl>

 

 
