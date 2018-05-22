---
title: DisassociateColorProfileFromDevice function
description: The DisassociateColorProfileFromDevice function disassociates a specified color profile with a specified device on a specified computer.
ms.assetid: '731b4172-3bd6-4f6f-9045-07f36197e120'
keywords: ["DisassociateColorProfileFromDevice function Windows Color System"]
topic_type:
- apiref
api_name:
- DisassociateColorProfileFromDevice
- DisassociateColorProfileFromDeviceA
- DisassociateColorProfileFromDeviceW
api_location:
- mscms.dll
api_type:
- DllExport
---

# DisassociateColorProfileFromDevice function

The **DisassociateColorProfileFromDevice** function disassociates a specified color profile with a specified device on a specified computer.

## Syntax


```C++
BOOL WINAPI DisassociateColorProfileFromDevice(
   PCTSTR pMachineName,
   PCTSTR pProfileName,
   PCTSTR pDeviceName
);
```



## Parameters

<dl> <dt>

*pMachineName* 
</dt> <dd>

Reserved. Must be **NULL**. This parameter is intended to point to the name of the computer on which to disassociate the specified profile and device. A **NULL** pointer indicates the local computer.

</dd> <dt>

*pProfileName* 
</dt> <dd>

Pointer to the file name of the profile to disassociate.

</dd> <dt>

*pDeviceName* 
</dt> <dd>

Pointer to the name of the device to disassociate.

</dd> </dl>

## Return value

If this function succeeds, the return value is **TRUE**.

If this function fails, the return value is **FALSE**. For extended error information, call **GetLastError**.

## Remarks

If more than one profile is associated with a device, WCS uses the last one associated as the default. That is, if your application sequentially associates three profiles with a device, WCS will use the last one associated as the default. If your application then calls the **DisassociateColorProfileFromDevice** function to disassociate the third profile (which is the default in this example), the WCS will use the second profile as the default.

If your application disassociates all profiles from a device, WCS uses the sRGB profile as the default.

**DisassociateColorProfileFromDevice** always removes the specified profile from the current user's per-user profile association list for the specified device. Before removing the profile from the list, **DisassociateColorProfileFromDevice** determines whether the user has previously expressed the desire to use a per-user profile association list for the device. If so, then **DisassociateColorProfileFromDevice** simply removes the specified profile from the existing per-user profile association list for the device. If not, then **DisassociateColorProfileFromDevice** creates a new per-user profile association list for the device by copying the system-wide association list for that device. It then removes the specified profile from the per-user list. From that point on, the current user will be using a per-user profile association list for the specified device, as if [**WcsSetUsePerUserProfiles**](wcssetuseperuserprofiles.md) had been called for *pDevice* with the *usePerUserProfiles* parameter set to **TRUE**.

## Requirements



|                                     |                                                                                                                 |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                      |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                            |
| Header<br/>                   | <dl> <dt>Icm.h</dt> </dl>                                |
| Library<br/>                  | <dl> <dt>Mscms.lib</dt> </dl>                            |
| DLL<br/>                      | <dl> <dt>Mscms.dll</dt> </dl>                            |
| Unicode and ANSI names<br/>   | **DisassociateColorProfileFromDeviceW** (Unicode) and **DisassociateColorProfileFromDeviceA** (ANSI)<br/> |



## See also

<dl> <dt>

[Basic Color Management Concepts](basic-color-management-concepts.md)
</dt> <dt>

[Functions](functions.md)
</dt> <dt>

[**AssociateColorProfileWithDevice**](associatecolorprofilewithdevice.md)
</dt> </dl>

 

 





