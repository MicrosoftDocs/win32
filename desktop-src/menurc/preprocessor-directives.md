---
title: Preprocessor Directives (Menus and Other Resources)
description: You can use the directives described in the following table as needed in your resource script. They instruct RC to perform actions or to assign values to names.
ms.assetid: 162f946e-54d8-4e23-9aa7-8e91eda4ee68
keywords:
- resource compiler,preprocessor directives
ms.topic: article
ms.date: 05/31/2018
---

# Preprocessor Directives (Menus and Other Resources)

You can use the directives described in the following table as needed in your resource script. They instruct RC to perform actions or to assign values to names.



| Directive                     | Description                                                           |
|-------------------------------|-----------------------------------------------------------------------|
| [**\#define**](-define.md)   | Defines a specified name by assigning it a given value.               |
| [**\#elif**](-elif.md)       | Marks an optional clause of a conditional-compilation block.          |
| [**\#else**](-else.md)       | Marks the last optional clause of a conditional-compilation block.    |
| [**\#endif**](-endif.md)     | Marks the end of a conditional-compilation block.                     |
| [**\#if**](-if.md)           | Conditionally compiles the script if a specified expression is true.  |
| [**\#ifdef**](-ifdef.md)     | Conditionally compiles the script if a specified name is defined.     |
| [**\#ifndef**](-ifndef.md)   | Conditionally compiles the script if a specified name is not defined. |
| [**\#include**](-include.md) | Copies the contents of a file into the resource-definition file.      |
| [**\#undef**](-undef.md)     | Removes the definition of the specified name.                         |



 

To define symbols for your resource identifiers, use the **\#define** directive to define them in a header file. Include this header both in the resource script and your application source code. Similarly, you define the values for resource attributes and styles by including Windows.h in the resource script.

RC treats files with the .c and .h extensions in a special manner. It assumes that a file with one of these extensions does not contain resources. If a file has the .c or .h file name extension, RC ignores all lines in the file except the preprocessor directives. Therefore, to include a file that contains resources in another resource script, give the file to be included an extension other than .c or .h.

## Related topics

<dl> <dt>

[Pragma Directives](pragma-directives.md)
</dt> </dl>

 

 




