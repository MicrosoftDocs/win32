---
title: /c_ext switch
description: This switch is obsolete as of version 3.0 of the MIDL compiler. However, using the c\_ext switch will not generate a compiler error, so you do not have to remove references to /ms\_ext or /c\_ext from an existing makefile.
ms.assetid: 3d4072ba-5563-4014-a4ed-2e3aa26bb00a
keywords:
- /c_ext switch MIDL
topic_type:
- apiref
api_name:
- /c_ext
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# /c\_ext switch

This switch is obsolete as of version 3.0 of the MIDL compiler. However, using the **c\_ext** switch will not generate a compiler error, so you do not have to remove references to [**/ms\_ext**](-ms-ext.md) or **/c\_ext** from an existing makefile.

``` syntax
midl /c_ext
```

## Switch Options

This switch has no parameters.

## Remarks

The following features are now available by default:

-   Many existing header files define types with qualifiers, such as **far** and **stdcall**, that are not part of the DCE IDL. Those compilers (and the MIDL compiler in DCE-compatibility mode) generate errors when they attempt to process these qualifiers. The MIDL compiler allows you to compile IDL files that contain these qualifiers. The type qualifiers do not affect the way the data is transmitted on the network.
-   You can omit directional attributes such as [**\[in\]**](in.md) or [**\[out\]**](out-idl.md).

The following C-language extensions are supported in default mode:

-   Bit fields in structures and unions
-   Comments that start with two slash characters (//)
-   External declarations
-   Procedures with ellipses in the parameter list (…)
-   On 32-bit platforms, [**int**](int.md) is a native 32-bit base type; on 16-bit platforms, **int** is recognized but is not a remotable type
-   Type [**void \***](void.md) that is not used in remote operations
-   Type qualifiers—including the form with the ANSI-conformant prefix—contain two underscore characters: **cdecl**, **\_\_cdecl**, [**const**](const.md), **\_\_const**, **export**, **\_\_export**, **far**, **\_\_far**, **loadds**, **\_\_loadds**, **near**, **\_\_near**, **pascal**, **\_\_pascal**, **stdcall**, **\_\_stdcall**, **volatile**, and **\_\_volatile**.

For more information about declaration qualifiers, see your Microsoft C/C++ documentation.

## See also

<dl> <dt>

[**/app\_config**](-app-config.md)
</dt> <dt>

[**/osf**](-osf.md)
</dt> <dt>

[General MIDL Command-line Syntax](general-midl-command-line-syntax.md)
</dt> </dl>

 

 




