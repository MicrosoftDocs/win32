---
title: union
description: This statement defines a C-style union.
ms.assetid: 00bfcd0a-ac92-45f7-957a-b90790fb1982
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# union

This statement defines a C-style union.

## Syntax

``` syntax
typedef [attributes] union [tag] {
   memberlist
} unionname;
```

<dl> <dt>

<span id="attributes"></span><span id="ATTRIBUTES"></span>*attributes*
</dt> <dd>

The attributes helpstring, helpcontext, uuid, hidden, and version are accepted before a union. The helpstring, helpcontext, and Constants \[Automation\] attributes are accepted on a union member. Attributes (including the square brackets) can be omitted. If uuid is omitted, the union is not uniquely specified in the system.

</dd> <dt>

<span id="tag"></span><span id="TAG"></span>*tag*
</dt> <dd>

An optional tag.

</dd> <dt>

<span id="memberlist"></span><span id="MEMBERLIST"></span>*memberlist*
</dt> <dd>

The list of union members defined with C syntax.

</dd> <dt>

<span id="unionname"></span><span id="UNIONNAME"></span>*unionname*
</dt> <dd>

The name by which the union is known in the type library.

</dd> </dl>

## Remarks

The union keyword must be preceded with a typedef. The union description must precede other references to the structure in the library. Members of a union can be of any built-in type, or any type defined lexically as a typedef before the union. For a description of how strings and arrays can be entered, see the sections [String Definitions](string-definitions.md) and [Array Definitions](array-definitions.md).

## Example


```C++
[uuid(BFB7334C-822A-1068-8849-00DD011087E8), helpstring("A task"), helpcontext(1019)] 
typedef union {
   COLOR polycolor;
   int   cVertices;
   boolean filled;
   SAFEARRAY (int) subtasks; 
} UNIONSHOP;
```



 

 




