---
title: ld_structured (sm5 - asm)
description: Random-access read of 1-4 32bit components from a structured buffer.
ms.assetid: ED572B76-FF6C-405E-9110-4B12AD5E5AE6
ms.topic: reference
ms.date: 05/31/2018
---

# ld\_structured (sm5 - asm)

Random-access read of 1-4 32bit components from a structured buffer.



| : ld\_structured dst0\[.mask\], srcAddress\[.select\_component\], srcByteOffset\[.select\_component\], src0\[.swizzle\] |
|-------------------------------------------------------------------------------------------------------------------------|



 



| Item                                                                                                                       | Description                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="dst0"></span><span id="DST0"></span>*dst0*<br/>                                                            | \[in\] The address of the results of the operation.<br/>                                                                                             |
| <span id="srcAddress"></span><span id="srcaddress"></span><span id="SRCADDRESS"></span>*srcAddress*<br/>             | \[in\] Specifies the index of the structure to read.<br/>                                                                                            |
| <span id="srcByteOffset"></span><span id="srcbyteoffset"></span><span id="SRCBYTEOFFSET"></span>*srcByteOffset*<br/> | \[in\] Specifies the byte offset in the structure to start reading from. <br/>                                                                       |
| <span id="src0"></span><span id="SRC0"></span>*src0*<br/>                                                            | The buffer to read from. This parameter must be a SRV (t\#), UAV (u\#). In the compute shader it can also be thread group shared memory (g\#). <br/> |



 

## Remarks

The data read from the structure is equivalent to the following pseudocode: where we have the offset, address, pointer to the buffer contents, stride of the source, and the data stored linearly.

``` syntax
                    BYTE *BufferContents;         // from SRV or UAV
                    UINT BufferStride;            // from base resource
                    UINT srcAddress, srcByteOffset;   // from source registers
                    BYTE *ReadLocation;           // value to calculate
                    ReadLocation = BufferContents 
                                + BufferStride * srcByteOffset
                                + srcOffset;

                    UINT32 Temp[4];  // used to make code shorter

                    // apply the source resource swizzle on source data
                    Temp = read_and_swizzle(ReadLocation, srcSwizzle);

                    // write the components to the output based on mask
                    ApplyWriteMask(dstRegister, dstWriteMask, Temp);
```

This pseudocode shows how the operation functions, but the actual data does not have to be stored linearly. If the data is not stored linearly, the actual operation of the instruction needs to match the behavior of the above operation.

Out of bounds addressing on u\#/t\# of any given 32-bit component returns 0 for that component, except if *srcByteOffset*, plus swizzle is what causes out of bounds access to u\#/t\#, the returned value for all component(s) is undefined.

Out of bounds addressing on g\# (the bounds of that particular g\#, as opposed to all shared memory) for any given 32-bit component returns an undefined result.

*srcByteOffset* is a separate argument from *srcAddress* because it is commonly a literal. This parameter separation has not been done for atomics on structured memory.

cs\_4\_0 and cs\_4\_1 support this instruction for UAV, SRV, and TGSM.

This instruction applies to the following shader stages:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
| X      | X    | X      | X        | X     | X       |



 

Because UAVs are available at all shader stages for Direct3D 11.1, this instruction applies to all shader stages for UAVs for the Direct3D 11.1 runtime, which is available starting with Windows 8.



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



 

cs\_4\_0 and cs\_4\_1 support this instruction for UAV, SRV and TGSM.

## Related topics

<dl> <dt>

[Shader Model 5 Assembly (DirectX HLSL)](shader-model-5-assembly--directx-hlsl-.md)
</dt> </dl>

 

 





