---
title: Importing System Header Files
description: While it is often possible to use the \ include directive to include header files in your IDL file, it is not recommended.
ms.assetid: ff524965-424d-416d-97cd-c2780ebf69ef
keywords:
- importing MIDL , system header files
ms.topic: article
ms.date: 05/31/2018
---

# Importing System Header Files

While it is often possible to use the **\#include** directive to include header files in your IDL file, it is not recommended. The MIDL compiler will generate stubs for all functions defined in the IDL file being compiled. Usually a header file contains a number of prototypes that you neither need nor want to include in your stub files, and a **\#include** effectively puts all those definitions into your main IDL file. Furthermore, if there are nonremotable types defined in the header file, the IDL file may not compile.

There are two ways to include type definitions from header files in an IDL file:

-   Use the [**import**](import.md) directive to include data types defined in a header file. Unlike the C-language **\#include** directive, the **import** directive only picks up type and constant definitions and ignores procedure prototypes. This approach will work as long as your main IDL file does not reference any nonremotable types defined in the header file.
-   Create a helper IDL file with a dummy interface that includes the header files. Then, use the [**import**](import.md) directive to include the helper file. In this way, only the [**typedef**](typedef.md)s will appear in the compiled stubs. For example:

```syntax
//in helper.idl:
interface dummy
{ 
   #include "kitchensink.h"
   #include "system.h"
}

//in main.idl:
import "helper.idl";
```
