---
title: WcsAssociateColorProfileWithDevice function
description: Associates a specified WCS color profile with a specified device.
ms.assetid: '4a4c9175-6af4-4bc3-9a44-1f1614e7240d'
keywords: ["WcsAssociateColorProfileWithDevice function Windows Color System"]
topic_type:
- apiref
api_name:
- WcsAssociateColorProfileWithDevice
- WcsAssociateColorProfileWithDeviceA
- WcsAssociateColorProfileWithDeviceW
api_location:
- mscms.dll
api_type:
- DllExport
---

# WcsAssociateColorProfileWithDevice function

Associates a specified WCS color profile with a specified device.

## Syntax


```C++
BOOL WINAPI WcsAssociateColorProfileWithDevice(
  _In_ WCS_PROFILE_MANAGEMENT_SCOPE profileManagementScope,
  _In_ PCWSTR                       pProfileName,
  _In_ PCWSTR                       pDeviceName
);
```



## Parameters

<dl> <dt>

*profileManagementScope* \[in\]
</dt> <dd>

A [**WCS\_PROFILE\_MANAGEMENT\_SCOPE**](wcs-profile-management-scope.md) value that specifies the scope of this profile management operation, which could be system-wide or for the current user.

</dd> <dt>

*pProfileName* \[in\]
</dt> <dd>

A pointer to the file name of the profile to associate.

</dd> <dt>

*pDeviceName* \[in\]
</dt> <dd>

A pointer to the name of the device with which the profile is to be associated.

</dd> </dl>

## Return value

If this function succeeds, the return value is **TRUE**.

If this function fails, the return value is **FALSE**. For extended error information, call **GetLastError**.

## Remarks

The **WCSAssociateColorProfileWithDevice** function fails if the profile has not been installed on the computer using the [**InstallColorProfile**](installcolorprofile.md) function.

If the *profileManagementScope* parameter is WCS\_PROFILE\_MANAGEMENT\_SCOPE\_SYSTEM\_WIDE, the profile association is system-wide and applies to all users. If *profileManagementScope* is WCS\_PROFILE\_MANAGEMENT\_SCOPE\_CURRENT\_USER, the association is only for the current user.

This function is executable in Least-Privileged User Account (LUA) context if *profileManagementScope* is WCS\_PROFILE\_MANAGEMENT\_SCOPE\_CURRENT\_USER. Otherwise, administrative privileges are required.

## Requirements



|                                     |                                                                                                                 |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                            |
| Header<br/>                   | <dl> <dt>Icm.h</dt> </dl>                                |
| Library<br/>                  | <dl> <dt>Mscms.lib</dt> </dl>                            |
| DLL<br/>                      | <dl> <dt>Mscms.dll</dt> </dl>                            |
| Unicode and ANSI names<br/>   | **WcsAssociateColorProfileWithDeviceW** (Unicode) and **WcsAssociateColorProfileWithDeviceA** (ANSI)<br/> |



## See also

<dl> <dt>

[Basic Color Management Concepts](basic-color-management-concepts.md)
</dt> <dt>

[Windows Color System Schemas and Algorithms](windows-color-system-schemas-and-algorithms.md)
</dt> <dt>

[Functions](functions.md)
</dt> <dt>

[**WcsDisassociateColorProfileFromDevice**](wcsdisassociatecolorprofilefromdevice.md)
</dt> </dl>

 

 





