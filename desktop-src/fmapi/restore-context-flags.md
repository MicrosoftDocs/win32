---
title: RESTORE\_CONTEXT\_FLAGS enumeration
description: Defines values that are used in the CreateFileRestoreContext function to specify the file restore context for the volume or for the physical drive. These enumeration values are used in the Flags argument to the CreateFileRestoreContext function.
ms.assetid: 9436bed9-c88d-4ad7-8e7a-6673d177901a
keywords:
- RESTORE_CONTEXT_FLAGS enumeration
topic_type:
- apiref
api_name:
- RESTORE_CONTEXT_FLAGS
api_type:
- NA
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# RESTORE\_CONTEXT\_FLAGS enumeration

Defines values that are used in the [**CreateFileRestoreContext**](createfilerestorecontext.md) function to specify the file restore context for the volume or for the physical drive. These enumeration values are used in the *Flags* argument to the **CreateFileRestoreContext** function.

> [!Note]  
> FMAPI can only be used in the Windows Preinstallation Environment (WinPE) for Windows Vista, Windows Server 2008, and later. Applications that use FMAPI must license WinPE.

 

## Syntax


```C++
typedef enum  { 
  ContextFlagVolume                  = 0x00000001,
  ContextFlagDisk                    = 0x00000002,
  FlagScanRemovedFiles               = 0x00000004,
  FlagScanRegularFiles               = 0x00000008,
  FlagScanIncludeRemovedDirectories  = 0x00000010
} RESTORE_CONTEXT_FLAGS;
```



## Constants

<dl> <dt>

<span id="ContextFlagVolume"></span><span id="contextflagvolume"></span><span id="CONTEXTFLAGVOLUME"></span>**ContextFlagVolume**
</dt> <dd>

Indicates that the string in the *Volume* parameter to the [**CreateFileRestoreContext**](createfilerestorecontext.md) function represents a path of a volume

This flag cannot be combined with **ContextFlagDisk.**

.

</dd> <dt>

<span id="ContextFlagDisk"></span><span id="contextflagdisk"></span><span id="CONTEXTFLAGDISK"></span>**ContextFlagDisk**
</dt> <dd>

Indicates that the string in the *Volume* parameter to the [**CreateFileRestoreContext**](createfilerestorecontext.md) function represents a path of a physical disk.

This flag cannot be combined with **ContextFlagVolume.**

</dd> <dt>

<span id="FlagScanRemovedFiles"></span><span id="flagscanremovedfiles"></span><span id="FLAGSCANREMOVEDFILES"></span>**FlagScanRemovedFiles**
</dt> <dd>

Indicates that the [**ScanRestorableFiles**](scanrestorablefiles.md) function will search for files that have been deleted.

</dd> <dt>

<span id="FlagScanRegularFiles"></span><span id="flagscanregularfiles"></span><span id="FLAGSCANREGULARFILES"></span>**FlagScanRegularFiles**
</dt> <dd>

Indicates that the that [**ScanRestorableFiles**](scanrestorablefiles.md) function will search for files that have not been deleted (also called "regular files").

</dd> <dt>

<span id="FlagScanIncludeRemovedDirectories"></span><span id="flagscanincluderemoveddirectories"></span><span id="FLAGSCANINCLUDEREMOVEDDIRECTORIES"></span>**FlagScanIncludeRemovedDirectories**
</dt> <dd>

Indicates that the that the [**ScanRestorableFiles**](scanrestorablefiles.md) function will search for directories that have been deleted. This flag is only used with the **FlagScanRemovedFiles** flag.

</dd> </dl>

## Remarks

Note that there is no associated header file for this enumeration.

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**CreateFileRestoreContext**](createfilerestorecontext.md)
</dt> </dl>

 

 





