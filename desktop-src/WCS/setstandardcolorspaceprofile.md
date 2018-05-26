---
title: SetStandardColorSpaceProfile function
description: The SetStandardColorSpaceProfile function registers a specified profile for a given standard color space. The profile can be queried using GetStandardColorSpaceProfile.
ms.assetid: fb1d95f0-7f6c-4ad9-a382-459833f177f5
keywords:
- SetStandardColorSpaceProfile function Windows Color System
topic_type:
- apiref
api_name:
- SetStandardColorSpaceProfile
- SetStandardColorSpaceProfileA
- SetStandardColorSpaceProfileW
api_location:
- mscms.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SetStandardColorSpaceProfile function

The **SetStandardColorSpaceProfile** function registers a specified profile for a given standard [color space](c.md#-color-wcs-1-0-glossary-color-space-gloss). The profile can be queried using [**GetStandardColorSpaceProfile**](getstandardcolorspaceprofile.md).

## Syntax


```C++
BOOL WINAPI SetStandardColorSpaceProfile(
   PCTSTR pMachineName,
   DWORD  dwProfileID,
   PCSTR  pProfilename
);
```



## Parameters

<dl> <dt>

*pMachineName* 
</dt> <dd>

Reserved. Must be **NULL**. This parameter is intended to point to the name of the machine on which to set a standard color space profile. A **NULL** pointer indicates the local machine.

</dd> <dt>

*dwProfileID* 
</dt> <dd>

Specifies the ID value of the standard color space that the given profile represents. This is a custom ID value used to uniquely identify the color space profile within your application.

</dd> <dt>

*pProfilename* 
</dt> <dd>

Points to a fully qualified path to the profile file.

</dd> </dl>

## Return value

If this function succeeds, the return value is **TRUE**.

If this function fails, the return value is **FALSE**. For extended error information, call [**GetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms679360).

## Remarks

The profile must already be installed on the system before it can be registered for a standard color space.

This function supports Windows Color System (WCS) device model profiles (DMPs) in addition to International Color Consortium (ICC) profiles. It does not support WCS CAMP or GMMP profiles and will return an error if such profiles are used.

***Per-user/LUA support***

This will register a specified profile for a given standard color space only for current user.

This uses **WcsSetDefaultColorProfile** with WCS\_PROFILE\_MANAGEMENT\_SCOPE\_CURRENT\_USER.

This is executable in LUA context if the profile is already installed, fails otherwise with access denied since install is system-wide and requires administrator privileges.

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                |
| Header<br/>                   | <dl> <dt>Icm.h</dt> </dl>                    |
| Library<br/>                  | <dl> <dt>Mscms.lib</dt> </dl>                |
| DLL<br/>                      | <dl> <dt>Mscms.dll</dt> </dl>                |
| Unicode and ANSI names<br/>   | **SetStandardColorSpaceProfileW** (Unicode) and **SetStandardColorSpaceProfileA** (ANSI)<br/> |



## See also

<dl> <dt>

[Basic Color Management Concepts](basic-color-management-concepts.md)
</dt> <dt>

[Functions](functions.md)
</dt> <dt>

[**GetStandardColorSpaceProfile**](getstandardcolorspaceprofile.md)
</dt> </dl>

 

 





