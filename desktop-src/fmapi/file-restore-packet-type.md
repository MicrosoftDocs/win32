---
title: FILE\_RESTORE\_PACKET\_TYPE enumeration
description: Defines the message types that can be sent by the RestoreFile function.
ms.assetid: 86ae4d0e-a417-4caf-aa88-0d40c91da97b
keywords:
- FILE_RESTORE_PACKET_TYPE enumeration Files
- FILE_RESTORE_PACKET_TYPE, PFILE_RESTORE_PACKET_TYPE enumeration Files
topic_type:
- apiref
api_name:
- FILE_RESTORE_PACKET_TYPE, PFILE_RESTORE_PACKET_TYPE
api_type:
- NA
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FILE\_RESTORE\_PACKET\_TYPE enumeration

Defines the message types that can be sent by the [**RestoreFile**](restorefile.md) function.

> [!Note]  
> FMAPI can only be used in the Windows Preinstallation Environment (WinPE) for Windows Vista, Windows Server 2008, and later. Applications that use FMAPI must license WinPE.

 

## Syntax


```C++
typedef enum  { 
  FileRestoreProgressInfo  = 100,
  FileRestoreFinished      = 101
} FILE_RESTORE_PACKET_TYPE, *PFILE_RESTORE_PACKET_TYPE;
```



## Constants

<dl> <dt>

<span id="FileRestoreProgressInfo"></span><span id="filerestoreprogressinfo"></span><span id="FILERESTOREPROGRESSINFO"></span>**FileRestoreProgressInfo**
</dt> <dd>

The progress of the restoration process is reported by the callback function. The structure of the progress information is defined in [**FILE\_RESTORE\_PROGRESS\_INFORMATION**](file-restore-progress-information.md).

</dd> <dt>

<span id="FileRestoreFinished"></span><span id="filerestorefinished"></span><span id="FILERESTOREFINISHED"></span>**FileRestoreFinished**
</dt> <dd>

The final status of the restoration process is reported by the callback function. The structure of the status information is defined in [**FILE\_RESTORE\_FINISHED\_INFORMATION**](file-restore-finished-information.md).

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

[**RestoreFile**](restorefile.md)
</dt> </dl>

 

 





