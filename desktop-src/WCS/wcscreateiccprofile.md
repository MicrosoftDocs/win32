---
title: WcsCreateIccProfile function
description: Converts a WCS profile into an International Color Consortium (ICC) profile.
ms.assetid: 6e9aaad6-a7d4-4685-b694-89d499a411e1
keywords:
- WcsCreateIccProfile function Windows Color System
topic_type:
- apiref
api_name:
- WcsCreateIccProfile
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

# WcsCreateIccProfile function

Converts a WCS profile into an International Color Consortium (ICC) profile.

## Syntax


```C++
HPROFILE WINAPI WcsCreateIccProfile(
  _In_ HPROFILE hWcsProfile,
  _In_ DWORD    dwOptions
);
```



## Parameters

<dl> <dt>

*hWcsProfile* \[in\]
</dt> <dd>

A handle to the WCS color profile that is converted. See Remarks.

</dd> <dt>

*dwOptions* \[in\]
</dt> <dd>

A flag value that specifies the profile conversion options.

 

 

By default, the original WCS profiles used for the conversion are embedded in the output ICC profile in a Microsoft private tag, *WcsProfilesTag* (with signature "MS000". This produces an ICC profile that is compatible with ICC software, yet retains the original WCS profile data available to code designed to parse it.

 

 

The possible values of this parameter are as follows. Any bits not defined in this list are reserved and should be set to zero:



|              |                                                                                                            |
|--------------|------------------------------------------------------------------------------------------------------------|
| WCS\_DEFAULT | Specifies that the new ICC profile contains the original WCS profile in a private WcsProfilesTag.          |
| WCS\_ICCONLY | Specifies that the new ICC profile does not contain either the WcsProfilesTag or the original WCS profile. |



 

</dd> </dl>

## Return value

If this function succeeds, the return value is the handle of the new color profile.

If this function fails, the return value is **NULL**. For extended error information, call [GetLastError](https://msdn.microsoft.com/library/windows/desktop/ms679360).

## Remarks

This function can be used with ASCII or Unicode strings.

The **CloseColorProfile** function should be used to close the returned HPROFILE handle when it is no longer needed.

The DMP, CAMP, and GMMP from the HPROFILE are embedded in a private tag within the created ICC profile.

The ICC profile created using this API will have its profile description tag constructed from the ProfileName elements of the WCS profiles according to the following pattern: "Created by Microsoft WCS from DMP:\[the DMP ProfileName\], CAMP:\[the CAMP ProfileName\], GMMP:\[the GMMP ProfileName\]"

When WCS encounters this ICC profile (via [**OpenColorProfile**](opencolorprofile.md) or [**WcsOpenColorProfile**](wcsopencolorprofile.md) ) it extracts and uses the WCS profile(s) contained in the *WcsProfilesTag*.

The out-of-gamut information in the gamut tags created in WCS uses the perceptual color distance in CIECAM02, which is the mean square root in CIECAM02 Jab space. The distance in legacy ICC profile gamut tags is the mean square root in CIELAB space. It is recommended that you use the CIECAM02 space when it is available, to provide more perceptually accurate distance metrics.

WCS extracts and uses the original WCS profile by means of an XML profile explicitly associated with a device, or an ICC profile that has a*WcsProfilesTag*.

The *WcsProfilesTag* is a Microsoft private ICC profile tag used in profiles created by **WcsCreateIccProfile** to contain the WCS profiles input to **WcsCreateIccProfile**. This tag conforms to ICC profile requirements for profile tags. The non-XML components of the tag must be in "Big-Endian" byte ordering, which is standard for ICC profiles. Further, the tag data must be aligned on a 4-byte boundary (measured from the start of the ICC profile). The structure of the tag is defined by the **WcsProfilesTagType** below. Note that the XML components of the tag, the WCS profiles contained in the WcsProfileTag, are left in their native byte ordering, which may be either little-endian or big-endian since XML parsers correctly process either.

The WcsProfilesTag signature is "MS00". This is the tag signature that will appear in the ICC profiles tag table for the WcsProfilesTag.

The **WcsProfilesTagType Structure** has the following structure:



| Byte Offset | Content                                                                                                                                 |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| 0-3         | The MS10 type signature.                                                                                                                |
| 4-7         | Reserved, must be set to 0 (ICC tradition).                                                                                             |
| 8-11        | Byte offset from the beginning of the tag to the CDMP data.                                                                             |
| 12-15       | Size of the CDMP data in bytes.                                                                                                         |
| 16-19       | Byte offset from the beginning of the tag to the CAMP data.                                                                             |
| 20-23       | Size of the CAMP data in bytes.                                                                                                         |
| 24-27       | Byte offset from the beginning of the tag to the GMMP data.                                                                             |
| 28-31       | Byte offset from the beginning of the tag to the GMMP data.                                                                             |
| 31-n        | A sequence of (element size -32) bytes \[where element size is the tag size recorded in the ICC profile tag table entry for this tag.\] |



 

These are the WCS XML profiles that were used by **WcsCreateIccProfile** to create this ICC profile. The WCS profiles are ordered: the DMP (required) first, followed by the CAMP (if present), followed by the GMMP (if present).

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
</dt> </dl>

 

 





