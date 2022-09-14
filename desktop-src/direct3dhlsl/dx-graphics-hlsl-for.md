---
title: for Statement
description: Iteratively executes a series of statements, based on the evaluation of the conditional expression.
ms.assetid: d795c89e-7088-4bf3-93a8-798ed9c1a353
keywords:
- for Statement HLSL
topic_type:
- apiref
api_name:
- for Statement
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# for Statement

Iteratively executes a series of statements, based on the evaluation of the conditional expression.

\[*Attribute*\] for ( *Initializer; Conditional; Iterator* ) {   *Statement Block*; }



 

## Parameters

<dl> <dt>

<span id="Attribute"></span><span id="attribute"></span><span id="ATTRIBUTE"></span>*Attribute*
</dt> <dd>

An optional parameter that controls how the statement is compiled. When no attribute is specified the compiler will first attempt to emit a rolled version of the loop, and if that fails, or if some operations would be easier if the loop was unrolled, will fall back to an unrolled version of the loop.



| Attribute             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| unroll(x)             | Unroll the loop until it stops executing. Can optionally specify the maximum number of times the loop is to execute. Not compatible with the **\[loop\]** attribute.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| loop                  | Generate code that uses flow control to execute each iteration of the loop. Not compatible with the **\[unroll\]** attribute.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| fastopt               | Reduces the compile time but produces less aggressive optimizations. If you use this attribute, the compiler will not unroll loops.<br/> This attribute affects only shader model targets that support [break](dx-graphics-hlsl-break.md) instructions. This attribute is available in shader model [vs\_2\_x](dx9-graphics-reference-asm-vs-2-x.md) and [shader model 3](dx-graphics-hlsl-sm3.md) and later. It is particularly useful in [shader model 4](dx-graphics-hlsl-sm4.md) and later when the compiler compiles loops. The compiler simulates loops by default to evaluate whether it can unroll them. If you do not want the compiler to unroll loops, use this attribute to reduce compile time. <br/> |
| allow\_uav\_condition | Allows a compute shader loop termination condition to be based off of a UAV read. The loop must not contain synchronization intrinsics.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |



 

</dd> <dt>

<span id="Initializer"></span><span id="initializer"></span><span id="INITIALIZER"></span>*Initializer*
</dt> <dd>

The initial value of the loop counter.

</dd> <dt>

<span id="Conditional"></span><span id="conditional"></span><span id="CONDITIONAL"></span>*Conditional*
</dt> <dd>

A conditional [expression](dx-graphics-hlsl-expressions.md). If the conditional expression evaluates to true, the statement block is executed. The loop ends when the expression evaluates to false.

</dd> <dt>

<span id="Iterator"></span><span id="iterator"></span><span id="ITERATOR"></span>*Iterator*
</dt> <dd>

Update the value of the loop counter.

</dd> <dt>

<span id="Statement_Block"></span><span id="statement_block"></span><span id="STATEMENT_BLOCK"></span>*Statement Block*
</dt> <dd>

One or more [HLSL statements](dx-graphics-hlsl-statement-blocks.md).

</dd> </dl>

## Remarks

The **\[unroll\]** and **\[loop\]** attributes are mutually exclusive and will generate compiler errors when both are specified.

The **\[fastopt\]** and **\[allow\_uav\_condition\]** attributes are ignored if **\[unroll\]** is specified.

## See also

<dl> <dt>

[Flow Control](dx-graphics-hlsl-flow-control.md)
</dt> </dl>

 

 





