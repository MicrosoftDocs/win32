---
title: do Statement (Ocidl.h)
description: Execute a series of statements continuously until the conditional expression fails.
ms.assetid: 07fd37b0-59c2-404b-a755-7178e4a058e4
keywords:
- do Statement HLSL
topic_type:
- apiref
api_name:
- do Statement
api_location:
- ocidl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# do Statement

Execute a series of statements continuously until the conditional expression fails.



|                                                                     |
|---------------------------------------------------------------------|
| \[*Attribute*\] do {   *Statement Block*; } while( *Conditional* ); |



 

## Parameters

<dl> <dt>

<span id="Attribute"></span><span id="attribute"></span><span id="ATTRIBUTE"></span>*Attribute*
</dt> <dd>

An optional parameter that controls how the statement is compiled.



| Attribute | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| fastopt   | Reduces the compile time but produces less aggressive optimizations. If you use this attribute, the compiler will not unroll loops.<br/> This attribute affects only shader model targets that support [break](dx-graphics-hlsl-break.md) instructions. This attribute is available in shader model [vs\_2\_x](dx9-graphics-reference-asm-vs-2-x.md) and [shader model 3](dx-graphics-hlsl-sm3.md) and later. It is particularly useful in [shader model 4](dx-graphics-hlsl-sm4.md) and later when the compiler compiles loops. The compiler simulates loops by default to evaluate whether it can unroll them. If you do not want the compiler to unroll loops, use this attribute to reduce compile time.<br/> |



 

</dd> <dt>

<span id="Statement_Block"></span><span id="statement_block"></span><span id="STATEMENT_BLOCK"></span>*Statement Block*
</dt> <dd>

One or more [statements](dx-graphics-hlsl-statement-blocks.md).

</dd> <dt>

<span id="Conditional"></span><span id="conditional"></span><span id="CONDITIONAL"></span>*Conditional*
</dt> <dd>

A conditional [expression](dx-graphics-hlsl-expressions.md). The statement block is executed before the expression is evaluated. The loop is exited when the expression evaluates to false.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ocidl.h</dt> </dl> |



## See also

<dl> <dt>

[Flow Control](dx-graphics-hlsl-flow-control.md)
</dt> </dl>

 

 





