---
description: The system file checker utility, Sfc.exe, allows administrators to scan all protected resources to verify their versions.
ms.assetid: 72f69ad2-15d9-4191-a8aa-4c23a2392006
title: System File Checker
ms.topic: article
ms.date: 05/31/2018
---

# System File Checker

The system file checker utility, Sfc.exe, allows administrators to scan all protected resources to verify their versions.

Files critical to restart Windows that do not match the expected Windows version may be replaced with the correct versions. If a file is repaired, the corresponding registry data is also repaired. Protected files not critical to restart Windows are not repaired.

## Syntax

The following is the command-line syntax for Sfc.

**SFC options \[=full file path\]**

## Options

<dl> <dt>

<span id="_CACHESIZE_x"></span><span id="_cachesize_x"></span><span id="_CACHESIZE_X"></span>/CACHESIZE=*x*
</dt> <dd>

This value is not supported.

**Windows Server 2003 and Windows XP:** Sets the file cache size. The default size of the cache is 0x32 (50 MB).

</dd> <dt>

<span id="_CANCEL"></span><span id="_cancel"></span>/CANCEL
</dt> <dd>

This value is not supported.

</dd> <dt>

<span id="_ENABLE"></span><span id="_enable"></span>/ENABLE
</dt> <dd>

This value is not supported.

</dd> <dt>

<span id="_FILESONLY"></span><span id="_filesonly"></span>/FILESONLY
</dt> <dd>

Verify or repair only files. Do not verify or repair registry keys.

**Windows XP:** Not supported.

</dd> <dt>

<span id="_OFFBOOTDIR"></span><span id="_offbootdir"></span>/OFFBOOTDIR
</dt> <dd>

Use this option for offline repairs. Specify the location of the offline boot directory.

**Windows XP:** Not supported.

</dd> <dt>

<span id="_OFFWINDIR"></span><span id="_offwindir"></span>/OFFWINDIR
</dt> <dd>

Use this option for offline repairs. Specify the location of the offline Windows directory.

**Windows XP:** Not supported.

</dd> <dt>

<span id="_PURGECACHE"></span><span id="_purgecache"></span>/PURGECACHE
</dt> <dd>

This value is not supported.

**Windows Server 2003 and Windows XP:** Empties the file cache and scans all protected system files.

</dd> <dt>

<span id="_QUIET"></span><span id="_quiet"></span>/QUIET
</dt> <dd>

This value is not supported.

</dd> <dt>

<span id="_REVERT"></span><span id="_revert"></span>/REVERT
</dt> <dd>

Return to default settings.

**Windows Server 2008 and Windows Vista:** Not supported.

</dd> <dt>

<span id="_SCANBOOT"></span><span id="_scanboot"></span>/SCANBOOT
</dt> <dd>

This value is not supported.

**Windows Server 2003 and Windows XP:** Scans all protected system files at every boot.

</dd> <dt>

<span id="_SCANFILE"></span><span id="_scanfile"></span>/SCANFILE
</dt> <dd>

Scans and repairs the file located at the specified full path.

**Windows XP:** Not supported.

</dd> <dt>

<span id="_SCANNOW"></span><span id="_scannow"></span>/SCANNOW
</dt> <dd>

Scans all protected system files immediately.

</dd> <dt>

<span id="_SCANONCE"></span><span id="_scanonce"></span>/SCANONCE
</dt> <dd>

This value is not supported.

**Windows Server 2003 and Windows XP:** Scans all protected system files at the next boot.

</dd> <dt>

<span id="_VERIFYFILE"></span><span id="_verifyfile"></span>/VERIFYFILE
</dt> <dd>

Verifies the file at the specified full path. This option does not repair the file.

**Windows XP:** Not supported.

</dd> <dt>

<span id="_VERIFYONLY"></span><span id="_verifyonly"></span>/VERIFYONLY
</dt> <dd>

Scans all protected system files but does not repair files.

**Windows XP:** Not supported.

</dd> </dl>

Sfc sets the following registry value:

 = HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon\\SFCScan

For more information, see [WFP Registry Values](wfp-registry-values.md).

## Remarks

On Windows Vista only, you can set the **WINDOWS\_TRACING\_LOGFILE** environment variable to the location of a valid directory to receive a log file.

## Examples

The following sample command lines are examples of sfc.exe syntax.

**sfc /SCANNOW**

**sfc /VERIFYFILE=c:\\windows\\system32\\kernel32.dll**

**sfc /SCANFILE=d:\\windows\\system32\\kernel32.dll /OFFBOOTDIR=d:\\ /OFFWINDIR=d:\\windows**

**sfc /VERIFYONLY /FILESONLY**

 

 



