---
description: Removes an exception package.
ms.assetid: d590d0f8-c9b2-4973-999b-99bbf94d4928
title: UninstallComponent function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- UninstallComponent
api_type: 
- DllExport
api_location: 
- Msoobci.dll
---

# UninstallComponent function

Removes an exception package.

## Syntax


```C++
void UninstallComponent(
  _In_opt_ const GUID  *CompGuid,
  _In_           DWORD Flags,
  _In_opt_       INT   VerMajor,
  _In_opt_       INT   VerMinor,
  _In_opt_       INT   VerBuild,
  _In_opt_       INT   VerQFE
);
```



## Parameters

<dl> <dt>

*CompGuid* \[in, optional\]
</dt> <dd>

The GUID of the exception component being uninstalled.

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

The flags used to control installation behaviors. This parameter can be a combination of the following values.



| Value                                                                                                                                                                                                         | Meaning                                                                                      |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| <span id="COMP_FLAGS_NOUI"></span><span id="comp_flags_noui"></span><dl> <dt>**COMP\_FLAGS\_NOUI**</dt> </dl>                                          | Suppresses all UI.<br/>                                                                |
| <span id="COMP_FLAGS_UPDATE_DLLCACHE"></span><span id="comp_flags_update_dllcache"></span><dl> <dt>**COMP\_FLAGS\_UPDATE\_DLLCACHE**</dt> </dl>        | Forces the DLLCACHE directory to be updated when a system file is updated.<br/>        |
| <span id="COMP_FLAGS_USE_SVCPACK_CACHE"></span><span id="comp_flags_use_svcpack_cache"></span><dl> <dt>**COMP\_FLAGS\_USE\_SVCPACK\_CACHE**</dt> </dl> | Uses files cached by a Windows service pack install to supersede files backed up.<br/> |



 

</dd> <dt>

*VerMajor* \[in, optional\]
</dt> <dd>

The major version of the Exception component to be uninstalled.

</dd> <dt>

*VerMinor* \[in, optional\]
</dt> <dd>

The minor version of the Exception component to be uninstalled.

</dd> <dt>

*VerBuild* \[in, optional\]
</dt> <dd>

The build version of the Exception component to be uninstalled.

</dd> <dt>

*VerQFE* \[in, optional\]
</dt> <dd>

The hotfix revision of the Exception component to be uninstalled.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

Exception packages are Windows system files that are released outside of a full package Windows release and that update operating-system files. Exception packages are authored only by operating-system teams that have been granted authorization to update Windows system files.

To install and uninstall files that are not protected by Windows File Protection, use the functions documented in [General Setup Functions](https://msdn.microsoft.com/library/ms794585.aspx). To install device drivers, venders should use functions documented in [Device Installation Functions](https://msdn.microsoft.com/library/ms792954.aspx) and [PnP Configuration Manager Functions](https://msdn.microsoft.com/library/ms790838.aspx).

This function has no associated import library or header file; you must call it by using the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions.

## Requirements



| Requirement | Value |
|----------------|----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Msoobci.dll</dt> </dl> |



## See also

<dl> <dt>


</dt> <dt>

[**InstallComponentW**](installcomponentw.md)
</dt> </dl>

 

 
