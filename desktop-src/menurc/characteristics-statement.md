---
title: CHARACTERISTICS statement
description: Defines information about a resource that can be used by tools that read and write resource-definition files.
ms.assetid: 07834b02-a36e-40cc-8907-bff6631842f3
keywords:
- CHARACTERISTICS statement Menus and Other Resources
topic_type:
- apiref
api_name:
- CHARACTERISTICS
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# CHARACTERISTICS statement

Defines information about a resource that can be used by tools that read and write resource-definition files. The specified **DWORD** value appears with the resource in the compiled .res file. However, the value is not stored in the executable file and has no significance to the system.

The **CHARACTERISTICS** statement appears before the beginning of the body of an [**ACCELERATORS**](accelerators-resource.md), [**DIALOG**](dialog-resource.md), [**MENU**](menu-resource.md), [**RCDATA**](rcdata-resource.md), or [**STRINGTABLE**](stringtable-resource.md) resource definition. The specified value applies only to that resource.

``` syntax
CHARACTERISTICS dword
```

<dl> <dt>

<span id="dword"></span><span id="DWORD"></span>*dword*
</dt> <dd>

User-defined **DWORD** value.

</dd> </dl>

## See also

<dl> <dt>

[**ACCELERATORS**](accelerators-resource.md)
</dt> <dt>

[**DIALOG**](dialog-resource.md)
</dt> <dt>

[**LANGUAGE**](language-statement.md)
</dt> <dt>

[**MENU**](menu-resource.md)
</dt> <dt>

[**RCDATA**](rcdata-resource.md)
</dt> <dt>

[**STRINGTABLE**](stringtable-resource.md)
</dt> </dl>

 

 




