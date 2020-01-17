---
title: include attribute
description: The ACF include statement specifies one or more header files to be included in the generated stub code.
ms.assetid: f83a704b-2f6e-4498-97ff-593fef2e92dc
keywords:
- include attribute MIDL
topic_type:
- apiref
api_name:
- include
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# include attribute

The ACF **include** statement specifies one or more header files to be included in the generated stub code.

``` syntax
include filenames;
```

## Parameters

<dl> <dt>

*filenames* 
</dt> <dd>

Specifies the name of one or more C-language header files. Use the full file name, including the .H extension and enclose each file name in quotation marks. Separate multiple C-language header file names with commas.

</dd> </dl>

## Remarks

As a result of the **include** statement, the generated stub code will contain a C-preprocessor **\#include** statement. You supply the C-language header file when compiling the stubs. Include statements rely on the C-compiler mechanism of searching the directory structure for included files.

> [!Note]  
> Use the [**import**](import.md) directive rather than the **include** directive for system files that contain data types you want to make available to the IDL file. The **import** directive ignores function prototypes and allows you to use MIDL compiler switches that optimize the generation of support routines.

 

## Examples

``` syntax
include "local.h";
include "gendefs.h", "protos.h", "mystuff.h";
```

## See also

<dl> <dt>

[Application Configuration File (ACF)](application-configuration-file-acf-.md)
</dt> <dt>

[**import**](import.md)
</dt> <dt>

[Importing Files and Type Libraries](importing-files-and-type-libraries.md)
</dt> <dt>

[Importing System Header Files](importing-system-header-files.md)
</dt> </dl>

 

 




