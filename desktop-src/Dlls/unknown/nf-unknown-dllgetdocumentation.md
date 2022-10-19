---
title: DLLGetDocumentation function
description: Retrieves a localized string for a given help context value.
ms.topic: reference
ms.date: 10/19/2022
req.header: 
req.dll: 
req.lib: 
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
dev_langs:
 - c++
topic_type:
 - APIRef
 - kbSyntax
api_type:
 - DllExport
api_location:
 - Unknown.dll
api_name:
 - DLLGetDocumentation
targetos: Windows
product:
 - Windows
ms.product: Windows
req.product: Windows
---

# DLLGetDocumentation function

Retrieves a localized string for a given help context value.

## Syntax

```cpp

STDAPI DLLGetDocumentation
(
  ITypeLib * ptlib,
  ITypeInfo * ptinfo,
  LCID lcid,
  DWORD dwCtx,
  BSTR * pbstrHelpString
);
```

## Parameters

`ptlib`

The TypeLib associated with help context.

`ptinfo`

The TypeInfo associated with help context.

`lcid`

Windows Language Code Identifier.

`dwCtx`

Cookie value representing the help context id being looked for.

`pbstrHelpString`

Localized help string associated with the context id passed in.

## Return value

This function doesn't return a value.

## Remarks

For more info, see [To specify localized help strings](https://github.com/MicrosoftDocs/visualstudio-docs/blob/main/docs/extensibility/internals/properties-window-fields-and-interfaces.md#to-specify-localized-help-strings) on GitHub.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | N/A |
| **Library** | N/A |
| **DLL** | Unknown |

## See also

* [To specify localized help strings](https://github.com/MicrosoftDocs/visualstudio-docs/blob/main/docs/extensibility/internals/properties-window-fields-and-interfaces.md#to-specify-localized-help-strings) on GitHub
