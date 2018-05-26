---
title: Data types
description: The Rights Management Service Client 2.1 declares the following data types.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 44D3EB62-7A60-45D9-BA7E-45A06E7D598F
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- IPC_AUTH_TOKEN_HANDLE
- PIPC_AUTH_TOKEN_HANDLE
- PCIPCF_FILE_BASIC_INFORMATION
- IPCF_FILE_HANDLE
- PIPCF_FILE_HANDLE
- PCIPCF_FILE_RANGE
- IPC_HANDLE
- PIPC_HANDLE
- IPC_KEY_HANDLE
- PIPC_KEY_HANDLE
- IPC_LICENSE_HANDLE
- PIPC_LICENSE_HANDLE
- IPC_LICENSE_METADATA_HANDLE
- PIPC_LICENSE_METADATA_HANDLE
- PCIPCF_PROTECTED_FILE_HEADER
- PCIPCF_RAW_FILE_RANGE
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Data types

The Rights Management Service Client 2.1 declares the following data types.

<dl> <dt>

**IPC\_AUTH\_TOKEN\_HANDLE**
</dt> <dd>

A handle to an IPC authentication token object.

This type is declared in Ipcbase.h as follows:

`DECLARE_HANDLE(IPC_AUTH_TOKEN_HANDLE);`

</dd> <dt>

**PIPC\_AUTH\_TOKEN\_HANDLE**
</dt> <dd>

A pointer to a handle to an IPC authentication token object

This type is declared in Ipcbase.h as follows:

`typedef IPC_AUTH_TOKEN_HANDLE* PIPC_AUTH_TOKEN_HANDLE;`

</dd> <dt>

**PCIPCF\_FILE\_BASIC\_INFORMATION**
</dt> <dd>

Const pointer to an [**IPCF\_FILE\_BASIC\_INFORMATION**](ipcf-file-basc-information.md) structure.

This type is declared in Ipcbase.h as follows:

`typedef const IPCF_FILE_BASIC_INFORMATION *PCIPCF_FILE_BASIC_INFORMATION;`

</dd> <dt>

**IPCF\_FILE\_HANDLE**
</dt> <dd>

A handle to a pfile.

This type is declared in Ipcbase.h as follows:

`DECLARE_HANDLE(IPCF_FILE_HANDLE);`

</dd> <dt>

**PIPCF\_FILE\_HANDLE**
</dt> <dd>

Pointer to an **IPCF\_FILE\_HANDLE** type.

This type is declared in Ipcbase.h as follows:

`typedef IPCF_FILE_HANDLE* PIPCF_FILE_HANDLE;`

</dd> <dt>

**PCIPCF\_FILE\_RANGE**
</dt> <dd>

Const Pointer to an [**IPCF\_FILE\_RANGE**](ipcf-file-range.md) structure.

This type is declared in Ipcbase.h as follows:

`typedef const IPCF_FILE_RANGE *PCIPCF_FILE_RANGE;`

</dd> <dt>

**IPC\_HANDLE**
</dt> <dd>

A handle to an IPC object.

This type is declared in Ipcbase.h as follows:

`DECLARE_HANDLE(IPC_HANDLE);`

</dd> <dt>

**PIPC\_HANDLE**
</dt> <dd>

A pointer to a handle to an IPC object.

This type is declared in Ipcbase.h as follows:

`typedef IPC_HANDLE* PIPC_HANDLE;`

</dd> <dt>

**IPC\_KEY\_HANDLE**
</dt> <dd>

A handle to an IPC key object.

This type is declared in Ipcbase.h as follows:

`DECLARE_HANDLE(IPC_KEY_HANDLE);`

</dd> <dt>

**PIPC\_KEY\_HANDLE**
</dt> <dd>

A pointer to a handle to an IPC key object.

This type is declared in Ipcbase.h as follows:

`typedef IPC_KEY_HANDLE* PIPC_KEY_HANDLE;`

</dd> <dt>

**IPC\_LICENSE\_HANDLE**
</dt> <dd>

A handle to an IPC license object.

This type is declared in Ipcbase.h as follows:

`DECLARE_HANDLE(IPC_LICENSE_HANDLE);`

</dd> <dt>

**PIPC\_LICENSE\_HANDLE**
</dt> <dd>

A pointer to a handle to an IPC license object.

This type is declared in Ipcbase.h as follows:

`typedef IPC_LICENSE_HANDLE* PIPC_LICENSE_HANDLE;`

</dd> <dt>

**IPC\_LICENSE\_METADATA\_HANDLE**
</dt> <dd>

A handle to the metadata section in the IPC license.

This type is declared in Ipcbase.h as follows:

`DECLARE_HANDLE(IPC_LICENSE_METADATA_HANDLE);`

</dd> <dt>

**PIPC\_LICENSE\_METADATA\_HANDLE**
</dt> <dd>

Pointer to an **IPC\_LICENSE\_METADATA\_HANDLE** type.

This type is declared in Ipcbase.h as follows:

`typedef IPC_LICENSE_METADATA_HANDLE* PIPC_LICENSE_METADATA_HANDLE;`

</dd> <dt>

**PCIPCF\_PROTECTED\_FILE\_HEADER**
</dt> <dd>

Const Pointer to an [**IPCF\_PROTECTED\_FILE\_HEADER**](ipcf-protected-file-header.md) structure.

This type is declared in Ipcbase.h as follows:

`typedef const IPCF_PROTECTED_FILE_HEADER *PCIPCF_PROTECTED_FILE_HEADER;`

</dd> <dt>

**PCIPCF\_RAW\_FILE\_RANGE**
</dt> <dd>

Const Pointer to an [**IPCF\_RAW\_FILE\_RANGE**](ipcf-raw-file-range.md) structure.

This type is declared in Ipcbase.h as follows:

`typedef const IPCF_RAW_FILE_RANGE *PCIPCF_RAW_FILE_RANGE;`

</dd> </dl>

## Requirements



|                                     |                                                                                                                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP2<br/>                                                                                                                                                         |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                                                                                                            |
| Header<br/>                   | <dl> <dt>Ipcbase.h (include Msipc.h); </dt> <dt>Ipcfile.h (include Msipc.h)</dt> </dl> |



 

 





