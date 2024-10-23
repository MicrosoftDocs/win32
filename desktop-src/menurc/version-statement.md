---
title: VERSION statement
description: Defines version information about a resource that can be used by tools that read and write resource files.
ms.assetid: 3a33cff3-b8b3-43f4-b43a-ff1d1728cdc1
keywords:
- VERSION statement Menus and Other Resources
topic_type:
- apiref
api_name:
- VERSION
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# VERSION statement

Defines version information about a resource that can be used by tools that read and write resource files. The specified *dword* value appears with the resource in the compiled .RES file. However, the value is not stored in the executable file and has no significance to the system.

When the **VERSION** statement appears before the beginning of the body of an [**ACCELERATORS**](accelerators-resource.md), [**DIALOGEX**](dialogex-resource.md), [**MENU**](menu-resource.md), [**RCDATA**](rcdata-resource.md), or [**STRINGTABLE**](stringtable-resource.md) resource definition, the specified value applies only to that resource. Otherwise, the specified value applies to all resources up to the next **VERSION** statement or to the end of the file.

``` syntax
VERSION dword
```

<dl> <dt>

<span id="dword"></span><span id="DWORD"></span>*dword*
</dt> <dd>

A user-defined **DWORD** value.

</dd> </dl>

## See also

<dl> <dt>

[**ACCELERATORS**](accelerators-resource.md)
</dt> <dt>

[**CHARACTERISTICS**](characteristics-statement.md)
</dt> <dt>

[**LANGUAGE**](language-statement.md)
</dt> <dt>

[**MENU**](menu-resource.md)
</dt> <dt>

[**RCDATA**](rcdata-resource.md)
</dt> <dt>

[**STRINGTABLE**](stringtable-resource.md)
</dt> </dl>

 

 




