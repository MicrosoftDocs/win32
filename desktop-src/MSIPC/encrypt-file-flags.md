---
title: Encrypt file flags
description: Constants for specifying the type of file input.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 7FF748B8-9CAB-48CD-B420-AA93FC39F65A
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
topic_type:
- apiref
api_name:
- IPCF_EF_FLAG_DEFAULT
- IPCF_EF_FLAG_UPDATELICENSE_BLOCKED
- IPC_EF_FLAG_KEY_NO_PERSIST
- IPC_EF_FLAG_KEY_NO_PERSIST_DISK
- IPC_EF_FLAG_KEY_NO_PERSIST_LICENSE
- IPCF_EF_FLAG_FORCE_PFILE
- IPCF_EF_FLAG_FORCE_NATIVE
api_location:
- Ipcfile.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Encrypt file flags

Constants for specifying the type of file input.

<dl> <dt>

<span id="IPCF_EF_FLAG_DEFAULT"></span><span id="ipcf_ef_flag_default"></span>**IPCF\_EF\_FLAG\_DEFAULT**
</dt> <dd> <dl> <dt>

0
</dt> <dt>



Uses all of the default settings for [**IpcfEncryptFile**](ipcfencryptfile.md).

By default, [**IpcfEncryptFile**](ipcfencryptfile.md) will try to apply the new policy specified in *pvLicenseInfo*.

When the file is already encrypted, if the new policy is different from the old one in the current file or the protector to be used to protect this type of file, specified by administrator configuration, is different from the one already used in encrypting the current file, the file will be decrypted and re-encrypted with the new policy or new protectors.


</dt> </dl> </dd> <dt>

<span id="IPCF_EF_FLAG_UPDATELICENSE_BLOCKED"></span><span id="ipcf_ef_flag_updatelicense_blocked"></span>**IPCF\_EF\_FLAG\_UPDATELICENSE\_BLOCKED**
</dt> <dd> <dl> <dt>

1
</dt> <dt>



When this flag is specified, if the file is already encrypted, the file will not be decrypted and re-encrypted with the new policy.


</dt> </dl> </dd> <dt>

<span id="IPC_EF_FLAG_KEY_NO_PERSIST"></span><span id="ipc_ef_flag_key_no_persist"></span>**IPC\_EF\_FLAG\_KEY\_NO\_PERSIST**
</dt> <dd> <dl> <dt>

2
</dt> <dt>



Use this flag to prevent a key from being cached locally and inserted within the serialized license.

If this flag is used, the content creator must contact the RMS server in order to access the content.


</dt> </dl> </dd> <dt>

<span id="IPC_EF_FLAG_KEY_NO_PERSIST_DISK"></span><span id="ipc_ef_flag_key_no_persist_disk"></span>**IPC\_EF\_FLAG\_KEY\_NO\_PERSIST\_DISK**
</dt> <dd> <dl> <dt>

4
</dt> <dt>



Use this flag to prevent a key from being cached locally but the key can be inserted within the serialized license.


</dt> </dl> </dd> <dt>

<span id="IPC_EF_FLAG_KEY_NO_PERSIST_LICENSE"></span><span id="ipc_ef_flag_key_no_persist_license"></span>**IPC\_EF\_FLAG\_KEY\_NO\_PERSIST\_LICENSE**
</dt> <dd> <dl> <dt>

8
</dt> <dt>



Use this flag to prevent a key from being inserted within the serialized license but cached locally in license store.


</dt> </dl> </dd> <dt>

<span id="IPCF_EF_FLAG_FORCE_PFILE"></span><span id="ipcf_ef_flag_force_pfile"></span>**IPCF\_EF\_FLAG\_FORCE\_PFILE**
</dt> <dd> <dl> <dt>

0x00000010
</dt> <dt>



Specifying this flag will cause the File Api to ignore the admin specified rules for encryption and create a pfile that can be opened by any application.

This flag cannot be used along with **IPCF\_EF\_FLAG\_FORCE\_NATIVE**


</dt> </dl> </dd> <dt>

<span id="IPCF_EF_FLAG_FORCE_NATIVE"></span><span id="ipcf_ef_flag_force_native"></span>**IPCF\_EF\_FLAG\_FORCE\_NATIVE**
</dt> <dd> <dl> <dt>

0x00000020
</dt> <dt>



Specifying this flag will make the file only opened by RMS aware applications.

This flag cannot be used along with **IPCF\_EF\_FLAG\_FORCE\_PFILE**


</dt> </dl> </dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP2<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                         |
| Header<br/>                   | <dl> <dt>Ipcfile.h (include Msipc.h)</dt> </dl> |



 

 





