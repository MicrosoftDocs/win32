---
title: WcsEnumColorProfiles function
description: Enumerates all color profiles that satisfy the enumeration criteria in the specified profile management scope.
ms.assetid: 45d670ae-a2f1-4281-bcd8-0663ee3e7fe4
keywords:
- WcsEnumColorProfiles function Windows Color System
topic_type:
- apiref
api_name:
- WcsEnumColorProfiles
- WcsEnumColorProfilesA
- WcsEnumColorProfilesW
api_location:
- mscms.dll
api_type:
- DllExport
ms.localizationpriority: high


ms.topic: article
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# WcsEnumColorProfiles function

Enumerates all color profiles that satisfy the enumeration criteria in the specified profile management scope.

## Syntax


```C++
BOOL WINAPI WcsEnumColorProfiles(
  _In_      WCS_PROFILE_MANAGEMENT_SCOPE profileManagementScope,
  _In_      PENUMTYPEW                   pEnumRecord,
  _Out_     PBYTE                        pBuffer,
  _In_      DWORD                        dwSize,
  _Out_opt_ PDWORD                       pnProfiles
);
```



## Parameters

<dl> <dt>

*profileManagementScope* \[in\]
</dt> <dd>

A [**WCS\_PROFILE\_MANAGEMENT\_SCOPE**](/windows/win32/api/icm/ne-icm-wcs_profile_management_scope) value specifying the scope of this profile management operation.

</dd> <dt>

*pEnumRecord* \[in\]
</dt> <dd>

A pointer to a structure specifying the enumeration criteria.

</dd> <dt>

*pBuffer* \[out\]
</dt> <dd>

A pointer to a buffer in which the profile names are to be enumerated. The **WcsEnumColorProfiles** function places, in this buffer, a MULTI\_SZ string that consists of profile names that satisfy the criteria specified in *\*pEnumRecord*.

</dd> <dt>

*dwSize* \[in\]
</dt> <dd>

A variable that contains the size, in bytes, of the buffer that is pointed to by *pBuffer*. See Remarks.

</dd> <dt>

*pnProfiles* \[out, optional\]
</dt> <dd>

An optional pointer to a variable that receives the number of profile names that are copied to the buffer to which *pBuffer* points. Can be **NULL** if this information is not needed.

</dd> </dl>

## Return value

If this function succeeds, the return value is **TRUE**.

If this function fails, the return value is **FALSE**. For extended error information, call **GetLastError**.

## Remarks

Use the [**WcsEnumColorProfilesSize**](wcsenumcolorprofilessize.md) function to retrieve the value for the *dwSize* parameter, which is the size, in bytes, of the buffer pointed to by the *pBuffer* parameter.

If the *profileManagementScope* parameter is WCS\_PROFILE\_MANAGEMENT\_SCOPE\_SYSTEM\_WIDE, only system-wide associations of profiles to the device are considered. If *profileManagementScope* is WCS\_PROFILE\_MANAGEMENT\_SCOPE\_CURRENT\_USER, only per-user associations for the current user are considered. If [**WcsSetUsePerUserProfiles**](wcssetuseperuserprofiles.md) has never been called for this user, or if **WcsSetUsePerUserProfiles** was most recently called for this user with its *usePerUserProfiles* parameter set to **FALSE**, then **WCSEnumColorProfiles** returns an empty list.

If WCS\_PROFILE\_MANAGEMENT\_SCOPE\_CURRENT\_USER (the current user setting) is present, it overrides the system-wide default for the *profileManagementScope* parameter.

This function is executable in Least-Privileged User Account (LUA) context.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Icm.h</dt> </dl>     |
| Library<br/>                  | <dl> <dt>Mscms.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Mscms.dll</dt> </dl> |
| Unicode and ANSI names<br/>   | **WcsEnumColorProfilesW** (Unicode) and **WcsEnumColorProfilesA** (ANSI)<br/>  |



## See also

<dl> <dt>

[Basic color management concepts](basic-color-management-concepts.md)
</dt> <dt>

[Windows Color System Schemas and Algorithms](windows-color-system-schemas-and-algorithms.md)
</dt> <dt>

[Functions](functions.md)
</dt> <dt>

[**WCS\_PROFILE\_MANAGEMENT\_SCOPE**](/windows/win32/api/icm/ne-icm-wcs_profile_management_scope)
</dt> <dt>

[**WcsEnumColorProfilesSize**](wcsenumcolorprofilessize.md)
</dt> </dl>

 

 





