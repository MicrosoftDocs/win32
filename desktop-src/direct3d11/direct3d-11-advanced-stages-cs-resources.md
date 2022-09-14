---
title: New Resource Types
description: Several new resource types have been added in Direct3D 11.
ms.assetid: 597cc12f-dd0e-4603-b670-3f584f25e192
keywords:
- Byte Address Buffer (Overview)
- Read/Write Buffer (Overview)
- Structured Buffer (Overview)
- Unordered Access Buffer
ms.topic: article
ms.date: 05/31/2018
---

# New Resource Types

Several new resource types have been added in Direct3D 11.

-   [Read/Write Buffers and Textures](#readwrite-buffers-and-textures)
-   [Structured Buffer](#structured-buffer)
-   [Byte Address Buffer](#byte-address-buffer)
-   [Unordered Access Buffer or Texture](#unordered-access-buffer-or-texture)
    -   [Append and Consume Buffer](#append-and-consume-buffer)
-   [Related topics](#related-topics)

## Read/Write Buffers and Textures

Shader model 4 resources are read only. Shader model 5 implements a new corresponding set of read/write resources:

-   [RWBuffer](/windows/desktop/direct3dhlsl/sm5-object-rwbuffer)
-   [RWTexture1D](/windows/desktop/direct3dhlsl/sm5-object-rwtexture1d), [RWTexture1DArray](/windows/desktop/direct3dhlsl/sm5-object-rwtexture1darray)
-   [RWTexture2D](/windows/desktop/direct3dhlsl/sm5-object-rwtexture2d), [RWTexture2DArray](/windows/desktop/direct3dhlsl/sm5-object-rwtexture2darray)
-   [RWTexture3D](/windows/desktop/direct3dhlsl/sm5-object-rwtexture3d)

These resources require a resource variable to access memory (through indexing) as there are no methods for accessing memory directly. A resource variable can be used on the left and right sides of an equation; if used on the right side, the template type must be single component (float, int, or uint).

## Structured Buffer

A structured buffer is a buffer that contains elements of equal sizes. Use a structure with one or more member types to define an element. Here is a structure with three members.


```
struct MyStruct
{
    float4 Color;
    float4 Normal;
    bool isAwesome;
};
```



Use this structure to declare a structured buffer like this:


```
StructuredBuffer<MyStruct> mySB;
```



In addition to indexing, a structured buffer supports accessing a single member like this:


```
float4 myColor = mySb[27].Color;
```



Use the following object types to access a structured buffer:

-   [StructuredBuffer](/windows/desktop/direct3dhlsl/sm5-object-structuredbuffer) is a read only structured buffer.
-   [RWStructuredBuffer](/windows/desktop/direct3dhlsl/sm5-object-rwstructuredbuffer) is a read/write structured buffer.

[Atomic functions](direct3d-11-advanced-stages-cs-atomic-functions.md) which implement interlocked operations are allowed on int and uint elements in an **RWStructuredBuffer**.

## Byte Address Buffer

A byte address buffer is a buffer whose contents are addressable by a byte offset. Normally, the contents of a [buffer](overviews-direct3d-11-resources-buffers-intro.md) are indexed per element using a stride for each element (S) and the element number (N) as given by S\*N. A byte address buffer, which can also be called a raw buffer, uses a byte value offset from the beginning of the buffer to access data. The byte value must be a multiple of four so that it is DWORD aligned. If any other value is provided, behavior is undefined.

Shader model 5 introduces objects for accessing a [read-only byte address buffer](/windows/desktop/direct3dhlsl/sm5-object-byteaddressbuffer) as well as a [read-write byte address buffer](/windows/desktop/direct3dhlsl/sm5-object-rwbyteaddressbuffer). The contents of a byte address buffer is designed to be a 32-bit unsigned integer; if the value in the buffer is not really an unsigned integer, use a function such as [**asfloat**](/windows/desktop/direct3dhlsl/dx-graphics-hlsl-asfloat) to read it.

## Unordered Access Buffer or Texture

An unordered access resource (which includes buffers, textures, and texture arrays - without multisampling), allows temporally unordered read/write access from multiple threads. This means that this resource type can be read/written simultaneously by multiple threads without generating memory conflicts through the use of [Atomic Functions](direct3d-11-advanced-stages-cs-atomic-functions.md).

Create an unordered access buffer or texture by calling a function such as [**ID3D11Device::CreateBuffer**](/windows/desktop/api/D3D11/nf-d3d11-id3d11device-createbuffer) or [**ID3D11Device::CreateTexture2D**](/windows/desktop/api/D3D11/nf-d3d11-id3d11device-createtexture2d) and passing in the **D3D11\_BIND\_UNORDERED\_ACCESS** flag from the [**D3D11\_BIND\_FLAG**](/windows/desktop/api/D3D11/ne-d3d11-d3d11_bind_flag) enumeration.

Unordered access resources can only be bound to pixel shaders and compute shaders. During execution, pixel shaders or compute shaders running in parallel have the same unordered access resources bound.

### Append and Consume Buffer

An append and consume buffer is a special type of an unordered resource that supports adding and removing values from the end of a buffer similar to the way a stack works.

An append and consume buffer must be a structured buffer:

-   [AppendStructuredBuffer](/windows/desktop/direct3dhlsl/sm5-object-appendstructuredbuffer)
-   [ConsumeStructuredBuffer](/windows/desktop/direct3dhlsl/sm5-object-consumestructuredbuffer)

Use these resources through their methods, these resources do not use resource variables.

## Related topics

<dl> <dt>

[Compute Shader Overview](direct3d-11-advanced-stages-compute-shader.md)
</dt> </dl>

 

 