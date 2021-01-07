---
description: The UiCreatePatchPackageEx function takes a package creation file (.pcp file) and generates a Windows Installer patch package (.msp package). Calling Msimsp.exe is the recommended method for using Patchwiz.dll.
ms.assetid: 76d9a21d-73bc-41fc-8ed0-7d7d7deff815
title: UiCreatePatchPackageEx (Patchwiz.dll)
ms.topic: article
ms.date: 05/31/2018
---

# UiCreatePatchPackageEx (Patchwiz.dll)

The UiCreatePatchPackageEx function takes a package creation file (.pcp file) and generates a Windows Installer patch package (.msp package). Calling [Msimsp.exe](msimsp-exe.md) is the recommended method for using [Patchwiz.dll](patchwiz-dll.md).

The UiCreatePatchPackageEx function is available beginning with Patchwiz.dll version 4.0 and extends the functionality of the [UiCreatePatchPackage](uicreatepatchpackage-patchwiz-dll-.md) function.

``` syntax
UINT UiCreatePatchPackageEx(
  LPCTSTR szPcpPath,              
  LPCTSTR szPatchPath,            
  LPCTSTR szLogPath,             
  HWND hwndStatus,                
  LPCTSTR szTempFolder,           
  BOOL fRemoveTempFolderContents,
  DWORD dwFlags,
  DWORD dwReserved    
);
```

## Parameters

<dl> <dt>

<span id="szPcpPath"></span><span id="szpcppath"></span><span id="SZPCPPATH"></span>*szPcpPath*
</dt> <dd>

Full path to the patch creation properties file (.pcp file) for this patch.

</dd> <dt>

<span id="szPatchPath"></span><span id="szpatchpath"></span><span id="SZPATCHPATH"></span>*szPatchPath*
</dt> <dd>

Full path to the Windows Installer patch package (.msp file) that is to be created. This parameter may be **NULL** or an empty string but may not be omitted. If it is **NULL** or an empty string, the function uses the value of PatchOutputPath in the [Properties Table (Patchwiz.dll)](properties-table-patchwiz-dll-.md).

</dd> <dt>

<span id="szLogPath"></span><span id="szlogpath"></span><span id="SZLOGPATH"></span>*szLogPath*
</dt> <dd>

Full path to a text log file that will be appended. This parameter may be **NULL** or an empty string but may not be omitted.

</dd> <dt>

<span id="hwndStatus"></span><span id="hwndstatus"></span><span id="HWNDSTATUS"></span>*hwndStatus*
</dt> <dd>

Handle to a window that displays the status text. This parameter may be **NULL** or an empty string but may not be omitted.

</dd> <dt>

<span id="szTempFolder"></span><span id="sztempfolder"></span><span id="SZTEMPFOLDER"></span>*szTempFolder*
</dt> <dd>

Location for temporary files. This parameter may be **NULL** or an empty string but may not be omitted. The user must have sufficient privileges to read and write to this folder. The default location is %TMP%\\~pcw\_tmp.tmp\\.

</dd> <dt>

<span id="fRemoveTempFolderContents"></span><span id="fremovetempfoldercontents"></span><span id="FREMOVETEMPFOLDERCONTENTS"></span>*fRemoveTempFolderContents*
</dt> <dd>

If **TRUE**, remove the temporary folder and all of its contents if present. If **FALSE**, and folder is present, the function fails.

</dd> <dt>

<span id="dwFlags"></span><span id="dwflags"></span><span id="DWFLAGS"></span>*dwFlags*
</dt> <dd>

This parameter can be set to one or a combination of the following values to specify logging or user interface options.



| Flag            | Value       | Meaning                                  |
|-----------------|-------------|------------------------------------------|
| LOGNONE         | 0x00000000  | Write no messages to the log.            |
| LOGINFO         | 0x00000001  | Write informational messages to the log. |
| LOGWARN         | 0x00000002  | Write warnings to the log.               |
| LOGERR          | 0x00000004  | Write error messages to the log.         |
| LOGPERFMESSAGES | 0x00000008  | Write performance messages to the log.   |
| UINONE          | 0x00000000f | Do not display the user interface.       |
| UIALL           | 0x00000010  | Display the user interface.              |



 

</dd> <dt>

<span id="dwReserved"></span><span id="dwreserved"></span><span id="DWRESERVED"></span>*dwReserved*
</dt> <dd>

Reserved. This parameter must be set to zero.

</dd> </dl>

## Return Values

See the table in [Return Values for UiCreatePatchPackage](return-values-for-uicreatepatchpackage.md).

## Remarks

For an example of authoring a .pcp file and using [UiCreatePatchPackage](uicreatepatchpackage-patchwiz-dll-.md) to generate a Windows Installer patch package, see the section [A Small Update Patching Example](a-small-update-patching-example.md).

Creating a patch requires an uncompressed setup image, such as an administrative image or an uncompressed setup image from a CD-ROM. [UiCreatePatchPackage](uicreatepatchpackage-patchwiz-dll-.md) does not generate binary patches for files in cabinets.

 

 



