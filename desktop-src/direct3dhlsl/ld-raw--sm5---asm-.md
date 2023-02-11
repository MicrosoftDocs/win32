---
title: ld_raw (sm5 - asm)
description: Random-access read of 1-4 32bit components from a raw buffer.
ms.assetid: F7DBA80D-4DD5-4271-B571-24FB6188ABFE
ms.topic: reference
ms.date: 05/31/2018
---

# ld\_raw (sm5 - asm)

Random-access read of 1-4 32bit components from a raw buffer.



| ld\_raw dest\[.mask\], srcByteOffset\[.select\_component\], src0\[.swizzle\] |
|------------------------------------------------------------------------------|



 



| Item                                                                                                                       | Description                                                   |
|----------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| <span id="dest"></span><span id="DEST"></span>*dest*<br/>                                                            | \[in\] The address of the result of the operation.<br/> |
| <span id="srcByteOffset"></span><span id="srcbyteoffset"></span><span id="SRCBYTEOFFSET"></span>*srcByteOffset*<br/> | \[in\] Specifies the offset to read from.<br/>          |
| <span id="src0"></span><span id="SRC0"></span>*src0*<br/>                                                            | \[in\] The component to read. <br/>                     |



 

## Remarks

*src0* must be:

-   Any shader stage: SRV (t\#)ld st
-   Compute shader or pixel shader: UAV (u\#)
-   Compute shader: thread group shared memory (g\#)

*srcByteOffset* specifies the base 32-bit value in memory for a window of 4 sequential 32-bit values in which data may be read, depending on the swizzle and mask on other parameters.

The data read from the raw buffer is equivalent to the following pseudocode: where we have the offset, address, pointer to the buffer contents, stride of the source, and the data stored linearly.

``` syntax
                    BYTE *BufferContents;         // from src0
                    UINT srcByteOffset;           // from srcByteOffset
                    BYTE *ReadLocation;           // value to calculate
                    ReadLocation = BufferContents 
                                + srcByteOffset;

                    UINT32 Temp[4];  // used to make code shorter

                    // apply the source resource swizzle on source data
                    Temp = read_and_swizzle(ReadLocation, srcSwizzle);

                    // write the components to the output based on mask
                    ApplyWriteMask(dstRegister, dstWriteMask, Temp);
```

Out of bounds addressing on u\#/t\# of any given 32-bit component returns 0 for that component.

Out of bounds addressing on g\# (the bounds of that particular g\#, as opposed to all shared memory) for any given 32-bit component returns an undefined result.

cs\_4\_0 and cs\_4\_1 support this instruction for UAV and SRV.

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



 

cs\_4\_0 and cs\_4\_1 support this instruction for UAV and SRV.

## Related topics

<dl> <dt>

[Shader Model 5 Assembly (DirectX HLSL)](shader-model-5-assembly--directx-hlsl-.md)
</dt> </dl>

 

 





