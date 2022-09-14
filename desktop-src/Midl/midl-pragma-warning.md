---
title: midl_pragma warning attribute
description: Use the midl\_pragma warning option to temporarily override MIDL's warning message behavior at compile time.
ms.assetid: d32a3d3f-5c4d-4f93-a72a-2224ceed0012
keywords:
- midl_pragma warning attribute MIDL
topic_type:
- apiref
api_name:
- midl_pragma warning
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# midl\_pragma warning attribute

Use the **midl\_pragma warning** option to temporarily override MIDL's warning message behavior at compile time.

``` syntax
midl_pragma warning ( warning_option : message_list )
```

## Parameters

<dl> <dt>

*warning\_option* 
</dt> <dd>

The warning option can be one of the following: disable, enable, default.

</dd> <dt>

*message\_list* 
</dt> <dd>

A list of message numbers separated by spaces.

</dd> </dl>

## Remarks

The pragma can be used like a C-compiler pragma. That is, it disables, enables, or returns to the default behavior for a given MIDL warning.

## Examples

``` syntax
#if (__midl >= 501)
midl_pragma warning( disable: 2007 )   // file already imported midl_pragma warning( disable: 2209 )   // ignored redundant attr
#endif
```

## See also

<dl> <dt>

[**pragma**](pragma.md)
</dt> </dl>

 

 




