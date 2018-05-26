---
title: IPCF\_FILE\_BASIC\_INFORMATION structure
description: Describes the basic information about a protected file.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: B514EBF7-B932-47DC-B08C-F6CE1C3DB42F
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- IPCF_FILE_BASIC_INFORMATION structure Active Directory Rights Management Services SDK 2.0
- IPCF_FILE_BASC_INFORMATION structure Active Directory Rights Management Services SDK 2.0
- PIPCF_FILE_BASC_INFORMATION structure pointer Active Directory Rights Management Services SDK 2.0
topic_type:
- apiref
api_name:
- IPCF_FILE_BASC_INFORMATION
api_location:
- Ipcfile.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
---

# IPCF\_FILE\_BASIC\_INFORMATION structure

Describes the basic information about a protected file. For more information on protected file, see [Supported File Formats](supported-file-formats.md)

## Syntax


```C++
typedef struct _IPCF_FILE_BASC_INFORMATION {
  DWORD               cbSize;
  LPCWSTR             wszDecryptedFileName;
  DWORD64             qwDecryptedFileSize;
  FILETIME            ftDateModified;
  IPC_NAME_VALUE_LIST pAppSpecificProperties;
} IPCF_FILE_BASC_INFORMATION, *PIPCF_FILE_BASC_INFORMATION;
```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

This is the size of this structure and needs to be initialized to

sizeof(**IPCF\_FILE\_BASIC\_INFORMATION**)

</dd> <dt>

**wszDecryptedFileName**
</dt> <dd>

Name of the decrypted file. Can be optionally stored in the metadata section.

</dd> <dt>

**qwDecryptedFileSize**
</dt> <dd>

Size of the decrypted file, in bytes.

</dd> <dt>

**ftDateModified**
</dt> <dd>

The date modified on the file.

</dd> <dt>

**pAppSpecificProperties**
</dt> <dd>

Custom application specific properties as name-value pairs.

</dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP2<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                         |
| Header<br/>                   | <dl> <dt>Ipcfile.h (include Msipc.h)</dt> </dl> |



## See also

<dl> <dt>

[Supported File Formats](supported-file-formats.md)
</dt> <dt>

[Structures](msipc-structures.md)
</dt> </dl>

 

 





