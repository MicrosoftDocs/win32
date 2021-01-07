---
description: This function enables or disables support for end-user-defined characters (EUDC).
ms.assetid: 9e531d8c-6008-4189-ae25-cda707be5e2c
title: EnableEUDC function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- EnableEUDC
api_type: 
- DllExport
api_location: 
- Gdi32.dll
---

# EnableEUDC function

This function enables or disables support for end-user-defined characters (EUDC).

## Syntax


```C++
BOOL EnableEUDC(
  _In_ HDC BOOL fEnableEUDC
);
```



## Parameters

<dl> <dt>

*fEnableEUDC* \[in\]
</dt> <dd>

Boolean that is set to **TRUE** to enable EUDC, and to **FALSE** to disable EUDC.

</dd> </dl>

## Return value

If the function succeeds, the return value is nonzero.

If the function fails, the return value is zero.

## Remarks

If EUDC is disabled, trying to display EUDC characters will result in missing or bad glyphs.

During multi-session, this function affects the current session only.

It is recommended that you use this function with Windows XP SP2 or later.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Library<br/>                  | <dl> <dt>Gdi32.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Gdi32.dll</dt> </dl> |



 

 




