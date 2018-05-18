---
title: How To Design a Hull Shader
description: This topics shows how to design a hull shader.
ms.assetid: 'c11c5652-dd7d-433d-bfa2-9853618ba334'
---

# How To: Design a Hull Shader

A hull shader is the first of three stages that work together to implement [tessellation](direct3d-11-advanced-stages-tessellation.md) (the other two stages are the tessellator and a domain shader). This topics shows how to design a hull shader.

A hull shader requires two functions, the main hull shader and a patch constant function. The hull shader implements calculations on each control point; the hull shader also calls the patch constant function which implements calculations on each patch.

After you have designed a hull shader, see [How To: Create a Hull Shader](direct3d-11-advanced-stages-hull-shader-create.md) to learn how to create a hull shader.

**To design a hull shader**

1.  Define hull shader input control and output control points.

    ```
    // Input control point
    struct VS_CONTROL_POINT_OUTPUT
    {
        float3 vPosition : WORLDPOS;
        float2 vUV       : TEXCOORD0;
        float3 vTangent  : TANGENT;
    };

    // Output control point
    struct BEZIER_CONTROL_POINT
    {
        float3 vPosition    : BEZIERPOS;
    };
    ```

    

2.  Define output patch constant data.

    ```
    // Output patch constant data.
    struct HS_CONSTANT_DATA_OUTPUT
    {
        float Edges[4]        : SV_TessFactor;
        float Inside[2]       : SV_InsideTessFactor;
        
        float3 vTangent[4]    : TANGENT;
        float2 vUV[4]         : TEXCOORD;
        float3 vTanUCorner[4] : TANUCORNER;
        float3 vTanVCorner[4] : TANVCORNER;
        float4 vCWts          : TANWEIGHTS;
    };
    ```

    

    For a quad domain, [SV\_TessFactor](https://msdn.microsoft.com/library/windows/desktop/ff471574) defines 4 edge tessellation factors (to tessellate the edges), since the fixed function tessellator needs to know how much to tessellate. The required outputs are different for the triangle and isoline domains.

    The fixed function tessellator doesn't look at any other hull shader outputs, such as other patch constant data or any of the control points. The domain shader -- which is invoked for each point the fixed function tessellator generates -- will see as its input all the hull shader's output control points and all the output patch constant data; the shader evaluates the patch at its location.

3.  Define a patch constant function. A patch constant function executes once for each patch to calculate any data that is constant for the entire patch (as opposed to per-control point data, which is computed in the hull shader).

    ```
    
    #define MAX_POINTS 32

    // Patch Constant Function
    HS_CONSTANT_DATA_OUTPUT SubDToBezierConstantsHS( 
        InputPatch<VS_CONTROL_POINT_OUTPUT, MAX_POINTS> ip,
        uint PatchID : SV_PrimitiveID )
    {   
        HS_CONSTANT_DATA_OUTPUT Output;

        // Insert code to compute Output here
        
        return Output;
    }
    ```

    

    Properties of the patch constant function include:

    -   One input specifies a variable containing a patch id, and is identified by the **SV\_PrimitiveID** system value (see [semantics](http://msdn.microsoft.com/library/bb509647(VS.85).aspx) in shader model 4).
    -   One input parameter is the input control points, declared in **VS\_CONTROL\_POINT\_OUTPUT** in this example. A patch function can see all the input control points for each patch, there are 32 control points per patch in this example.
    -   As a minimum, the function must calculate per-patch tessellation factors for the tessellator stage which are identified with [SV\_TessFactor](https://msdn.microsoft.com/library/windows/desktop/ff471574). A quad domain requires four tessellation factors for the edges and two additional factors (identified by [SV\_InsideTessFactor](https://msdn.microsoft.com/library/windows/desktop/ff471572)) for tessellating the inside of the patch. The fixed function tessellator doesn't look at any other hull shader outputs (such as the patch constant data or any of the control points).
    -   The outputs are usually defined by a structure and is identified by **HS\_CONSTANT\_DATA\_OUTPUT** in this example; the structure depends on the domain type and would be different for triangle or isoline domains.

    A domain shader on the other hand is invoked for each point the fixed function tessellator generates and needs to see the output control points and the output patch constant data (both from the hull shader) to evaluate a patch at its location.

4.  Define a hull shader. A hull shader identifies the properties of a patch including a patch constant function. A hull shader is invoked once for each output control point.

    ```
    [domain("quad")]
    [partitioning("integer")]
    [outputtopology("triangle_cw")]
    [outputcontrolpoints(16)]
    [patchconstantfunc("SubDToBezierConstantsHS")]
    BEZIER_CONTROL_POINT SubDToBezierHS( 
        InputPatch<VS_CONTROL_POINT_OUTPUT, MAX_POINTS> ip, 
        uint i : SV_OutputControlPointID,
        uint PatchID : SV_PrimitiveID )
    {
        VS_CONTROL_POINT_OUTPUT Output;

        // Insert code to compute Output here.
        
        return Output;
    }
    ```

    

    A hull shader uses the following attributes:

    -   A [domain](https://msdn.microsoft.com/library/windows/desktop/ff471438) attribute.
    -   A [partitioning](https://msdn.microsoft.com/library/windows/desktop/ff471446) attribute.
    -   An [outputtopology](https://msdn.microsoft.com/library/windows/desktop/ff471445) attribute.
    -   An [outputcontrolpoints](https://msdn.microsoft.com/library/windows/desktop/ff471443) attribute.
    -   A [patchconstantfunc](https://msdn.microsoft.com/library/windows/desktop/ff471447) attribute. A hull shader calculates output control points, there are 16 output Bezier control points in this example.

All the input control points (identified by **VS\_CONTROL\_POINT\_OUTPUT**) are visible to each hull shader invocation. In this example, there are 32 input control points.

A hull shader is invoked once per output control point (identified with [SV\_OutputControlPointID](https://msdn.microsoft.com/library/windows/desktop/ff471573)) for each patch (identified with SV\_PrimitiveID). The purpose of this particular shader is to calculate output *i*, which was defined to be a BEZIER control point (this example has 16 output control points defined by outputcontrolpoints).

A hull shader runs a routine once per patch (the patch constant function) to compute patch-constant data (tessellation factors as a minimum). Separately, a hull shader runs a patch constant function (called SubDToBezierConstantsHS) on each patch to compute patch-constant data such as tessellation factors for the tessellator stage.

## Related topics

<dl> <dt>

[How to Use Direct3D 11](how-to-use-direct3d-11.md)
</dt> <dt>

[Tessellation Overview](direct3d-11-advanced-stages-tessellation.md)
</dt> </dl>

 

 




