---
title: /savePP switch
description: When the /savePP directive is specified, the MIDL compiler does not delete the output of the C/C++ preprocessor.
ms.assetid: 65a687a5-55ec-4e76-bcfc-38c0a317b85b
keywords:
- /savePP switch MIDL
topic_type:
- apiref
api_name:
- /savePP
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# /savePP switch

When the **/savePP** directive is specified, the MIDL compiler does not delete the output of the C/C++ preprocessor.

``` syntax
midl /savePP
```

## Switch Options

This switch has no parameters.

## Remarks

This switch enables developers to discern what is being parsed by the MIDL compiler, and is useful for debugging. The output of the preprocessor is written to one or more temporary files in the directory indicated by the TEMP environment variable. The name of the output file, or files, follows a naming convention of MID\*.tmp. Note that a single compile may generate several preprocessed input streams; this is because importing an IDL file, as opposed to using **\#include**, causes a separate preprocessor run.

## See also

<dl> <dt>

[**/cpp\_cmd**](-cpp-cmd.md)
</dt> <dt>

[**/cpp\_opt**](-cpp-opt.md)
</dt> <dt>

[/no\_cpp, /nocpp](-no-cpp-nocpp.md)
</dt> </dl>

 

 




