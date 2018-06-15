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
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Buffer Type

Use the following syntax to declare a buffer variable.



| Buffer&lt;*Type*&gt; *Name*; |
|------------------------------|



 

## Parameters

<dl> <dt>

<span id="Buffer"></span><span id="buffer"></span><span id="BUFFER"></span>**Buffer**
</dt> <dd>

Required keyword.

</dd> <dt>

<span id="Type"></span><span id="type"></span><span id="TYPE"></span>*Type*
</dt> <dd>

One of the [scalar](dx-graphics-hlsl-scalar.md), [vector](dx-graphics-hlsl-vector.md), and some [matrix](dx-graphics-hlsl-matrix.md) HLSL types. You can declare a buffer variable with a matrix as long as it fits in 4 32-bit quantities. So, you can write Buffer&lt;float2x2&gt;. But Buffer&lt;float4x4&gt; is too large, and the compiler will generate an error.

</dd> <dt>

<span id="Name"></span><span id="name"></span><span id="NAME"></span>*Name*
</dt> <dd>

An ASCII string that uniquely identifies the variable name.

</dd> </dl>

## Example

Here is an example of a buffer declaration from the PipesGS.fx file in [PipesGS Sample](https://msdn.microsoft.com/en-us/library/Ee416423(v=VS.85).aspx).


```
Buffer<float4> g_Buffer;
```



Data is read from a buffer using an overloaded version of the [**Load**](dx-graphics-hlsl-to-load.md) HLSL intrinsic function that takes one input parameter (an integer index). A buffer is accessed like an array of elements; therefore, this example reads the second element.


```
float4 bufferData = g_Buffer.Load( 1 );
```



Use the [stream-output stage](https://msdn.microsoft.com/library/windows/desktop/bb205121) to output data to a buffer.

## See also

<dl> <dt>

[Data Types (DirectX HLSL)](dx-graphics-hlsl-data-types.md)
</dt> </dl>

 

 




