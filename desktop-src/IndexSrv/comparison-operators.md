---
title: Comparison Operators
description: Comparison Operators
ms.assetid: 9343e7f6-67fd-422f-9364-bbdeabb2fb3a
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Comparison Operators

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The following list describes the comparison operators.

<dl> <dt>

<span id="DBOP_is_NULL__DBOP_is_NOT_NULL"></span><span id="dbop_is_null__dbop_is_not_null"></span><span id="DBOP_IS_NULL__DBOP_IS_NOT_NULL"></span>DBOP\_is\_NULL, DBOP\_is\_NOT\_NULL
</dt> <dd>

Comparison to NULL value. Both operators are needed, since "NOT is\_NULL" and "is\_NOT\_NULL" differ in SQL if the operand is a row with some (but not all) NULL values. These operators take one scalar input and produce a Boolean result.

</dd> <dt>

<span id="DBOP_equal__DBOP_not_equal__DBOP_less__DBOP_less_equal__DBOP_greater__DBOP_greater_equal__DBOP_equal_all__DBOP_not_equal_all__DBOP_less_all__DBOP_less_equal_all__DBOP_greater_all__DBOP_greater_equal_all__DBOP_equal_any__DBOP_not_equal_any__DBOP_less_any__DBOP_less_equal_any__DBOP_greater_any__DBOP_greater_equal_any"></span><span id="dbop_equal__dbop_not_equal__dbop_less__dbop_less_equal__dbop_greater__dbop_greater_equal__dbop_equal_all__dbop_not_equal_all__dbop_less_all__dbop_less_equal_all__dbop_greater_all__dbop_greater_equal_all__dbop_equal_any__dbop_not_equal_any__dbop_less_any__dbop_less_equal_any__dbop_greater_any__dbop_greater_equal_any"></span><span id="DBOP_EQUAL__DBOP_NOT_EQUAL__DBOP_LESS__DBOP_LESS_EQUAL__DBOP_GREATER__DBOP_GREATER_EQUAL__DBOP_EQUAL_ALL__DBOP_NOT_EQUAL_ALL__DBOP_LESS_ALL__DBOP_LESS_EQUAL_ALL__DBOP_GREATER_ALL__DBOP_GREATER_EQUAL_ALL__DBOP_EQUAL_ANY__DBOP_NOT_EQUAL_ANY__DBOP_LESS_ANY__DBOP_LESS_EQUAL_ANY__DBOP_GREATER_ANY__DBOP_GREATER_EQUAL_ANY"></span>DBOP\_equal, DBOP\_not\_equal, DBOP\_less, DBOP\_less\_equal, DBOP\_greater, DBOP\_greater\_equal, DBOP\_equal\_all, DBOP\_not\_equal\_all, DBOP\_less\_all, DBOP\_less\_equal\_all, DBOP\_greater\_all, DBOP\_greater\_equal\_all, DBOP\_equal\_any, DBOP\_not\_equal\_any, DBOP\_less\_any, DBOP\_less\_equal\_any, DBOP\_greater\_any, DBOP\_greater\_equal\_any
</dt> <dd>

Comparison operators with semantics as in SQL. For the normal comparison operators, the two input rows must both be scalars or both be rows. Otherwise, the scalar is converted into a one-column row as necessary. The "\_all" and "\_any" operators require a scalar left input and a table-valued right input, where a column value in a chaptered column is a special case of a table. These operators produce Boolean output.

Row-valued comparison refers to the comparison between two row instances. Multivalued comparison refers to the comparison between a row instance and a table (such as "\_all" and "\_any" operators). The rules for row-valued comparisons are based on ANSI SQL semantics. The rules for multivalued comparisons are an extension of the rule-valued comparisons.

The weight of this node is stored as a DBVALUEKIND\_I4 in an **lValue** member of the [**DBCOMMANDTREE**](dbcommandtree.md) structure.

</dd> <dt>

<span id="DBOP_anybits__DBOP_allbits__DBOP_anybits_any__DBOP_allbits_any__DBOP_anybits_all__DBOP_allbits_all"></span><span id="dbop_anybits__dbop_allbits__dbop_anybits_any__dbop_allbits_any__dbop_anybits_all__dbop_allbits_all"></span><span id="DBOP_ANYBITS__DBOP_ALLBITS__DBOP_ANYBITS_ANY__DBOP_ALLBITS_ANY__DBOP_ANYBITS_ALL__DBOP_ALLBITS_ALL"></span>DBOP\_anybits, DBOP\_allbits, DBOP\_anybits\_any, DBOP\_allbits\_any, DBOP\_anybits\_all, DBOP\_allbits\_all
</dt> <dd>

Comparison operators that have the same syntax as other comparison operators. These operators take two inputs, with the first being a column and the second being a scalar value to compare with the column. The specific semantics of these nodes are as follows: DBOP\_any\_bits is true if the result of a bitwise **AND** operation performed on the column value and the constant is nonzero. DBOP\_all\_bits is true if the result of a bitwise **AND** operation performed on a column value and the constant equals the constant. As with other comparison operators, there are also "\_any" and "\_all" versions of these nodes.

The weight of this node is stored as a DBVALUEKIND\_I4 in the **lValue** member of the [**DBCOMMANDTREE**](dbcommandtree.md) structure.

</dd> <dt>

<span id="DBOP_between__DBOP_between_unordered"></span><span id="dbop_between__dbop_between_unordered"></span><span id="DBOP_BETWEEN__DBOP_BETWEEN_UNORDERED"></span>DBOP\_between, DBOP\_between\_unordered
</dt> <dd>

SQL comparison operations. "Between\_unordered" first sorts the bounding values; "a between\_unordered b and c" is equivalent to "a &gt;= min (b, c) and a &lt;= max (b, c)", whereas "a between b and c" is equivalent to "a &gt;= b and a &lt;= c." All variants of "between" are inclusive, meaning that a value equal to one of the end points is acceptable. There is no exclusive "between" variant. These operations require three scalar inputs (which may be rows), and produce a Boolean result.

</dd> <dt>

<span id="DBOP_match__DBOP_match_unique__DBOP_match_partial__DBOP_match_partial_unique__DBOP_match_full__DBOP_match_full_unique"></span><span id="dbop_match__dbop_match_unique__dbop_match_partial__dbop_match_partial_unique__dbop_match_full__dbop_match_full_unique"></span><span id="DBOP_MATCH__DBOP_MATCH_UNIQUE__DBOP_MATCH_PARTIAL__DBOP_MATCH_PARTIAL_UNIQUE__DBOP_MATCH_FULL__DBOP_MATCH_FULL_UNIQUE"></span>DBOP\_match, DBOP\_match\_unique, DBOP\_match\_partial, DBOP\_match\_partial\_unique, DBOP\_match\_full, DBOP\_match\_full\_unique
</dt> <dd>

SQL's match predicate. These operation require two scalar inputs (which may be rows), and produce a Boolean output.

</dd> <dt>

<span id="DBOP_and__DBOP_or__DBOP_xor__DBOP_equivalent"></span><span id="dbop_and__dbop_or__dbop_xor__dbop_equivalent"></span><span id="DBOP_AND__DBOP_OR__DBOP_XOR__DBOP_EQUIVALENT"></span>DBOP\_and, DBOP\_or, DBOP\_xor, DBOP\_equivalent
</dt> <dd>

These Boolean operators represent the logical **AND**, **OR**, exclusive **OR**, and equivalence operators. They take two or more Boolean inputs (except DBOP\_equivalent, which takes exactly two), and produce a Boolean result. The weight of this node is stored as DBVALUEKIND\_I4 in the **value.lValue** member.

</dd> <dt>

<span id="DBOP_not"></span><span id="dbop_not"></span><span id="DBOP_NOT"></span>DBOP\_not
</dt> <dd>

This operator requires one Boolean input and produces one Boolean result. The weight of this node is stored as DBVALUEKIND\_I4 in the **value.lValue** member.

</dd> <dt>

<span id="DBOP_implies"></span><span id="dbop_implies"></span><span id="DBOP_IMPLIES"></span>DBOP\_implies
</dt> <dd>

This operator represents Boolean implication. It takes two mandatory Boolean inputs and produces a Boolean output according to the following table:



| Input1 | Input2 | Result |
|--------|--------|--------|
| False  | False  | True   |
| False  | True   | True   |
| True   | False  | False  |
| True   | True   | True   |



 

</dd> </dl>

 

 




