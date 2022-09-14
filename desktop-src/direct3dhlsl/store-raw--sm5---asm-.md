---
title: store_raw (sm5 - asm)
description: Random-access write of 1-4 32bit components into typeless memory.
ms.assetid: D166116A-CF4E-4020-9F6A-F9CEEFCDAB21
ms.topic: reference
ms.date: 05/31/2018
---

# store\_raw (sm5 - asm)

Random-access write of 1-4 32bit components into typeless memory.



| store\_raw dst0\[.write\_mask\], dstByteOffset\[.select\_component\], src0\[.swizzle\] |
|----------------------------------------------------------------------------------------|



 



| Item                                                                                                                       | Description                                |
|----------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|
| <span id="dst0"></span><span id="DST0"></span>*dst0*<br/>                                                            | \[in\] The memory address.<br/>      |
| <span id="dstByteOffset"></span><span id="dstbyteoffset"></span><span id="DSTBYTEOFFSET"></span>*dstByteOffset*<br/> | \[in\] The offset.<br/>              |
| <span id="src0"></span><span id="SRC0"></span>*src0*<br/>                                                            | \[in\] The components to write.<br/> |



 

## Remarks

This instruction performs 1-4 component \*32-bit components written from *src0* to *dst0* at the offset in *dstByteOffset*. There is no format conversion.

*dst0* must be a UAV (u\#), or in the compute shader it can also be thread group shared memory (g\#).

*dstByteOffset* specifies the base 32-bit value in memory for a window of 4 sequential 32-bit values in which data may be written, depending on the swizzle and mask on other parameters.

The location of the data written is equivalent to the following pseudocode which show the address, pointer to the buffer contents, and the data stored linearly.

``` syntax
                    BYTE *BufferContents;          // from src0
                    UINT dstByteOffset;            // source register
                    BYTE *WriteLocation;           // value to calculate

                    // calculate writing location
                    WriteLocation = BufferContents 
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
                             WriteComponents * sizeof(UINT32));
```

This pseudocode shows how the operation functions, but the actual data does not have to be stored linearly. *dst0* can only have a write mask that is one of the following: .x, .xy, .xyz, .xyzw. The write mask determines the number of 32bit components to write without gaps.

Out of bounds addressing on u\# means nothing is written to the out of bounds memory; any part that is in bounds is written correctly.

Out of bounds addressing on g\# (the bounds of that particular g\#, as opposed to all shared memory) for any given 32-bit component causes the entire contents of all shared memory to become undefined.

cs\_4\_0 and cs\_4\_1 support this instruction for UAV.

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

 

 





