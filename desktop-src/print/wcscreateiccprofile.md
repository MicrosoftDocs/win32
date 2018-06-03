---
Description: The WcsCreateIccProfile function converts a WCS profile into an ICC profile.
ms.assetid: fbe37d6c-9b91-46d8-9d29-1de3ef542c19
title: WcsCreateIccProfile function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WcsCreateIccProfile function

The `WcsCreateIccProfile` function converts a WCS profile into an ICC profile.

## Syntax


```C++
HPROFILE WcsCreateIccProfile(
  _In_ HPROFILE hWcsProfile,
  _In_ DWORD    dwOptions
);
```



## Parameters

<dl> <dt>

*hWcsProfile* \[in\]
</dt> <dd>

A handle to the WCS color profile to transform. See Remarks.

</dd> <dt>

*dwOptions* \[in\]
</dt> <dd>

A flag value that specifies the profile conversion options. This parameter must take the following value:

<dl> <dt>

<span id="PREFER_WCS_PROFILES"></span><span id="prefer_wcs_profiles"></span>PREFER\_WCS\_PROFILES
</dt> <dd>

Specifies that when WCS encounters an ICC profile, it should extract and use the WCS profiles that are contained in **WcsProfilesTag**.

</dd> </dl> </dd> </dl>

## 

If this function succeeds, the return value is the handle of the color profile that is created.

If this function fails, the return value is **NULL**. For extended error information, call **GetLastError** (described in the Microsoft Windows SDK documentation).

## Remarks

The WCS profile that is to be translated must be a Device Model Profile (DMP) in combination with a Color Appearance Model Profile (CAMP) and a Gamut Map Model Profile (GMMP).

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Version<br/>         | Included in Windows Vista and later.<br/>                                                                                         |
| Header<br/>          | <dl> <dt>Icm.h</dt> </dl>                                                        |
| Library<br/>         | <dl> <dt>Mscms.lib</dt> </dl>                                                    |
| DLL<br/>             | <dl> <dt>Mscms.dll</dt> </dl>                                                    |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20WcsCreateIccProfile%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




