---
title: ' include'
description: The \ include directive causes the resource compiler to process the file specified in the filename parameter.
ms.assetid: 9a3505c6-c19f-4c4f-85a4-94fbcfc0f9c6
ms.topic: article
ms.date: 05/31/2018
---

# ' include'

The **\#include** directive causes the resource compiler to process the file specified in the *filename* parameter. This file should be a header file that defines the constants used in the resource-definition file. The file can use single-byte, double-byte, or Unicode characters.

``` syntax
#include filename
```

<dl> <dt>

<span id="filename"></span><span id="FILENAME"></span>*filename*
</dt> <dd>

Name of the file to be included. If the file is in the current directory, the string must be enclosed in double quotation marks; if the file is in the directory specified by the INCLUDE environment variable, the string must be enclosed in less-than and greater-than characters (<>). You must give a full path enclosed in double quotation marks (") if the file is not in the current directory or in the directory specified by the INCLUDE environment variable.

</dd> </dl>

## Remarks

Use the following statement in your header file to surround statements that can be compiled by a C compiler but not RC:

``` syntax
#ifndef RC_INVOKED
```

This way, you can use the same include files in your .c and .rc files.

## Example

This example processes the header files Windows.h and MyDefs.h while compiling the resource-definition file:

``` syntax
#include <windows.h>
#include "headers\mydefs.h"
```

## Related topics

<dl> <dt>

[Preprocessor Directives](preprocessor-directives.md)
</dt> </dl>

 

 




