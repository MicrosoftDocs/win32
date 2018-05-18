---
title: File Management Constants
description: File Management contains the following constants.
ms.assetid: '4c81dded-3864-4fc8-b06e-0d13fa04f63a'
topic_type:
- apiref
api_name:
- FILE_RESTORE_MAJOR_VERSION_1
- FILE_RESTORE_MINOR_VERSION_1
- FILE_RESTORE_VERSION_1
- FILE_RESTORE_MAJOR_VERSION_2
- FILE_RESTORE_MINOR_VERSION_2
- FILE_RESTORE_VERSION_2
- FILE_RESTORE_VERSION_CURRENT
- VOLUME_INFO_ENCRYPTED
- VOLUME_INFO_LOCKED
api_type:
- NA
---

# File Management Constants

File Management contains the following constants.

> [!Note]  
> FMAPI can only be used in the Windows Preinstallation Environment (WinPE) for Windows Vista, Windows Server 2008, and later. Applications that use FMAPI must license WinPE.

 

<dl> <dt>

<span id="FILE_RESTORE_MAJOR_VERSION_1"></span><span id="file_restore_major_version_1"></span>**FILE\_RESTORE\_MAJOR\_VERSION\_1**
</dt> <dd> <dl> <dt>

0x0001
</dt> <dt>



Used to define the major version number of the file restore functions.


</dt> </dl> </dd> <dt>

<span id="FILE_RESTORE_MINOR_VERSION_1"></span><span id="file_restore_minor_version_1"></span>**FILE\_RESTORE\_MINOR\_VERSION\_1**
</dt> <dd> <dl> <dt>

0x0001
</dt> <dt>



Used to define the minor version number of the file restore functions.


</dt> </dl> </dd> <dt>

<span id="FILE_RESTORE_VERSION_1"></span><span id="file_restore_version_1"></span>**FILE\_RESTORE\_VERSION\_1**
</dt> <dd> <dl> <dt>

((FILE\_RESTORE\_MAJOR\_VERSION\_1 &lt;&lt; 16) \| FILE\_RESTORE\_MINOR\_VERSION\_1)
</dt> <dt>



Used to define the complete version number of the file restore functions.


</dt> </dl> </dd> <dt>

<span id="FILE_RESTORE_MAJOR_VERSION_2"></span><span id="file_restore_major_version_2"></span>**FILE\_RESTORE\_MAJOR\_VERSION\_2**
</dt> <dd> <dl> <dt>

0x0002
</dt> <dt>



Used to define the major version number of the file restore functions.


</dt> </dl> </dd> <dt>

<span id="FILE_RESTORE_MINOR_VERSION_2"></span><span id="file_restore_minor_version_2"></span>**FILE\_RESTORE\_MINOR\_VERSION\_2**
</dt> <dd> <dl> <dt>

0x0000
</dt> <dt>



Used to define the minor version number of the file restore functions.


</dt> </dl> </dd> <dt>

<span id="FILE_RESTORE_VERSION_2"></span><span id="file_restore_version_2"></span>**FILE\_RESTORE\_VERSION\_2**
</dt> <dd> <dl> <dt>

((FILE\_RESTORE\_MAJOR\_VERSION\_2 &lt;&lt; 16) \| FILE\_RESTORE\_MINOR\_VERSION\_2)
</dt> <dt>



Used to define the complete version number of the file restore functions.


</dt> </dl> </dd> <dt>

<span id="FILE_RESTORE_VERSION_CURRENT"></span><span id="file_restore_version_current"></span>**FILE\_RESTORE\_VERSION\_CURRENT**
</dt> <dd> <dl> <dt>

FILE\_RESTORE\_VERSION\_2
</dt> <dt>



Used to define the current version number for file restore functions.


</dt> </dl> </dd> <dt>

<span id="VOLUME_INFO_ENCRYPTED"></span><span id="volume_info_encrypted"></span>**VOLUME\_INFO\_ENCRYPTED**
</dt> <dd> <dl> <dt>

0x0001
</dt> <dt>



Used to define the encrypted status of a volume.


</dt> </dl> </dd> <dt>

<span id="VOLUME_INFO_LOCKED"></span><span id="volume_info_locked"></span>**VOLUME\_INFO\_LOCKED**
</dt> <dd> <dl> <dt>

0x0002
</dt> <dt>



Used to define the locked status of a volume.


</dt> </dl> </dd> </dl>

## Remarks

Note that there is no associated header file for these constants.

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





