---
description: Using Bump Mapping (Direct3D 9)
ms.assetid: ded07764-1a11-42df-9a16-e4c3a328fb23
title: Using Bump Mapping (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Using Bump Mapping (Direct3D 9)

## Detecting Support for Bump Mapping

A device can perform bump mapping if it supports either the D3DTOP\_BUMPENVMAP or D3DTOP\_BUMPENVMAPLUMINANCE texture blending operation. Use [**IDirect3D9::CheckDeviceFormat**](/windows/win32/api/d3d9/nf-d3d9-idirect3d9-checkdeviceformat) with D3DUSAGE\_QUERY\_LEGACYBUMPMAP to see if a format is supported for bump mapping.

Additionally, applications should check the device capabilities to make sure the device supports an appropriate number of blending stages, usually at least three, and exposes at least one bump-mapping pixel format.

The following code example checks device capabilities to detect support for bump mapping in the current device, using the given criteria.


```
BOOL SupportsBumpMapping()
{
    D3DCAPS9 d3dCaps;

    d3dDevice->GetDeviceCaps( &d3dCaps );

    // Does this device support the two bump mapping blend operations?
    if ( 0 == d3dCaps.TextureOpCaps & ( D3DTEXOPCAPS_BUMPENVMAP |
                                            D3DTEXOPCAPS_BUMPENVMAPLUMINANCE ))
        return FALSE;

    // Does this device support up to three blending stages?
    if( d3dCaps.MaxTextureBlendStages < 3 )
        return FALSE;

    return TRUE;
}
```



## Creating a Bump Map Texture

You create a bump map texture like any other texture. Your application verifies support for bump mapping and retrieves a valid pixel format, as discussed in Detecting Support for Bump Mapping.

After the surface is created, you can load each pixel with the appropriate delta values, and luminance, if the surface format includes luminance. The values for each pixel component are described in [Bump Map Pixel Formats (Direct3D 9)](bump-map-pixel-formats.md).

## Configuring Bump Mapping Parameters

When your application has created a bump map and set the contents of each pixel, you can prepare for rendering by configuring bump mapping parameters. Bump mapping parameters include setting the required textures and their blending operations, as well as the transformation and luminance controls for the bump map itself.

1.  Set the base texture map if used, bump map, and environment map textures into texture blending stages.
2.  Set the color and alpha blending operations for each texture stage.
3.  Set the bump map transformation matrix.
4.  Set the luminance scale and offset values as needed.

The following code example sets three textures (the base texture map, the bump map, and a specular environment map) to the appropriate texture blending stages.


```
// Set the three textures.
d3dDevice->SetTexture( 0, d3dBaseTexture );
d3dDevice->SetTexture( 1, d3dBumpMap );
d3dDevice->SetTexture( 2, d3dEnvMap );
```



After setting the textures to their blending stages, the following code example prepares the blending operations and arguments for each stage.


```
// Set the color operations and arguments to prepare for
//   bump mapping.

// Stage 0: The base texture
d3dDevice->SetTextureStageState( 0, D3DTSS_COLOROP, D3DTOP_MODULATE );
d3dDevice->SetTextureStageState( 0, D3DTSS_COLORARG1, D3DTA_TEXTURE );
d3dDevice->SetTextureStageState( 0, D3DTSS_COLORARG2, D3DTA_DIFFUSE );
d3dDevice->SetTextureStageState( 0, D3DTSS_ALPHAOP, D3DTOP_SELECTARG1 );
d3dDevice->SetTextureStageState( 0, D3DTSS_ALPHAARG1, D3DTA_TEXTURE ); 
d3dDevice->SetTextureStageState( 0, D3DTSS_TEXCOORDINDEX, 1 );

// Stage 1: The bump map - Use luminance for this example.
d3dDevice->SetTextureStageState( 1, D3DTSS_TEXCOORDINDEX, 1 );
d3dDevice->SetTextureStageState( 1, D3DTSS_COLOROP, D3DTOP_BUMPENVMAPLUMINANCE);
d3dDevice->SetTextureStageState( 1, D3DTSS_COLORARG1, D3DTA_TEXTURE );
d3dDevice->SetTextureStageState( 1, D3DTSS_COLORARG2, D3DTA_CURRENT );

// Stage 2: A specular environment map
d3dDevice->SetTextureStageState( 2, D3DTSS_TEXCOORDINDEX, 0 );
d3dDevice->SetTextureStageState( 2, D3DTSS_COLOROP, D3DTOP_ADD );
d3dDevice->SetTextureStageState( 2, D3DTSS_COLORARG1, D3DTA_TEXTURE );
d3dDevice->SetTextureStageState( 2, D3DTSS_COLORARG2, D3DTA_CURRENT );
```



When the blending operations and arguments are set, the following code example sets the 2x2 bump mapping matrix to the identity matrix by setting the D3DTSS\_BUMPENVMAPMAT00 and the D3DTSS\_BUMPENVMAPMAT11 members of [**D3DTEXTURESTAGESTATETYPE**](./d3dtexturestagestatetype.md) to 1.0. Setting the matrix to the identity causes the system to use the delta values in the bump map unmodified, but this is not a requirement.


```
// Set the bump mapping matrix.
//
// Note  These calls rely on the following inline shortcut function:
//   inline DWORD F2DW( FLOAT f ) { return *((DWORD*)&f); }
d3dDevice->SetTextureStageState( 1, D3DTSS_BUMPENVMAT00, F2DW(1.0f) );
d3dDevice->SetTextureStageState( 1, D3DTSS_BUMPENVMAT01, F2DW(0.0f) );
d3dDevice->SetTextureStageState( 1, D3DTSS_BUMPENVMAT10, F2DW(0.0f) );
d3dDevice->SetTextureStageState( 1, D3DTSS_BUMPENVMAT11, F2DW(1.0f) );
```



If you set the bump mapping operation to include luminance (D3DTOP\_BUMPENVMAPLUMINANCE), you must set the luminance controls. The luminance controls configure how the system computes luminance before modulating the color from the texture in the next stage. For details, see [Bump Mapping Formulas (Direct3D 9)](bump-mapping-formulas.md).


```
// Set luminance controls. This is only needed when using
// a bump map that contains luminance, and when the 
// D3DTOP_BUMPENVMAPLUMINANCE texture blending operation is
// being used.
//
// Note  These calls rely on the following inline shortcut function:
//   inline DWORD F2DW( FLOAT f ) { return *((DWORD*)&f); }
d3dDevice->SetTextureStageState( 1, D3DTSS_BUMPENVLSCALE, F2DW(0.5f) );
d3dDevice->SetTextureStageState( 1, D3DTSS_BUMPENVLOFFSET, F2DW(0.0f) );
```



After your application configures bump mapping parameters, it can render as normal, and the rendered polygons receive bump mapping effects.

Note that the preceding example shows parameters set for specular environment mapping. When performing diffuse light mapping, applications set the texture blending operation for the last stage to D3DTOP\_MODULATE. For more information, see [Diffuse Light Maps (Direct3D 9)](diffuse-light-maps.md).

## Related topics

<dl> <dt>

[Bump Mapping](bump-mapping.md)
</dt> </dl>

 

 
