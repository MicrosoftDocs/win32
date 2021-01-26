---
title: WcsEnumColorProfilesSize function
description: Returns the size, in bytes, of the buffer that is required by the WcsEnumColorProfiles function to enumerate color profiles.
ms.assetid: 1fc76f8a-dad5-4447-bffc-2df58b4201de
keywords:
- WcsEnumColorProfilesSize function Windows Color System
topic_type:
- apiref
api_name:
- WcsEnumColorProfilesSize
api_location:
- mscms.dll
api_type:
- DllExport
ms.localizationpriority: high


ms.topic: article
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# WcsEnumColorProfilesSize function

Returns the size, in bytes, of the buffer that is required by the [**WcsEnumColorProfiles**](wcsenumcolorprofiles.md) function to enumerate color profiles.

## Syntax


```C++
BOOL WINAPI WcsEnumColorProfilesSize(
  _In_  WCS_PROFILE_MANAGEMENT_SCOPE profileManagementScope,
  _In_  PENUMTYPEW                   pEnumRecord,
  _Out_ PDWORD                       pdwSize
);
```



## Parameters

<dl> <dt>

*profileManagementScope* \[in\]
</dt> <dd>

A [**WCS\_PROFILE\_MANAGEMENT\_SCOPE**](wcs-profile-management-scope.md) value that specifies the scope of the profile management operation that is performed by this function.

</dd> <dt>

*pEnumRecord* \[in\]
</dt> <dd>

A pointer to a structure that specifies the enumeration criteria.

</dd> <dt>

*pdwSize* \[out\]
</dt> <dd>

A pointer to a variable that receives the size of the buffer that is required to receive all enumerated profile names. This value is used by the *dwSize* parameter of the [**WcsEnumColorProfiles**](wcsenumcolorprofiles.md) function.

</dd> </dl>

## Return value

If this function succeeds, the return value is **TRUE**.

If this function fails, the return value is **FALSE**. For extended error information, call **GetLastError**.

## Remarks

This function is executable in Least-Privileged User Account (LUA) context.

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
</dt> <dt>

[**WcsEnumColorProfiles**](wcsenumcolorprofiles.md)
</dt> <dt>

[**WCS\_PROFILE\_MANAGEMENT\_SCOPE**](wcs-profile-management-scope.md)
</dt> </dl>

 

 





