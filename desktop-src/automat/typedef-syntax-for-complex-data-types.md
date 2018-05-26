---
title: TypeDef Syntax for Complex Data Types
description: In MIDL, the first definition will generate a TKIND\_RECORD for \ 0034;myStruct \ 0034; and a TKIND\_ALIAS for \ 0034;testStruct \ 0034; (defining \ 0034;testStruct \ 0034; as an alias for \ 0034;myStruct \ 0034;).
ms.assetid: 9251b327-2125-4301-b8ea-cde178d424d5
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# TypeDef Syntax for Complex Data Types

In MIDL, the first definition will generate a TKIND\_RECORD for "myStruct" and a TKIND\_ALIAS for "testStruct" (defining "testStruct" as an alias for "myStruct"). For the second definition, MIDL will generate a TKIND\_RECORD for a mangled name internal to MIDL that is not meaningful to the user and a TKIND\_ALIAS for "testStruct".


```C++
typedef struct myStruct  { ... } testStruct;
typedef struct { ... } testStruct;
```



This has potential implications for type library browsers that simply show the name of a record in its user interface. If you expect a TKIND\_RECORD to have a real name, there is a potential for unrecognizable names to appear in the user interface. This behavior also applies to [union](union.md) and [enum](enum.md) definitions, with the MIDL compiler generating TKIND\_UNIONs and TKIND\_ENUMs, respectively.

MIDL also allows C-style [struct](struct.md), **union** and **enum** definitions. For example, the following definition is legal in MIDL:


```C++
struct myStruct { ... };
typedef struct myStruct testStruct;
```



 

 




