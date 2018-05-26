---
title: EnumColorProfiles function
description: The EnumColorProfiles function enumerates all the profiles satisfying the given enumeration criteria.
ms.assetid: 92d38155-e950-4c96-94e9-b66dbf090fca
keywords:
- EnumColorProfiles function Windows Color System
topic_type:
- apiref
api_name:
- EnumColorProfiles
- EnumColorProfilesA
- EnumColorProfilesW
api_location:
- mscms.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# EnumColorProfiles function

The **EnumColorProfiles** function enumerates all the profiles satisfying the given enumeration criteria.

## Syntax


```C++
BOOL WINAPI EnumColorProfiles(
   PCTSTR    pMachineName,
   PENUMTYPE pEnumRecord,
   PBYTE     pBuffer,
   PDWORD    pdwSize,
   PDWORD    pnProfiles
);
```



## Parameters

<dl> <dt>

*pMachineName* 
</dt> <dd>

Reserved. Must be **NULL**. This parameter is intended to point to the name of the computer on which to enumerate profiles. A **NULL** pointer indicates the local computer.

</dd> <dt>

*pEnumRecord* 
</dt> <dd>

Pointer to a structure specifying the enumeration criteria.

</dd> <dt>

*pBuffer* 
</dt> <dd>

Pointer to a buffer in which the profiles are to be enumerated. A MULTI\_SZ string of profile names satisfying the criteria specified in *\*pEnumRecord* will be placed in this buffer.

</dd> <dt>

*pdwSize* 
</dt> <dd>

Pointer to a variable containing the size of the buffer pointed to by *pBuffer*. On return, *\*pdwSize* contains the size of buffer actually used or needed.

</dd> <dt>

*pnProfiles* 
</dt> <dd>

Pointer to a variable that will contain, on return, the number of profile names actually copied to the buffer.

</dd> </dl>

## Return value

If this function succeeds, the return value is **TRUE**.

If this function fails, the return value is **FALSE**. For extended error information, call [**GetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms679360).

## Remarks

Several profiles are typically associated with printers, based on the paper and ink types. There is a default profile for each device. For International Color Consortium (ICC) profiles, GDI selects the best one from the ICC-associated profiles when your application creates a device context (DC).

Do not attempt to use **EnumColorProfiles** to determine the default profile for a device. Instead, create a device context for the device and then invoke the [**GetICMProfile**](/windows/win32/Wingdi/nf-wingdi-geticmprofilea?branch=master) function. On Windows Vista and Windows 7, the [**WcsGetDefaultColorProfile**](wcsgetdefaultcolorprofile.md) function can also be used to determine a device's default color profile.

If the **dwFields** member of the structure of type **ENUMTYPE** that is pointed to by the *pEnumRecord* parameter is set to ET\_DEVICENAME, this function will enumerate all of the color profiles associated with all types of devices attached to the user's computer, regardless of the device class. If the **dwFields** member of the structure pointed to by the *pEnumRecord* parameter is set to ET\_DEVICENAME or ET\_DEVICECLASS and a device class is specified in the **dwDeviceClass** member of the structure, this function will only enumerate the profiles associated with the specified device class. If the **dwFields** member is set only to ET\_DEVICECLASS, the **EnumColorProfiles** function will enumerate all profiles that can be associated with that type of device.

Whenever **EnumColorProfiles** is examining the profiles associated with a specific device, the results depend on whether the user has chosen to use the system-wide list of profiles associated with that device, or his or her own ("per-user") list. Calling [**WcsSetUsePerUserProfiles**](wcssetuseperuserprofiles.md) with its *usePerUserProfiles* parameter set to **TRUE** causes future calls to **EnumColorProfiles** to look at only the current user's per-user list of profile associations for the specified device. Calling **WcsSetUsePerUserProfiles** with its *usePerUserProfiles* parameter set to **FALSE** causes future calls to **EnumColorProfiles** to look at the system-wide list of profile associations for the specified device. If **WcsSetUsePerUserProfiles** has never been called for the current user, **EnumColorProfiles** examines the system-wide list.

Your application can use **EnumColorProfiles** to obtain the size of the buffer in which the profiles are enumerated. It should call the **EnumColorProfiles** function with the *pBuffer* parameter set to **NULL**. When the function returns, the *pdwSize* parameter will contain the required buffer size in bytes. Your program can use that information to allocate the enumeration buffer. It can then invoke **EnumColorProfiles** again with the *pBuffer* parameter set to the address of the buffer.

This function will provide the information for converting WCS-specific DMP information to the legacy EnumType record in enable consistent profile enumeration. The defaults will be the same as ICC if this information is not present.

### Per-user/LUA support

The enumeration is specific to current user. Both system wide and current user device associations are considered. For default profile configuration, current user settings override system wide ones.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Icm.h</dt> </dl>     |
| Library<br/>                  | <dl> <dt>Mscms.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Mscms.dll</dt> </dl> |
| Unicode and ANSI names<br/>   | **EnumColorProfilesW** (Unicode) and **EnumColorProfilesA** (ANSI)<br/>        |



## See also

<dl> <dt>

[Basic Color Management Concepts](basic-color-management-concepts.md)
</dt> <dt>

[Functions](functions.md)
</dt> <dt>

[**GetICMProfile**](/windows/win32/Wingdi/nf-wingdi-geticmprofilea?branch=master)
</dt> <dt>

[**ENUMTYPE**](enumtype.md)
</dt> </dl>

 

 





