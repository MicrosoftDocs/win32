---
title: WcsGetDefaultColorProfile function
description: Retrieves the default color profile for a device, or for a device-independent default if the device is not specified.
ms.assetid: 'a40ea9f3-ec56-459e-a55d-aad1b60ae7d4'
keywords: ["WcsGetDefaultColorProfile function Windows Color System"]
topic_type:
- apiref
api_name:
- WcsGetDefaultColorProfile
api_location:
- mscms.dll
api_type:
- DllExport
---

# WcsGetDefaultColorProfile function

Retrieves the default color profile for a device, or for a device-independent default if the device is not specified.

## Syntax


```C++
BOOL WINAPI WcsGetDefaultColorProfile(
  _In_     WCS_PROFILE_MANAGEMENT_SCOPE profileManagementScope,
  _In_opt_ PCWSTR                       pDeviceName,
  _In_     COLORPROFILETYPE             cptColorProfileType,
  _In_     COLORPROFILESUBTYPE          cpstColorProfileSubType,
  _In_     DWORD                        dwProfileID,
  _In_     DWORD                        cbProfileName,
  _Out_    LPWSTR                       pProfileName
);
```



## Parameters

<dl> <dt>

*profileManagementScope* \[in\]
</dt> <dd>

A [**WCS\_PROFILE\_MANAGEMENT\_SCOPE**](wcs-profile-management-scope.md) value specifying the scope of this profile management operation.

</dd> <dt>

*pDeviceName* \[in, optional\]
</dt> <dd>

A pointer to the name of the device for which the default color profile is obtained. If **NULL**, a device-independent default profile is obtained.

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

*cbProfileName* \[in\]
</dt> <dd>

The buffer size, in bytes, of the buffer that is pointed to by *pProfileName*.

</dd> <dt>

*pProfileName* \[out\]
</dt> <dd>

A pointer to a buffer to receive the name of the color profile. The size of the buffer, in bytes, will be the indicated by *cbProfileName*.

</dd> </dl>

## Return value

If this function succeeds, the return value is **TRUE**.

If this function fails, the return value is **FALSE**. For extended error information, call **GetLastError**.

## Remarks

Use the [**WcsGetDefaultColorProfileSize**](wcsgetdefaultcolorprofilesize.md) function to obtain the required size of the buffer that is pointed to by the *pProfileName* parameter.

If WCS\_PROFILE\_MANAGEMENT\_SCOPE\_CURRENT\_USER is present, it overrides the system-wide default for *profileManagementScope*.

This function is executable in Least-Privileged User Account (LUA) context.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                 |
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

[**WcsGetDefaultColorProfileSize**](wcsgetdefaultcolorprofilesize.md)
</dt> </dl>

 

 





