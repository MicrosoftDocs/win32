---
Description: The WcsOpenColorProfile function creates a handle to a specified color profile.
ms.assetid: ecc573e6-c83c-4cf2-9dad-c3c75d9578eb
title: WcsOpenColorProfileA function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WcsOpenColorProfileA function

The `WcsOpenColorProfile` function creates a handle to a specified color profile.

## Syntax


```C++
HPROFILE WINAPI WcsOpenColorProfile(
  _In_     PROFILE pDMPProfile,
  _In_opt_ PROFILE pCAMPProfile,
  _In_opt_ PROFILE pGMMPProfile,
  _In_     DWORD   dwDesiredAccess,
  _In_     DWORD   dwShareMode,
  _In_     DWORD   dwCreationMode,
  _In_     DWORD   dwFlags
);
```



## Parameters

<dl> <dt>

*pDMPProfile* \[in\]
</dt> <dd>

A pointer to a profile structure that specifies a WCS device model profile (DMP). The *pDMPProfile* pointer can be freed as soon as the handle is created.

</dd> <dt>

*pCAMPProfile* \[in, optional\]
</dt> <dd>

A pointer to a profile structure that specifies a WCS color appearance model profile (CAMP). The *pCAMPProfile* pointer can be freed as soon as the handle is created. If **NULL**, the standard default CAMP is used, and the current user setting, WCS\_PROFILE\_MANAGEMENT\_SCOPE\_CURRENT\_USER, is used while querying the default CAMP.

</dd> <dt>

*pGMMPProfile* \[in, optional\]
</dt> <dd>

A pointer to a profile structure that specifies a WCS gamut map model profile (GMMP). The *pGMMPProfile* pointer can be freed as soon as the handle is created. If **NULL**, the default GMMP for the default rendering intent is used, and the current user setting, WCS\_PROFILE\_MANAGEMENT\_SCOPE\_CURRENT\_USER, is used while querying the default GMMP. For a description of rendering intents, see [Rendering Intents](http://go.microsoft.com/fwlink/p/?linkid=52269) in the Microsoft Windows SDK documentation.

</dd> <dt>

*dwDesiredAccess* \[in\]
</dt> <dd>

A flag value that specifies how to access the given color profile. This parameter must take one of the following values:

<dl> <dt>

<span id="PROFILE_READ"></span><span id="profile_read"></span>PROFILE\_READ
</dt> <dd>

Specifies that the color profile will be opened for read-only access.

</dd> <dt>

<span id="PROFILE_READWRITE"></span><span id="profile_readwrite"></span>PROFILE\_READWRITE
</dt> <dd>

Specifies that the color profile will be opened for both read and write access. This flag value is ignored when a WCS profile is opened.

</dd> </dl> </dd> <dt>

*dwShareMode* \[in\]
</dt> <dd>

A flag value that specifies actions to take while opening a color profile if it is contained in a file. This parameter must take one of the following values, which are defined in winnt.h:

<dl> <dt>

<span id="FILE_SHARE_READ"></span><span id="file_share_read"></span>FILE\_SHARE\_READ
</dt> <dd>

Specifies that other open operations can be performed on the profile for read access.

</dd> <dt>

<span id="FILE_SHARE_WRITE"></span><span id="file_share_write"></span>FILE\_SHARE\_WRITE
</dt> <dd>

Specifies that other open operations can be performed on the profile for write access. This flag value is ignored when a WCS profile is opened.

</dd> </dl> </dd> <dt>

*dwCreationMode* \[in\]
</dt> <dd>

A flag value that specifies actions to take while opening a color profile if it is contained in a file. This parameter must take one of the following values, which are defined in winbase.h:

<dl> <dt>

<span id="CREATE_NEW"></span><span id="create_new"></span>CREATE\_NEW
</dt> <dd>

Specifies that a new profile is to be created. The function fails if the profile already exists.

</dd> <dt>

<span id="CREATE_ALWAYS"></span><span id="create_always"></span>CREATE\_ALWAYS
</dt> <dd>

Specifies that a new profile is to be created. If a profile already exists, it is overwritten.

</dd> <dt>

<span id="OPEN_EXISTING"></span><span id="open_existing"></span>OPEN\_EXISTING
</dt> <dd>

Specifies that the profile is to be opened. The function fails if the profile does not exist.

</dd> <dt>

<span id="OPEN_ALWAYS"></span><span id="open_always"></span>OPEN\_ALWAYS
</dt> <dd>

Specifies that the profile is to be opened if an International Color Consortium (ICC) file exists. If an ICC profile does not exist, WCS creates a new ICC profile. The function will fail for WCS profiles if this flag is set and a WCS profile does not exist.

</dd> <dt>

<span id="TRUNCATE_EXISTING"></span><span id="truncate_existing"></span>TRUNCATE\_EXISTING
</dt> <dd>

Specifies that the profile is to be opened and truncated to zero bytes. The function fails if the profile does not exist.

</dd> </dl> </dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

A flag value that specifies whether to use the embedded WCS profile. This parameter has no effect unless *pCDMProfile* specifies an ICC profile that contains an embedded WCS profile.This parameter takes one of the following values:



|                                    |                                                                                                                     |
|------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| 0                                  | Specifies that the embedded WCS profile will be used and the ICC profile specfied by pCDMPProfile will be ignored.  |
| DONT\_USE\_EMBEDDED\_WCS\_PROFILES | Specifies that the ICC profile specified by pCDMPProfile will be used and the embedded WCS profile will be ignored. |



 

</dd> </dl>

## 

If this function succeeds, the return value is the handle of the color profile that is opened.

If this function fails, the return value is **NULL**. For extended error information, call **GetLastError** (described in the Microsoft Windows SDK documentation).

## Remarks

The handle returned by this function can be used in other color profile management functions.

The compiler setting also determinDeclared in Icm.hes the function version. If Unicode is defined, the function call resolves to **WcsOpenColorProfileW**. Otherwise, the function call resolves to **WcsOpenColorProfileA** because ANSI strings are being used.

If the color profile data is not specified using a file name, the *dwShareMode* and *dwCreationMode* values are ignored.

This function initially attempts to open the profile as an ICC profile. Even if a WCS profile is provided, the PROFILE\_READWRITE and FILE\_SHARE\_WRITE flags are not ignored. However, if the provided profile is not an ICC profile (and a new ICC profile is not being created), these flag values are ignored.

The *dwCreationMode* flags CREATE\_NEW, CREATE\_ALWAYS, and TRUNCATE\_EXISTING will always return an empty handle to the ICC color profile.

Once the handle to the color profile is created, any information used to create that handle can be deleted.

Use the [CloseColorProfile](http://go.microsoft.com/fwlink/p/?linkid=52323) function to close an object handle returned by `WcsOpenColorProfile`.

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Version<br/>         | Included in Windows Vista and later.<br/>                                                                                         |
| Header<br/>          | <dl> <dt>Icm.h</dt> </dl>                                                        |
| Library<br/>         | <dl> <dt>Mscms.lib</dt> </dl>                                                    |



## See also

<dl> <dt>

[CloseColorProfile](http://go.microsoft.com/fwlink/p/?linkid=52323)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20WcsOpenColorProfileA%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





