---
title: CreateDeviceLinkProfile function
description: The CreateDeviceLinkProfile function creates an International Color Consortium (ICC) device link profile from a set of color profiles, using the specified intents.
ms.assetid: 54f46d2c-ddcb-4597-9816-172e507a7fa2
keywords:
- CreateDeviceLinkProfile function Windows Color System
topic_type:
- apiref
api_name:
- CreateDeviceLinkProfile
- CreateColorTransformA
- CreateColorTransformW
api_location:
- Mscms.dll
api_type:
- DllExport
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CreateDeviceLinkProfile function

The [**CreateDeviceLinkProfile**](/windows/desktop/api/Wingdi/) function creates an International Color Consortium (ICC) *device link profile* from a set of color profiles, using the specified intents.

## Syntax


```C++
BOOL WINAPI CreateDeviceLinkProfile(
   PHPROFILE pahProfiles,
   DWORD     nProfiles,
   PDWORD    padwIntent,
   DWORD     nIntents,
   DWORD     dwFlags,
   PBYTE     pProfileData,
   DWORD     indexPreferredCMM
);
```



## Parameters

<dl> <dt>

*pahProfiles* 
</dt> <dd>

Pointer to an array of handles of the color profiles to be used. The function determines whether the HPROFILEs contain ICC profile information and, if so, it processes them appropriately.

</dd> <dt>

*nProfiles* 
</dt> <dd>

Specifies the number of profiles in the array pointed to by *pahProfiles*.

</dd> <dt>

*padwIntent* 
</dt> <dd>

Pointer to an array of **DWORDS** containing the intents to be used. See [Rendering Intents](rendering-intents.md).

</dd> <dt>

*nIntents* 
</dt> <dd>

The number of intents in the array pointed to by *padwIntent*.

</dd> <dt>

*dwFlags* 
</dt> <dd>

Specifies flags to used control creation of the transform. For details, see [CMM Transform Creation Flags](cmm-transform-creation-flags.md).

</dd> <dt>

*pProfileData* 
</dt> <dd>

Pointer to a pointer to a buffer. If successful, this function allocates the buffer, places its address in *\*pProfileData*, and fills it with a device link profile. If the function succeeds, the calling application must free the buffer after it is no longer needed.

</dd> <dt>

*indexPreferredCMM* 
</dt> <dd>

Specifies the one-based index of the color profile that indicates what color management module (CMM) to use. The application developer may allow Windows to choose the CMM by setting this parameter to INDEX\_DONT\_CARE. See [Using Color Management Modules (CMM)](using-color-management-modules--cmm.md).

</dd> </dl>

## Return value

If this function succeeds, the return value is a nonzero value.

If this function fails, the return value is zero. For extended error information, call GetLastError.

## Remarks

For HPROFILEs that contain WCS profile information, the HPROFILEs are converted into valid ICC profile handles and then these ICC profile handles are used in creating the device link profile.

The first and the last profiles in the array must be device profiles. The other profiles can be color space or abstract profiles.

Each profile's output color space must be the next profile's input color space.

The calling application must free the buffer allocated by this function and pointed to by the *pProfileData* parameter. The [**GlobalFree**](https://msdn.microsoft.com/library/windows/desktop/aa366579) function should be used to free the buffer.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Icm.h</dt> </dl>     |
| Library<br/>                  | <dl> <dt>Mscms.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Mscms.dll</dt> </dl> |
| Unicode and ANSI names<br/>   | **CreateColorTransformW** (Unicode) and **CreateColorTransformA** (ANSI)<br/>  |



## See also

<dl> <dt>

[Basic Color Management Concepts](basic-color-management-concepts.md)
</dt> <dt>

[Functions](functions.md)
</dt> <dt>

[**GlobalFree**](https://msdn.microsoft.com/library/windows/desktop/aa366579)
</dt> </dl>

 

 





