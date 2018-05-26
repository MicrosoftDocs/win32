---
Description: Effect states are name value pairs in the form of an expression.
ms.assetid: 4612c6bd-bc1f-42ad-8465-c0d4b577d1db
title: Effect State Groups (Direct3D 10)
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Effect State Groups (Direct3D 10)

Effect states are name value pairs in the form of an expression.

-   [Blend State](#blend-state)
-   [Depth and Stencil State](#depth-and-stencil-state)
-   [Rasterizer State](#rasterizer-state)
-   [Sampler State](#sampler-state)
-   [Effect Object State](#effect-object-state)
-   [Defining and using state objects](#defining-and-using-state-objects)
-   [Related topics](#related-topics)

## Blend State



|                                                                                                                       |                                                           |
|-----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| ALPHATOCOVERAGEENABLEBLENDENABLESRCBLENDDESTBLENDBLENDOP SRCBLENDALPHADESTBLENDALPHABLENDOPALPHARENDERTARGETWRITEMASK | Members of [**D3D10\_BLEND\_DESC**](/windows/win32/D3D10/ns-d3d10-d3d10_blend_desc?branch=master) |



 

## Depth and Stencil State



|                                                                                                                                                                |                                                                               |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| DEPTHENABLEDEPTHWRITEMASKDEPTHFUNCSTENCILENABLESTENCILREADMASKSTENCILWRITEMASK                                                                                 | Members of [**D3D10\_DEPTH\_STENCIL\_DESC**](/windows/win32/D3D10/ns-d3d10-d3d10_depth_stencil_desc?branch=master)    |
| FRONTFACESTENCILFAILFRONTFACESTENCILZFAILFRONTFACESTENCILPASSFRONTFACESTENCILFUNCBACKFACESTENCILFAILBACKFACESTENCILZFAILBACKFACESTENCILPASSBACKFACESTENCILFUNC | Member of [**D3D10\_DEPTH\_STENCILOP\_DESC**](/windows/win32/D3D10/ns-d3d10-d3d10_depth_stencilop_desc?branch=master) |



 

## Rasterizer State



|                                                                                                                                 |                                                                     |
|---------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| FILLMODE                                                                                                                        | [**D3D10\_FILL\_MODE**](/windows/win32/D3D10/ne-d3d10-d3d10_fill_mode?branch=master)                        |
| CULLMODE                                                                                                                        | [**D3D10\_CULL\_MODE**](/windows/win32/D3D10/ne-d3d10-d3d10_cull_mode?branch=master)                        |
| FRONTCOUNTERCLOCKWISEDEPTHBIASDEPTHBIASCLAMPSLOPESCALEDDEPTHBIAS ZCLIPENABLESCISSORENABLEMULTISAMPLEENABLEANTIALIASEDLINEENABLE | Members of [**D3D10\_RASTERIZER\_DESC**](/windows/win32/D3D10/ns-d3d10-d3d10_rasterizer_desc?branch=master) |



 

## Sampler State



|                                                                                                     |                                                               |
|-----------------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| Filter AddressU AddressV AddressW MipLODBias MaxAnisotropy ComparisonFunc BorderColor MinLOD MaxLOD | Members of [**D3D10\_SAMPLER\_DESC**](/windows/win32/D3D10/ns-d3d10-d3d10_sampler_desc?branch=master) |



 

See [Sampler Type (DirectX HLSL)](direct3dhlsl.dx_graphics_hlsl_sampler) for examples.

## Effect Object State



| This Effect Object                          | Maps to                                                             |
|---------------------------------------------|---------------------------------------------------------------------|
| RASTERIZERSTATE                             | A [Rasterizer State](#rasterizer-state) state object.               |
| DEPTHSTENCILSTATE                           | A [Depth and Stencil State](#depth-and-stencil-state) state object. |
| BLENDSTATE                                  | A [Blend State](#blend-state) state object.                         |
| VERTEXSHADER                                | A compiled vertex shader object.                                    |
| PIXELSHADER                                 | A compiled pixel shader object.                                     |
| GEOMETRYSHADER                              | A compiled geometry shader object.                                  |
| DS\_STENCILREFAB\_BLENDFACTORAB\_SAMPLEMASK | Members of [**D3D10\_PASS\_DESC**](/windows/win32/d3d10effect/ns-d3d10effect-_d3d10_pass_desc?branch=master).            |



 

## Defining and using state objects

State objects are declared in FX files in the following format. StateObjectType is one of the states listed above and MemberName is the name of any member that will have a non-default value.


```
StateObjectType ObjectName {
  MemberName = value;
  ...
  MemberName = value;
};
    
```



For example, to set up a blend state object with AlphaToCoverageEnable and BlendEnable\[0\] set to **FALSE** the following code would be used.


```
BlendState NoBlend {
  AlphaToCoverageEnable = FALSE;
  BlendEnable[0] = FALSE;
};
    
```



The state object is applied to a technique pass using one of the SetStateGroup functions described in [Effect Technique Syntax (Direct3D 10)](d3d10-effect-technique-syntax.md). For example, to apply the BlendState object described above the following code would be used.


```
SetBlendState( NoBlend, float4( 0.0f, 0.0f, 0.0f, 0.0f ), 0xFFFFFFFF );
    
```



For a tutorial describing the use of states see [State Management](be31385b-36ff-48e6-149b-423e356917a8).

## Related topics

<dl> <dt>

[Effect Technique Syntax](d3d10-effect-technique-syntax.md)
</dt> <dt>

[Effect Format (Direct3D 10)](d3d10-effect-format.md)
</dt> </dl>

 

 



