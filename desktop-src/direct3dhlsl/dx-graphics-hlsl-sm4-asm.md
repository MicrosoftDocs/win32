---
title: Shader Model 4 Assembly
description: Shader Model 4 Assembly
ms.assetid: 2896e195-b48b-4ce9-9421-f5fa40674b5e
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Shader Model 4 Assembly

Shader Model 4 requires you to program shaders in HLSL. However, the shader compiler compiles the HLSL code into assembly that runs on the device. If you are using PIX for Windows to debug your shaders, you can choose to display shader code in either HLSL or assembly. This section lists the Shader Model 4 and Shader Model 4.1 assembly instructions that you may encounter when debugging a shader.

<dl>

[Instruction Modifiers](instruction-modifiers.md)  
[add](add--sm4---asm-.md)  
[and](and--sm4---asm-.md)  
[break](break--sm4---asm-.md)  
[breakc](breakc--sm4---asm-.md)  
[call](call--sm4---asm-.md)  
[callc](callc--sm4---asm-.md)  
[case](case--sm4---asm-.md)  
[continue](continue--sm4---asm-.md)  
[continuec](continuec--sm4---asm-.md)  
[cut](cut--sm4---asm-.md)  
[dcl\_constantBuffer](dcl-constantbuffer.md)  
[dcl\_globalFlags](dcl-globalflags.md)  
[dcl\_immediateConstantBuffer](dcl-immediateconstantbuffer.md)  
[dcl\_indexableTemp](dcl-indexabletemp.md)  
[dcl\_indexRange](dcl-indexrange.md)  
[dcl\_input](dcl-input.md)  
[dcl\_input\_sv](dcl-input-sv.md)  
[dcl\_input vPrim](dcl-input-vprim.md)  
[dcl\_maxOutputVertexCount](dcl-maxoutputvertexcount.md)  
[dcl\_output](dcl-output.md)  
[dcl\_output oDepth](dcl-output-odepth.md)  
[dcl\_output\_sgv](dcl-output-sgv.md)  
[dcl\_output\_siv](dcl-output-siv.md)  
[dcl\_outputTopology](dcl-outputtopology.md)  
[dcl\_resource](dcl-resource.md)  
[dcl\_sampler](dcl-sampler.md)  
[dcl\_temps](dcl-temps.md)  
[default](default--sm4---asm-.md)  
[deriv\_rtx](deriv-rtx--sm4---asm-.md)  
[deriv\_rty](deriv-rty--sm4---asm-.md)  
[discard](discard--sm4---asm-.md)  
[div](div--sm4---asm-.md)    
[dne](dne--sm5---asm-.md)  
[dp2](dp2--sm4---asm-.md)  
[dp3](dp3--sm4---asm-.md)  
[dp4](dp4--sm4---asm-.md)  
[else](else--sm4---asm-.md)  
[emit](emit--sm4---asm-.md)  
[emitThenCut](emitthencut--sm4---asm-.md)  
[endif](endif--sm4---asm-.md)  
[endloop](endloop--sm4---asm-.md)  
[endswitch](endswitch--sm4---asm-.md)  
[eq](eq--sm4---asm-.md)  
[exp](exp--sm4---asm-.md)  
[frc](frc--sm4---asm-.md)  
[ftoi](ftoi--sm4---asm-.md)  
[ftou](ftou--sm4---asm-.md)  
[ge](ge--sm4---asm-.md)  
[iadd](iadd--sm4---asm-.md)
[ieq](ieq--sm4---asm-.md)  
[if](if--sm4---asm-.md)  
[ige](ige--sm4---asm-.md)  
[ilt](ilt--sm4---asm-.md)  
[imad](imad--sm4---asm-.md)  
[imin](imin--sm4---asm-.md)  
[imul](imul--sm4---asm-.md)  
[ine](ine--sm4---asm-.md)  
[ineg](ineg--sm4---asm-.md)  
[ishl](ishl--sm4---asm-.md)  
[ishr](ishr--sm4---asm-.md)  
[itof](itof--sm4---asm-.md)  
[label](label--sm4---asm-.md)  
[ld](ld--sm4---asm-.md)  
[log](log--sm4---asm-.md)  
[loop](loop--sm4---asm-.md)  
[lt](lt--sm4---asm-.md)  
[mad](mad--sm4---asm-.md)  
[max](max--sm4---asm-.md)  
[min](min--sm4---asm-.md)  
[mov](mov--sm4---asm-.md)  
[movc](movc--sm4---asm-.md)  
[mul](mul--sm4---asm-.md)  
[ne](ne--sm4---asm-.md)  
[nop](nop--sm4---asm-.md)  
[not](not--sm4---asm-.md)  
[or](or--sm4---asm-.md)  
[resinfo](resinfo--sm4---asm-.md)  
[ret](ret--sm4---asm-.md)  
[retc](retc--sm4---asm-.md)  
[round\_ne](round-ne--sm4---asm-.md)  
[round\_ni](round-ni--sm4---asm-.md)  
[round\_pi](round-pi--sm4---asm-.md)  
[round\_z](round-z--sm4---asm-.md)  
[rsq](rsq--sm4---asm-.md)  
[sample](sample--sm4---asm-.md)  
[sample\_b](sample-b--sm4---asm-.md)  
[sample\_c](sample-c--sm4---asm-.md)  
[sample\_c\_lz](sample-c-lz--sm4---asm-.md)  
[sample\_d](sample-d--sm4---asm-.md)  
[sample\_l](sample-l--sm4---asm-.md)  
[sincos](sincos--sm4---asm-.md)  
[sqrt](sqrt--sm4---asm-.md)  
[switch](switch--sm4---asm-.md)  
[udiv](udiv--sm4---asm-.md)  
[uge](uge--sm4---asm-.md)  
[ult](ult--sm4---asm-.md)  
[umad](umad--sm4---asm-.md)  
[umax](umax--sm4---asm-.md)  
[umin](umin--sm4---asm-.md)  
[umul](umul--sm4---asm-.md)  
[ushr](ushr--sm4---asm-.md)  
[utof](utof--sm4---asm-.md)  
[xor](xor--sm4---asm-.md)  
</dl>

## Shader Model 4.1 Assembly

Shader Model 4.1 supports all of the Shader Model 4.0 instructions and the following additional instructions:

<dl>

[gather4](gather4--sm4-1---asm-.md)  
[ld2dms](ld2dms--sm4-1---asm-.md)  
[lod](lod--sm4-1---asm-.md)  
[sampleinfo](sampleinfo--sm4-1---asm-.md)  
[samplepos](samplepos--sm4-1---asm-.md)  
</dl>

## Related topics

<dl> <dt>

[Asm Shader Reference](dx9-graphics-reference-asm.md)
</dt> <dt>

[Shader Model 4](dx-graphics-hlsl-sm4.md)
</dt> </dl>

 

 




