---
title: WcsSetDefaultColorProfile function
description: Sets the default color profile name for the specified profile type in the specified profile management scope.
ms.assetid: 6f9e8df8-e696-4fd0-8631-5e3d23719def
keywords:
- WcsSetDefaultColorProfile function Windows Color System
topic_type:
- apiref
api_name:
- WcsSetDefaultColorProfile
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

# WcsSetDefaultColorProfile function

Sets the default color profile name for the specified profile type in the specified profile management scope.

## Syntax


```C++
BOOL WINAPI WcsSetDefaultColorProfile(
  _In_     WCS_PROFILE_MANAGEMENT_SCOPE profileManagementScope,
  _In_opt_ PCWSTR                       pDeviceName,
  _In_     COLORPROFILETYPE             cptColorProfileType,
  _In_     COLORPROFILESUBTYPE          cpstColorProfileSubType,
  _In_     DWORD                        dwProfileID,
  _In_     LPCWSTR                      pProfileName
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

A pointer to the name of the device for which the default color profile is to be set. If **NULL**, a device-independent default profile is used.

</dd> <dt>

*cptColorProfileType* \[in\]
</dt> <dd>

A [**COLORPROFILETYPE**](colorprofiletype.md) value that specifies the color profile type.

</dd> <dt>

*cpstColorProfileSubType* \[in\]
</dt> <dd>

A [**COLORPROFILESUBTYPE**](colorprofilesubtype.md) value that specifies the color profile subtype.

</dd> <dt>

*dwProfileID* \[in\]
</dt> <dd>

The ID of the color space that the color profile represents. This is a custom ID value used to uniquely identify the color space profile within your application.

</dd> <dt>

*pProfileName* \[in\]
</dt> <dd>

A pointer to a buffer that holds the name of the color profile. See Remarks.

</dd> </dl>

## Return value

If this function succeeds, the return value is **TRUE**.

If this function fails, the return value is **FALSE**. For extended error information, call [**GetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms679360).

## Remarks

If the *pProfileName* parameter is **NULL** and the *profileManagementScope* parameter is WCS\_PROFILE\_MANAGEMENT\_SCOPE\_CURRENT\_USER, subsequent calls to **WcsSetDefaultColorProfile** will return the system-wide default profile.

If *profileManagementScope* is WCS\_PROFILE\_MANAGEMENT\_SCOPE\_CURRENT\_USER, this function is executable in Least-Privileged User Account (LUA) context. Otherwise, administrative privileges are required. The specified profile must already be installed, but it may be not yet associated with the specified device in the specified profile management scope.

When WcsSetDefaultColorProfile is called to set a device model profile DMP as the default profile for the RGB or custom working space, only a DMP profile that is of type RGBVirtualDevice, LCD, or CRT is valid; all others are invalid.

When WcsSetDefaultColorProfile is called to set an International Color Consortium (ICC) profile as the default profile for the RGB or custom working space, only an ICC profile with class "spac" or "disp", and "RGB" color space is valid; all others are invalid.

See notes on valid profile type/subtype combinations.

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

[**WcsGetDefaultColorProfileSize**](wcsgetdefaultcolorprofilesize.md)
</dt> </dl>

 

 





