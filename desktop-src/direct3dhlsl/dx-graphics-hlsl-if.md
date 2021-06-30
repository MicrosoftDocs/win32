---
title: if Statement
description: Conditionally execute a series of statements, based on the evaluation of the conditional expression.
ms.assetid: ed4e347b-b5ee-40bc-a3f8-36e83ccf45b8
keywords:
- if Statement HLSL
topic_type:
- apiref
api_name:
- if Statement
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# if Statement

Conditionally execute a series of statements, based on the evaluation of the conditional expression.

\[*Attribute*\] if ( *Conditional* ) {   *Statement Block*; }



 

## Parameters

<dl> <dt>

<span id="Attribute"></span><span id="attribute"></span><span id="ATTRIBUTE"></span>*Attribute*
</dt> <dd>

An optional parameter that controls how the statement is compiled.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>branch</td>
<td>Evaluate only one side of the if statement depending on the given condition.
<blockquote>
[!Note]<br />
When you use <a href="dx-graphics-hlsl-sm2.md">Shader Model 2.x</a> or <a href="dx-graphics-hlsl-sm3.md">Shader Model 3.0</a>, each time you use dynamic branching you consume resources. So, if you use dynamic branching excessively when you target these profiles, you can receive compilation errors.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>flatten</td>
<td>Evaluate both sides of the if statement and choose between the two resulting values.</td>
</tr>
</tbody>
</table>



 

</dd> <dt>

<span id="Conditional"></span><span id="conditional"></span><span id="CONDITIONAL"></span>*Conditional*
</dt> <dd>

A conditional [expression](dx-graphics-hlsl-expressions.md). The expression is evaluated, and if true, the statement block is executed.

</dd> <dt>

<span id="Statement_Block"></span><span id="statement_block"></span><span id="STATEMENT_BLOCK"></span>*Statement Block*
</dt> <dd>

One or more [HLSL statements](dx-graphics-hlsl-statement-blocks.md).

</dd> </dl>

## Remarks

When the compiler uses the branch method for compiling an if statement it will generate code that will evaluate only one side of the if statement depending on the given condition. For example, in the if statement:


```
[branch] if(x)
{
    x = sqrt(x);
}
```



The **if** statement has an implicit else block, which is equivalent to x = x. Because we have told the compiler to use the branch method with the preceding branch attribute, the compiled code will evaluate x and execute only the side that should be executed; if x is zero, then it will execute the **else** side, and if it is non-zero it will execute the **then** side.

Conversely, if the **flatten** attribute is used, then the compiled code will evaluate both sides of the **if** statement and choose between the two resulting values using the original value of x. Here is an example of a usage of the flatten attribute:


```
[flatten] if(x)
{
    x = sqrt(x);
}
```



There are certain cases where using the branch or flatten attributes may generate a compile error. The branch attribute may fail if either side of the if statement contains a gradient function, such as [**tex2D**](dx-graphics-hlsl-tex2d.md). The flatten attribute may fail if either side of the if statement contains a stream append statement or any other statement that has side-effects.

An **if** statement can also use an optional else block. If the **if** expression is true, the code in the statement block associated with the if statement is processed. Otherwise, the statement block associated with the optional else block is processed.

## See also

<dl> <dt>

[Flow Control](dx-graphics-hlsl-flow-control.md)
</dt> </dl>

 

 





