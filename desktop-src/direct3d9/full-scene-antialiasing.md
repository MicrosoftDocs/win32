---
description: Full-scene antialiasing refers to blurring the edges of each polygon in the scene as it is rasterized in a single pass; no second pass is required.
ms.assetid: b57974ab-5654-412d-ae59-58f67a88c121
title: Full-Scene Antialiasing (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Full-Scene Antialiasing (Direct3D 9)

Full-scene antialiasing refers to blurring the edges of each polygon in the scene as it is rasterized in a single pass; no second pass is required. Full-scene antialiasing, when supported, affects only triangles and groups of triangles. Lines cannot be antialiased by using Direct3D services. Full-scene antialiasing is done in Direct3D by using multisampling on each pixel. When multisampling is enabled, all subsamples of a pixel are updated in one pass but when used for other effects that involve multiple rendering passes, the application can specify that only some subsamples are to be affected by a given rendering pass. This latter approach enables simulation of motion blur, depth-of-field focus effects, reflection blur, and so on.

In both cases, the various samples recorded for each pixel are blended together and output to the screen. This enables the improved image quality of antialiasing or other effects.

Before creating a device with the [**IDirect3D9::CreateDevice**](/windows/desktop/api) method, you need to determine if full-scene antialiasing is supported. Do this by calling the [**IDirect3D9::CheckDeviceMultiSampleType**](/windows/win32/api/d3d9/nf-d3d9-idirect3d9-checkdevicemultisampletype) method as shown in the code example below.


```
/*
* The code below assumes that pD3D is a valid pointer 
*   to a IDirect3D9 interface.
*/

if( SUCCEEDED(pD3D->CheckDeviceMultiSampleType( D3DADAPTER_DEFAULT, 
                    D3DDEVTYPE_HAL , D3DFMT_R8G8B8, FALSE, 
                    D3DMULTISAMPLE_2_SAMPLES, NULL ) ) )
// Full-scene antialiasing is supported. Enable it here.
```



The first parameter that [**IDirect3D9::CheckDeviceMultiSampleType**](/windows/win32/api/d3d9/nf-d3d9-idirect3d9-checkdevicemultisampletype) accepts is an ordinal number that denotes the display adapter to query. This sample uses D3DADAPTER\_DEFAULT to specify the primary display adapter. The second parameter is a value from the [**D3DDEVTYPE**](./d3ddevtype.md) enumerated type, specifying the device type. The third parameter specifies the format of the surface. The fourth parameter tells Direct3D whether to inquire about full-windowed multisampling (**TRUE**) or full-scene antialiasing (**FALSE**). This sample uses **FALSE** to tell Direct3D that it is inquiring about full-scene antialiasing. The last parameter specifies the multisampling technique that you want to test. Use a value from the [**D3DMULTISAMPLE\_TYPE**](./d3dmultisample-type.md) enumerated type. This sample tests to see if two levels of multisampling are supported.

If the device supports the level of multisampling that you want to use, the next step is to set the presentation parameters by filling in the appropriate members of the [**D3DPRESENT\_PARAMETERS**](d3dpresent-parameters.md) structure to create a multisample rendering surface. After that, you can create the device. The sample code below shows how to set up a device with a multisampling render surface.


```
/*
* The example below assumes that pD3D is a valid pointer 
* to a IDirect3D9 interface, d3dDevice is a pointer to a 
* IDirect3DDevice9 interface, and hWnd is a valid handle
* to a window.
*/

D3DPRESENT_PARAMETER d3dPP
ZeroMemory( &d3dPP, sizeof( d3dPP ) );
d3dPP.Windowed        = FALSE
d3dPP.SwapEffect      = D3DSWAPEFFECT_DISCARD;
d3dPP.MultiSampleType = D3DMULTISAMPLE_2_SAMPLES;
pD3D->CreateDevice(D3DADAPTER_DEFAULT, D3DDEVTYPE_HAL, hWnd,
                    D3DCREATE_SOFTWARE_VERTEXPROCESSING,
                    &d3dpp, &d3dDevice)
```



To use multisampling, the SwapEffect member of D3DPRESENT\_PARAMETER must be set to D3DSWAPEFFECT\_DISCARD.

The last step is to enable multisampling antialiasing by calling the [**IDirect3DDevice9::SetRenderState**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setrenderstate) method and setting the D3DRS\_MULTISAMPLEANTIALIAS to **TRUE**. After setting this value to **TRUE**, any rendering that you do will have multisampling applied to it. You might want to enable and disable multisampling, depending on what you are rendering.

## Related topics

<dl> <dt>

[Antialiasing](antialiasing.md)
</dt> </dl>

 

 
