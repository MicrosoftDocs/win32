---
title: IPCF\_PROTECTED\_FILE\_HEADER structure
description: Describes the protected file header content.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: EB051D1D-B6C3-4026-AAD6-3047086E699D
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- IPCF_PROTECTED_FILE_HEADER structure Active Directory Rights Management Services SDK 2.0
- _IPCF_PROTECTED_FILE_HEADER structure Active Directory Rights Management Services SDK 2.0
topic_type:
- apiref
api_name:
- _IPCF_PROTECTED_FILE_HEADER
api_location:
- Ipcfile.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# IPCF\_PROTECTED\_FILE\_HEADER structure

Describes the protected file header content. For more information on protected file, see [Supported File Formats](supported-file-formats.md).

## Syntax


```C++
typedef struct _IPC_PROTECTED_FILE_HEADER {
  BYTE  magic[6];
  DWORD dwMajor;
  DWORD dwMinor;
  BYTE  rgbUndocumented[278];
  DWORD dwEncryptedContentsOffset;
} _IPCF_PROTECTED_FILE_HEADER, *IPCF_PROTECTED_FILE_HEADER;
```



## Members

<dl> <dt>

**magic\[6\]**
</dt> <dd>

The bytes at the start of the protected file which are used to recognize the file format. If the file is a protected file, these must be { 0x2E, 0x70, 0x66, 0x69, 0x6C, 0x65 }.

</dd> <dt>

**dwMajor**
</dt> <dd>

Major version of the protected file.

</dd> <dt>

**dwMinor**
</dt> <dd>

Minor version of the protected file.

</dd> <dt>

**rgbUndocumented\[278\]**
</dt> <dd>

Undocumented data in the protected file header.

</dd> <dt>

**dwEncryptedContentsOffset**
</dt> <dd>

The offset in the file where the encrypted payload of the protected file starts.

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

 

 





