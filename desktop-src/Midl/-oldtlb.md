---
title: /oldtlb switch
description: The /oldtlb switch directs the MIDL compiler to generate an old-format type library.
ms.assetid: cf5fe000-7262-4812-a6ab-f12a558ac068
keywords:
- /oldtlb switch MIDL
topic_type:
- apiref
api_name:
- /oldtlb
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# /oldtlb switch

The **/oldtlb** switch directs the MIDL compiler to generate an old-format type library.

``` syntax
midl /oldtlb
```

## Switch Options

This switch has no parameters.

## Remarks

The **/oldtlb** switch overrides the default and directs the MIDL compiler to generate old-format type libraries even on current versions of Windows by using [CreateTypeLib](/previous-versions/windows/desktop/api/oleauto/nf-oleauto-createtypelib) instead of [CreateTypeLib2](/previous-versions/windows/desktop/api/oleauto/nf-oleauto-createtypelib2).

## Examples

**midl /oldtlb filename.idl**

**midl /oldtlb myoldodl.odl**

## See also

<dl> <dt>

[General MIDL Command-line Syntax](general-midl-command-line-syntax.md)
</dt> <dt>

[**/newtlb**](-newtlb.md)
</dt> </dl>

 

 