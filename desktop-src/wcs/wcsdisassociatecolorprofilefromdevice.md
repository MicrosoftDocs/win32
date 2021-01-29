---
title: WcsDisassociateColorProfileFromDevice function
description: Disassociates a specified WCS color profile from a specified device on a computer.
ms.assetid: d5c2ee77-7cab-4f41-801c-bc749bba00c1
keywords:
- WcsDisassociateColorProfileFromDevice function Windows Color System
topic_type:
- apiref
api_name:
- WcsDisassociateColorProfileFromDevice
api_location:
- mscms.dll
api_type:
- DllExport
ms.localizationpriority: high


ms.topic: article
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# WcsDisassociateColorProfileFromDevice function

Disassociates a specified WCS color profile from a specified device on a computer.

## Syntax


```C++
BOOL WINAPI WcsDisassociateColorProfileFromDevice(
  _In_ WCS_PROFILE_MANAGEMENT_SCOPE profileManagementScope,
  _In_ PCWSTR                       pProfileName,
  _In_ PCWSTR                       pDeviceName
);
```



## Parameters

<dl> <dt>

*profileManagementScope* \[in\]
</dt> <dd>

A [**WCS\_PROFILE\_MANAGEMENT\_SCOPE**](/windows/win32/api/icm/ne-icm-wcs_profile_management_scope) value that specifies the scope of this profile management operation, which could be system-wide or for the current user.

</dd> <dt>

*pProfileName* \[in\]
</dt> <dd>

A pointer to the file name of the profile to disassociate.

</dd> <dt>

*pDeviceName* \[in\]
</dt> <dd>

A pointer to the name of the device from which to disassociate the profile.

</dd> </dl>

## Return value

If this function succeeds, the return value is **TRUE**.

If this function fails, the return value is **FALSE**. For extended error information, call **GetLastError**.

## Remarks

The WCS color profile should be installed. Moreover, you must use the same *profileManagementScope* value as when the device was associated with the profile. See [**WcsAssociateColorProfileWithDevice**](wcsassociatecolorprofilewithdevice.md).

If *profileManagementScope* is WCS\_PROFILE\_MANAGEMENT\_SCOPE\_SYSTEM\_WIDE, the profile disassociation is systemwide and applies to all users. If *profileManagementScope* is WCS\_PROFILE\_MANAGEMENT\_SCOPE\_CURRENT\_USER, the disassociation is only for the current user.

If more than one color profile is associated with a device, WCS uses the last associated profile as the default. For example, if your application sequentially associates three profiles with a device, WCS uses the last profile associated as the default. If your application then calls the **WcsDisassociateColorProfileFromDevice** function to disassociate the third profile (which is the default in this example), WCS uses the second profile as the default.

If your application disassociates all profiles from a device, WCS uses the sRGB profile as the default.

If *profileManagementScope* is WCS\_PROFILE\_MANAGEMENT\_SCOPE\_CURRENT\_USER, this function is executable in Least-Privileged User Account (LUA) context. Otherwise, administrative privileges are required.

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

[**WcsAssociateColorProfileWithDevice**](wcsassociatecolorprofilewithdevice.md)
</dt> </dl>

 

 





