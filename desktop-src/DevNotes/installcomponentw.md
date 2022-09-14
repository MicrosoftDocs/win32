---
description: Installs an exception package.
ms.assetid: c4c3c01c-9aaf-42cd-a690-13e2113b15b3
title: InstallComponentW function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- InstallComponentW
api_type: 
- DllExport
api_location: 
- Msoobci.dll
---

# InstallComponentW function

Installs an exception package.

## Syntax


```C++
void InstallComponentW(
  _In_           LPCWSTR InfPath,
  _In_opt_ const GUID    *CompGuid,
  _In_           DWORD   Flags,
  _In_opt_       INT     VerMajor,
  _In_opt_       INT     VerMinor,
  _In_opt_       INT     VerBuild,
  _In_opt_       INT     VerQFE,
  _In_opt_       LPCWSTR Name
);
```



## Parameters

<dl> <dt>

*InfPath* \[in\]
</dt> <dd>

The path to the exception INF to process.

</dd> <dt>

*CompGuid* \[in, optional\]
</dt> <dd>

The GUID of the exception component being installed.

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

The flags used to control installation behaviors. This parameter can be a combination of the following values.



| Value                                                                                                                                                                                                                                                               | Meaning                                                                                                                                                     |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="COMP_FLAGS_FORCE"></span><span id="comp_flags_force"></span><dl> <dt>**COMP\_FLAGS\_FORCE**</dt> <dt>0x00000020</dt> </dl>                             | Skips the version check on file replacements.<br/>                                                                                                    |
| <span id="COMP_FLAGS_NEEDS_UNINSTALL"></span><span id="comp_flags_needs_uninstall"></span><dl> <dt>**COMP\_FLAGS\_NEEDS\_UNINSTALL**</dt> <dt></dt> </dl>        | Back up files that are updated to be used by an uninstall of the component.<br/>                                                                      |
| <span id="COMP_FLAGS_NO_OVERWRITE"></span><span id="comp_flags_no_overwrite"></span><dl> <dt>**COMP\_FLAGS\_NO\_OVERWRITE**</dt> <dt></dt> </dl>                 | Skips backing up files if the Exception component version is the same as an installed component. This flag is used in a reinstallation scenario.<br/> |
| <span id="COMP_FLAGS_NOUI"></span><span id="comp_flags_noui"></span><dl> <dt>**COMP\_FLAGS\_NOUI**</dt> <dt>0x00000002</dt> </dl>                                | Suppresses all UI.<br/>                                                                                                                               |
| <span id="COMP_FLAGS_UPDATE_DLLCACHE"></span><span id="comp_flags_update_dllcache"></span><dl> <dt>**COMP\_FLAGS\_UPDATE\_DLLCACHE**</dt> <dt></dt> </dl>        | Forces the DLLCACHE directory to be updated when a system file is updated.<br/>                                                                       |
| <span id="COMP_FLAGS_USE_SVCPACK_CACHE"></span><span id="comp_flags_use_svcpack_cache"></span><dl> <dt>**COMP\_FLAGS\_USE\_SVCPACK\_CACHE**</dt> <dt></dt> </dl> | Uses files cached by a Windows service pack install to supersede files backed up.<br/>                                                                |



 

</dd> <dt>

*VerMajor* \[in, optional\]
</dt> <dd>

The major version of the Exception component.

</dd> <dt>

*VerMinor* \[in, optional\]
</dt> <dd>

The minor version of the Exception component.

</dd> <dt>

*VerBuild* \[in, optional\]
</dt> <dd>

The build version of the Exception component.

</dd> <dt>

*VerQFE* \[in, optional\]
</dt> <dd>

The hotfix revision of the Exception component.

</dd> <dt>

*Name* \[in, optional\]
</dt> <dd>

The descriptive string of the component shown by the Windows File Protection dialog box if the operating system detects that a Windows File Protection protect file is damaged, tampered with, or corrupted.

</dd> </dl>

## Return value

This function returns an **HRESULT** value (S\_OK or a failure code). A failure code can be checked against a value of 0x20000100 to determine whether the failure is because a reboot is required.

## Remarks

Exception packages are Windows system files that are released outside of a full package Windows release and that update operating-system files. Exception packages are authored only by operating-system teams that have been granted authorization to update Windows system files.

To install and uninstall files that are not protected by Windows File Protection, use the functions documented in [General Setup Functions](https://msdn.microsoft.com/library/ms794585.aspx). To install device drivers, venders should use functions documented in [Device Installation Functions](https://msdn.microsoft.com/library/ms792954.aspx) and [PnP Configuration Manager Functions](https://msdn.microsoft.com/library/ms790838.aspx).

This function has no associated import library or header file; you must call it by using the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions.

## Requirements



| Requirement | Value |
|----------------|----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Msoobci.dll</dt> </dl> |



 

 
