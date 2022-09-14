---
title: Accessing Resources
description: There are several ways to access resources.
ms.assetid: 83950c4d-5df2-4ed1-9d8f-222a62791c18
ms.topic: article
ms.date: 05/31/2018
---

# Accessing Resources

There are several ways to access [resources](overviews-direct3d-11-resources-types.md). Regardless, Direct3D guarantees to return zero for any resource that is accessed out of bounds.

-   [Access By Byte Offset](#access-by-byte-offset)
-   [Access By Index](#access-by-index)
-   [Access By Mips Method](#access-by-mips-method)
-   [Related topics](#related-topics)

## Access By Byte Offset

Two new buffer types can be accessed using a byte offset:

-   [**ByteAddressBuffer**](/windows/desktop/direct3dhlsl/sm5-object-byteaddressbuffer) is a read-only buffer.
-   [**RWByteAddressBuffer**](/windows/desktop/direct3dhlsl/sm5-object-rwbyteaddressbuffer) is a read or write buffer.

## Access By Index

Resource types can use an index to reference a specific location in the resource. Consider this example:


```
uint2 pos;
Texture2D<float4> myTexture;
float4 myVar = myTexture[pos];
```



This example assigns the 4 float values that are stored at the texel located at the *pos* position in the *myTexture* 2D texture resource to the *myVar* variable.

> [!Note]  
> The default for accessing a texture in this way is mipmap level zero (the most detailed level).

 

> [!Note]  
> The "float4 myVar = myTexture\[pos\];" line is equivalent to "float4 myVar = myTexture.Load(uint3(pos,0));". Access by index is a new HLSL syntax enhancement.

 

> [!Note]  
> The compiler in the June 2010 version of the DirectX SDK and later lets you index all resource types except for [byte address buffers](direct3d-11-advanced-stages-cs-resources.md).

 

> [!Note]  
> The June 2010 compiler and later lets you declare local resource variables. You can assign globally defined resources (like *myTexture*) to these variables and use them the same way as their global counterparts.

 

## Access By Mips Method

Texture objects have a **mips** method (for example, [**Texture2D.mips**](/previous-versions/windows/desktop/legacy/ff471560(v=vs.85))), which you can use to specify the mipmap level. This example reads the color stored at (7,16) on mipmap level 2 in a 2D texture:


```
uint x = 7;
uint y = 16;
float4 myColor = myTexture.mips[2][uint2(x,y)];
```



This is an enhancement from the June 2010 compiler and later. The "myTexture.mips\[2\]\[uint2(x,y)\]" expression is equivalent to "myTexture.Load(uint3(x,y,2))".

## Related topics

<dl> <dt>

[Compute Shader Overview](direct3d-11-advanced-stages-compute-shader.md)
</dt> </dl>

 

 