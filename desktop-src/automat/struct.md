---
title: struct
description: This statement defines a C-style structure.
ms.assetid: 'df2aa076-5ad0-4479-ac6b-d3be6b81480a'
---

# struct

This statement defines a C-style structure.

## Syntax

``` syntax
typedef [attributes] 
struct [tag] {
   memberlist
} structname;
```

<dl> <dt>

<span id="attributes"></span><span id="ATTRIBUTES"></span>*attributes*
</dt> <dd>

The attributes helpstring, helpcontext, uuid, hidden, and version are accepted before a struct statement. The attributes helpstring, helpcontext, and string are accepted on a structure member. Attributes (including the brackets) can be omitted. If uuid is omitted, the structure is not specified uniquely in the system.

</dd> <dt>

<span id="tag"></span><span id="TAG"></span>*tag*
</dt> <dd>

An optional tag.

</dd> <dt>

<span id="memberlist"></span><span id="MEMBERLIST"></span>*memberlist*
</dt> <dd>

The list of structure members defined with C syntax.

</dd> <dt>

<span id="structname_"></span><span id="STRUCTNAME_"></span>*structname* 
</dt> <dd>

The name by which the structure is known in the type library.

</dd> </dl>

## Remarks

The struct keyword must be preceded with a typedef. The structure description must precede other references to the structure in the library. Members of a struct can be of any built-in type, or any type defined lexically as a typedef before the struct. For a description of how strings and arrays can be entered, see the sections [String Definitions](string-definitions.md) and [Array Definitions](array-definitions.md).

## Example


```C++
typedef [uuid(BFB7334B-822A-1068-8849-00DD011087E8),
   helpstring("A task"), helpcontext(1019)]
struct {
   DATE startdate;
   DATE enddate;
   BSTR ownername;
   SAFEARRAY (int) subtasks;
   int A_C_array[10];
} TASKS;
```



 

 




