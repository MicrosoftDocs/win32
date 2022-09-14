---
description: C++ applications can use alpha testing to control when pixels are written to the render-target surface.
ms.assetid: 368c3d12-2c8b-43e3-94c3-bccfe6c73e66
title: Alpha Testing State (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Alpha Testing State (Direct3D 9)

C++ applications can use alpha testing to control when pixels are written to the render-target surface. By using the [**D3DRS\_ALPHATESTENABLE**](./d3drenderstatetype.md) render state, your application sets the current Direct3D device so that it tests each pixel according to an alpha test function. If the test succeeds, the pixel is written to the surface. If it does not, Direct3D ignores the pixel. Select the alpha test function with the **D3DRS\_ALPHAFUNC** render state. Your application can set a reference alpha value for all pixels to compare against by using the **D3DRS\_ALPHAREF** render state.

The most common use for alpha testing is to improve performance when rasterizing objects that are nearly transparent. If the color data being rasterized is more opaque than the color at a given pixel (D3DPCMPCAPS\_GREATEREQUAL), then the pixel is written. Otherwise, the rasterizer ignores the pixel altogether, saving the processing required to blend the two colors. The following code example checks if a given comparison function is supported and, if so, it sets the comparison function parameters required to improve performance during rendering.


```
// This code example assumes that pCaps is a
// D3DCAPS9 structure that was filled with a 
// previous call to IDirect3D9::GetDeviceCaps.

if (pCaps.AlphaCmpCaps & D3DPCMPCAPS_GREATEREQUAL)
{
    dev->SetRenderState(D3DRS_ALPHAREF, (DWORD)0x00000001);
    dev->SetRenderState(D3DRS_ALPHATESTENABLE, TRUE); 
    dev->SetRenderState(D3DRS_ALPHAFUNC, D3DCMP_GREATEREQUAL);
}

// If the comparison is not supported, render anyway. 
// The only drawback is no performance gain.
```



Not all hardware supports all alpha-testing features. You can check the device capabilities by calling the [**IDirect3D9::GetDeviceCaps**](/windows/desktop/api) method. After retrieving the device capabilities, check the associated [**D3DCAPS9**](/windows/desktop/api/D3D9Caps/ns-d3d9caps-d3dcaps9) structure's AlphaCmpCaps member for the desired comparison function. If the AlphaCmpCaps member contains only the D3DPCMPCAPS\_ALWAYS capability or only the D3DPCMPCAPS\_NEVER capability, the driver does not support alpha tests.

## Related topics

<dl> <dt>

[Render States](render-states.md)
</dt> </dl>

 

 
