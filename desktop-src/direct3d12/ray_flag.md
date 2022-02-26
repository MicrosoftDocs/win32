---
description: Flags passed to the TraceRay function to override transparency, culling, and early-out behavior.
ms.assetid: 
title: RAY_FLAG enumeration
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- RAY_FLAG
api_type: 
- NA
---

# RAY\_FLAG enumeration

Flags passed to the [**TraceRay**](traceray-function.md) function to override transparency, culling, and early-out behavior.

## Syntax


```
enum RAY_FLAG : uint
{
    RAY_FLAG_NONE                            = 0x00,
    RAY_FLAG_FORCE_OPAQUE                    = 0x01,
    RAY_FLAG_FORCE_NON_OPAQUE                = 0x02,
    RAY_FLAG_ACCEPT_FIRST_HIT_AND_END_SEARCH = 0x04,
    RAY_FLAG_SKIP_CLOSEST_HIT_SHADER         = 0x08,
    RAY_FLAG_CULL_BACK_FACING_TRIANGLES      = 0x10,
    RAY_FLAG_CULL_FRONT_FACING_TRIANGLES     = 0x20,
    RAY_FLAG_CULL_OPAQUE                     = 0x40,
    RAY_FLAG_CULL_NON_OPAQUE                 = 0x80,
    RAY_FLAG_SKIP_TRIANGLES                  = 0x100,
    RAY_FLAG_SKIP_PROCEDURAL_PRIMITIVES      = 0x200,
}; 
```



## Constants

<dl> <dt>

<span id="RAY_FLAG_NONE"></span><span id="ray_flag_none"></span>**RAY\_FLAG\_NONE**
</dt> <dd>

No options selected.

</dd> <dt>

<span id="RAY_FLAG_FORCE_OPAQUE"></span><span id="ray_flag_force_opaque"></span>**RAY\_FLAG\_FORCE\_OPAQUE**
</dt> <dd>

All ray-primitive intersections encountered in a raytrace are treated as opaque.  So no any hit shaders will be executed regardless of whether or not the hit geometry specifies D3D12\_RAYTRACING\_GEOMETRY\_FLAG\_OPAQUE, and regardless of the instance flags on the instance that was hit.

This flag is mutually exclusive with RAY\_FLAG\_FORCE\_NON\_OPAQUE, RAY\_FLAG\_CULL\_OPAQUE and RAY\_FLAG\_CULL\_NON\_OPAQUE.


</dd> <dt>

<span id="RAY_FLAG_FORCE_NON_OPAQUE"></span><span id="ray_flag_force_non_opaque"></span>**RAY\_FLAG\_FORCE\_NON\_OPAQUE**
</dt> <dd>

All ray-primitive intersections encountered in a raytrace are treated as non-opaque.  So any hit shaders, if present, will be executed regardless of whether or not the hit geometry specifies D3D12\_RAYTRACING\_GEOMETRY\_FLAG\_OPAQUE, and regardless of the instance flags on the instance that was hit.
This flag is mutually exclusive with RAY\_FLAG\_FORCE_\OPAQUE, RAY\_FLAG\_CULL\_OPAQUE and RAY\_FLAG\_CULL\_NON\_OPAQUE.


</dd> <dt>

<span id="RAY_FLAG_ACCEPT_FIRST_HIT_AND_END_SEARCH"></span><span id="ray_flag_accept_first_hit_and_end_search"></span>**RAY\_FLAG\_ACCEPT\_FIRST\_HIT\_AND\_END\_SEARCH**
</dt> <dd>

The first ray-primitive intersection encountered in a raytrace automatically causes **AcceptHitAndEndSearch** to be called immediately after the any hit shader, including if there is no any hit shader. 
 
The only exception is when the preceding any hit shader calls **IgnoreHit**, in which case the ray continues unaffected such that the next hit becomes another candidate to be the first hit.  For this exception to apply, the any hit shader has to actually be executed.  So if the any hit shader is skipped because the hit is treated as opaque (e.g. due to RAY\_FLAG\_FORCE\_OPAQUE or D3D12\_RAYTRACING\_GEOMETRY\_FLAG\_OPAQUE or D3D12\_RAYTRACING\_INSTANCE\_FLAG\_OPAQUE being set), then **AcceptHitAndEndSearch** is called.

If a closest hit shader is present at the first hit, it gets invoked unless RAY\_FLAG\_SKIP\_CLOSEST\_HIT\_SHADER is also present.  The one hit that was found is considered “closest”, even though other potential hits that might be closer on the ray may not have been visited.

A typical use for this flag is for shadows, where only a single hit needs to be found.


</dd> <dt>

<span id="RAY_FLAG_SKIP_CLOSEST_HIT_SHADER"></span><span id="ray_flag_skip_closest_hit_shader"></span>**RAY\_FLAG\_SKIP\_CLOSEST\_HIT\_SHADER**
</dt> <dd>

Even if at least one hit has been committed, and the hit group for the closest hit contains a closest hit shader, skip execution of that shader. 

</dd> <dt>

<span id="RAY_FLAG_CULL_BACK_FACING_TRIANGLES"></span><span id="ray_flag_cull_back_facing_triangles"></span>**RAY\_FLAG\_CULL\_BACK\_FACING\_TRIANGLES**
</dt> <dd>

Enables culling of back facing triangles. See **D3D12\_RAYTRACING\_INSTANCE\_FLAGS** for selecting which triangles are back facing, per-instance.

On instances that specify D3D12\_RAYTRACING\_INSTANCE\_FLAG\_TRIANGLE\_CULL\_DISABLE, this flag has no effect.

On geometry types other than D3D12\_RAYTRACING\_GEOMETRY\_TYPE\_TRIANGLES, this flag has no effect.

This flag is mutually exclusive with RAY\_FLAG\_CULL\_FRONT\_FACING\_TRIANGLES.


</dd> <dt>

<span id="RAY_FLAG_CULL_FRONT_FACING_TRIANGLES"></span><span id="ray_flag_cull_front_facing_trianglesag_none"></span>**RAY\_FLAG\_CULL\_FRONT\_FACING\_TRIANGLES**
</dt> <dd>

Enables culling of front facing triangles. See **D3D12\_RAYTRACING\_INSTANCE\_FLAGS** for selecting which triangles are back facing, per-instance.

On instances that specify D3D12\_RAYTRACING\_INSTANCE\_FLAG\_TRIANGLE\_CULL\_DISABLE, this flag has no effect.

On geometry types other than D3D12\_RAYTRACING\_GEOMETRY\_TYPE\_TRIANGLES, this flag has no effect.

This flag is mutually exclusive with RAY\_FLAG\_CULL\_BACK\_FACING\_TRIANGLES.


</dd> <dt>

<span id="RAY_FLAG_CULL_OPAQUE"></span><span id="ray_flag_cull_opaque"></span>**RAY\_FLAG\_CULL\_OPAQUE**
</dt> <dd>

Culls all primitives that are considered opaque based on their geometry and instance flags.

This flag is mutually exclusive with RAY\_FLAG\_FORCE\_OPAQUE, RAY\_FLAG\_FORCE\_NON\_OPAQUE, and RAY\_FLAG\_CULL\_NON\_OPAQUE.


</dd> <dt>

<span id="RAY_FLAG_CULL_NON_OPAQUE"></span><span id="ray_flag_cull_non_opaque"></span>**RAY\_FLAG\_CULL\_NON\_OPAQUE**
</dt> <dd>

Culls all primitives that are considered non-opaque based on their geometry and instance flags.

This flag is mutually exclusive with RAY\_FLAG\_FORCE\_OPAQUE, RAY\_FLAG\_FORCE\_NON\_OPAQUE, and RAY\_FLAG\_CULL\_OPAQUE.


</dd>

## Requirements



## See also

<dl> <dt>

[Direct3D 12 Raytracing HLSL Reference](direct3d-12-raytracing-hlsl-reference.md)
</dt> </dl>

 

 




