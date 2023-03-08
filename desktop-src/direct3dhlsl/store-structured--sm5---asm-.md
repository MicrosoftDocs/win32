---
title: store_structured (sm5 - asm)
description: Random-access write of 1-4 32-bit components into a structured buffer unordered access view (UAV).
ms.assetid: 8080B2CA-5BDA-4F01-8B2B-B85BDD58C5AF
ms.topic: reference
ms.date: 05/31/2018
---

# store\_structured (sm5 - asm)

Random-access write of 1-4 32-bit components into a structured buffer unordered access view (UAV).



| store\_structured dest\[.write\_mask\], dstAddress\[.select\_component\], dstByteOffset\[.select\_component\], src0\[.swizzle\] |
|---------------------------------------------------------------------------------------------------------------------------------|



 



| Item                                                                                                                       | Description                                                    |
|----------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| <span id="dest"></span><span id="DEST"></span>*dest*<br/>                                                            | \[in\] The address of the results of the operation.<br/> |
| <span id="dstAddress"></span><span id="dstaddress"></span><span id="DSTADDRESS"></span>*dstAddress*<br/>             | \[in\] The address at which to write.<br/>               |
| <span id="dstByteOffset"></span><span id="dstbyteoffset"></span><span id="DSTBYTEOFFSET"></span>*dstByteOffset*<br/> | \[in\] The index of the structure to write.<br/>         |
| <span id="src0"></span><span id="SRC0"></span>*src0*<br/>                                                            | \[in\] The components to write.<br/>                     |



 

## Remarks

This instruction performs 1-4 component \*32bit components written from *src0* to *dest* at the address in *dstAddress* and *dstByteOffset*. No format conversion.

*dest* must be a UAV (u\#). In the compute shader it can also be thread group shared memory (g\#).

*dstAddress* specifies the index of the structure to write.

The location of the data written is equivalent to the following pseudocode which shows the offset, address, pointer to the buffer contents, stride of the source, and the data stored linearly.

``` syntax
                    BYTE *BufferContents;             // from dest
                    UINT BufferStride;                // from dest
                    UINT dstAddress, dstByteOffset;   // source registers
                    BYTE *WriteLocation;              // value to calculate

                    // calculate writing location
                     WriteLocation = BufferContents 
                                + BufferStride * dstAddress 
                                + dstByteOffset;

                    // calculate the number of components to write
                    switch (dstWriteMask)
                    {
                        x:    WriteComponents = 1; break;
                        xy:   WriteComponents = 2; break;
                        xyz:  WriteComponents = 3; break;
                        xyzw: WriteComponents = 4; break;
                        default:  // only these masks are valid                              
                    }

                    // copy the data from the source register with
                    //    the swizzle applied
                    memcpy(WriteLocation, swizzle(src0, src0.swizzle), 
                             WriteComponents * sizeof(INT32));
```

This pseudocode shows how the operation functions, but the actual data does not have to be stored linearly. If the data is not stored linearly, the actual operation of the instruction needs to match the behavior of the above operation.

*dest* can only have a write mask that is one of the following: .x, .xy, .xyz, .xyzw. The write mask determines the number of 32-bit components to write without gaps.

Out of bounds addressing on u\# casued by *dstAddress* means nothing is written to the out of bounds memory.

If the *dstByteOffset*, including *dstWriteMask*, is what causes out of bounds access to u\#, the entire contents of the UAV become undefined.

Out of bounds addressing on g\# (the bounds of that particular g\#, as opposed to all shared memory) for any given 32-bit component causes the entire contents of all shared memory to become undefined.

*dstByteOffset* is a separate argument from *dstAddress* because it is commonly a literal. This parameter separation has not been done for atomics on structured memory.

cs\_4\_0 and cs\_4\_1 support this instruction for UAV and TGSM.

This instruction applies to the following shader stages:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
|        |      |        |          | X     | X       |



 

Because UAVs are available at all shader stages for Direct3D 11.1, this instruction applies to all shader stages for the Direct3D 11.1 runtime, which is available starting with Windows 8.



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
| X      | X    | X      | X        | X     | X       |



 

## Minimum Shader Model

This instruction is supported in the following shader models:



| Shader Model                                              | Supported |
|-----------------------------------------------------------|-----------|
| [Shader Model 5](d3d11-graphics-reference-sm5.md)        | yes       |
| [Shader Model 4.1](dx-graphics-hlsl-sm4.md)              | no        |
| [Shader Model 4](dx-graphics-hlsl-sm4.md)                | no        |
| [Shader Model 3 (DirectX HLSL)](dx-graphics-hlsl-sm3.md) | no        |
| [Shader Model 2 (DirectX HLSL)](dx-graphics-hlsl-sm2.md) | no        |
| [Shader Model 1 (DirectX HLSL)](dx-graphics-hlsl-sm1.md) | no        |



 

## Related topics

<dl> <dt>

[Shader Model 5 Assembly (DirectX HLSL)](shader-model-5-assembly--directx-hlsl-.md)
</dt> </dl>

 

 





