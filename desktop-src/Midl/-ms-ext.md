---
title: /ms_ext switch
description: Effective with MIDL version 3.0, the features enabled by the ms\_ext switch are now the default mode for the MIDL compiler.
ms.assetid: 175894c9-fa7e-4907-966d-e9df5a8e2745
keywords:
- /ms_ext switch MIDL
topic_type:
- apiref
api_name:
- /ms_ext
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# /ms\_ext switch

Effective with MIDL version 3.0, the features enabled by the **ms\_ext** switch are now the default mode for the MIDL compiler.

``` syntax
midl /ms_ext
```

## Switch Options

This switch has no parameters.

## Remarks

Using the switch will not generate a compiler error, so you do not have to remove references to **/ms\_ext** or [**/c\_ext**](-c-ext.md) from an existing makefile.

The following Microsoft extensions to OSF DCE are now available by default:

-   Interface definitions for OLE objects. For more information on the files generated for OLE interfaces, see [Files Generated for a COM Interface](files-generated-for-a-com-interface.md)
-   A [**\[callback\]**](callback.md) attribute specifying a static callback function on the client
-   [**cpp\_quote**](cpp-quote.md)(*quoted\_string*) and [**\#pragma midl\_echo**](pragma.md)
-   [**wchar\_t**](wchar-t.md) wide-character types, constants, and strings
-   [**enum initialization**](enum.md) (sparse enumerators)
-   Expressions as size and discriminator specifiers
-   [Handle extensions](/windows/desktop/Rpc/microsoft-rpc-binding-handle-extensions)
-   [Pointer-attribute type inheritance](/windows/desktop/Rpc/pointer-attribute-type-inheritance)
-   [Multiple interfaces](/windows/desktop/Rpc/registering-interfaces)
-   Definitions outside of the interface block
-   You can omit [directional attributes](/windows/desktop/Rpc/directional-parameter-attributes) \[[**in**](in.md), [**out**](out-idl.md)\]

## See also

<dl> <dt>

[General MIDL Command-line Syntax](general-midl-command-line-syntax.md)
</dt> <dt>

[Pointer-attribute type inheritance](/windows/desktop/Rpc/pointer-attribute-type-inheritance)
</dt> <dt>

[**/app\_config**](-app-config.md)
</dt> <dt>

[**/osf**](-osf.md)
</dt> </dl>

 

 