---
Description: The WcsEnumColorProfiles function enumerates all color profiles that satisfy the enumeration criteria in the specified profile management scope.
ms.assetid: 54cb2647-5685-4856-9b70-97733758aac2
title: WcsEnumColorProfiles function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WcsEnumColorProfiles function

The `WcsEnumColorProfiles` function enumerates all color profiles that satisfy the enumeration criteria in the specified profile management scope.

## Syntax


```C++
BOOL WcsEnumColorProfiles(
  _In_      WCS_PROFILE_MANAGEMENT_SCOPE profileManagementScope,
  _In_      PENUMTYPEW                   pEnumRecord,
  _Out_     PBYTE                        pBuffer,
  _In_      DWORD                        dwSize,
  _Out_opt_ PDWORD                       pnProfiles
);
```



## Parameters

<dl> <dt>

*profileManagementScope* \[in\]
</dt> <dd>

A [**WCS\_PROFILE\_MANAGEMENT\_SCOPE**](wcs-profile-management-scope.md) value that specifies the scope of this profile management operation.

</dd> <dt>

*pEnumRecord* \[in\]
</dt> <dd>

A pointer to a structure that specifies the enumeration criteria.

</dd> <dt>

*pBuffer* \[out\]
</dt> <dd>

A pointer to a buffer in which the profile names are to be enumerated. A MULTI\_SZ string that consists of profile names that satisfy the criteria specified in *\*pEnumRecord* will be placed in this buffer.

</dd> <dt>

*dwSize* \[in\]
</dt> <dd>

A variable that contains the size, in bytes, of the buffer pointed to by *pBuffer*. See Remarks.

</dd> <dt>

*pnProfiles* \[out, optional\]
</dt> <dd>

An optional pointer to a variable that receives the number of profile names actually copied to the buffer pointed to by *pBuffer*. Can be **NULL** if this information is not needed.

</dd> </dl>

## 

If this function succeeds, the return value is **TRUE**.

If this function fails, the return value is **FALSE**. For extended error information, call **GetLastError** (described in the Microsoft Windows SDK documentation).

## Remarks

Use the [**WcsEnumColorProfilesSize**](wcsenumcolorprofilessize.md) function to obtain the value for the *dwSize* parameter, which is the size, in bytes, of the buffer pointed to by the *pBuffer* parameter.

If the *profileManagementScope* parameter is WCS\_PROFILE\_MANAGEMENT\_SCOPE\_SYSTEM\_WIDE, only system-wide associations of profiles to the device are considered. If *profileManagementScope* is WCS\_PROFILE\_MANAGEMENT\_SCOPE\_CURRENT\_USER, only per-user associations for the current user are considered. If either [**WcsSetUsePerUserProfiles**](wcssetuseperuserprofiles.md) has never been called for this user, or **WcsSetUsePerUserProfiles** was most recently called for this user with its *usePerUserProfiles* parameter set to **FALSE**, then `WCSEnumColorProfiles` returns an empty list.

If WCS\_PROFILE\_MANAGEMENT\_SCOPE\_CURRENT\_USER, the current user setting, is present, it overrides the system-wide default for the *profileManagementScope* parameter.

This function is executable in Least-Privileged User Account (LUA) context.

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Version<br/>         | Included in Windows Vista and later.<br/>                                                                                         |
| Header<br/>          | <dl> <dt>Icm.h</dt> </dl>                                                        |
| Library<br/>         | <dl> <dt>Mscms.lib</dt> </dl>                                                    |
| DLL<br/>             | <dl> <dt>Mscms.dll</dt> </dl>                                                    |



## See also

<dl> <dt>

[**WCS\_PROFILE\_MANAGEMENT\_SCOPE**](wcs-profile-management-scope.md)
</dt> <dt>

[**WcsEnumColorProfilesSize**](wcsenumcolorprofilessize.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20WcsEnumColorProfiles%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





