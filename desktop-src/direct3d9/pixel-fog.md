---
description: Pixel fog gets its name from the fact that it is calculated on a per-pixel basis in the device driver.
ms.assetid: 6fcfb9fa-cacc-4dbc-bfc6-85d533dbfbf8
title: Pixel Fog (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Pixel Fog (Direct3D 9)

Pixel fog gets its name from the fact that it is calculated on a per-pixel basis in the device driver. This is different from vertex fog, which is computed by the pipeline during transformation and lighting calculations. Pixel fog is sometimes called table fog because some drivers use a precalculated lookup table to determine the fog factor, using the depth of each pixel to apply in blending computations. It can be applied using any fog formula identified by members of the [**D3DFOGMODE**](./d3dfogmode.md) enumerated type. The implementations of these formulas are driver-specific. If a driver doesn't support a complex fog formula, it should degrade to a less complex formula.

## Eye-Relative vs. Z-Based Depth

To alleviate fog-related graphic artifacts caused by uneven distribution of z-values in a depth buffer, most hardware devices use eye-relative depth instead of z-based depth values for pixel fog. Eye-relative depth is essentially the w element from a homogeneous coordinate set. Microsoft Direct3D takes the reciprocal of the RHW element from a device space coordinate set to reproduce true w. If a device supports eye-relative fog, it sets the **D3DPRASTERCAPS\_WFOG** flag in the RasterCaps member of the [**D3DCAPS9**](/windows/desktop/api/D3D9Caps/ns-d3d9caps-d3dcaps9) structure when you call the [**IDirect3DDevice9::GetDeviceCaps**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-getdevicecaps) method. With the exception of the reference rasterizer, software devices always use z to calculate pixel fog effects.

When eye-relative fog is supported, the system automatically uses eye-relative depth rather than z-based depth if the provided projection matrix produces z-values in world space that are equivalent to w-values in device space. You set the projection matrix by calling the [**IDirect3DDevice9::SetTransform**](/windows/desktop/api) method, using the D3DTS\_PROJECTION value and passing a [**D3DMATRIX**](d3dmatrix.md) structure that represents the desired matrix. If the projection matrix isn't compliant with this requirement, fog effects are not applied properly. For details about producing a compliant matrix, see [Projection Transform (Direct3D 9)](projection-transform.md).

Direct3D uses the currently set projection matrix in its w-based depth calculations. As a result, an application must set a compliant projection matrix to receive the desired w-based features, even if it does not use the Direct3D transformation pipeline.

Direct3D checks the fourth column of the projection matrix. If the coefficients are \[0,0,0,1\] (for an affine projection) the system will use z-based depth values for fog. In this case, you must also specify the start and end distances for linear fog effects in device space, which ranges from 0.0 at the nearest point to the user, and 1.0 at the farthest point.

## Using Pixel Fog

Use the following steps to enable pixel fog in your application.

1.  Enable fog blending by setting the D3DRS\_FOGENABLE render state to **TRUE**.
2.  Set the desired fog color in the D3DRS\_FOGCOLOR render state.
3.  Choose the fog formula to use by setting the D3DRS\_FOGTABLEMODE render state to the corresponding member of the [**D3DFOGMODE**](./d3dfogmode.md) enumerated type.
4.  Set the fog parameters as desired for the selected fog mode in the associated render states. This includes the start and end distances for linear fog, and fog density for exponential fog mode.

The following example shows what these steps might look like in code.


```
// For brevity, error values in this example are not checked 
//   after each call. A real-world application should check 
//   these values appropriately.
//
// For the purposes of this example, g_pDevice is a valid
//   pointer to an IDirect3DDevice9 interface.
void SetupPixelFog(DWORD Color, DWORD Mode)
{
    float Start   = 0.5f;    // For linear mode
    float End     = 0.8f;
    float Density = 0.66f;   // For exponential modes
 
    // Enable fog blending.
    g_pDevice->SetRenderState(D3DRS_FOGENABLE, TRUE);
 
    // Set the fog color.
    g_pDevice->SetRenderState(D3DRS_FOGCOLOR, Color);
    
    // Set fog parameters.
    if( Mode == D3DFOG_LINEAR )
    {
        g_pDevice->SetRenderState(D3DRS_FOGTABLEMODE, Mode);
        g_pDevice->SetRenderState(D3DRS_FOGSTART, *(DWORD *)(&Start));
        g_pDevice->SetRenderState(D3DRS_FOGEND,   *(DWORD *)(&End));
    }
    else
    {
        g_pDevice->SetRenderState(D3DRS_FOGTABLEMODE, Mode);
        g_pDevice->SetRenderState(D3DRS_FOGDENSITY, *(DWORD *)(&Density));
    }
```



Some fog parameters are required as floating-point values, even though the [**IDirect3DDevice9::SetRenderState**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setrenderstate) method accepts only DWORD values in the second parameter. The preceding example provides the floating-point values to **IDirect3DDevice9::SetRenderState** without data translation by casting the addresses of the floating-point variables as DWORD pointers, and then dereferencing them.

## Related topics

<dl> <dt>

[Fog Types](fog-types.md)
</dt> </dl>

 

 
