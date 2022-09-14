---
title: /no_def_idir switch
description: When directories are specified with the /I switch, the /no\_def\_idir switch instructs the MIDL compiler to search only directories specified with the /I switch.
ms.assetid: 9a396de4-332d-4832-8e8b-291690cd3a10
keywords:
- /no_def_idir switch MIDL
topic_type:
- apiref
api_name:
- /no_def_idir
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# /no\_def\_idir switch

When directories are specified with the [**/I**](-i.md) switch, the **/no\_def\_idir** switch instructs the MIDL compiler to search only the directories specified with the **/I** switch, ignoring the current directory as well as the directories specified by the INCLUDE environment variable.

``` syntax
midl /no_def_idir
```

## Switch Options

This switch has no parameters.

## Remarks

When no directories are specified with the [**/I**](-i.md) switch, the **/no\_def\_idir** switch instructs the MIDL compiler to search only the current directory.

## Examples

``` syntax
; search only the current directory 
midl /no_def_idir filename.idl  

; search only the specified directories 
midl /no_def_idir /I c:\c700\include filename.idl 
```

## See also

<dl> <dt>

[General MIDL Command-line Syntax](general-midl-command-line-syntax.md)
</dt> <dt>

[**/acf**](-acf.md)
</dt> <dt>

[**/I**](-i.md)
</dt> </dl>

 

 




