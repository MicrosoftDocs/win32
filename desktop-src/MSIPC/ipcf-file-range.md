---
title: IPCF\_FILE\_RANGE structure
description: Describes the logical file range in a protected file.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 7A1CC338-FB40-4D63-9556-966454745791
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- IPCF_FILE_RANGE structure Active Directory Rights Management Services SDK 2.0
topic_type:
- apiref
api_name:
- IPCF_FILE_RANGE
api_location:
- Ipcfile.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
---

# IPCF\_FILE\_RANGE structure

Describes the logical file range in a protected file. For more information on protected file, see [Supported File Formats](supported-file-formats.md).

## Syntax


```C++
typedef struct _IPCF_FILE_RANGE {
  DWORD64 qwOffset;
  DWORD64 qwSize;
} IPCF_FILE_RANGE, *IPCF_FILE_RANGE;
```



## Members

<dl> <dt>

**qwOffset**
</dt> <dd>

Logical offset of the data of interest.

</dd> <dt>

**qwSize**
</dt> <dd>

Size of the data of interest.

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

 

 





