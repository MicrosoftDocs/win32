---
title: /win64 switch
description: The /win64 switch directs the MIDL compiler to generate stub files, or a type library file, for a 64-bit environment.Note  This switch is obsolete.
ms.assetid: 6f4780d3-6415-42af-a8ee-3884a8cebe26
keywords:
- /win64 switch MIDL
topic_type:
- apiref
api_name:
- /win64
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# /win64 switch

The **/win64** switch directs the MIDL compiler to generate stub files, or a type library file, for a 64-bit environment.

> [!Note]  
> This switch is obsolete. Please use the [**/ia64**](-ia64.md) or [**/amd64**](-amd64.md) switch instead. The **/win64** switch is equivalent to the **/ia64** switch.

 

``` syntax
midl /win64
```

## Switch Options

This switch has no parameters.

## Remarks

The **/win64** switch is equivalent to setting the [**/env**](-env.md) switch to win64.

> [!Note]  
> It is not possible to use MIDL.exe to produce a 64bit tlb on Windows 2000.

 

## See also

<dl> <dt>

[**/env**](-env.md)
</dt> <dt>

[**/ia64**](-ia64.md)
</dt> <dt>

[**/amd64**](-amd64.md)
</dt> </dl>

 

 




