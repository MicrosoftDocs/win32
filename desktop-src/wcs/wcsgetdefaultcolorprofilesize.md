---
title: WcsGetDefaultColorProfileSize function
description: Returns the size, in bytes, of the default color profile name (including the NULL terminator), for a device.
ms.assetid: 68f589ac-15e0-4d13-a2fa-e3f74d7d3d19
keywords:
- WcsGetDefaultColorProfileSize function Windows Color System
topic_type:
- apiref
api_name:
- WcsGetDefaultColorProfileSize
api_location:
- mscms.dll
api_type:
- DllExport
ms.localizationpriority: high


ms.topic: article
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# WcsGetDefaultColorProfileSize function

Returns the size, in bytes, of the default color profile name (including the **NULL** terminator), for a device.

## Syntax


```C++
BOOL WINAPI WcsGetDefaultColorProfileSize(
  _In_     WCS_PROFILE_MANAGEMENT_SCOPE profileManagementScope,
  _In_opt_ PCWSTR                       pDeviceName,
  _In_     COLORPROFILETYPE             cptColorProfileType,
  _In_     COLORPROFILESUBTYPE          cpstColorProfileSubType,
  _In_     DWORD                        dwProfileID,
  _Out_    PDWORD                       pcbProfileName
);
```



## Parameters

<dl> <dt>

*profileManagementScope* \[in\]
</dt> <dd>

A [**WCS\_PROFILE\_MANAGEMENT\_SCOPE**](wcs-profile-management-scope.md) value that specifies the scope of this profile management operation.

</dd> <dt>

*pDeviceName* \[in, optional\]
</dt> <dd>

A pointer to the name of the device for which the default color profile is to be obtained. If **NULL**, a device-independent default profile will be used.

</dd> <dt>

*cptColorProfileType* \[in\]
</dt> <dd>

A [**COLORPROFILETYPE**](colorprofiletype.md) value specifying the color profile type.

</dd> <dt>

*cpstColorProfileSubType* \[in\]
</dt> <dd>

A [**COLORPROFILESUBTYPE**](colorprofilesubtype.md) value specifying the color profile subtype.

</dd> <dt>

*dwProfileID* \[in\]
</dt> <dd>

The ID of the color space that the color profile represents.

</dd> <dt>

*pcbProfileName* \[out\]
</dt> <dd>

A pointer to a location that receives the size, in bytes, of the path name of the default color profile, including the **NULL** terminator.

</dd> </dl>

## Return value

If this function succeeds, the return value is **TRUE**.

If this function fails, the return value is **FALSE**. For extended error information, call **GetLastError**.

## Remarks

Use this function to return the required size of the buffer that is pointed to by the *pProfileName* parameter in the [**WcsGetDefaultColorProfile**](wcsgetdefaultcolorprofile.md) function.

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

[**COLORPROFILESUBTYPE**](colorprofilesubtype.md)
</dt> <dt>

[**COLORPROFILETYPE**](colorprofiletype.md)
</dt> <dt>

[**WCS\_PROFILE\_MANAGEMENT\_SCOPE**](wcs-profile-management-scope.md)
</dt> <dt>

[**WcsGetDefaultColorProfile**](wcsgetdefaultcolorprofile.md)
</dt> </dl>

 

 





