---
Description: 'The WcsDisassociateColorProfileFromDevice function disassociates a specified WCS color profile from a specified device.'
ms.assetid: 'd2ab6fe4-131a-4952-864c-7135026cb25c'
title: WcsDisassociateColorProfileFromDevice function
---

# WcsDisassociateColorProfileFromDevice function

The `WcsDisassociateColorProfileFromDevice` function disassociates a specified WCS color profile from a specified device.

## Syntax


```C++
BOOL WcsDisassociateColorProfileFromDevice(
  _In_ WCS_PROFILE_MANAGEMENT_SCOPE profileManagementScope,
  _In_ PCWSTR                       pProfileName,
  _In_ PCWSTR                       pDeviceName
);
```



## Parameters

<dl> <dt>

*profileManagementScope* \[in\]
</dt> <dd>

A [**WCS\_PROFILE\_MANAGEMENT\_SCOPE**](wcs-profile-management-scope.md) value that specifies the scope of this profile management operation.

</dd> <dt>

*pProfileName* \[in\]
</dt> <dd>

A pointer to the file name of the profile to disassociate.

</dd> <dt>

*pDeviceName* \[in\]
</dt> <dd>

A pointer to the name of the device from which the profile is to be disassociated.

</dd> </dl>

## 

If this function succeeds, the return value is **TRUE**.

If this function fails, the return value is **FALSE**. For extended error information, call **GetLastError** (described in the Microsoft Windows SDK documentation).

## Remarks

The WCS color profile should be installed on the system and must have been associated with the device using the same value for the *profileManagementScope* parameter.

If *profileManagementScope* is WCS\_PROFILE\_MANAGEMENT\_SCOPE\_SYSTEM\_WIDE, the profile disassociation is system-wide and applies to all users. If *profileManagementScope* is WCS\_PROFILE\_MANAGEMENT\_SCOPE\_CURRENT\_USER, the disassociation is only for the current user.

If more than one WCS color profile is associated with a device, WCS uses the last one associated as the default. That is, if your application sequentially associates three profiles with a device, WCS will use the last one associated as the default. If your application then calls the `WcsDisassociateColorProfileFromDevice` function to disassociate the third profile (which is the default in this example), WCS will use the second profile as the default.

If your application disassociates all profiles from a device, WCS uses the sRGB profile as the default.

This function is executable in Least-Privileged User Account (LUA) context if *profileManagementScope* is WCS\_PROFILE\_MANAGEMENT\_SCOPE\_CURRENT\_USER. Otherwise, administrative privileges are required..

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

[**WcsAssociateColorProfileWithDevice**](wcsassociatecolorprofilewithdevice.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20WcsDisassociateColorProfileFromDevice%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





