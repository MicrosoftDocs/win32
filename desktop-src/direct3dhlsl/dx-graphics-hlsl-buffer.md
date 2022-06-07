---
title: Buffer Type
description: Use the following syntax to declare a buffer variable.
ms.assetid: f21f0de5-58e3-466b-97bb-e4e7efa9cc1c
keywords:
- Buffer Type HLSL
topic_type:
- apiref
api_name:
- Buffer Type
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Buffer Type

Use the following syntax to declare a buffer variable.



| Buffer<*Type*> *Name*; |
|------------------------------|



 

## Parameters

<dl> <dt>

<span id="Buffer"></span><span id="buffer"></span><span id="BUFFER"></span>**Buffer**
</dt> <dd>

Required keyword.

</dd> <dt>

<span id="Type"></span><span id="type"></span><span id="TYPE"></span>*Type*
</dt> <dd>

One of the [scalar](dx-graphics-hlsl-scalar.md), [vector](dx-graphics-hlsl-vector.md), and some [matrix](dx-graphics-hlsl-matrix.md) HLSL types. You can declare a buffer variable with a matrix as long as it fits in 4 32-bit quantities. So, you can write `Buffer<float2x2>`. But `Buffer<float4x4>` is too large, and the compiler will generate an error.

</dd> <dt>

<span id="Name"></span><span id="name"></span><span id="NAME"></span>*Name*
</dt> <dd>

An ASCII string that uniquely identifies the variable name.

</dd> </dl>

## Example

Here is an example of a buffer declaration.


```
Buffer<float4> g_Buffer;
```



Data is read from a buffer using an overloaded version of the [**Load**](dx-graphics-hlsl-to-load.md) HLSL intrinsic function that takes one input parameter (an integer index). A buffer is accessed like an array of elements; therefore, this example reads the second element.


```
float4 bufferData = g_Buffer.Load( 1 );
```



Use the [stream-output stage](/windows/desktop/direct3d11/d3d10-graphics-programming-guide-output-stream-stage) to output data to a buffer.

## See also

<dl> <dt>

[Data Types (DirectX HLSL)](dx-graphics-hlsl-data-types.md)
</dt> </dl>

 

 
