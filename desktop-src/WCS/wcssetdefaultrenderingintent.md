---
title: WcsSetDefaultRenderingIntent function
description: Sets the default rendering intent in the specified profile management scope.
ms.assetid: 8f0c216c-f501-4b33-92f3-8b2f953a1d2d
keywords:
- WcsSetDefaultRenderingIntent function Windows Color System
topic_type:
- apiref
api_name:
- WcsSetDefaultRenderingIntent
api_location:
- mscms.dll
api_type:
- DllExport
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WcsSetDefaultRenderingIntent function

Sets the default rendering intent in the specified profile management scope.

## Syntax


```C++
BOOL WINAPI WcsSetDefaultRenderingIntent(
  _In_ WCS_PROFILE_MANAGEMENT_SCOPE scope,
  _In_ DWORD                        dwRenderingIntent
);
```



## Parameters

<dl> <dt>

*scope* \[in\]
</dt> <dd>

The profile management scope for this operation, which can be system-wide or the current user only.

</dd> <dt>

*dwRenderingIntent* \[in\]
</dt> <dd>

The rendering intent. It can be set to one of the following values:

INTENT\_PERCEPTUAL

 

INTENT\_RELATIVE\_COLORIMETRIC

 

INTENT\_SATURATION

 

INTENT\_ABSOLUTE\_COLORIMETRIC

 

DWORD\_MAX

If *dwRenderingIntent* is DWORD\_MAX and *scope* is WCS\_PROFILE\_MANAGEMENT\_SCOPE\_CURRENT\_USER, the default rendering intent for the current user reverts to the system-wide default.

For more information, see [Rendering Intents](rendering-intents.md).

</dd> </dl>

## Return value

If this function succeeds, the return value is **TRUE**.

If this function fails, the return value is **FALSE**. For extended error information, call **GetLastError**.

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

[Basic Color Management Concepts](basic-color-management-concepts.md)
</dt> <dt>

[Windows Color System Schemas and Algorithms](windows-color-system-schemas-and-algorithms.md)
</dt> <dt>

[Functions](functions.md)
</dt> </dl>

 

 





