---
title: GetStandardColorSpaceProfile function
description: The GetStandardColorSpaceProfile function retrieves the color profile registered for the specified standard color space.
ms.assetid: b00f5c5c-f536-4d88-b61f-d2bdd0b180a0
keywords:
- GetStandardColorSpaceProfile function Windows Color System
topic_type:
- apiref
api_name:
- GetStandardColorSpaceProfile
- GetStandardColorSpaceProfileA
- GetStandardColorSpaceProfileW
api_location:
- Mscms.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# GetStandardColorSpaceProfile function

The **GetStandardColorSpaceProfile** function retrieves the color profile registered for the specified standard [color space](c.md#-color-wcs-1-0-glossary-color-space-gloss).

## Syntax


```C++
BOOL WINAPI GetStandardColorSpaceProfile(
   PCTSTR pMachineName,
   DWORD  dwProfileID,
   PTSTR  pProfileName,
   PDWORD pdwSize
);
```



## Parameters

<dl> <dt>

*pMachineName* 
</dt> <dd>

Reserved. Must be **NULL**. This parameter is intended to point to the name of the computer on which to get a standard color space profile. A **NULL** pointer indicates the local machine.

</dd> <dt>

*dwProfileID* 
</dt> <dd>

Specifies the ID value of the standard color space for which to retrieve the profile. The only valid values for this parameter are LCS\_sRGB and LCS\_WINDOWS\_COLOR\_SPACE.

</dd> <dt>

*pProfileName* 
</dt> <dd>

Pointer to the buffer in which the name of the profile is to be placed. If **NULL**, the call will return **TRUE** and the required size of the buffer is placed in *pdwSize.*

</dd> <dt>

*pdwSize* 
</dt> <dd>

Pointer to a variable containing the size in bytes of the buffer pointed to by *pProfileName*. On return, the variable contains the size of the buffer actually used or needed.

</dd> </dl>

## Return value

If this function succeeds, the return value is **TRUE**.

If this function fails, the return value is **FALSE**. For extended error information, call **GetLastError**.

## Remarks

If the buffer pointed to by *pProfileName* is to be dynamically allocated by an application, the application can call the **GetStandardColorSpaceProfile** function to retrieve the size required for the buffer. If **GetStandardColorSpaceProfile** is called with *pProfileName* set to **NULL**, it will return **FALSE** and the **DWORD** pointed at by *pdwSize* will contain the number of bytes needed for the buffer pointed at by *pProfileName*. The application can then allocate the buffer and call **GetStandardColorSpaceProfile** again with *pProfileName* set to the address of the buffer.

This function supports Windows Color System (WCS) device model profiles (DMPs) in addition to International Color Consortium (ICC) profiles. It does not support WCS CAMP or GMMP profiles and will return an error if such profiles are used.

**Overview of Windows Vista Specific Functionality**

This will support WCS DMPs in addition to ICC profiles. It will not support WCS CAMP or GMMP profiles and will return an error if such profiles are used with this API.

***Per-user/LUA support***

This will retrieve the color profile registered for the given standard color space for current user. If there is no such setting for the current user, it retrieves the system wide setting.

This uses **WcsGetDefaultColorProfile** with WCS\_PROFILE\_MANAGEMENT\_SCOPE\_CURRENT\_USER.

This is executable in LUA context.

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                |
| Header<br/>                   | <dl> <dt>Icm.h</dt> </dl>                    |
| Library<br/>                  | <dl> <dt>Mscms.lib</dt> </dl>                |
| DLL<br/>                      | <dl> <dt>Mscms.dll</dt> </dl>                |
| Unicode and ANSI names<br/>   | **GetStandardColorSpaceProfileW** (Unicode) and **GetStandardColorSpaceProfileA** (ANSI)<br/> |



## See also

<dl> <dt>

[Basic Color Management Concepts](basic-color-management-concepts.md)
</dt> <dt>

[Functions](functions.md)
</dt> <dt>

[**SetStandardColorSpaceProfile**](setstandardcolorspaceprofile.md)
</dt> </dl>

 

 





