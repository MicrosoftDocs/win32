---
title: while Statement
description: Executes a statement block until the conditional expression fails.
ms.assetid: 0fe420db-3c09-40bd-b689-f85c02e2f817
keywords:
- while Statement HLSL
topic_type:
- apiref
api_name:
- while Statement
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# while Statement

Executes a statement block until the conditional expression fails.

\[*Attribute*\] while ( *Conditional* ) {   *Statement Block*; }



 

## Parameters

<dl> <dt>

<span id="Attribute"></span><span id="attribute"></span><span id="ATTRIBUTE"></span>*Attribute*
</dt> <dd>

An optional parameter that controls how the statement is compiled.



| Attribute             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| unroll(x)             | Unroll the loop until it stops executing. Optionally, you can specify the maximum number of times the loop can execute.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| loop                  | Use flow-control statements in the compiled shader; do not unroll the loop.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| fastopt               | Reduces the compile time but produces less aggressive optimizations. If you use this attribute, the compiler will not unroll loops.<br/> This attribute affects only shader model targets that support [break](dx-graphics-hlsl-break.md) instructions. This attribute is available in shader model [vs\_2\_x](dx9-graphics-reference-asm-vs-2-x.md) and [shader model 3](dx-graphics-hlsl-sm3.md) and later. It is particularly useful in [shader model 4](dx-graphics-hlsl-sm4.md) and later when the compiler compiles loops. The compiler simulates loops by default to evaluate whether it can unroll them. If you do not want the compiler to unroll loops, use this attribute to reduce compile time.<br/> |
| allow\_uav\_condition | Allows a compute shader loop termination condition to be based off of a UAV read. The loop must not contain synchronization intrinsics.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |



 

</dd> <dt>

<span id="Conditional"></span><span id="conditional"></span><span id="CONDITIONAL"></span>*Conditional*
</dt> <dd>

A conditional [expression](dx-graphics-hlsl-expressions.md). If the expression evaluates to true, the statement block is executed. The loop ends when the expression evaluates to false.

</dd> <dt>

<span id="Statement_Block"></span><span id="statement_block"></span><span id="STATEMENT_BLOCK"></span>*Statement Block*
</dt> <dd>

One or more [statements](dx-graphics-hlsl-statement-blocks.md).

</dd> </dl>

## See also

<dl> <dt>

[Flow Control](dx-graphics-hlsl-flow-control.md)
</dt> </dl>

 

 





