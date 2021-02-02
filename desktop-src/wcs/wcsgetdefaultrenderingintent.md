---
title: WcsGetDefaultRenderingIntent function
description: Retrieves the default rendering intent in the specified profile management scope.
ms.assetid: 1bb1c09d-1d8a-4568-bdb3-c051781495fa
keywords:
- WcsGetDefaultRenderingIntent function Windows Color System
topic_type:
- apiref
api_name:
- WcsGetDefaultRenderingIntent
api_location:
- mscms.dll
api_type:
- DllExport
ms.localizationpriority: high


ms.topic: article
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# WcsGetDefaultRenderingIntent function

Retrieves the default rendering intent in the specified profile management scope.

## Syntax


```C++
BOOL WINAPI WcsGetDefaultRenderingIntent(
  _In_  WCS_PROFILE_MANAGEMENT_SCOPE scope,
  _Out_ PDWORD                       pdwRenderingIntent
);
```



## Parameters

<dl> <dt>

*scope* \[in\]
</dt> <dd>

The profile management scope for this operation, which can be system-wide or the current user only.

</dd> <dt>

*pdwRenderingIntent* \[out\]
</dt> <dd>

A pointer to the variable that will hold the rendering intent.

For more information, see [Rendering Intents](rendering-intents.md).

</dd> </dl>

## Return value

If this function succeeds, the return value is **TRUE**.

If this function fails, the return value is **FALSE**. For extended error information, call **GetLastError**.

## Remarks

This function does not revert to the system-wide scope if you do not set the per-user default rendering intent. Instead, it fails, which allows the calling process to distinguish between the per-user and the system-wide setting. If the per-user rendering intent cannot be retrieved, call this function again with system-wide.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Icm.h</dt> </dl>     |
| Library<br/>                  | <dl> <dt>Mscms.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Mscms.dll</dt> </dl> |



## See also

<dl> <dt>

[Basic color management concepts](basic-color-management-concepts.md)
</dt> <dt>

[Windows Color System Schemas and Algorithms](windows-color-system-schemas-and-algorithms.md)
</dt> <dt>

[Functions](functions.md)
</dt> </dl>

 

 





