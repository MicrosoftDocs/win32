---
title: AssociateColorProfileWithDevice function
description: The AssociateColorProfileWithDevice function associates a specified color profile with a specified device.
ms.assetid: 2a4adfde-ab91-48f1-8212-3263006ea3a1
keywords:
- AssociateColorProfileWithDevice function Windows Color System
topic_type:
- apiref
api_name:
- AssociateColorProfileWithDevice
- AssociateColorProfileWithDeviceA
- AssociateColorProfileWithDeviceW
api_location:
- mscms.dll
api_type:
- DllExport
ms.localizationpriority: high


ms.topic: article
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# AssociateColorProfileWithDevice function

The **AssociateColorProfileWithDevice** function associates a specified color profile with a specified device.

## Syntax


```C++
BOOL WINAPI AssociateColorProfileWithDevice(
   PCTSTR pMachineName,
   PCTSTR pProfileName,
   PCTSTR pDeviceName
);
```



## Parameters

<dl> <dt>

*pMachineName* 
</dt> <dd>

Reserved. Must be **NULL**. This parameter is intended to point to the name of the machine on which to associate the specified profile and device. A **NULL** pointer indicates the local machine.

</dd> <dt>

*pProfileName* 
</dt> <dd>

Points to the file name of the profile to associate.

</dd> <dt>

*pDeviceName* 
</dt> <dd>

Points to the name of the device to associate.

</dd> </dl>

## Return value

If this function succeeds, the return value is **TRUE**.

If this function fails, the return value is **FALSE**. For extended error information, call [**GetLastError**](https://www.bing.com/search?q=**GetLastError**).

## Remarks

The **AssociateColorProfileWithDevice** function will fail if the profile has not been installed on the computer using the [**InstallColorProfile**](installcolorprofile.md) function.

Note that under Windows (Windows 95 or later), the PostScript device driver for printers assumes a CMYK color model. Therefore, all PostScript printers must use a CMYK color profile. Windows 2000 does not have this limitation.

If the specified device is a monitor, this function updates the default profile.

Several profiles are typically associated with printers, based on paper and ink types. There is no default. The GDI selects the best one from the associated profiles when your application creates a device context (DC).

Scanners also have no default profile. However, it is atypical to associate more than one profile with a scanner.

**AssociateColorProfileWithDevice** always adds the specified profile to the current user's per-user profile association list for the specified device. Before adding the profile to the list, **AssociateColorProfileWithDevice** determines whether the user has previously expressed the desire to use a per-user profile association list for the device. If so, then **AssociateColorProfileWithDevice** simply adds the specified profile to the existing per-user profile association list for the device. If not, then **AssociateColorProfileWithDevice** creates a new per-user profile association list for the device by copying the system-wide association list for that device. It then appends the specified profile to the per-user list. From that point on, the current user will be using a per-user profile association list for the specified device, as if [**WcsSetUsePerUserProfiles**](wcssetuseperuserprofiles.md) had been called for *pDevice* with the *usePerUserProfiles* parameter set to **TRUE**.

## Requirements



|                                     |                                                                                                           |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Icm.h</dt> </dl>                          |
| Library<br/>                  | <dl> <dt>Mscms.lib</dt> </dl>                      |
| DLL<br/>                      | <dl> <dt>Mscms.dll</dt> </dl>                      |
| Unicode and ANSI names<br/>   | **AssociateColorProfileWithDeviceW** (Unicode) and **AssociateColorProfileWithDeviceA** (ANSI)<br/> |



## See also

<dl> <dt>

[Basic Color Management Concepts](basic-color-management-concepts.md)
</dt> <dt>

[Functions](functions.md)
</dt> <dt>

[**DisassociateColorProfileFromDevice**](disassociatecolorprofilefromdevice.md)
</dt> </dl>

 

 





