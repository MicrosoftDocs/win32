---
title: Data Types in the Interface Body
description: The interface body, which is enclosed in braces ( ), contains the data types that will be used in remote procedure calls and prototypes for the functions that will be executed remotely.
ms.assetid: a5130744-6b14-48a4-b439-16f0ecaf08c2
keywords:
- interfaces MIDL , data types
ms.topic: article
ms.date: 05/31/2018
---

# Data Types in the Interface Body

The interface body, which is enclosed in braces ({ }), contains the data types that will be used in remote procedure calls and prototypes for the functions that will be executed remotely. An interface body can contain imports, pragmas, constant declarations, type declarations, and function declarations. Except in OSF-compatibility mode, the MIDL compiler also allows implicit declarations in the form of variable definitions.

Note that the OSF-DCE specification for RPC interfaces does not allow multiple interfaces in a single IDL file. Therefore, if you are compiling in MIDL's OSF-compatibility mode ( [**/osf**](-osf.md)), your IDL file can contain only one interface.

For details on using the MIDL compiler to produce type libraries, see [Generating a Type Library with MIDL](generating-a-type-library-with-midl-2.md).

In Microsoft RPC, an IDL file can contain multiple interfaces and these interfaces can be forward declared (within the IDL file that defines them). For example:

``` syntax
interface ITwo; //forward declaration
interface IOne 
{
...uses ITwo...
}
interface ITwo 
{
...uses IOne...
}
```

 

 




