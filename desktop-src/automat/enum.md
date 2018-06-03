---
title: enum
description: This statement defines a C-style enumerated type.
ms.assetid: d7d577e3-4a45-4dfc-be01-6018234a3cc9
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# enum

This statement defines a C-style enumerated type.

## Syntax

``` syntax
typedef [attributes] enum [tag] {
   enumlist
} enumname;
```

<dl> <dt>

<span id="attributes"></span><span id="ATTRIBUTES"></span>*attributes*
</dt> <dd>

The helpstring, helpcontext, hidden, uuid, and version attributes are accepted before an enum statement. The helpstring and helpcontext attributes are accepted on an enumeration element. Attributes (including the brackets) can be omitted. If uuid is omitted, the enumeration is not uniquely specified in the system.

</dd> <dt>

<span id="tag"></span><span id="TAG"></span>*tag*
</dt> <dd>

An optional tag.

</dd> <dt>

<span id="enumlist"></span><span id="ENUMLIST"></span>*enumlist*
</dt> <dd>

The list of enumerated elements.

</dd> <dt>

<span id="enumname"></span><span id="ENUMNAME"></span>*enumname*
</dt> <dd>

The name by which the enumeration is known in the type library.

</dd> </dl>

## Remarks

The enum keyword must be preceded by typedef. The enumeration description must precede other references to the enumeration in the library. If value is not specified for enumerators, the numbering progresses, as with enumerations in C. The type of the enum element is int, the system default integer, which depends on the target type library specification.

## Example


```C++
typedef [uuid(DEADF00D-C0DE-B1FF-F001-A100FF001ED),
      helpstring("Farm Animals are friendly"), helpcontext(234)]
enum {
   [helpstring("Moo")] cows = 1,
   pigs = 2
} ANIMALS;
```



 

 




